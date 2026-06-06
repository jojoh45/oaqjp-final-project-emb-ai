"""
Flask server for the Emotion Detector application.
Exposes a REST endpoint to analyze emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_route():
    """
    Analyze the emotion of a given text string.
 
    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.
 
    Returns:
        str: A formatted string with emotion scores and dominant emotion.
        400: If text is missing or invalid.
    """
    emotion = request.args.get('textToAnalyze')

    if emotion is None:
        return "Invalid text! Please try again!"

    result = emotion_detector(emotion)

    return result

@app.route("/")
def render_index_page():
    """
    Return the html page

    Returns:
        index.html page
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    