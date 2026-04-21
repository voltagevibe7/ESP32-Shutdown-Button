# ⚡ ESP32 Instant PC Killswitch

A physical hardware trigger to instantly shut down a Windows PC. This project uses an ESP32 with an OLED display as a "deployment station" and a Python backend to execute the system command.

## 🚀 Features
- **OLED Status Display:** Shows "READY TO DEPLOY" when active.
- **Visual Feedback:** Screen flashes during execution.
- **Force Shutdown:** Uses a forced command to bypass hung applications.
- **Physical Trigger:** Tactical button execution via GPIO.

## 🛠 Hardware Setup

### Components
- ESP32 Development Board
- 0.96" I2C OLED Display (SSD1306)
- 1x Push Button
- Jumper Wires

### Wiring Diagram
| Component | ESP32 Pin |
| :--- | :--- |
| **OLED VCC** | 3.3V |
| **OLED GND** | GND |
| **OLED SCL** | GPIO 22 |
| **OLED SDA** | GPIO 21 |
| **Button Leg 1**| GPIO 23 |
| **Button Leg 2**| GND |

## 💻 Software Installation

### 1. ESP32 Firmware
1. Open `ESP32_Killswitch.ino` in the Arduino IDE.
2. Install the **Adafruit SSD1306** and **Adafruit GFX** libraries.
3. Select your ESP32 board and the correct COM Port.
4. Click **Upload**.

### 2. Python Receiver (Target PC)
The Python script listens to the ESP32 via Serial and executes the shutdown.
1. Install Python 3.x.
2. Install the required library:
   ```bash
   pip install pyserial
