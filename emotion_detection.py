import requests
from requests.auth import HTTPBasicAuth
import json

API_URL = "https://api.us-south.nlu.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze"
API_KEY = "YOUR_API_KEY"


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the provided text using Watson NLP.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion,
              or error information if status code is 400
    """
    # Validate input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'surprise': None,
            'dominant_emotion': None,
            'error': 'Invalid input - text cannot be blank'
        }
    
    # Request parameters
    headers = {
        'Content-Type': 'application/json'
    }
    
    parameters = {
        'text': text_to_analyze,
        'features': {
            'emotion': {}
        },
        'returnAnalyzedText': True
    }
    
    try:
        # Make API request
        response = requests.post(
            API_URL,
            headers=headers,
            auth=HTTPBasicAuth('apikey', API_KEY),
            json=parameters,
            timeout=10
        )
        
        # Handle response
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'surprise': None,
                'dominant_emotion': None
            }
        
        if response.status_code == 200:
            # Parse response
            result = response.json()
            emotion_data = result.get('emotion', {})
            
            if emotion_data:
                # Extract emotion scores
                emotions = {
                    'anger': emotion_data.get('anger', 0),
                    'disgust': emotion_data.get('disgust', 0),
                    'fear': emotion_data.get('fear', 0),
                    'joy': emotion_data.get('joy', 0),
                    'sadness': emotion_data.get('sadness', 0),
                    'surprise': emotion_data.get('surprise', 0)
                }
                
                # Find dominant emotion
                dominant_emotion = max(emotions, key=emotions.get)
                
                return {
                    'anger': emotions['anger'],
                    'disgust': emotions['disgust'],
                    'fear': emotions['fear'],
                    'joy': emotions['joy'],
                    'sadness': emotions['sadness'],
                    'surprise': emotions['surprise'],
                    'dominant_emotion': dominant_emotion
                }
        
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'surprise': None,
            'dominant_emotion': None,
            'error': 'Unable to process emotion detection'
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'surprise': None,
            'dominant_emotion': None,
            'error': str(e)
        }
