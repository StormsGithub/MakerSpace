int buzzerPin = 10;   // Digital pin the buzzer is attached to
int buzzerTone = 750; // Frequency to play back

double value;         // Initialise variable to hold value from LM35
double temperature;   // Initialise variable to hold calibrated temperature

void setup()
{
  pinMode(buzzerPin, OUTPUT); // Initialise Buzzer pin
  Serial.begin(9600);         // Initialise serial monitoring
}

void loop()
{
  value = analogRead(0);      // Read in value from LM35
  temperature = (double(value) * (5.0 / 10.23));  // Convert from mV to Celsius

  // If the temperature is greater than 29 degrees, sound the alarm
  if(temperature > 29)
  {
    tone(buzzerPin, buzzerTone);
  }
  // Otherwise, turn off the alarm
  else
  {    
   noTone(buzzerPin);
  }

  // Print the current temperature to the serial monitor so we can watch it :)
  Serial.print("Current Temperature: ");
  Serial.print(temperature);
  Serial.println("C");

  delay(500);   // Only run every 500 milliseconds
}
