// Using Digital Pins 12, 11, and 10 to control the RGB LED
int LED_R_Channel = 10;
int LED_B_Channel = 11;
int LED_G_Channel = 12;

void setup()
{
  // Set up pin to output
  pinMode(LED_R_Channel, OUTPUT);
  pinMode(LED_B_Channel, OUTPUT);
  pinMode(LED_G_Channel, OUTPUT);
}

void loop()
{
  // Use analogWrite to set the Red and Blue channel
  // To their maximum values to make purple
  analogWrite(LED_R_Channel, 255);
  analogWrite(LED_B_Channel, 255);
}
