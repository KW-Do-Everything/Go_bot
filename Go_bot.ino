#include <Dynamixel2Arduino.h>

#if defined(ARDUINO_OpenCR)
#define DXL_SERIAL   Serial3
#define DEBUG_SERIAL Serial
const uint8_t DXL_DIR_PIN = 84; // OpenCR Board's DIR PIN.
#endif

const uint8_t DXL_ID_1 = 5;
const uint8_t DXL_ID_2 = 6;
const float DXL_PROTOCOL_VERSION = 1.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

using namespace ControlTableItem;

void setup() {
  // put your setup code here, to run once:

  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);

  // Set Port baudrate to 57600bps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(1000000);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
  dxl.ping(DXL_ID_1);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID_1);
  dxl.setOperatingMode(DXL_ID_1, OP_VELOCITY);
  dxl.torqueOn(DXL_ID_1);

  dxl.ping(DXL_ID_2);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID_2);
  dxl.setOperatingMode(DXL_ID_2, OP_VELOCITY);
  dxl.torqueOn(DXL_ID_2);
}

void loop()
{
  char input=' '; 
  if (Serial.available()) {
    input = Serial.read();
  }

  if(input=='a') dxl.setGoalVelocity(DXL_ID_1, 1523);
  if(input=='d') dxl.setGoalVelocity(DXL_ID_1, 500);
  if(input=='w') dxl.setGoalVelocity(DXL_ID_2, 1523);
  if(input=='s') dxl.setGoalVelocity(DXL_ID_2, 500);
  if(input=='q') dxl.setGoalVelocity(DXL_ID_1, 0);
  if(input=='q') dxl.setGoalVelocity(DXL_ID_2, 0);
}