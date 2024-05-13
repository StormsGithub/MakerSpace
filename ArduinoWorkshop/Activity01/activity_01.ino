// Using Digital Pin 11 to control the LED
int LED_Pin = 11;

void setup()
{
  // Set up pin to output
  pinMode(LED_Pin, OUTPUT);
}

void loop()
{
  // Write HIGH signal to digital pin
  digitalWrite(LED_Pin, HIGH);
}
