# 🤝 Contributing to FlavorSnap

Thank you for your interest in contributing to FlavorSnap! This guide will help you get started with contributing to our AI-powered food classification application.

## 📋 Table of Contents

- [🚀 Getting Started](#-getting-started)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Development Workflow](#-development-workflow)
- [📝 Contribution Guidelines](#-contribution-guidelines)
- [🧪 Testing Requirements](#-testing-requirements)
- [📋 Pull Request Process](#-pull-request-process)
- [🎯 Contribution Areas](#-contribution-areas)
- [📚 Resources](#-resources)

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18+ and npm/yarn/pnpm
- **Python** 3.8+ and pip
- **Rust** 1.70+ (for contracts)
- **Docker** & Docker Compose
- **Git** for version control

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/olaleyeolajide81-sketch/flavorsnap.git
cd flavorsnap

# Automated setup (recommended)
python scripts/install.py

# Or manual setup
npm run setup
```

### Environment Configuration

```bash
# Copy environment templates
cp .env.example .env
cp frontend/.env.example frontend/.env.local

# Configure essential variables
python scripts/validate_config.py --environment development
```

## 🏗️ Project Structure

Understanding the project structure is essential for effective contributions. FlavorSnap follows a modular microservices architecture:

```
flavorsnap/
├── 📁 frontend/                    # Next.js web application
├── 📁 ml-model-api/               # Flask ML inference API
├── 📁 contracts/                  # Soroban smart contracts
├── 📁 flavorsnap-food-registry/   # Rust-based food registry
├── 📁 dataset/                    # Training and validation data
├── 📁 docs/                       # Comprehensive documentation
├── 📁 scripts/                    # Utility and setup scripts
└── 📁 config/                     # Configuration files
```

### Key Documentation

- **[Project Structure](docs/project_structure.md)** - Complete directory structure and organization
- **[Development Workflow](docs/development_workflow.md)** - Detailed development process
- **[File Purposes](docs/file_purposes.md)** - Detailed file responsibilities
- **[Installation Guide](docs/installation.md)** - Comprehensive setup instructions

## 🔄 Development Workflow

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/flavorsnap.git
cd flavorsnap
git remote add upstream https://github.com/olaleyeolajide81-sketch/flavorsnap.git
```

### 2. Setup Development Environment

```bash
# Install dependencies and setup environment
python scripts/install.py

# Start development services
./scripts/docker_run.sh -e development -d
```

### 3. Create Feature Branch

```bash
# Sync with upstream
git fetch upstream
git checkout develop
git merge upstream/develop

# Create feature branch
git checkout -b feature/your-feature-name
```

### 4. Make Changes

- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Use meaningful commit messages

### 5. Test Your Changes

```bash
# Run all tests
npm run test

# Run linting
npm run lint

# Build project
npm run build
```

### 6. Commit & Push

```bash
# Stage changes
git add .

# Commit with conventional message
git commit -m "feat: add amazing feature"

# Push to your fork
git push origin feature/your-feature-name
```

## 📝 Contribution Guidelines

### Code Style

#### Frontend (TypeScript/React)

- Use **TypeScript** strict mode
- Follow **React** functional component patterns
- Use **TailwindCSS** utility classes
- Implement **ESLint** and **Prettier** formatting

```typescript
// Example component structure
import React from 'react';

interface FoodClassifierProps {
  onClassification: (result: ClassificationResult) => void;
}

export const FoodClassifier: React.FC<FoodClassifierProps> = ({ onClassification }) => {
  // Component logic
  return <div>Component JSX</div>;
};
```

#### Backend (Python)

- Follow **PEP 8** style guidelines
- Use **type hints** for function signatures
- Implement proper **error handling**
- Add **docstrings** for all functions

```python
# Example function structure
from typing import Dict, List, Optional

def classify_image(image_path: str, confidence_threshold: float = 0.6) -> Dict[str, any]:
    """
    Classify food image using trained model.
    
    Args:
        image_path: Path to the image file
        confidence_threshold: Minimum confidence for classification
        
    Returns:
        Dictionary containing classification results
        
    Raises:
        ValueError: If image file is invalid
    """
    # Implementation
    return result
```

#### Smart Contracts (Rust)

- Use **rustfmt** for formatting
- Follow **Rust** naming conventions
- Implement proper **error handling**
- Add comprehensive **tests**

```rust
// Example contract structure
use soroban_sdk::{contract, contractimpl, Address, Env};

#[contract]
pub struct FoodRegistry;

#[contractimpl]
impl FoodRegistry {
    pub fn register_food(env: Env, food_id: u64, name: String) -> Result<(), Error> {
        // Implementation
        Ok(())
    }
}
```

### Commit Messages

Follow [Conventional Commits](https://conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no functional changes)
- `refactor`: Code refactoring
- `test`: Test additions/modifications
- `chore`: Maintenance tasks
- `perf`: Performance improvements

#### Examples

```bash
feat(classification): add confidence threshold setting
fix(upload): resolve image validation error
docs(api): update endpoint documentation
style(frontend): format components with prettier
refactor(model): optimize image preprocessing
test(api): add integration tests for endpoints
chore(deps): update dependencies to latest versions
```

## 🧪 Testing Requirements

### Test Coverage

- **Frontend**: Minimum 80% coverage
- **Backend**: Minimum 85% coverage
- **Contracts**: Minimum 90% coverage

### Test Types

#### Unit Tests

```bash
# Frontend unit tests
cd frontend
npm run test

# Backend unit tests
cd ml-model-api
python -m pytest tests/unit/

# Contract tests
cd contracts
cargo test
```

#### Integration Tests

```bash
# API integration tests
npm run test:integration

# Database integration tests
python -m pytest tests/integration/
```

#### End-to-End Tests

```bash
# E2E tests with Playwright
npm run test:e2e

# Visual regression tests
npm run test:visual
```

### Test Data

```bash
# Generate test data
python scripts/generate_test_data.py

# Clean test data
npm run test:clean

# Seed test database
npm run test:seed
```

## 📋 Pull Request Process

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] Tests added for new functionality
- [ ] Documentation updated
- [ ] All tests pass
- [ ] Build succeeds
- [ ] No security vulnerabilities
- [ ] Performance impact considered

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated

## Screenshots (if applicable)
Add screenshots for UI changes

## Additional Notes
Any additional context or considerations
```

### Review Process

1. **Self-Review**: Review your own changes first
2. **Automated Checks**: CI/CD pipeline validation
3. **Peer Review**: At least one team member review
4. **Approval**: Required approvals before merge
5. **Merge**: Squash and merge to maintain clean history

## 🎯 Contribution Areas

### Frontend Contributions

- **UI/UX Improvements**: Enhanced user interface and experience
- **New Components**: Reusable React components
- **Performance**: Optimization and speed improvements
- **Mobile**: Responsive design and mobile features
- **Accessibility**: A11y improvements and screen reader support
- **Internationalization**: Add new languages and translations

#### Example Frontend Projects

- Add dark mode toggle
- Implement image gallery with filters
- Create classification history dashboard
- Add social sharing features
- Implement progressive web app features

### Backend Contributions

- **API Enhancements**: New endpoints and features
- **Model Optimization**: Improve ML model performance
- **Security**: Authentication, authorization, and data protection
- **Database**: Schema improvements and optimizations
- **Performance**: Caching, optimization, and scaling
- **Monitoring**: Enhanced logging and metrics

#### Example Backend Projects

- Add user authentication system
- Implement batch classification API
- Add model version management
- Create analytics dashboard API
- Implement rate limiting and caching

### Machine Learning Contributions

- **Model Architecture**: Improve classification accuracy
- **New Categories**: Add support for more food types
- **Training Pipeline**: Enhance data preprocessing and training
- **Explainable AI**: Add model interpretation features
- **Performance**: Optimize inference speed and memory usage

#### Example ML Projects

- Implement transfer learning with new models
- Add data augmentation techniques
- Create model evaluation dashboard
- Implement active learning for dataset improvement
- Add support for video classification

### Blockchain Contributions

- **Smart Contracts**: New governance and incentive mechanisms
- **Token Economics**: Design and implement reward systems
- **Integration**: Connect blockchain with frontend/backend
- **Security**: Audit and improve contract security
- **Scalability**: Optimize contract performance

#### Example Blockchain Projects

- Create decentralized model validation system
- Implement token rewards for data contributions
- Add voting mechanism for model updates
- Create food provenance tracking
- Implement decentralized storage for models

### Documentation Contributions

- **API Documentation**: Enhance API docs and examples
- **Tutorials**: Create step-by-step guides
- **Examples**: Add code examples and use cases
- **Translation**: Translate documentation to other languages
- **Video Content**: Create tutorial videos

#### Example Documentation Projects

- Create comprehensive API reference
- Write deployment guides for different platforms
- Create video tutorials for new users
- Add troubleshooting guides for common issues
- Write developer blog posts

### DevOps Contributions

- **CI/CD**: Improve build and deployment pipelines
- **Docker**: Optimize container images and configurations
- **Monitoring**: Enhanced observability and alerting
- **Security**: Implement security best practices
- **Automation**: Create scripts for common tasks

#### Example DevOps Projects

- Set up GitHub Actions for automated testing
- Create Kubernetes deployment manifests
- Implement automated security scanning
- Add performance monitoring and alerting
- Create automated backup and recovery systems

## 📚 Resources

### Documentation

- **[Project Structure](docs/project_structure.md)** - Complete directory structure
- **[Development Workflow](docs/development_workflow.md)** - Detailed development process
- **[File Purposes](docs/file_purposes.md)** - File responsibilities
- **[Installation Guide](docs/installation.md)** - Setup instructions
- **[Configuration Guide](docs/configuration.md)** - Configuration options
- **[Troubleshooting Guide](docs/troubleshooting.md)** - Common issues

### Development Tools

- **🔍 Structure Analysis**: `python scripts/analyze_structure.py`
- **⚡ Quick Setup**: `python scripts/install.py`
- **🧪 Environment Check**: `python scripts/check_environment.py`
- **🐳 Docker Management**: `./scripts/docker_run.sh`

### Community

- **Telegram Group**: [Join our community](https://t.me/+Tf3Ll4oRiGk5ZTM0)
- **GitHub Issues**: [Report bugs and request features](https://github.com/olaleyeolajide81-sketch/flavorsnap/issues)
- **Discussions**: [Join GitHub Discussions](https://github.com/olaleyeolajide81-sketch/flavorsnap/discussions)

### Learning Resources

- **Next.js Documentation**: [https://nextjs.org/docs](https://nextjs.org/docs)
- **React Documentation**: [https://react.dev](https://react.dev)
- **PyTorch Documentation**: [https://pytorch.org/docs](https://pytorch.org/docs)
- **Soroban Documentation**: [https://soroban.stellar.org/docs](https://soroban.stellar.org/docs)
- **Docker Documentation**: [https://docs.docker.com](https://docs.docker.com)

## 🏆 Recognition

Contributors are recognized in multiple ways:

- **GitHub Contributors**: Listed in repository contributors
- **Release Notes**: Mentioned in release changelogs
- **Community Spotlight**: Featured in community updates
- **Swag Opportunities**: Receive project merchandise
- **Speaking Opportunities**: Present at community events

## 📞 Getting Help

If you need help with your contribution:

1. **Check Documentation**: Review existing docs and guides
2. **Search Issues**: Look for similar issues or discussions
3. **Join Community**: Ask questions in our Telegram group
4. **Create Issue**: Open an issue for specific questions
5. **Contact Maintainers**: Reach out to project maintainers

## 📄 Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences
- Gracefully accept constructive criticism
- Show empathy towards other community members

---

Thank you for contributing to FlavorSnap! Your contributions help make AI-powered food classification accessible to everyone.

**Made with 💚 by the FlavorSnap community**

---

*Last updated: March 2026*
*Version: 1.0.0*
