#include <Arduino.h>
#include <stdio.h>

String readString;

void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps

  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);

}

void Send() {
  char ard_sends = '1';
  Serial.print("Arduino sends: ");
  Serial.println(ard_sends);
  Serial.print("\n");
  Serial.flush();
}

void loop()
{
  while(!Serial.available()) {}

  // serial read section
  while (Serial.available())
  {
    digitalWrite(8, HIGH);   // turn the LED on (HIGH is the voltage level)
    if (Serial.available() > 0)
    {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }

  if (readString.length() > 0)
  {
    digitalWrite(8, LOW);    // turn the LED off by making the voltage LOW
    Serial.print("Arduino received: ");  
    Serial.println(readString); //see what was received
  }

  for (unsigned int i = 0; i < readString.length(); i++) {

    // Set the current output digitalwire as the index + 8 (0 + 8 = 8, where the wires are hooked up)
    int output = i + 8;

    if (readString[i] == '1')
    {    
      digitalWrite(output, HIGH);
    }
    else
    {
      digitalWrite(output, LOW);
    }
  }

  delay(500); //Wait 500ms before sending

  // serial write section

  Send();
  
}