import time
import os

SHARED_DIR = "/shared_data"
FILE_PATH = os.path.join(SHARED_DIR, "messaggio.txt")

print(f"Reader avviato. Ascolto su: {FILE_PATH}")

last_content = ""

while True:
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            content = f.read()
            
        if content != last_content:
            print(f"[READER] Nuovi dati ricevuti: {content}")
            last_content = content
    else:
        print("[READER] In attesa del file...")
        
    time.sleep(2)