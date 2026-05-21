import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    """
    
    def test_emotion_detector_joy(self):
        """
        Test emotion detection for joyful text.
        """
        result = emotion_detector("I love this!")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        """
        Test emotion detection for angry text.
        """
        result = emotion_detector("I hate this!")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_fear(self):
        """
        Test emotion detection for fearful text.
        """
        result = emotion_detector("I am afraid!")
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_emotion_detector_sadness(self):
        """
        Test emotion detection for sad text.
        """
        result = emotion_detector("I am very sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_disgust(self):
        """
        Test emotion detection for disgusted text.
        """
        result = emotion_detector("I am disgusted")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_surprise(self):
        """
        Test emotion detection for surprised text.
        """
        result = emotion_detector("I am surprised")
        self.assertEqual(result['dominant_emotion'], 'surprise')
    
    def test_emotion_detector_blank_input(self):
        """
        Test emotion detection with blank input.
        """
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
    
    def test_emotion_detector_none_input(self):
        """
        Test emotion detection with None input.
        """
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])
    
    def test_emotion_detector_whitespace_input(self):
        """
        Test emotion detection with whitespace-only input.
        """
        result = emotion_detector("   ")
        self.assertIsNone(result['dominant_emotion'])
    
    def test_emotion_detector_returns_dict(self):
        """
        Test that emotion_detector returns a dictionary.
        """
        result = emotion_detector("This is a test")
        self.assertIsInstance(result, dict)
    
    def test_emotion_detector_contains_all_emotions(self):
        """
        Test that result contains all emotion keys.
        """
        result = emotion_detector("This is a test")
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']
        for emotion in emotions:
            self.assertIn(emotion, result)


if __name__ == '__main__':
    unittest.main()
