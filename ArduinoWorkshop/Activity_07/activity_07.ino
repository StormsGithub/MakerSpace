
int raw_data;           // Holds the raw data from LM35 sensor.
double temperature;     // Holds the converted temperature data from LM35 sensor.

int relay_pin = 3;      // Digital pin the relay is attached to.
int relay_state = HIGH; // Initial state of relay.

void setup()
{
  pinMode(3, OUTPUT); // Output is relay. 
  Serial.begin(9600); // Begin serial monitoring.
}

void loop()
{
  // Read raw data from LM35 temperature sensor.
  raw_data = analogRead(0);
  // Convert raw data to celsius using conversion factor (data * 5 / 10.24).
  temperature = (double) raw_data * (5/10.24);

  // Check if the current temperature has exceeded 26 degrees celsius.
  // Must do an additional check that the temperature is not >100 (junk data).
  if (temperature > 26 && temperature < 100)
  {
    // If the relay state is set so the fan is off, then toggle the relay to enable the fan.
    relay_state = LOW;
  }
  // Else, check the sensor has cooled to below 24c, then disable the relay.
  // Must do an additional check that the temperature is not ~0 (junk data).
  else if (temperature < 24 && temperature > 1)
  {
    relay_state = HIGH;
  }

  // Write current state to relay.
  digitalWrite(relay_pin, relay_state);

  // Print the current temperature to the serial monitor.
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("C");

  // Run the program once every half a second.
  delay(500);
}
