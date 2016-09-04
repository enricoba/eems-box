int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  Serial.println("ON");
  delay(2000);
  digitalWrite(ledPin, LOW);
  Serial.println("OFF");
  delay(2000);
}
