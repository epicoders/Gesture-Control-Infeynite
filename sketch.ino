#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>

// Create an instance for the MPU6050
MPU6050 mpu;

// Define the SoftwareSerial pins for HC-05 Bluetooth
SoftwareSerial BTSerial(2, 3);  // RX, TX

void setup() {
  Wire.begin();
  Serial.begin(9600);  // Start Serial communication for debugging
  BTSerial.begin(9600);  // Start Bluetooth communication

  // Initialize the MPU6050
  mpu.initialize();
  if (mpu.testConnection()) {
    Serial.println("MPU6050 connected successfully.");
  } else {
    Serial.println("MPU6050 connection failed.");
  }
}

void loop() {
  // Variables to store the accelerometer data
  int16_t ax, ay, az;
  
  // Read accelerometer data from the MPU6050
  mpu.getAcceleration(&ax, &ay, &az);
  
  // Detect gestures based on accelerometer data
  if (ax > 15000) {  // Move Right (threshold might need tuning)
    Serial.println("NEXT_TRACK");
    BTSerial.println("NEXT_TRACK");  // Send the command via Bluetooth
    delay(500); // Delay to prevent multiple detections for a single gesture
  } else if (ax < -15000) {  // Move Left
    Serial.println("PREV_TRACK");
    BTSerial.println("PREV_TRACK");
    delay(500);
  } else if (ay > 15000) {  // Move Up
    Serial.println("VOL_UP");
    BTSerial.println("VOL_UP");
    delay(500);
  } else if (ay < -15000) {  // Move Down
    Serial.println("VOL_DOWN");
    BTSerial.println("VOL_DOWN");
    delay(500);
  } else if (az > 20000) {  // Tap gesture (Z-axis movement as a tap)
    Serial.println("PLAY");
    BTSerial.println("PLAY");
    delay(500);
  }
  else if (az > -20000) {  // Tap gesture (Z-axis movement as a tap)
    Serial.println("PAUSE");
    BTSerial.println("PAUSE");
    delay(500);
  }

  delay(100);  // Loop delay, adjust as necessary

  /* Check if there's any data from the Bluetooth module
  if (BTSerial.available()) {
    String received = BTSerial.readString();
    Serial.println("Received via Bluetooth: " + received);
    // Handle the received Bluetooth commands if needed
  }*/
}