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

### 1. Run Ansible Setup

1. Ensure you are in the `ansible` directory:
   ```bash
   cd ansible
   ```
2. Run the Ansible playbook to configure the Raspberry Pi:
   ```bash
   ansible-playbook -i inventory.ini playbook.yml
   ```
3. Verify that the application files have been deployed to `/home/pi/webradio` on the target system.

### 2. Access the Web Interface

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
│       └── webradio/
│           └── tasks/
│               └── main.yml  # Tasks for Webradio setup
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
