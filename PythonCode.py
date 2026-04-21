import serial
import os
import time

# --- KONFIGURATION ---
PORT = 'COM3'  # MUSS mit deiner Arduino IDE übereinstimmen!
BAUD = 115200

def main():
    print("========================================")
    print("   ESP32 KILLSWITCH RECEIVER ACTIVE     ")
    print("========================================")
    
    try:
        # Verbindung aufbauen
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2) # Kurz warten, bis der ESP32 stabil ist
        print(f"[*] Erfolgreich mit {PORT} verbunden.")
        print("[*] Warte auf Deployment-Signal vom Button...")
    except Exception as e:
        print(f"[!] FEHLER: Konnte Port {PORT} nicht öffnen.")
        print(f"    Check: Ist der ESP32 eingesteckt?")
        print(f"    Check: Ist der Serial Monitor in Arduino geschlossen?")
        input("\nDrücke Enter zum Beenden...")
        return

    while True:
        try:
            if ser.in_waiting > 0:
                # Daten vom ESP32 lesen
                line = ser.readline().decode('utf-8').strip()
                
                if "EXECUTE:shutdown" in line:
                    print("\n[!!!] SIGNAL ERHALTEN: SHUTDOWN WIRD AUSGEFÜHRT!")
                    # Der ultimative Shutdown-Befehl
                    os.system("shutdown /s /f /t 0")
                    break # Programm beenden, da PC eh ausgeht
                
        except serial.SerialException:
            print("\n[!] Verbindung zum ESP32 verloren!")
            break
        except KeyboardInterrupt:
            print("\n[*] Beendet durch User.")
            break

if __name__ == "__main__":
    main()
