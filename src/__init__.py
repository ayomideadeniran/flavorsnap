"""
FlavorSnap - AI-Powered Food Classification Package

This package provides the core functionality for the FlavorSnap food classification system.
It includes utilities for configuration, model management, and shared components used across
the frontend, backend, and blockchain components.

Project Structure:
- flavorsnap/
  ├── frontend/          # Next.js web application
  ├── ml-model-api/      # Flask ML inference API
  ├── contracts/         # Soroban smart contracts
  ├── src/              # Shared source code (this package)
  ├── docs/             # Comprehensive documentation
  └── scripts/          # Utility and setup scripts

Key Features:
- AI-powered food classification using PyTorch ResNet18
- Microservices architecture with clear separation of concerns
- Blockchain integration for model governance
- Comprehensive documentation and development tools
- Docker support for containerized deployment

Documentation:
- Project Structure: docs/project_structure.md
- Development Workflow: docs/development_workflow.md
- File Purposes: docs/file_purposes.md
- Installation Guide: docs/installation.md
- Configuration Guide: docs/configuration.md

Development Tools:
- Structure Analysis: python scripts/analyze_structure.py
- Quick Setup: python scripts/install.py
- Environment Check: python scripts/check_environment.py
- Docker Management: ./scripts/docker_run.sh

Author: FlavorSnap Team
License: MIT
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "FlavorSnap Team"
__license__ = "MIT"
__description__ = "AI-Powered Food Classification System"

# Package metadata
PACKAGE_INFO = {
    "name": "flavorsnap",
    "version": __version__,
    "description": __description__,
    "author": __author__,
    "license": __license__,
    "url": "https://github.com/olaleyeolajide81-sketch/flavorsnap",
    "documentation": "https://docs.flavorsnap.com",
    "repository": "https://github.com/olaleyeolajide81-sketch/flavorsnap"
}

# Core components
from .config import (
    load_config,
    validate_config,
    get_environment_config
)

from .core import (
    FoodClassifier,
    ModelManager,
    ImageProcessor
)

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    "__description__",
    "PACKAGE_INFO",
    
    # Configuration
    "load_config",
    "validate_config", 
    "get_environment_config",
    
    # Core components
    "FoodClassifier",
    "ModelManager",
    "ImageProcessor"
]

def get_package_info():
    """Get comprehensive package information.
    
    Returns:
        dict: Package metadata and information
    """
    return {
        **PACKAGE_INFO,
        "python_requires": ">=3.8",
        "install_requires": [
            "torch>=1.9.0",
            "torchvision>=0.10.0",
            "pillow>=8.0.0",
            "numpy>=1.19.0",
            "pyyaml>=5.4.0"
        ],
        "extras_require": {
            "dev": [
                "pytest>=6.0.0",
                "pytest-cov>=2.10.0",
                "black>=21.0.0",
                "flake8>=3.8.0",
                "mypy>=0.800"
            ],
            "docs": [
                "sphinx>=4.0.0",
                "sphinx-rtd-theme>=0.5.0"
            ]
        },
        "classifiers": [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ]
    }

def get_project_structure():
    """Get project structure information.
    
    Returns:
        dict: Project structure and component information
    """
    return {
        "architecture": "microservices",
        "components": {
            "frontend": {
                "technology": "Next.js 15 + React 19",
                "language": "TypeScript",
                "styling": "TailwindCSS",
                "purpose": "User interface and client-side logic"
            },
            "backend": {
                "technology": "Flask",
                "language": "Python",
                "ml_framework": "PyTorch",
                "purpose": "ML inference and API services"
            },
            "contracts": {
                "technology": "Soroban",
                "language": "Rust",
                "blockchain": "Stellar",
                "purpose": "Smart contracts for governance and incentives"
            },
            "shared": {
                "technology": "Python Package",
                "language": "Python",
                "purpose": "Common utilities and configuration"
            }
        },
        "directories": {
            "frontend/": "Next.js web application",
            "ml-model-api/": "Flask ML inference API",
            "contracts/": "Soroban smart contracts",
            "flavorsnap-food-registry/": "Rust-based food registry",
            "dataset/": "Training and validation data",
            "models/": "Trained model files",
            "docs/": "Comprehensive documentation",
            "scripts/": "Utility and setup scripts",
            "config/": "Configuration files",
            "uploads/": "User uploaded images",
            "src/": "Shared source code (this package)"
        }
    }

def get_development_info():
    """Get development and contribution information.
    
    Returns:
        dict: Development workflow and contribution guidelines
    """
    return {
        "setup": {
            "automated": "python scripts/install.py",
            "manual": "npm run setup",
            "docker": "./scripts/docker_run.sh -e development -d"
        },
        "development": {
            "frontend": "cd frontend && npm run dev",
            "backend": "cd ml-model-api && python app.py",
            "contracts": "cd contracts && cargo build"
        },
        "testing": {
            "frontend": "cd frontend && npm run test",
            "backend": "cd ml-model-api && python -m pytest",
            "contracts": "cd contracts && cargo test",
            "e2e": "npm run test:e2e"
        },
        "documentation": [
            "docs/project_structure.md",
            "docs/development_workflow.md",
            "docs/file_purposes.md",
            "docs/installation.md",
            "docs/configuration.md",
            "docs/troubleshooting.md"
        ],
        "tools": {
            "structure_analysis": "python scripts/analyze_structure.py",
            "environment_check": "python scripts/check_environment.py",
            "config_validation": "python scripts/validate_config.py"
        }
    }

# Package initialization
def _initialize_package():
    """Initialize the FlavorSnap package."""
    import logging
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"FlavorSnap v{__version__} initialized")
    logger.info(f"Documentation available at: docs/")

# Initialize package on import
_initialize_package()
