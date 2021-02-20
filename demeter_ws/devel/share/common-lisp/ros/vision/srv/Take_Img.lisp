; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Take_Img-request.msg.html

(cl:defclass <Take_Img-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Take_Img-request (<Take_Img-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Take_Img-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Take_Img-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Take_Img-request> is deprecated: use vision-srv:Take_Img-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Take_Img-request>) ostream)
  "Serializes a message object of type '<Take_Img-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Take_Img-request>) istream)
  "Deserializes a message object of type '<Take_Img-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Take_Img-request>)))
  "Returns string type for a service object of type '<Take_Img-request>"
  "vision/Take_ImgRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Take_Img-request)))
  "Returns string type for a service object of type 'Take_Img-request"
  "vision/Take_ImgRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Take_Img-request>)))
  "Returns md5sum for a message object of type '<Take_Img-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Take_Img-request)))
  "Returns md5sum for a message object of type 'Take_Img-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Take_Img-request>)))
  "Returns full string definition for message of type '<Take_Img-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Take_Img-request)))
  "Returns full string definition for message of type 'Take_Img-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Take_Img-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Take_Img-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Take_Img-request
))
;//! \htmlinclude Take_Img-response.msg.html

(cl:defclass <Take_Img-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Take_Img-response (<Take_Img-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Take_Img-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Take_Img-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Take_Img-response> is deprecated: use vision-srv:Take_Img-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Take_Img-response>) ostream)
  "Serializes a message object of type '<Take_Img-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Take_Img-response>) istream)
  "Deserializes a message object of type '<Take_Img-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Take_Img-response>)))
  "Returns string type for a service object of type '<Take_Img-response>"
  "vision/Take_ImgResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Take_Img-response)))
  "Returns string type for a service object of type 'Take_Img-response"
  "vision/Take_ImgResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Take_Img-response>)))
  "Returns md5sum for a message object of type '<Take_Img-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Take_Img-response)))
  "Returns md5sum for a message object of type 'Take_Img-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Take_Img-response>)))
  "Returns full string definition for message of type '<Take_Img-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Take_Img-response)))
  "Returns full string definition for message of type 'Take_Img-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Take_Img-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Take_Img-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Take_Img-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Take_Img)))
  'Take_Img-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Take_Img)))
  'Take_Img-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Take_Img)))
  "Returns string type for a service object of type '<Take_Img>"
  "vision/Take_Img")