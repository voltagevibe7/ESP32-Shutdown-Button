#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
#define SCREEN_ADDRESS 0x3C

// Dein I2C Setup
#define SDA_PIN 21
#define SCL_PIN 22
#define BUTTON_PIN 23 // Dein Knopf an Pin 23

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Serial.begin(115200);
  
  // I2C mit deinen Pins 21 & 22 starten
  Wire.begin(SDA_PIN, SCL_PIN);
  
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    for(;;); 
  }

  // Erster Screen: Ready to Deploy
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.setCursor(0, 5);
  display.println("ESP32 SYSTEM V1.0");
  display.println("---------------------");
  display.setTextSize(2);
  display.setCursor(0, 30);
  display.println("READY TO");
  display.println("DEPLOY");
  display.display();
}

void loop() {
  // Wenn Knopf an Pin 23 gedrückt wird (zieht gegen GND)
  if (digitalRead(BUTTON_PIN) == LOW) {
    display.clearDisplay();
    display.fillScreen(WHITE); // Screen blitzt weiß auf für Effekt
    display.setTextColor(BLACK);
    display.setCursor(10, 25);
    display.setTextSize(2);
    display.println("EXECUTING");
    display.display();

    // Signal an Python schicken
    Serial.println("EXECUTE:shutdown");
    
    delay(3000); // 3 Sek warten damit man den Effekt sieht

    // Reset Display
    display.clearDisplay();
    display.fillScreen(BLACK);
    display.setTextColor(WHITE);
    display.setTextSize(1);
    display.setCursor(0, 5);
    display.println("ESP32 SYSTEM V1.0");
    display.println("---------------------");
    display.setTextSize(2);
    display.setCursor(0, 30);
    display.println("READY TO");
    display.println("DEPLOY");
    display.display();
  }
}
