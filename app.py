from flask import Flask, render_template, request, jsonify ,send_from_directory
import os
from models.asr_model import transcribe_audio
from models.sentiment_model import analyze_tone
from models.evaluation import evaluate_performance



app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]
    audio_path = "uploaded_audio.wav"
    audio_file.save(audio_path)

    transcription = transcribe_audio(audio_path)
    tone_analysis = analyze_tone(transcription)
    evaluation = evaluate_performance(transcription)

    return jsonify({
        "transcription": transcription,
        "analysis": tone_analysis,
        "evaluation": evaluation
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)