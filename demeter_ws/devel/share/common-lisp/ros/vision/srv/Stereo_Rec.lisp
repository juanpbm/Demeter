; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Stereo_Rec-request.msg.html

(cl:defclass <Stereo_Rec-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Stereo_Rec-request (<Stereo_Rec-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Stereo_Rec-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Stereo_Rec-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Stereo_Rec-request> is deprecated: use vision-srv:Stereo_Rec-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Stereo_Rec-request>) ostream)
  "Serializes a message object of type '<Stereo_Rec-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Stereo_Rec-request>) istream)
  "Deserializes a message object of type '<Stereo_Rec-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Stereo_Rec-request>)))
  "Returns string type for a service object of type '<Stereo_Rec-request>"
  "vision/Stereo_RecRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Stereo_Rec-request)))
  "Returns string type for a service object of type 'Stereo_Rec-request"
  "vision/Stereo_RecRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Stereo_Rec-request>)))
  "Returns md5sum for a message object of type '<Stereo_Rec-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Stereo_Rec-request)))
  "Returns md5sum for a message object of type 'Stereo_Rec-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Stereo_Rec-request>)))
  "Returns full string definition for message of type '<Stereo_Rec-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Stereo_Rec-request)))
  "Returns full string definition for message of type 'Stereo_Rec-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Stereo_Rec-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Stereo_Rec-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Stereo_Rec-request
))
;//! \htmlinclude Stereo_Rec-response.msg.html

(cl:defclass <Stereo_Rec-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Stereo_Rec-response (<Stereo_Rec-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Stereo_Rec-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Stereo_Rec-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Stereo_Rec-response> is deprecated: use vision-srv:Stereo_Rec-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Stereo_Rec-response>) ostream)
  "Serializes a message object of type '<Stereo_Rec-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Stereo_Rec-response>) istream)
  "Deserializes a message object of type '<Stereo_Rec-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Stereo_Rec-response>)))
  "Returns string type for a service object of type '<Stereo_Rec-response>"
  "vision/Stereo_RecResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Stereo_Rec-response)))
  "Returns string type for a service object of type 'Stereo_Rec-response"
  "vision/Stereo_RecResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Stereo_Rec-response>)))
  "Returns md5sum for a message object of type '<Stereo_Rec-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Stereo_Rec-response)))
  "Returns md5sum for a message object of type 'Stereo_Rec-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Stereo_Rec-response>)))
  "Returns full string definition for message of type '<Stereo_Rec-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Stereo_Rec-response)))
  "Returns full string definition for message of type 'Stereo_Rec-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Stereo_Rec-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Stereo_Rec-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Stereo_Rec-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Stereo_Rec)))
  'Stereo_Rec-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Stereo_Rec)))
  'Stereo_Rec-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Stereo_Rec)))
  "Returns string type for a service object of type '<Stereo_Rec>"
  "vision/Stereo_Rec")