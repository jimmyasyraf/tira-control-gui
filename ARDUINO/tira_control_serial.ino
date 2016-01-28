#include <Servo.h> 

Servo servo1, servo2, servo3, servo4a, servo4b, servo5; 
  

const unsigned int BAUD_RATE = 9600;

int incomingByte;
int angle1 = 90;
int angle2 = 170;
int angle3 = 90;
int angle4a = 100;
int angle4b = 60;
int angle5 = 90;

void setup() {
  servo1.attach(2);  
  servo2.attach(4); 
  servo3.attach(6);
  servo4a.attach(8);
  servo4b.attach(10);
  servo5.attach(12);
  servo1.write(angle1);
  servo2.write(angle2);
  servo3.write(angle3);
  servo4a.write(angle4a);
  servo4b.write(angle4b);
  servo5.write(angle5);
  
  Serial.begin(BAUD_RATE);
}

void loop() {
  if (Serial.available()) {
     incomingByte = Serial.read();
     if (incomingByte == 'j') 
     {       
       angle1 = angle1 - 5;
            servo1.write(angle1);          
            delay(100);                   
         }
      
     else if (incomingByte == 'k') 
     {                  
          angle1 = angle1 + 5;       
            servo1.write(angle1);         
            delay(100);                      
         
     }
     else if (incomingByte == 'l') 
     {       
            angle1 = 90;       
            servo1.write(angle1);         
            delay(100);                      
         
     }
     else if (incomingByte == 'f') 
     { // up           
      angle2 = angle2 - 5;     
            servo2.write(angle2);          
            delay(100);                        
         } 
     else if (incomingByte == 'g') 
     { // down         
     angle2 = angle2 + 5;
            servo2.write(angle2);            
            delay(100);                       
         }
     else if (incomingByte == 'h') 
     { // up           
      angle2 = 170;     
            servo2.write(angle2);          
            delay(100);                        
         } 
     else if (incomingByte == 'a') 
     { // up           
      angle3 = 65;     
            servo3.write(angle3);          
            delay(100);                        
         }
     else if (incomingByte == 's') 
     { // up           
      angle3 = 115;     
            servo3.write(angle3);          
            delay(100);                        
         }
     else if (incomingByte == 'd') 
     { // up           
      angle3 = 90;     
            servo3.write(angle3);          
            delay(100);                        
         }
     else if (incomingByte == 'q') 
     { // down         
     angle4a = angle4a - 3;
     servo4a.write(angle4a);
     angle4b = angle4b + 3;
     servo4b.write(angle4b);
     delay(100);                       
         }
     else if (incomingByte == 'w') 
     { // down         
     angle4a = angle4a + 3;
     servo4a.write(angle4a);
     angle4b = angle4b - 3;
     servo4b.write(angle4b);
     delay(100);                       
         }
     else if (incomingByte == 'e') 
     { // down         
     angle4a = 100;
     servo4a.write(angle4a);
     angle4b = 60;
     servo4b.write(angle4b);
     delay(100);                       
         }
     else if (incomingByte == 'r') 
     { // down         
     angle5 = angle5 + 5;
            servo5.write(angle5);            
            delay(100);                       
         }
     else if (incomingByte == 't') 
     { // down         
     angle5 = angle5 - 5;
            servo5.write(angle5);            
            delay(100);                       
         }
     else if (incomingByte == 'y') 
     { // down         
     angle5 = 90;
            servo5.write(angle5);            
            delay(100);                       
         }
   }
}

