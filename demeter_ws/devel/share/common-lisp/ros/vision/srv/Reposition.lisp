; Auto-generated. Do not edit!


(cl:in-package vision-srv)


;//! \htmlinclude Reposition-request.msg.html

(cl:defclass <Reposition-request> (roslisp-msg-protocol:ros-message)
  ((Location
    :reader Location
    :initarg :Location
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass Reposition-request (<Reposition-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Reposition-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Reposition-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Reposition-request> is deprecated: use vision-srv:Reposition-request instead.")))

(cl:ensure-generic-function 'Location-val :lambda-list '(m))
(cl:defmethod Location-val ((m <Reposition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:Location-val is deprecated.  Use vision-srv:Location instead.")
  (Location m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Reposition-request>) ostream)
  "Serializes a message object of type '<Reposition-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Location) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Reposition-request>) istream)
  "Deserializes a message object of type '<Reposition-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Location) istream)
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
  "47be5df2ac38fbdb1ce8731a7f11ea4b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Reposition-request)))
  "Returns md5sum for a message object of type 'Reposition-request"
  "47be5df2ac38fbdb1ce8731a7f11ea4b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Reposition-request>)))
  "Returns full string definition for message of type '<Reposition-request>"
  (cl:format cl:nil "~%geometry_msgs/Vector3 Location ~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Reposition-request)))
  "Returns full string definition for message of type 'Reposition-request"
  (cl:format cl:nil "~%geometry_msgs/Vector3 Location ~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Reposition-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Location))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Reposition-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Reposition-request
    (cl:cons ':Location (Location msg))
))
;//! \htmlinclude Reposition-response.msg.html

(cl:defclass <Reposition-response> (roslisp-msg-protocol:ros-message)
  ((Ack
    :reader Ack
    :initarg :Ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Reposition-response (<Reposition-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Reposition-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Reposition-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-srv:<Reposition-response> is deprecated: use vision-srv:Reposition-response instead.")))

(cl:ensure-generic-function 'Ack-val :lambda-list '(m))
(cl:defmethod Ack-val ((m <Reposition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-srv:Ack-val is deprecated.  Use vision-srv:Ack instead.")
  (Ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Reposition-response>) ostream)
  "Serializes a message object of type '<Reposition-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Reposition-response>) istream)
  "Deserializes a message object of type '<Reposition-response>"
    (cl:setf (cl:slot-value msg 'Ack) (cl:not (cl:zerop (cl:read-byte istream))))
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
  "47be5df2ac38fbdb1ce8731a7f11ea4b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Reposition-response)))
  "Returns md5sum for a message object of type 'Reposition-response"
  "47be5df2ac38fbdb1ce8731a7f11ea4b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Reposition-response>)))
  "Returns full string definition for message of type '<Reposition-response>"
  (cl:format cl:nil "bool Ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Reposition-response)))
  "Returns full string definition for message of type 'Reposition-response"
  (cl:format cl:nil "bool Ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Reposition-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Reposition-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Reposition-response
    (cl:cons ':Ack (Ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Reposition)))
  'Reposition-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Reposition)))
  'Reposition-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reposition)))
  "Returns string type for a service object of type '<Reposition>"
  "vision/Reposition")