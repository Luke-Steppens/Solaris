#include <FastLED.h>
#include <Client.h>
// How many leds in your strip?
#define NUM_LEDS 40 //number of leds on light strip active
#define DATA_PIN 5 // middle pin

CRGB leds[NUM_LEDS];

void setup() { 
    Serial.begin(115200);
    FastLED.addLeds<WS2812, DATA_PIN, RGB>(leds, NUM_LEDS); //type of led used
    FastLED.setBrightness(100);
    
  }

void loop() { 
  // Turn the LED on, then pause
  while (Serial.available() > 0){
    if (Serial.readString() == "[ERROR]") {
     
        for (int i = 0 ;i <= 41; i++){
          leds[i].setRGB(0, 255 , 0); //GRB
          FastLED.show();
          delay(50);
          
        }
      
    }
    else{
      for (int i = 0 ;i <= 41; i++){
        leds[i].setRGB(250, 0 , 0); //GRB
        FastLED.show();
        delay(50);
      }
      Serial.end();

    }
  }
  if (Serial.available() == 0){
    for (int i = 0 ;i <= 41; i++){
          leds[i].setRGB(0, 255 , 0); //GRB
          FastLED.show();
          delay(50);
        }
  }
  
}