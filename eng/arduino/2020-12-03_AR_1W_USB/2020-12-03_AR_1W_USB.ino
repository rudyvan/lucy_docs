
/*
 2020-12-03_Arduino_1wire-incoming:
 by Rudy Vandenberghe

 The arduino is supposed to be connected to a Raspberry PI through a USB cable.

 The Arduino monitors pull up input lines and a 1w input and send serial output: 
 - if iButtons are sensed on the 1wire pin and then sends the 1w=xxx\n with xxx being the iButton code.
   The iButton code repeats only every 5 seconds
 - if the pull up input line change state then sends ix=y\n  with x the input 0 or 1 and y the state 0 or 1

 Serial commands can also be sent to the Arduino:
 - input request:    ix\n  with x the input 0 or 1  --> returns ix=y\n  with x the input 0 or 1 and y the state 0 or 1
 - output set request: ox=y\n with x the output 0 or 1 and x the desired state 0 or 1

 If the Arduino cannot recognise the serial request, then ?\n is returned

Learnings sofar:
1.do not use power through usb AND use external power. Some devices need lots of power, then disconnect 5V power line feed from usb
2.use a 4.7KOhm resistor between the white 1w reader pin and 5V
3.do not use Strings as function parameters, they seem to blow up the heap memory and that is not mentioned enough anywhere
*/

#include <SPI.h>            // needed for Arduino versions later than 0018
#include <OneWire.h>        // one wire magic
#include <elapsedMillis.h>  // a timer library

/* iButton reader */
const int w1_1w_pin    = 6; // loxone reader wire white AND do not forget to connect this pin with 4,7K ohm resistor to 5V
// int grnd_pin     = // loxone reader wire yellow and grey
OneWire ds(w1_1w_pin);
String was_button="";
String cur_button="";
elapsedMillis since_button = 0;

/* inputs/ outputs */
int nr_out_pins = 2;     // !! arrays below should have this number of elements
int out_pins[] = {12, 13};
int out_state[] = {HIGH, HIGH};
int nr_in_pins = 2;      // !! arrays below should have this number of elements
int in_pins[] = {2, 4};
int in_state[] = {0, 0}; 

String i_str="ix=y";
String o_str="ox=y";

/* serial in/out */
String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  /* initialise serial */
  Serial.begin(38400);
  inputString.reserve(200);
  /* initialise inputs */
  for (byte i = 0; i < nr_in_pins; i = i + 1) {
    pinMode(in_pins[i], INPUT_PULLUP); // sets the digital pin as input
    in_state[i] = digitalRead(in_pins[i]); // reads the initial state 
  }
  /* initialise outputs */
  for (byte i = 0; i < nr_out_pins; i = i + 1) {
    pinMode(out_pins[i], OUTPUT); // sets the digital pin as output
    digitalWrite(out_pins[i], out_state[i]); // sets the initial output state  
  }
}

int mk_button(uint8_t *data, uint8_t length){ // prints 8-bit data in hex and paches up cur_button
 char tmp[length*2+1];
 byte first;
 int j=0;
 for (uint8_t i=0; i<length; i++) 
 {
   first = (data[length-i] >> 4) | 48;
   if (first > 57) tmp[j] = first + (byte)7;  // add 39 for small cap
   else tmp[j] = first ;
   j++;

   first = (data[length-i] & 0x0F) | 48;
   if (first > 57) tmp[j] = first + (byte)7; 
   else tmp[j] = first;
   j++;
 }
 tmp[length*2] = 0;
 cur_button=tmp;
}

int print_button(){
 Serial.print("w0="); 
 Serial.println(cur_button);
}

int lp_button() {
  byte i;
  byte data[20];
  byte addr[20];
  if (since_button >= 3000) { // allow same button reread only after 5 seconds
    if (was_button != "") { was_button="";}
    since_button=0;}
  // 3. any iButtons detected?
  for (uint8_t i=0; i<16; i++) {addr[i]=0x00;}
  if (!ds.search(addr)) {
    ds.reset_search();
    return 0;
  }  
  // 4.we have an iButton!
  mk_button(addr,8); // it assigns cur_button
  if ( OneWire::crc8( addr, 7) != addr[7]) { return 0;} //CRC is not valid!
  // 5. right family??
  if (addr[8] != 0x00) {return 0;} //is not a 1Button family device
  // 6. now check if this is a new button or we can have a repeat button
  if (cur_button!=was_button) {
    since_button=0; was_button=cur_button;
    print_button(); // it prints the button  
  } // else duplicate button read cancelled
}

int latch_in(){ // read input and send serial message if it changes
  for (byte i = 0; i < nr_in_pins; i = i + 1) {
    int new_state = digitalRead(in_pins[i]); // read the initial state
    if (new_state!=in_state[i]) {   // new state then report
      i_str[1]='0'+i;
      i_str[3]='0'+new_state;
      Serial.println(i_str);
      in_state[i]=new_state;
    }
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

int latch_serial(){
  if (stringComplete){
    if (inputString[0]=='i') {
      int pin=inputString[1]-'0';
      if (pin < nr_in_pins) {
        i_str[1]=inputString[1];
        i_str[3]='0'+in_state[pin];
        Serial.println(i_str);
        } else {
          Serial.println("?");          
      }
    } else if (inputString[0]=='o' && inputString[2]=='=') {
      int pin = inputString[1]-'0';
      if (pin < nr_out_pins) {
        int pin_state=inputString[3]-'0';
        digitalWrite(out_pins[pin],pin_state);
        Serial.print(inputString);
      } else {
        Serial.println("?");          
      }
    } else {Serial.println("?");}     
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

void loop(void) {
  lp_button();  // 1wire button reader
  latch_in();   // sample inputs 
  latch_serial(); // read serial and do outputs
}
