"""
This module provides an API for emotion detection using Flask.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=["POST"])
def detect_emotion():
    """
    Detects emotions from the provided text and returns the emotion scores
    along with the dominant emotion.
    
    Expects a JSON payload with a 'text' field. Returns the emotion values 
    (anger, disgust, fear, joy, sadness) along with the dominant emotion.
    
    If the text is invalid, returns an error message with a 400 status code.
    """
    # Get JSON data from the request
    data = request.get_json()

    # Extract the 'text' from the input
    text = data.get("text", None)

    if text is None:
        # Handle the case where the 'text' field is missing
        return "Invalid text! Please try again!", 400

    # Get emotion prediction
    response = emotion_detector(text)

    if response.get('dominant_emotion') is None:
        # Handle the case where the dominant emotion is missing
        return "Invalid text! Please try again!", 400

    # Return emotion scores and the dominant emotion
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    # Run the app with debug mode enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
