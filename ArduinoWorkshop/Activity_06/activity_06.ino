// Credit to DFRobot for this functional code.
// I have only modified variable names and commenting for readability.
// Last modified: 6/06/2024 2:50PM
// By: Tom @ Auchmuty Library MakerSpace

int buttonPin = 2;          // Digital pin the button is attached to
int relayPin = 3;           // Digital pin the relay is attached to

int relayState = HIGH;      // Initial state for the relay
int buttonState;            // Initial state for the button
int lastButtonState = LOW;  // Previous state for the button

long debounceTime = 0;  // Debounce Time
long debounceDelay = 50;    // Amount of Debounce delay

void setup()
{
  pinMode(buttonPin, INPUT);  // Input is button
  pinMode(relayPin, OUTPUT);  // Output is relay

  digitalWrite(relayPin, relayState); // Close the relay
}
void loop()
{
   // Read the state of the button
  int value = digitalRead(buttonPin);

  // If the new value is different to the last value
  if (value != lastButtonState)
  {
    // Begin a timer
    debounceTime = millis();
  }

  // If 50ms has elapsed since the button was pressed
  if ((millis() - debounceTime) > debounceDelay)
  {
    // Check if the current state of the button is different to the saved state 
    if (value != buttonState)
    {
      // Update saved state to current state  
      buttonState = value;

      // Check if the change in button state was HIGH (press), instead of LOW (release)
      if (buttonState == HIGH)
      {
        // Toggle the current saved relay state
        relayState = !relayState;
      }
    }
  }

  // Write saved Relay state to the digital output pin
  digitalWrite(relayPin, relayState);

  // Store the current button state for the next pass of the loop
  lastButtonState = value;
}
