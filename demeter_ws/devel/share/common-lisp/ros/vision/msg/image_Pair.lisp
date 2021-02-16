; Auto-generated. Do not edit!


(cl:in-package vision-msg)


;//! \htmlinclude image_Pair.msg.html

(cl:defclass <image_Pair> (roslisp-msg-protocol:ros-message)
  ((center
    :reader center
    :initarg :center
    :type (cl:vector cl:float)
   :initform (cl:make-array 4 :element-type 'cl:float :initial-element 0.0))
   (left_Img
    :reader left_Img
    :initarg :left_Img
    :type sensor_msgs-msg:CompressedImage
    :initform (cl:make-instance 'sensor_msgs-msg:CompressedImage))
   (right_Img
    :reader right_Img
    :initarg :right_Img
    :type sensor_msgs-msg:CompressedImage
    :initform (cl:make-instance 'sensor_msgs-msg:CompressedImage)))
)

(cl:defclass image_Pair (<image_Pair>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <image_Pair>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'image_Pair)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-msg:<image_Pair> is deprecated: use vision-msg:image_Pair instead.")))

(cl:ensure-generic-function 'center-val :lambda-list '(m))
(cl:defmethod center-val ((m <image_Pair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:center-val is deprecated.  Use vision-msg:center instead.")
  (center m))

(cl:ensure-generic-function 'left_Img-val :lambda-list '(m))
(cl:defmethod left_Img-val ((m <image_Pair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:left_Img-val is deprecated.  Use vision-msg:left_Img instead.")
  (left_Img m))

(cl:ensure-generic-function 'right_Img-val :lambda-list '(m))
(cl:defmethod right_Img-val ((m <image_Pair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:right_Img-val is deprecated.  Use vision-msg:right_Img instead.")
  (right_Img m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <image_Pair>) ostream)
  "Serializes a message object of type '<image_Pair>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'center))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'left_Img) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'right_Img) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <image_Pair>) istream)
  "Deserializes a message object of type '<image_Pair>"
  (cl:setf (cl:slot-value msg 'center) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'center)))
    (cl:dotimes (i 4)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'left_Img) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'right_Img) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<image_Pair>)))
  "Returns string type for a message object of type '<image_Pair>"
  "vision/image_Pair")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'image_Pair)))
  "Returns string type for a message object of type 'image_Pair"
  "vision/image_Pair")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<image_Pair>)))
  "Returns md5sum for a message object of type '<image_Pair>"
  "b64fa04f706d93801fa4dc20bbfdd0fa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'image_Pair)))
  "Returns md5sum for a message object of type 'image_Pair"
  "b64fa04f706d93801fa4dc20bbfdd0fa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<image_Pair>)))
  "Returns full string definition for message of type '<image_Pair>"
  (cl:format cl:nil "float32[4] center~%sensor_msgs/CompressedImage left_Img~%sensor_msgs/CompressedImage right_Img~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'image_Pair)))
  "Returns full string definition for message of type 'image_Pair"
  (cl:format cl:nil "float32[4] center~%sensor_msgs/CompressedImage left_Img~%sensor_msgs/CompressedImage right_Img~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <image_Pair>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'center) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'left_Img))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'right_Img))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <image_Pair>))
  "Converts a ROS message object to a list"
  (cl:list 'image_Pair
    (cl:cons ':center (center msg))
    (cl:cons ':left_Img (left_Img msg))
    (cl:cons ':right_Img (right_Img msg))
))
