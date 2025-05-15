from flask import Flask, request, jsonify

app = Flask(__name__)
latest_light = {}  # 用來暫存最新一筆燈光參數

def normalize_vad(vad):
    v, a, d = vad
    return {
        "brightness": (a + 1) / 2,
        "color_hue": (v + 1) / 2 * 360,
        "pulse_speed": (d + 1) / 2
    }

@app.route("/predict", methods=["POST"])
def predict_light():
    global latest_light
    data = request.json
    vad = data.get("vad")  # 預期格式: {"vad": [V, A, D]}
    if vad is None or len(vad) != 3:
        return jsonify({"error": "Invalid VAD input"}), 400
    light_params = normalize_vad(vad)
    latest_light = light_params  # 更新暫存的資料
    return jsonify(light_params)

@app.route("/current", methods=["GET"])
def get_latest_light():
    if not latest_light:
        return jsonify({"error": "No data available"}), 404
    return jsonify(latest_light)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
