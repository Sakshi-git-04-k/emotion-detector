"""
Flask Web Application for Emotion Detection with Static Code Analysis

This module implements a REST API for emotion detection using Flask.
It provides endpoints for detecting emotions from text input and includes
error handling for invalid requests. Code follows PEP 8 standards and
includes comprehensive documentation for static code analysis.

Static Code Analysis Considerations:
- Type hints for better code clarity and IDE support
- Comprehensive docstrings for all functions
- Proper exception handling with specific error types
- Clear variable naming conventions
- Code organization following Python best practices
"""

from flask import Flask, request, jsonify
from typing import Dict, Tuple, Any, Optional
from EmotionDetection import emotion_detector
import logging

# Configure logging for code analysis and debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/emotion_detector', methods=['POST'])
def detect_emotion() -> Tuple[Dict[str, Any], int]:
    """
    API endpoint for emotion detection.
    
    Expected JSON payload:
    {
        "text": "The text to analyze"
    }
    
    Returns:
        Tuple[Dict[str, Any], int]: JSON response with emotion data and HTTP status code
        - 200 OK with emotion scores if successful
        - 400 Bad Request if text is blank or invalid
        - 500 Internal Server Error for other failures
    
    Raises:
        Exception: Caught and returned as 500 error response
    """
    try:
        # Get JSON data from request
        data: Optional[Dict] = request.get_json()
        
        # Validate request data - ensure text field is present
        if not data or 'text' not in data:
            logger.warning("Invalid request format: missing or empty data")
            return jsonify({
                'error': 'Invalid request format. Please provide text field.'
            }), 400
        
        # Extract and normalize text input
        text_to_analyze: str = data.get('text', '').strip()
        
        # Check for blank input - error handling for empty text
        if not text_to_analyze:
            logger.warning("Blank text provided for analysis")
            return jsonify({
                'error': 'Invalid text. Text cannot be blank.'
            }), 400
        
        # Call emotion detector function
        result: Dict[str, Any] = emotion_detector(text_to_analyze)
        
        # Check if there was an error in emotion detection
        if result.get('dominant_emotion') is None and 'error' not in result:
            logger.error("Emotion detection failed without error information")
            return jsonify({
                'error': 'Unable to process emotion detection'
            }), 500
        
        # Return successful response with emotion analysis
        logger.info(f"Successfully analyzed text. Dominant emotion: {result.get('dominant_emotion')}")
        return jsonify({
            'text': text_to_analyze,
            'emotion': {
                'anger': result.get('anger'),
                'disgust': result.get('disgust'),
                'fear': result.get('fear'),
                'joy': result.get('joy'),
                'sadness': result.get('sadness'),
                'surprise': result.get('surprise')
            },
            'dominant_emotion': result.get('dominant_emotion')
        }), 200
        
    except Exception as e:
        logger.exception(f"Unexpected error in emotion detection: {str(e)}")
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health_check() -> Tuple[Dict[str, str], int]:
    """
    Health check endpoint for monitoring server status.
    
    Returns:
        Tuple[Dict[str, str], int]: JSON response indicating server health and HTTP 200 status
    """
    logger.info("Health check requested")
    return jsonify({'status': 'healthy'}), 200


@app.route('/', methods=['GET'])
def welcome() -> Tuple[Dict[str, Any], int]:
    """
    Welcome endpoint providing API documentation.
    
    Returns:
        Tuple[Dict[str, Any], int]: JSON response with API information and HTTP 200 status
    """
    logger.info("Welcome endpoint accessed")
    return jsonify({
        'message': 'Welcome to the Emotion Detector API',
        'version': '1.0.0',
        'endpoints': {
            'emotion_detection': {
                'method': 'POST',
                'path': '/emotion_detector',
                'description': 'Detect emotions from text',
                'payload': {'text': 'The text to analyze'}
            },
            'health_check': {
                'method': 'GET',
                'path': '/health',
                'description': 'Check API health status'
            }
        }
    }), 200


if __name__ == '__main__':
    # Run the Flask development server
    # Note: Set debug=False in production environment
    app.run(host='0.0.0.0', port=5000, debug=True)
