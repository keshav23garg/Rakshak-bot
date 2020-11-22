int left = 0;

int right = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);

}

void loop()
{
  digitalWrite(3,LOW);
  digitalWrite(2,LOW);
  // measure the ping time in cm
  right = 0.01723 * readUltrasonicDistance(7, 7);
  left = 0.01723 * readUltrasonicDistance(6, 6);
  if(right - left > 10){
    Serial.println("Right turn");
    digitalWrite(2,HIGH);
  }else if(left - right > 10){
    Serial.println("Left turn");
    digitalWrite(3,HIGH);
  }delay(100); 
}