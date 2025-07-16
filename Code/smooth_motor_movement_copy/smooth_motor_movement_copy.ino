#include <AccelStepper.h>
 
#define STEP_PIN        3
#define DIR_PIN         2
#define MAX_SPEED       2000
#define MAX_ACCEL       500

// Define a stepper and the pins it will use
AccelStepper stepper(2, STEP_PIN, DIR_PIN);

 // to change the speed (its a bit finicky)
void setup()
{  
    stepper.setMaxSpeed(1000);
    stepper.setAcceleration(3000);
}

 // for changing the length of one direction
 // currently goes back and forth 
void loop()
{    
    stepper.runToNewPosition(0);
    stepper.runToNewPosition(2000);
    

}