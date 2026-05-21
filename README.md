# Emotion Detector

An AI-based emotion detection web application using IBM Watson NLP library.

## Overview
This project detects emotions from text input using the IBM Watson NLP library. It provides both a Python module and a Flask web interface for emotion analysis.

## Features
- Emotion detection using Watson NLP
- REST API endpoints
- Comprehensive error handling
- Unit test coverage
- Static code analysis compliance
- Flask web deployment

## Supported Emotions
- Anger
- Disgust
- Fear
- Joy
- Sadness
- Surprise

## Tech Stack
- Python 3.x
- Flask
- IBM Watson NLP Library
- Pytest
- Pylint

## Installation

```bash
git clone https://github.com/Sakshi-git-04-k/emotion-detector.git
cd emotion-detector
pip install -r requirements.txt
```

## Usage

### Python Module
```python
from EmotionDetection import emotion_detector
result = emotion_detector("I love this!")
print(result)
```

### Flask Web Application
```bash
python server.py
```

Access at `http://localhost:5000`

### Running Tests
```bash
python -m pytest test_emotion_detection.py -v
```

### Static Code Analysis
```bash
pylint server.py
```

## Project Structure
```
emotion-detector/
├── README.md
├── requirements.txt
├── emotion_detection.py
├── server.py
├── test_emotion_detection.py
└── EmotionDetection/
    └── __init__.py
```

## License
Apache License 2.0

## Author
Sakshi - [Sakshi-git-04-k](https://github.com/Sakshi-git-04-k)
