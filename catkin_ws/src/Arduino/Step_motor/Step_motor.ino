#include <AccelStepper.h>
#include <ros.h>
#include <std_msgs/Int32.h>

const int stepPin = 3;
const int dirPin = 4;
const int enPin = 5;
const int limitSwitchPin0 = 7;  // Pin cho công tắc hành trình tại 0 độ
const int limitSwitchPin180 = 8; // Pin cho công tắc hành trình tại 180 độ

AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);
ros::NodeHandle nh;
std_msgs::Int32 angle_msg;
ros::Publisher pub("step_motor_angle", &angle_msg);

int current_angle = -1;  // Giá trị ban đầu không xác định
bool homing_done = false; // Biến để xác định xem quá trình homing đã hoàn thành chưa

void setup() {
  pinMode(enPin, OUTPUT);
  pinMode(limitSwitchPin0, INPUT_PULLUP);
  pinMode(limitSwitchPin180, INPUT_PULLUP);

  Serial.begin(9600);
  nh.initNode();
  nh.advertise(pub);

  // Kích hoạt động cơ
  digitalWrite(enPin, LOW);

  stepper.setMaxSpeed(50);
  stepper.setAcceleration(30);
  
  // Bắt đầu quay ngược chiều kim đồng hồ để tìm vị trí ban đầu
  stepper.moveTo(-10000);
}

void loop() {
  if (!homing_done) {
    // Quay liên tục để tìm vị trí ban đầu
    stepper.run();
    checkLimitSwitches();
  } else {
    // Quay động cơ từ 0 đến 180 độ và ngược lại
    if (stepper.distanceToGo() == 0) {
      if (stepper.currentPosition() == 0) {
        stepper.moveTo(180);
      } else if (stepper.currentPosition() == 180) {
        stepper.moveTo(0);
      }
    }
    stepper.run();
    checkLimitSwitches();
  }
  nh.spinOnce();
}

void checkLimitSwitches() {
  if (digitalRead(limitSwitchPin0) == LOW) {
    stepper.setCurrentPosition(0);  // Thiết lập vị trí hiện tại là 0 độ
    current_angle = 0;
    publishAngle();
    homing_done = true;
    stepper.moveTo(180);  // Quay ngược lại
  } 
  else if (digitalRead(limitSwitchPin180) == LOW) {
    stepper.setCurrentPosition(180);  // Thiết lập vị trí hiện tại là 180 độ
    current_angle = 180;
    publishAngle();
    homing_done = true;
    stepper.moveTo(0);  // Quay ngược lại
  }
}

void publishAngle() {
  angle_msg.data = current_angle;
  pub.publish(&angle_msg);
  nh.spinOnce();
}
