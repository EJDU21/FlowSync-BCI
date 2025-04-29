from flask import Flask, request, jsonify

app = Flask(__name__)

def normalize_vad(vad):
    v, a, d = vad
    return {
        "brightness": (a + 1) / 2,
        "color_hue": (v + 1) / 2 * 360,
        "pulse_speed": (d + 1) / 2
    }

@app.route("/predict", methods=["POST"])
def predict_light():
    data = request.json
    vad = data.get("vad")  # 預期格式: {"vad": [V, A, D]}
    if vad is None or len(vad) != 3:
        return jsonify({"error": "Invalid VAD input"}), 400
    light_params = normalize_vad(vad)
    return jsonify(light_params)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
