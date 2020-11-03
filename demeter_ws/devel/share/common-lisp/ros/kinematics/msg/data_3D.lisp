; Auto-generated. Do not edit!


(cl:in-package kinematics-msg)


;//! \htmlinclude data_3D.msg.html

(cl:defclass <data_3D> (roslisp-msg-protocol:ros-message)
  ((center
    :reader center
    :initarg :center
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (top
    :reader top
    :initarg :top
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (bottom
    :reader bottom
    :initarg :bottom
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass data_3D (<data_3D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <data_3D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'data_3D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinematics-msg:<data_3D> is deprecated: use kinematics-msg:data_3D instead.")))

(cl:ensure-generic-function 'center-val :lambda-list '(m))
(cl:defmethod center-val ((m <data_3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinematics-msg:center-val is deprecated.  Use kinematics-msg:center instead.")
  (center m))

(cl:ensure-generic-function 'top-val :lambda-list '(m))
(cl:defmethod top-val ((m <data_3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinematics-msg:top-val is deprecated.  Use kinematics-msg:top instead.")
  (top m))

(cl:ensure-generic-function 'bottom-val :lambda-list '(m))
(cl:defmethod bottom-val ((m <data_3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinematics-msg:bottom-val is deprecated.  Use kinematics-msg:bottom instead.")
  (bottom m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <data_3D>) ostream)
  "Serializes a message object of type '<data_3D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'center) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'top) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'bottom) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <data_3D>) istream)
  "Deserializes a message object of type '<data_3D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'center) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'top) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'bottom) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<data_3D>)))
  "Returns string type for a message object of type '<data_3D>"
  "kinematics/data_3D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'data_3D)))
  "Returns string type for a message object of type 'data_3D"
  "kinematics/data_3D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<data_3D>)))
  "Returns md5sum for a message object of type '<data_3D>"
  "6ac37e820af93783df7652e7b435f796")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'data_3D)))
  "Returns md5sum for a message object of type 'data_3D"
  "6ac37e820af93783df7652e7b435f796")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<data_3D>)))
  "Returns full string definition for message of type '<data_3D>"
  (cl:format cl:nil "geometry_msgs/Point center~%geometry_msgs/Point top~%geometry_msgs/Point bottom~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'data_3D)))
  "Returns full string definition for message of type 'data_3D"
  (cl:format cl:nil "geometry_msgs/Point center~%geometry_msgs/Point top~%geometry_msgs/Point bottom~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <data_3D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'center))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'top))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'bottom))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <data_3D>))
  "Converts a ROS message object to a list"
  (cl:list 'data_3D
    (cl:cons ':center (center msg))
    (cl:cons ':top (top msg))
    (cl:cons ':bottom (bottom msg))
))
