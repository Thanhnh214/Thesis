#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry
import tf
from geometry_msgs.msg import Quaternion

class StepMotorOdom:
    def __init__(self):
        rospy.init_node('step_motor_odom')
        self.angle_sub = rospy.Subscriber('/step_motor_angle', Int32, self.angle_callback)
        self.odom_pub = rospy.Publisher('/step_motor_odom', Odometry, queue_size=10)
        self.angle = 0

    def angle_callback(self, msg):
        rospy.loginfo("Received angle: %d", msg.data)
        self.angle = msg.data
        self.publish_odom()

    def publish_odom(self):
        odom = Odometry()
        odom.header.stamp = rospy.Time.now()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"

        # Giả định rằng động cơ bước không di chuyển theo x, y, z
        odom.pose.pose.position.x = 0.0
        odom.pose.pose.position.y = 0.0
        odom.pose.pose.position.z = 0.0

        # Tính toán quaternion từ góc yaw
        quaternion = tf.transformations.quaternion_from_euler(0, 0, self.angle * (3.14 / 180.0))
        odom.pose.pose.orientation = Quaternion(*quaternion)

        # Giả định rằng không có vận tốc tuyến tính và góc quay
        odom.twist.twist.linear.x = 0.0
        odom.twist.twist.linear.y = 0.0
        odom.twist.twist.linear.z = 0.0
        odom.twist.twist.angular.x = 0.0
        odom.twist.twist.angular.y = 0.0
        odom.twist.twist.angular.z = 0.0

        rospy.loginfo("Publishing odom")
        self.odom_pub.publish(odom)

if __name__ == '__main__':
    try:
        StepMotorOdom()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass