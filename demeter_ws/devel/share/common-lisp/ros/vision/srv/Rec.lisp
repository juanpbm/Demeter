; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Rec-request.msg.html

(cl:defclass <Rec-request> (roslisp-msg-protocol:ros-message)
  ((left_Img
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

(cl:defclass Rec-request (<Rec-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Rec-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Rec-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Rec-request> is deprecated: use vision-srv:Rec-request instead.")))

(cl:ensure-generic-function 'left_Img-val :lambda-list '(m))
(cl:defmethod left_Img-val ((m <Rec-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:left_Img-val is deprecated.  Use vision-srv:left_Img instead.")
  (left_Img m))

(cl:ensure-generic-function 'right_Img-val :lambda-list '(m))
(cl:defmethod right_Img-val ((m <Rec-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:right_Img-val is deprecated.  Use vision-srv:right_Img instead.")
  (right_Img m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Rec-request>) ostream)
  "Serializes a message object of type '<Rec-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'left_Img) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'right_Img) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Rec-request>) istream)
  "Deserializes a message object of type '<Rec-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'left_Img) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'right_Img) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Rec-request>)))
  "Returns string type for a service object of type '<Rec-request>"
  "vision/RecRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Rec-request)))
  "Returns string type for a service object of type 'Rec-request"
  "vision/RecRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Rec-request>)))
  "Returns md5sum for a message object of type '<Rec-request>"
  "524aec0a2d224648b866e7ced15102d4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Rec-request)))
  "Returns md5sum for a message object of type 'Rec-request"
  "524aec0a2d224648b866e7ced15102d4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Rec-request>)))
  "Returns full string definition for message of type '<Rec-request>"
  (cl:format cl:nil "sensor_msgs/CompressedImage left_Img~%sensor_msgs/CompressedImage right_Img~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Rec-request)))
  "Returns full string definition for message of type 'Rec-request"
  (cl:format cl:nil "sensor_msgs/CompressedImage left_Img~%sensor_msgs/CompressedImage right_Img~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Rec-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'left_Img))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'right_Img))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Rec-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Rec-request
    (cl:cons ':left_Img (left_Img msg))
    (cl:cons ':right_Img (right_Img msg))
))
;//! \htmlinclude Rec-response.msg.html

(cl:defclass <Rec-response> (roslisp-msg-protocol:ros-message)
  ((coordinates
    :reader coordinates
    :initarg :coordinates
    :type (cl:vector cl:float)
   :initform (cl:make-array 4 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Rec-response (<Rec-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Rec-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Rec-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Rec-response> is deprecated: use vision-srv:Rec-response instead.")))

(cl:ensure-generic-function 'coordinates-val :lambda-list '(m))
(cl:defmethod coordinates-val ((m <Rec-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:coordinates-val is deprecated.  Use vision-srv:coordinates instead.")
  (coordinates m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Rec-response>) ostream)
  "Serializes a message object of type '<Rec-response>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'coordinates))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Rec-response>) istream)
  "Deserializes a message object of type '<Rec-response>"
  (cl:setf (cl:slot-value msg 'coordinates) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'coordinates)))
    (cl:dotimes (i 4)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Rec-response>)))
  "Returns string type for a service object of type '<Rec-response>"
  "vision/RecResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Rec-response)))
  "Returns string type for a service object of type 'Rec-response"
  "vision/RecResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Rec-response>)))
  "Returns md5sum for a message object of type '<Rec-response>"
  "524aec0a2d224648b866e7ced15102d4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Rec-response)))
  "Returns md5sum for a message object of type 'Rec-response"
  "524aec0a2d224648b866e7ced15102d4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Rec-response>)))
  "Returns full string definition for message of type '<Rec-response>"
  (cl:format cl:nil "float32[4] coordinates ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Rec-response)))
  "Returns full string definition for message of type 'Rec-response"
  (cl:format cl:nil "float32[4] coordinates ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Rec-response>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'coordinates) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Rec-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Rec-response
    (cl:cons ':coordinates (coordinates msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Rec)))
  'Rec-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Rec)))
  'Rec-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Rec)))
  "Returns string type for a service object of type '<Rec>"
  "vision/Rec")