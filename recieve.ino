void setup() 
{
  pinMode(13,OUTPUT);
  digitalWrite(13,HIGH);  
  Serial.begin(9600);
}

void e() {
  digitalWrite(13,HIGH);
  loop();
}

void loop() 
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'o')
    {
      digitalWrite(13,LOW);
      delay(100);
    }
    if(Serial.read() == 'e')
    {
      e();
    }
    
  }  

    else
    {
      digitalWrite(13,HIGH);
    }
}
