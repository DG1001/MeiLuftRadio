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
current_title = "No stream playing"

def play_first_station():
    global current_process, current_title
    first_station = next(iter(stations.values()))
    current_title = "Loading..."
    current_process = subprocess.Popen(
        ["mpv", "--no-video", "--quiet", "--term-playing-msg=${icy-title}", first_station],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    threading.Thread(target=read_icy_title, args=(current_process,), daemon=True).start()

def read_icy_title(process):
    global current_title
    while True:
        line = process.stdout.readline()
        if not line:
            break
        line = line.decode("utf-8").strip()
        print(f"MPV Output: {line}")  # Debug-Ausgabe
        if "icy-title" in line.lower():
            # Extrahiere den Titel aus der Ausgabe
            title_start = line.find("icy-title:") + len("icy-title:")
            current_title = line[title_start:].strip()

# Starte den ersten Sender in einem separaten Thread
threading.Thread(target=play_first_station, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html", stations=stations)

@app.route("/play", methods=["POST"])
def play():
    global current_process, current_title
    station = request.form.get("station")

    if current_process and current_process.poll() is None:
        current_process.terminate()

    stream_url = stations[station]
    current_title = "Loading..."
    current_process = subprocess.Popen(
        ["mpv", "--no-video", "--quiet", "--term-playing-msg=${icy-title}", stream_url],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    threading.Thread(target=read_icy_title, args=(current_process,), daemon=True).start()
    return f"Playing {station}"

@app.route("/stop", methods=["POST"])
def stop():
    global current_process, current_title
    if current_process and current_process.poll() is None:
        current_process.terminate()
        current_process = None
    current_title = "No stream playing"
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

@app.route("/current_title", methods=["GET"])
def get_current_title():
    return jsonify({"title": current_title})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
