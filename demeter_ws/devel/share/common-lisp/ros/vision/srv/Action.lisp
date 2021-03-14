; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Action-request.msg.html

(cl:defclass <Action-request> (roslisp-msg-protocol:ros-message)
  ((Action
    :reader Action
    :initarg :Action
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Action-request (<Action-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Action-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Action-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Action-request> is deprecated: use vision-srv:Action-request instead.")))

(cl:ensure-generic-function 'Action-val :lambda-list '(m))
(cl:defmethod Action-val ((m <Action-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:Action-val is deprecated.  Use vision-srv:Action instead.")
  (Action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Action-request>) ostream)
  "Serializes a message object of type '<Action-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Action) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Action-request>) istream)
  "Deserializes a message object of type '<Action-request>"
    (cl:setf (cl:slot-value msg 'Action) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Action-request>)))
  "Returns string type for a service object of type '<Action-request>"
  "vision/ActionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Action-request)))
  "Returns string type for a service object of type 'Action-request"
  "vision/ActionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Action-request>)))
  "Returns md5sum for a message object of type '<Action-request>"
  "48a9460ec0cc64685337f3762768aa1d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Action-request)))
  "Returns md5sum for a message object of type 'Action-request"
  "48a9460ec0cc64685337f3762768aa1d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Action-request>)))
  "Returns full string definition for message of type '<Action-request>"
  (cl:format cl:nil "bool Action ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Action-request)))
  "Returns full string definition for message of type 'Action-request"
  (cl:format cl:nil "bool Action ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Action-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Action-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Action-request
    (cl:cons ':Action (Action msg))
))
;//! \htmlinclude Action-response.msg.html

(cl:defclass <Action-response> (roslisp-msg-protocol:ros-message)
  ((Ack
    :reader Ack
    :initarg :Ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Action-response (<Action-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Action-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Action-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Action-response> is deprecated: use vision-srv:Action-response instead.")))

(cl:ensure-generic-function 'Ack-val :lambda-list '(m))
(cl:defmethod Ack-val ((m <Action-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:Ack-val is deprecated.  Use vision-srv:Ack instead.")
  (Ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Action-response>) ostream)
  "Serializes a message object of type '<Action-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Action-response>) istream)
  "Deserializes a message object of type '<Action-response>"
    (cl:setf (cl:slot-value msg 'Ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Action-response>)))
  "Returns string type for a service object of type '<Action-response>"
  "vision/ActionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Action-response)))
  "Returns string type for a service object of type 'Action-response"
  "vision/ActionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Action-response>)))
  "Returns md5sum for a message object of type '<Action-response>"
  "48a9460ec0cc64685337f3762768aa1d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Action-response)))
  "Returns md5sum for a message object of type 'Action-response"
  "48a9460ec0cc64685337f3762768aa1d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Action-response>)))
  "Returns full string definition for message of type '<Action-response>"
  (cl:format cl:nil "bool Ack ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Action-response)))
  "Returns full string definition for message of type 'Action-response"
  (cl:format cl:nil "bool Ack ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Action-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Action-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Action-response
    (cl:cons ':Ack (Ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Action)))
  'Action-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Action)))
  'Action-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Action)))
  "Returns string type for a service object of type '<Action>"
  "vision/Action")