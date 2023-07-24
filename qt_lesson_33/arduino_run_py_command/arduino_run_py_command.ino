int incoming_data{0};

void blink_blue()
{ 
  for(int i=0; i<10; ++i)
  {
    digitalWrite(6, HIGH);
    delay(500);
    digitalWrite(6, LOW);
    delay(500);
 }
}

void blink_white()
{ 
  for(int i=0; i<10; ++i)
  {
    digitalWrite(4, HIGH);
    delay(500);
//    /millis();
    digitalWrite(4, LOW);
    delay(500);

//
//    event -> timer -> 2 sec
 }
}

void setup()
{
  pinMode(6, OUTPUT);
  pinMode(4, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  while(Serial.available())
  {
    incoming_data = Serial.read();
    if (incoming_data == '1')
    {
      digitalWrite(6, HIGH);
    }
    if (incoming_data == '0')
    {
      digitalWrite(6, LOW);
    }
    if (incoming_data == '2')
    {
      blink_blue();
    }
    if (incoming_data == '3')
    {
      blink_white();
    }
  }
}
