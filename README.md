 # Scam Detector

A Python program that reads messages and tells if they are scams using AI.

## Features

- Reads messages from `messages.txt`
- Detects scam messages using AI zero-shot classification
- Automatically checks every 5 minutes
- Prints results on the screen

## How to Use

1. Clone or download the project.
2. Open a terminal and go to the project folder.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
# Install dependencies:

```bash
pip install -r requirements.txt
```
# Add your messages in messages.txt (one message per line)
```bash
python scam_detector.py
```
# Automation
The program runs the scam check every 5 minutes automatically using the schedule library.

# License
This project is licensed under the MIT License.
