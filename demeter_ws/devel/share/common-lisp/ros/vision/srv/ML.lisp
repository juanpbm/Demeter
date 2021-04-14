; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude ML-request.msg.html

(cl:defclass <ML-request> (roslisp-msg-protocol:ros-message)
  ((Left_Img
    :reader Left_Img
    :initarg :Left_Img
    :type sensor_msgs-msg:CompressedImage
    :initform (cl:make-instance 'sensor_msgs-msg:CompressedImage)))
)

(cl:defclass ML-request (<ML-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ML-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ML-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<ML-request> is deprecated: use vision-srv:ML-request instead.")))

(cl:ensure-generic-function 'Left_Img-val :lambda-list '(m))
(cl:defmethod Left_Img-val ((m <ML-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:Left_Img-val is deprecated.  Use vision-srv:Left_Img instead.")
  (Left_Img m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ML-request>) ostream)
  "Serializes a message object of type '<ML-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Left_Img) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ML-request>) istream)
  "Deserializes a message object of type '<ML-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Left_Img) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ML-request>)))
  "Returns string type for a service object of type '<ML-request>"
  "vision/MLRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ML-request)))
  "Returns string type for a service object of type 'ML-request"
  "vision/MLRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ML-request>)))
  "Returns md5sum for a message object of type '<ML-request>"
  "4972fcc8dd87e24ab9b33086558f9dc5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ML-request)))
  "Returns md5sum for a message object of type 'ML-request"
  "4972fcc8dd87e24ab9b33086558f9dc5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ML-request>)))
  "Returns full string definition for message of type '<ML-request>"
  (cl:format cl:nil "sensor_msgs/CompressedImage Left_Img~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ML-request)))
  "Returns full string definition for message of type 'ML-request"
  (cl:format cl:nil "sensor_msgs/CompressedImage Left_Img~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ML-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Left_Img))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ML-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ML-request
    (cl:cons ':Left_Img (Left_Img msg))
))
;//! \htmlinclude ML-response.msg.html

(cl:defclass <ML-response> (roslisp-msg-protocol:ros-message)
  ((Percentage
    :reader Percentage
    :initarg :Percentage
    :type cl:float
    :initform 0.0))
)

(cl:defclass ML-response (<ML-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ML-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ML-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<ML-response> is deprecated: use vision-srv:ML-response instead.")))

(cl:ensure-generic-function 'Percentage-val :lambda-list '(m))
(cl:defmethod Percentage-val ((m <ML-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:Percentage-val is deprecated.  Use vision-srv:Percentage instead.")
  (Percentage m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ML-response>) ostream)
  "Serializes a message object of type '<ML-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'Percentage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ML-response>) istream)
  "Deserializes a message object of type '<ML-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Percentage) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ML-response>)))
  "Returns string type for a service object of type '<ML-response>"
  "vision/MLResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ML-response)))
  "Returns string type for a service object of type 'ML-response"
  "vision/MLResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ML-response>)))
  "Returns md5sum for a message object of type '<ML-response>"
  "4972fcc8dd87e24ab9b33086558f9dc5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ML-response)))
  "Returns md5sum for a message object of type 'ML-response"
  "4972fcc8dd87e24ab9b33086558f9dc5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ML-response>)))
  "Returns full string definition for message of type '<ML-response>"
  (cl:format cl:nil "float32 Percentage~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ML-response)))
  "Returns full string definition for message of type 'ML-response"
  (cl:format cl:nil "float32 Percentage~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ML-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ML-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ML-response
    (cl:cons ':Percentage (Percentage msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ML)))
  'ML-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ML)))
  'ML-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ML)))
  "Returns string type for a service object of type '<ML>"
  "vision/ML")