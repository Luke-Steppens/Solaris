#include "esp_camera.h"
#include <WiFi.h>

// Replace these with your network credentials
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

// Camera configuration (for AI-Thinker ESP32-CAM)
camera_config_t config;

void startCameraServer();

void setup() {
  Serial.begin(115200);
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi...");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  
  // Wi-Fi connected
  Serial.println();
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());  // Print the ESP32-CAM's IP address
  
  // Camera configuration (adjust pins based on your ESP32-CAM model)
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_pwdn = 32;
  config.pin_reset = -1;  // No reset pin on this board
  config.pin_xclk = 0;
  config.pin_sscb_sda = 26;
  config.pin_sscb_scl = 27;
  config.pin_d7 = 36;
  config.pin_d6 = 39;
  config.pin_d5 = 34;
  config.pin_d4 = 35;
  config.pin_d3 = 21;
  config.pin_d2 = 19;
  config.pin_d1 = 18;
  config.pin_d0 = 5;
  config.pin_vsync = 25;
  config.pin_href = 23;
  config.pin_pclk = 22;
  
  // Camera settings
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_SVGA;
  config.jpeg_quality = 12;
  config.fb_count = 1;
  
  // Initialize the camera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.println("Camera init failed");
    return;
  }
  
  // Start the camera server
  startCameraServer();
}

void loop() {
  delay(1);
}

// Start the camera server to stream video
void startCameraServer() {
  WiFiServer server(80);
  server.begin();
  Serial.println("HTTP server started");

  while (true) {
    WiFiClient client = server.available();
    
    if (!client) {
      return;
    }
    
    String request = client.readStringUntil('\r');
    client.flush();
    
    // Stream video (MJPEG format)
    if (request.indexOf("GET /stream") >= 0) {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: multipart/x-mixed-replace; boundary=frame");
      client.println();
      
      while (true) {
        // Capture a frame from the camera
        camera_fb_t *fb = esp_camera_fb_get();
        
        if (!fb) {
          Serial.println("Failed to capture image");
          return;
        }
        
        client.println("--frame");
        client.println("Content-Type: image/jpeg");
        client.println("Content-Length: " + String(fb->len));
        client.println();
        
        // Send the image data
        client.write(fb->buf, fb->len);
        
        client.println();
        esp_camera_fb_return(fb);  // Return the frame buffer to be reused
        
        delay(100);  // Limit the frame rate
      }
    }
    
    client.stop();
  }
}
