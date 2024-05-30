// Frequency to play back
int tone_Val = 700;

// Use a variable to store the pin number,
// So we can use a descriptive name to refer to it.
int buzzer_Pin = 10;

void setup()
{
  // Set pin to output
  pinMode(buzzer_Pin, OUTPUT);
}

void loop()
{
  tone(buzzer_Pin, tone_Val);
}
