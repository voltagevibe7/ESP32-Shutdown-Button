import serial
import os
import sys

# Konfiguration - Check deinen COM-Port!
PORT = 'COM3' 
BAUD = 115200

def listen():
    print(f"--- ESP32 KILLSWITCH RECEIVER ---")
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        print(f"[*] Port {PORT} offen. Warte auf Button-Press...")
    except Exception as e:
        print(f"[!] ERROR: {e}")
        return

    while True:
        try:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                
                if data == "EXECUTE:shutdown":
                    print("[!!!] DEPLOYMENT SIGNAL ERHALTEN!")
                    print("[*] Fahre System sofort herunter...")
                    os.system("shutdown /s /f /t 0")
        except KeyboardInterrupt:
            print("\n[*] Beendet durch User.")
            sys.exit()

if __name__ == "__main__":
    listen()
