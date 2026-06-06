from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def emotionDetector():
    emotion = request.args.get('textToAnalyze')

    result = emotion_detector(emotion)
    return result

@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__": app.run(host="0.0.0.0", port=54000)