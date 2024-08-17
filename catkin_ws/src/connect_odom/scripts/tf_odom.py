#!/usr/bin/env python3
import rospy
import tf
import tf2_ros
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

class CameraOdomTransformer:
    def __init__(self):
        rospy.init_node('camera_odom_transformer')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        self.camera_odom_sub = rospy.Subscriber('/camera_odom', Odometry, self.camera_odom_callback)
        self.transformed_odom_pub = rospy.Publisher('/camera_odom_transformed', Odometry, queue_size=10)

    def camera_odom_callback(self, msg):
        try:
            # Lookup the transform from 'camera_frame' to 'base_link'
            transform = self.tf_buffer.lookup_transform('base_link', 'camera_frame', rospy.Time(0), rospy.Duration(1.0))

            # Transform the odometry data
            transformed_odom = self.transform_odom(msg, transform)

            # Publish the transformed odometry
            self.transformed_odom_pub.publish(transformed_odom)
        except tf2_ros.TransformException as ex:
            rospy.logwarn('Could not transform camera odom: {}'.format(ex))

    def transform_odom(self, odom, transform):
        # Apply the transform to the odometry pose
        transformed_odom = Odometry()
        transformed_odom.header.stamp = odom.header.stamp
        transformed_odom.header.frame_id = 'base_link'
        transformed_odom.child_frame_id = odom.child_frame_id

        # Transform the position
        transformed_odom.pose.pose.position.x = odom.pose.pose.position.x + transform.transform.translation.x
        transformed_odom.pose.pose.position.y = odom.pose.pose.position.y + transform.transform.translation.y
        transformed_odom.pose.pose.position.z = odom.pose.pose.position.z + transform.transform.translation.z

        # Transform the orientation
        transformed_orientation = tf.transformations.quaternion_multiply(
            [odom.pose.pose.orientation.x, odom.pose.pose.orientation.y, odom.pose.pose.orientation.z, odom.pose.pose.orientation.w],
            [transform.transform.rotation.x, transform.transform.rotation.y, transform.transform.rotation.z, transform.transform.rotation.w]
        )
        transformed_odom.pose.pose.orientation.x = transformed_orientation[0]
        transformed_odom.pose.pose.orientation.y = transformed_orientation[1]
        transformed_odom.pose.pose.orientation.z = transformed_orientation[2]
        transformed_odom.pose.pose.orientation.w = transformed_orientation[3]

        # Copy the twist data
        transformed_odom.twist = odom.twist

        return transformed_odom

if __name__ == '__main__':
    CameraOdomTransformer()
    rospy.spin()