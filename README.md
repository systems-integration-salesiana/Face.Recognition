# Face Recognition

## Project Overview

The **Face Detection Monitor** is a background service designed to detect faces in images and send the results to a specified directory. This service is built using Python and leverages several powerful libraries to ensure accurate and efficient face detection. The project is configured using `pyproject.toml` and can be managed using modern Python tools like `uv`, `pip`, or `pipenv`.

---

## Project Details

### `pyproject.toml`

The `pyproject.toml` file defines the project's metadata, dependencies, and configuration. Below is an updated and more detailed version of the file:

```toml
[project]
name = "face-recognition-background-service"
version = "0.1.0"
description = "A background service that detects faces in images and sends the results to a specified directory. Built with Python and optimized for modern workflows."
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "dlib>=19.24.6",  # Machine learning toolkit for face detection
    "face-recognition>=0.1.0",  # High-level face recognition library
    "face-recognition-models>=0.3.0",  # Pre-trained models for face recognition
    "numpy>=2.2.2",  # Numerical computing library
    "pillow>=11.1.0",  # Image processing library
    "watchdog>=6.0.0",  # File system event monitoring
]
```

---

## Installation

You can install the project and its dependencies using `pip`, `pipenv`, or `uv`.

### Using `pip`:

1. Ensure you have Python 3.13 or later installed.
2. Install the dependencies from the `pyproject.toml` file:

   ```bash
   pip install .
   ```

### Using `pipenv`:

1. Install `pipenv` if you don't already have it:

   ```bash
   pip install pipenv
   ```

2. Install the dependencies and create a virtual environment:

   ```bash
   pipenv install
   ```

### Using `uv` (Modern Python Package Installer):

1. Install `uv` if you don't already have it:

   ```bash
   pip install uv
   ```

2. Install the dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

---

## Running the Application

Once the dependencies are installed, you can run the application using the following command:

### Using `pipenv`:

```bash
pipenv run python main.py
```

### Using `uv` or `pip`:

```bash
python main.py
```

---

## Dependencies

- **dlib**: A toolkit for machine learning, used for face detection.
- **face-recognition**: A high-level library for face recognition tasks.
- **face-recognition-models**: Pre-trained models for face recognition.
- **numpy**: A library for numerical computing, essential for image processing.
- **pillow**: A fork of the Python Imaging Library (PIL), used for image manipulation.
- **watchdog**: A library for monitoring file system events.
