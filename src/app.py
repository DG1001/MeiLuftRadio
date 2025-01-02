from flask import Flask, render_template, request, send_file, jsonify
import subprocess
import json
import os
import threading

app = Flask(__name__)

def load_stations():
    with open("stations.json", "r") as f:
        return json.load(f)

stations = load_stations()
current_process = None

def play_first_station():
    global current_process
    first_station = next(iter(stations.values()))
    current_process = subprocess.Popen(["mpv", first_station])

# Starte den ersten Sender in einem separaten Thread
threading.Thread(target=play_first_station, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html", stations=stations)

@app.route("/play", methods=["POST"])
def play():
    global current_process
    station = request.form.get("station")

    if current_process and current_process.poll() is None:
        current_process.terminate()

    stream_url = stations[station]
    current_process = subprocess.Popen(["mpv", stream_url])
    return f"Playing {station}"

@app.route("/stop", methods=["POST"])
def stop():
    global current_process
    if current_process and current_process.poll() is None:
        current_process.terminate()
        current_process = None
    return "Stopped"

# Funktion: Stationsliste herunterladen
@app.route("/download_stations", methods=["GET"])
def download_stations():
    return send_file("stations.json", as_attachment=True)

# Funktion: Stationsliste hochladen
@app.route("/upload_stations", methods=["POST"])
def upload_stations():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    if file and file.filename.endswith(".json"):
        file.save("stations.json")
        global stations
        stations = load_stations()
        return "Stations updated successfully", 200
    return "Invalid file format. Only .json files are allowed.", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

