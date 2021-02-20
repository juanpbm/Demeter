; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Reposition-request.msg.html

(cl:defclass <Reposition-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Reposition-request (<Reposition-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Reposition-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Reposition-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Reposition-request> is deprecated: use vision-srv:Reposition-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Reposition-request>) ostream)
  "Serializes a message object of type '<Reposition-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Reposition-request>) istream)
  "Deserializes a message object of type '<Reposition-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Reposition-request>)))
  "Returns string type for a service object of type '<Reposition-request>"
  "vision/RepositionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reposition-request)))
  "Returns string type for a service object of type 'Reposition-request"
  "vision/RepositionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Reposition-request>)))
  "Returns md5sum for a message object of type '<Reposition-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Reposition-request)))
  "Returns md5sum for a message object of type 'Reposition-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Reposition-request>)))
  "Returns full string definition for message of type '<Reposition-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Reposition-request)))
  "Returns full string definition for message of type 'Reposition-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Reposition-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Reposition-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Reposition-request
))
;//! \htmlinclude Reposition-response.msg.html

(cl:defclass <Reposition-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Reposition-response (<Reposition-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Reposition-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Reposition-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Reposition-response> is deprecated: use vision-srv:Reposition-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Reposition-response>) ostream)
  "Serializes a message object of type '<Reposition-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Reposition-response>) istream)
  "Deserializes a message object of type '<Reposition-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Reposition-response>)))
  "Returns string type for a service object of type '<Reposition-response>"
  "vision/RepositionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reposition-response)))
  "Returns string type for a service object of type 'Reposition-response"
  "vision/RepositionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Reposition-response>)))
  "Returns md5sum for a message object of type '<Reposition-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Reposition-response)))
  "Returns md5sum for a message object of type 'Reposition-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Reposition-response>)))
  "Returns full string definition for message of type '<Reposition-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Reposition-response)))
  "Returns full string definition for message of type 'Reposition-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Reposition-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Reposition-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Reposition-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Reposition)))
  'Reposition-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Reposition)))
  'Reposition-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reposition)))
  "Returns string type for a service object of type '<Reposition>"
  "vision/Reposition")