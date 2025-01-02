# Webradio Project

A lightweight Flask-based web application for playing online radio stations on a Raspberry Pi using `mpv`. This project provides a simple web interface for controlling radio playback, including options for selecting stations, stopping playback, uploading/downloading station lists, and displaying the current song title (`icy-title`).

## Features

- Play online radio streams with `mpv`
- Simple and responsive web interface
- Upload and download station lists in JSON format
- Display the current song title (`icy-title`) in real-time
- Written in Python with Flask

---

## Requirements

- Raspberry Pi OS Lite (32-bit)
- Raspberry Pi with network and audio output
- Python 3.7 or higher
- `mpv` for audio playback
- Flask for the web interface

---

## Installation

### 1. Set up the Raspberry Pi

1. Install Raspberry Pi OS Lite (32-bit) on your SD card.
2. Connect your Raspberry Pi to the network.
3. Update and upgrade the system:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

### 2. Install Dependencies

1. Install required software:
   ```bash
   sudo apt install mpv python3 python3-pip python3-flask -y
   ```
2. Test `mpv` to ensure it works:
   ```bash
   mpv http://streams.radiobob.de/bob-live/mp3-192/mediaplayer
   ```

### 3. Set Up the Web Application

1. Clone or copy the project files into a directory:
   ```bash
   mkdir -p ~/webradio
   cp app.py stations.json templates/index.html static/style.css ~/webradio/
   ```
2. Navigate to the project directory:
   ```bash
   cd ~/webradio
   ```
3. Start the application:
   ```bash
   python3 app.py
   ```

### 4. Access the Web Interface

1. Open a web browser and navigate to:
   ```
   http://<raspberry-pi-ip>:5000
   ```

---

## Usage

### Web Interface

- **Play a station**: Click on a station button.
- **Stop playback**: Click the "Stop" button.
- **Upload station list**: Use the upload button to add a new `stations.json`.
- **Download station list**: Use the download button to export the current station list.
- **View current song title**: The current song title (`icy-title`) is displayed and updated in real-time.

### Managing Stations

The stations are defined in the `stations.json` file. Example format:
```json
{
    "Radio Bob": "http://streams.radiobob.de/bob-live/mp3-192/mediaplayer",
    "Rock Antenne": "http://www.rockantenne.de/webradio/rockantenne"
}
```

---

## Project Structure

```
project/
├── ansible/              # Ansible configuration for setup
│   ├── playbook.yml      # Main Ansible playbook
│   ├── inventory.ini     # Inventory file for target hosts
│   └── roles/
│       └── tasks/
│           └── main.yml  # Tasks for Webradio setup
├── src/                  # Source files for the Webradio application
│   ├── app.py            # Flask application
│   ├── stations.json     # List of radio stations
│   ├── templates/
│   │   └── index.html    # HTML for the web interface
│   └── static/
│       └── style.css     # Styling for the web interface
└── README.md             # Project documentation
```

---

## Future Enhancements

- Add persistent autostart for the application on boot
- Support for multiple playback backends
- Enhanced error handling for stream playback

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.
