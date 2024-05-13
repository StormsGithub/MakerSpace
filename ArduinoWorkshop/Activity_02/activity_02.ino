// Using Digital Pin 11 to control the LED
int LED_Pin = 11;

void setup()
{
  // Set up pin to output
  pinMode(LED_Pin, OUTPUT);
}

void loop()
{
  // analogWrite creates a PWM output
  // on the specified pin. Range: 0-255
  analogWrite(LED_Pin, 100);
}
