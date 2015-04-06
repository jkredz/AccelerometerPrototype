//Maxim Integrated Max4618 Multiplexer

int B = 0;      
int A = 0;  // the two digital pins for the bits     

String data;
String data1;

 
/* Truth Table      
 B A On Switches
 0 0 X0,Y0 (Left x-accel , Right x-accel) green
 0 1 X1,Y1 (Left y-accel , Right y-accel) yellow
 1 0 X2,Y2 (Left z-accel , Right z-accel) red
 1 1 X3,Y3 (Chest x,y,z accel, N/A)
 
 
 */
int  bin [] = {00, 01, 10, 11};//list of binary values
 
void setup(){
 
  //Pin output
  pinMode(10, OUTPUT);    // B
  pinMode(11, OUTPUT);    // A
  
  //Acc Sensor Input Setup
  pinMode(0, OUTPUT); //Leg Left input
  pinMode(1, OUTPUT); //Leg Right input
  pinMode(2, OUTPUT); //Ankle Left input
  pinMode(3, OUTPUT); //Ankle Right input
  pinMode(5, OUTPUT); //Thigh Left input
  pinMode(6, OUTPUT); //Thigh Right input
  
  Serial.begin(9600); // fire up the serial
  Serial.println("Left Leg X, Right Leg X, Left Ankle X, Right Ankle X, Left Thigh X, Right Thigh X; Left Leg Y, Right Leg Y, Left Ankle Y, Right Ankle Y, Left Thigh Y, Right Thigh Y; Left Leg Z, Right Leg Z, Left Ankle Z, Right Ankle Z, Left Thigh Z, Right Thigh Z");  
  
}
 
  
void loop () {
 for (int count=0; count < 4; count++) { //loop through each channel, checking for a signal
    
   int row = bin[count]; //channel 5 = 5th element in the bin list -> 101 etc. 
   Serial.print("Truth Table BA: ");
   Serial.println(row);
   B = bitRead(row,1); //bitRead() -> parameter 1 = binary sequence, parameter 2 = which bit to read, starting from the right most bit
   Serial.print("B: ");
   Serial.println(B);
   A = bitRead(row,0); //channel 7 = 111, 1 = 2nd bit 
   Serial.print("A: ");
   Serial.println(A);
 
 
   digitalWrite(10, B); // send the bits to the digital pins 
   digitalWrite(11, A);
   
   Serial.print("Accelerometer Axis: ");
   if (count == 0) {
     Serial.println("X green");
   }
   else if (count == 1) {
     Serial.println("Y yellow");
   }
   else if (count ==2) {
     Serial.println("Z red");
   }
   else if (count == 3) {
     Serial.println("X,Y,Z");
   }
     
   
   
   int x[6];
   
   for (int sensor=0; sensor < 7; sensor++){ //loop through reading each accelerometer sensor data
     Serial.print("Sensor: ");
     Serial.println(sensor);
     digitalWrite(sensor, 1);
     delay(1000);
     digitalWrite(sensor, 0);
     //data=String(analogRead(sensor));
     data1 += data + " , ";
     Serial.println(data1);
   }
   
  
  data1= data1 + "; ";
 }
 Serial.println(data1);
 data1="";  
 delay (1000); // time to read the values
}
 
 
