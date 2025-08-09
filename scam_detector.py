from transformers import pipeline
import schedule
import time

ai_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

scam_labels = [
    "Fake invoice scam",
    "Advance fee scam",
    "Google Docs scam",
    "PayPal scam",
    "Message from HR scam",
    "Dropbox scam",
    "Council tax scam",
    "Unusual activity scam",
]

def detect_scams():
    with open("messages.txt", "r", encoding="utf-8") as f:
        messages = [line.strip() for line in f if line.strip()]
    
    print("Running scam detection...")
    for i, message in enumerate(messages, 1):
        result = ai_classifier(message, candidate_labels=scam_labels)
        print(f"Message {i}: {message}")
        for label, score in zip(result['labels'], result['scores']):
            if score > 0.5:
                print(f"  Detected Scam: {label} (Confidence: {score:.2f})")
        print("-" * 30)

schedule.every(5).minutes.do(detect_scams)

print("Scam Detector started - will check every 5 minutes.")
detect_scams()  # Run once at start

while True:
    schedule.run_pending()
    time.sleep(1)
