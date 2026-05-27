from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# URL del microservicio core_sxvars (ajústala según tu despliegue en Cloud Run)
CORE_SXVARS_URL = os.getenv("CORE_SXVARS_URL")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Servicio principal de Pasaportes Home"})

@app.route("/get_vars", methods=["GET"])
def get_vars_from_core():
    try:
        response = requests.get(CORE_SXVARS_URL, timeout=10)
        if response.status_code == 200:
            return jsonify({
                "origen": "core_sxvars",
                "datos": response.json()
            })
        else:
            return jsonify({
                "error": "core_sxvars_error",
                "status_code": response.status_code,
                "message": response.text
            }), 500
    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "connection_error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
