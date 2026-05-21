"""
Flask Web Application for Emotion Detection

This module implements a REST API for emotion detection using Flask.
It provides endpoints for detecting emotions from text input and includes
error handling for invalid requests and blank input errors.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotion_detector', methods=['POST'])
def detect_emotion():
    """
    API endpoint for emotion detection.
    
    Expected JSON payload:
    {
        "text": "The text to analyze"
    }
    
    Returns:
    - 200 OK with emotion scores if successful
    - 400 Bad Request if text is blank
    - 500 Internal Server Error for other failures
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate request data - check if data is provided
        if not data or 'text' not in data:
            return jsonify({
                'error': 'Invalid request format. Please provide text field.'
            }), 400
        
        text_to_analyze = data.get('text', '').strip()
        
        # Check for blank input - Error handling for blank input
        if not text_to_analyze:
            return jsonify({
                'error': 'Invalid text. Text cannot be blank.'
            }), 400
        
        # Call emotion detector
        result = emotion_detector(text_to_analyze)
        
        # Check if there was an error in emotion detection
        if result.get('dominant_emotion') is None and 'error' not in result:
            return jsonify({
                'error': 'Unable to process emotion detection'
            }), 500
        
        # Return successful response
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
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({'status': 'healthy'}), 200


@app.route('/', methods=['GET'])
def welcome():
    """
    Welcome endpoint providing API documentation.
    """
    return jsonify({
        'message': 'Welcome to the Emotion Detector API',
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
    app.run(host='0.0.0.0', port=5000, debug=True)
