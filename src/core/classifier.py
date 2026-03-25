"""
FlavorSnap Image Classifier with Preprocessing Support

This module handles image classification with preprocessing capabilities.
It integrates with the image enhancer to apply preprocessing before classification.
"""

import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import numpy as np
from typing import Dict, Any, Tuple, Optional
import logging
import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.image_enhancer import ImageEnhancer

logger = logging.getLogger(__name__)


class FlavorSnapClassifier:
    """Main classifier class with preprocessing support."""
    
    def __init__(self, model_path: str = 'models/best_model.pth'):
        """
        Initialize the classifier.
        
        Args:
            model_path: Path to the trained model file
        """
        self.model_path = model_path
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.class_names = ['Akara', 'Bread', 'Egusi', 'Moi Moi', 'Rice and Stew', 'Yam']
        self.image_enhancer = ImageEnhancer()
        
        # Default transforms for classification
        self.classification_transforms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        self._load_model()
    
    def _load_model(self) -> None:
        """Load the trained model."""
        try:
            # Initialize ResNet18 with ImageNet weights
            self.model = models.resnet18(weights='IMAGENET1K_V1')
            
            # Modify the final layer for our classes
            num_ftrs = self.model.fc.in_features
            self.model.fc = torch.nn.Linear(num_ftrs, len(self.class_names))
            
            # Load trained weights
            if Path(self.model_path).exists():
                self.model.load_state_dict(torch.load(self.model_path, map_location=self.device))
                logger.info(f"Model loaded successfully from {self.model_path}")
            else:
                logger.warning(f"Model file not found at {self.model_path}. Using untrained model.")
            
            # Move to device and set to evaluation mode
            self.model = self.model.to(self.device)
            self.model.eval()
            
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def preprocess_image(self, image: Image.Image, preprocessing_params: Optional[Dict[str, Any]] = None) -> Image.Image:
        """
        Apply preprocessing to the image before classification.
        
        Args:
            image: PIL Image to preprocess
            preprocessing_params: Dictionary of preprocessing parameters
            
        Returns:
            Preprocessed PIL Image
        """
        if preprocessing_params:
            return self.image_enhancer.apply_all_enhancements(image, preprocessing_params)
        else:
            return image
    
    def classify_image(self, image: Image.Image, preprocessing_params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Classify an image with optional preprocessing.
        
        Args:
            image: PIL Image to classify
            preprocessing_params: Optional preprocessing parameters
            
        Returns:
            Dictionary containing classification results and metadata
        """
        try:
            # Apply preprocessing if parameters provided
            if preprocessing_params:
                processed_image = self.preprocess_image(image, preprocessing_params)
                preprocessing_applied = True
            else:
                processed_image = image
                preprocessing_applied = False
            
            # Convert RGB if needed
            if processed_image.mode != 'RGB':
                processed_image = processed_image.convert('RGB')
            
            # Apply classification transforms
            input_tensor = self.classification_transforms(processed_image).unsqueeze(0)
            input_tensor = input_tensor.to(self.device)
            
            # Perform inference
            with torch.no_grad():
                outputs = self.model(input_tensor)
                probabilities = torch.nn.functional.softmax(outputs, dim=1)
                
                # Get top prediction
                confidence, predicted = torch.max(probabilities, 1)
                predicted_class = self.class_names[predicted.item()]
                confidence_score = confidence.item()
            
            # Get all class probabilities
            all_probabilities = {}
            for i, class_name in enumerate(self.class_names):
                all_probabilities[class_name] = probabilities[0][i].item()
            
            # Prepare result
            result = {
                'predicted_class': predicted_class,
                'confidence': confidence_score,
                'all_probabilities': all_probabilities,
                'preprocessing_applied': preprocessing_applied,
                'preprocessing_params': preprocessing_params or {},
                'image_info': {
                    'size': processed_image.size,
                    'mode': processed_image.mode
                }
            }
            
            logger.info(f"Classification successful: {predicted_class} (confidence: {confidence_score:.3f})")
            return result
            
        except Exception as e:
            logger.error(f"Error during classification: {e}")
            raise
    
    def batch_classify(self, images: list, preprocessing_params: Optional[Dict[str, Any]] = None) -> list:
        """
        Classify multiple images with the same preprocessing parameters.
        
        Args:
            images: List of PIL Images to classify
            preprocessing_params: Optional preprocessing parameters
            
        Returns:
            List of classification results
        """
        results = []
        
        for i, image in enumerate(images):
            try:
                result = self.classify_image(image, preprocessing_params)
                result['batch_index'] = i
                results.append(result)
            except Exception as e:
                logger.error(f"Error classifying image {i}: {e}")
                results.append({
                    'batch_index': i,
                    'error': str(e),
                    'predicted_class': None,
                    'confidence': 0.0
                })
        
        return results
    
    def get_preprocessing_recommendations(self, image: Image.Image) -> Dict[str, Any]:
        """
        Analyze image and recommend preprocessing parameters.
        
        Args:
            image: PIL Image to analyze
            
        Returns:
            Dictionary with recommended preprocessing parameters
        """
        try:
            # Convert to numpy array for analysis
            img_array = np.array(image.convert('RGB'))
            
            # Calculate basic statistics
            brightness = np.mean(img_array) / 255.0
            contrast = np.std(img_array) / 255.0
            
            recommendations = {}
            
            # Brightness recommendation
            if brightness < 0.3:
                recommendations['brightness'] = 1.3
            elif brightness > 0.8:
                recommendations['brightness'] = 0.8
            else:
                recommendations['brightness'] = 1.0
            
            # Contrast recommendation
            if contrast < 0.2:
                recommendations['contrast'] = 1.4
            elif contrast > 0.4:
                recommendations['contrast'] = 0.9
            else:
                recommendations['contrast'] = 1.0
            
            # Rotation recommendation (would need more sophisticated analysis)
            recommendations['rotation'] = 0.0
            
            # Aspect ratio recommendation
            width, height = image.size
            aspect_ratio = width / height
            
            if abs(aspect_ratio - 1.0) < 0.1:
                recommendations['aspect_ratio'] = '1:1'
            elif abs(aspect_ratio - 4/3) < 0.1:
                recommendations['aspect_ratio'] = '4:3'
            elif abs(aspect_ratio - 16/9) < 0.1:
                recommendations['aspect_ratio'] = '16:9'
            else:
                recommendations['aspect_ratio'] = 'Original'
            
            return {
                'recommendations': recommendations,
                'analysis': {
                    'brightness': brightness,
                    'contrast': contrast,
                    'aspect_ratio': aspect_ratio
                }
            }
            
        except Exception as e:
            logger.error(f"Error analyzing image for recommendations: {e}")
            return {
                'recommendations': {
                    'brightness': 1.0,
                    'contrast': 1.0,
                    'rotation': 0.0,
                    'aspect_ratio': 'Original'
                },
                'analysis': {},
                'error': str(e)
            }
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded model.
        
        Returns:
            Dictionary with model information
        """
        return {
            'model_path': self.model_path,
            'device': str(self.device),
            'num_classes': len(self.class_names),
            'class_names': self.class_names,
            'model_type': 'ResNet18',
            'input_size': (224, 224),
            'pretrained': True
        }
    
    def validate_image(self, image: Image.Image) -> Tuple[bool, str]:
        """
        Validate if the image is suitable for classification.
        
        Args:
            image: PIL Image to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            # Check if image is PIL Image
            if not isinstance(image, Image.Image):
                return False, "Input is not a PIL Image"
            
            # Check image mode
            if image.mode not in ['RGB', 'RGBA', 'L']:
                return False, f"Unsupported image mode: {image.mode}"
            
            # Check image size
            width, height = image.size
            if width < 32 or height < 32:
                return False, f"Image too small: {width}x{height}. Minimum is 32x32"
            
            if width > 4096 or height > 4096:
                return False, f"Image too large: {width}x{height}. Maximum is 4096x4096"
            
            # Try to convert to RGB
            try:
                image.convert('RGB')
            except Exception as e:
                return False, f"Cannot convert image to RGB: {str(e)}"
            
            return True, ""
            
        except Exception as e:
            return False, f"Validation error: {str(e)}"


# Convenience function for quick classification
def classify_food_image(image: Image.Image, preprocessing_params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Convenience function to classify a food image.
    
    Args:
        image: PIL Image to classify
        preprocessing_params: Optional preprocessing parameters
        
    Returns:
        Classification result dictionary
    """
    classifier = FlavorSnapClassifier()
    return classifier.classify_image(image, preprocessing_params)


# Function to get preprocessing recommendations
def get_image_preprocessing_tips(image: Image.Image) -> Dict[str, Any]:
    """
    Get preprocessing tips for an image.
    
    Args:
        image: PIL Image to analyze
        
    Returns:
        Dictionary with preprocessing recommendations
    """
    classifier = FlavorSnapClassifier()
    return classifier.get_preprocessing_recommendations(image)
