; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Harvest-request.msg.html

(cl:defclass <Harvest-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Harvest-request (<Harvest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Harvest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Harvest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Harvest-request> is deprecated: use vision-srv:Harvest-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Harvest-request>) ostream)
  "Serializes a message object of type '<Harvest-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Harvest-request>) istream)
  "Deserializes a message object of type '<Harvest-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Harvest-request>)))
  "Returns string type for a service object of type '<Harvest-request>"
  "vision/HarvestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Harvest-request)))
  "Returns string type for a service object of type 'Harvest-request"
  "vision/HarvestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Harvest-request>)))
  "Returns md5sum for a message object of type '<Harvest-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Harvest-request)))
  "Returns md5sum for a message object of type 'Harvest-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Harvest-request>)))
  "Returns full string definition for message of type '<Harvest-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Harvest-request)))
  "Returns full string definition for message of type 'Harvest-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Harvest-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Harvest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Harvest-request
))
;//! \htmlinclude Harvest-response.msg.html

(cl:defclass <Harvest-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Harvest-response (<Harvest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Harvest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Harvest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Harvest-response> is deprecated: use vision-srv:Harvest-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Harvest-response>) ostream)
  "Serializes a message object of type '<Harvest-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Harvest-response>) istream)
  "Deserializes a message object of type '<Harvest-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Harvest-response>)))
  "Returns string type for a service object of type '<Harvest-response>"
  "vision/HarvestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Harvest-response)))
  "Returns string type for a service object of type 'Harvest-response"
  "vision/HarvestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Harvest-response>)))
  "Returns md5sum for a message object of type '<Harvest-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Harvest-response)))
  "Returns md5sum for a message object of type 'Harvest-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Harvest-response>)))
  "Returns full string definition for message of type '<Harvest-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Harvest-response)))
  "Returns full string definition for message of type 'Harvest-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Harvest-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Harvest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Harvest-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Harvest)))
  'Harvest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Harvest)))
  'Harvest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Harvest)))
  "Returns string type for a service object of type '<Harvest>"
  "vision/Harvest")