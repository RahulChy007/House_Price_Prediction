# Contributing to House Price Prediction

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Setup Development Environment

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/House_Price_Prediction.git
   cd House_Price_Prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

## Development Workflow

### Creating a Feature Branch

1. **Update main branch**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Writing Code

- **Follow PEP 8 style guide**
- **Add docstrings** to functions and classes
- **Write meaningful commit messages**
- **Add tests** for new features

### Code Quality Checks

1. **Format code with Black**
   ```bash
   black src/
   ```

2. **Sort imports**
   ```bash
   isort src/
   ```

3. **Lint with Flake8**
   ```bash
   flake8 src/
   ```

4. **Run tests**
   ```bash
   pytest
   ```

## Submitting Changes

### Before Submitting

- [ ] Tests pass (`pytest`)
- [ ] Code is formatted (`black`)
- [ ] Imports are sorted (`isort`)
- [ ] No linting errors (`flake8`)
- [ ] Docstrings are added
- [ ] Commit messages are meaningful

### Pull Request Process

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Go to GitHub and create a PR
   - Describe what changes you made
   - Reference any related issues

3. **PR Title Format**
   ```
   [TYPE] Brief description
   
   Types: feat, fix, refactor, docs, test, chore
   Example: [feat] Add cross-validation to model training
   ```

4. **PR Description Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code refactoring
   
   ## Testing Done
   Describe what tests were run
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Tests are passing
   - [ ] Documentation updated
   ```

## Reporting Bugs

1. **Check existing issues** - Avoid duplicates
2. **Describe the bug clearly**
3. **Provide steps to reproduce**
4. **Include expected vs actual behavior**
5. **Add environment details** (OS, Python version, etc.)

## Suggesting Features

1. **Check existing issues and discussions**
2. **Describe the feature clearly**
3. **Explain the use case**
4. **Suggest implementation** (optional)

## Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions
- Update CONTRIBUTING.md if needed
- Keep comments clear and concise

## Project Structure

```
House_Price_Prediction/
├── src/              # Source code
│   ├── __init__.py
│   ├── config.py     # Configuration settings
│   ├── train.py      # Training script
│   ├── predict.py    # Prediction script
│   └── utils.py      # Utility functions
├── data/             # Dataset directory
├── models/           # Trained models
├── notebooks/        # Jupyter notebooks
├── tests/            # Test files
├── requirements.txt  # Production dependencies
└── README.md         # Project documentation
```

## Commit Message Guidelines

```
[TYPE] Short description (50 chars max)

Longer explanation if needed (72 chars per line).
Explain what and why, not how.

Related issues: #123
```

### Commit Types
- **feat**: New feature
- **fix**: Bug fix
- **refactor**: Code refactoring
- **docs**: Documentation changes
- **test**: Test additions/changes
- **chore**: Maintenance tasks

## Questions?

- Check existing issues and discussions
- Create a discussion on GitHub
- Reach out to maintainers

## Recognition

Contributors will be recognized in:
- README.md
- Release notes
- Community discussions

Thank you for contributing! 🎉