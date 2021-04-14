;; Auto-generated. Do not edit!


(when (boundp 'vision::Reposition)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'Reposition (find-package "VISION")))
(unless (find-package "VISION::REPOSITION")
  (make-package "VISION::REPOSITION"))
(unless (find-package "VISION::REPOSITIONREQUEST")
  (make-package "VISION::REPOSITIONREQUEST"))
(unless (find-package "VISION::REPOSITIONRESPONSE")
  (make-package "VISION::REPOSITIONRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass vision::RepositionRequest
  :super ros::object
  :slots (_Location ))

(defmethod vision::RepositionRequest
  (:init
   (&key
    ((:Location __Location) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _Location __Location)
   self)
  (:Location
   (&rest __Location)
   (if (keywordp (car __Location))
       (send* _Location __Location)
     (progn
       (if __Location (setq _Location (car __Location)))
       _Location)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _Location
    (send _Location :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _Location
       (send _Location :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _Location
     (send _Location :deserialize buf ptr-) (incf ptr- (send _Location :serialization-length))
   ;;
   self)
  )

(defclass vision::RepositionResponse
  :super ros::object
  :slots (_Ack ))

(defmethod vision::RepositionResponse
  (:init
   (&key
    ((:Ack __Ack) nil)
    )
   (send-super :init)
   (setq _Ack __Ack)
   self)
  (:Ack
   (&optional (__Ack :null))
   (if (not (eq __Ack :null)) (setq _Ack __Ack)) _Ack)
  (:serialization-length
   ()
   (+
    ;; bool _Ack
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _Ack
       (if _Ack (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _Ack
     (setq _Ack (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass vision::Reposition
  :super ros::object
  :slots ())

(setf (get vision::Reposition :md5sum-) "47be5df2ac38fbdb1ce8731a7f11ea4b")
(setf (get vision::Reposition :datatype-) "vision/Reposition")
(setf (get vision::Reposition :request) vision::RepositionRequest)
(setf (get vision::Reposition :response) vision::RepositionResponse)

(defmethod vision::RepositionRequest
  (:response () (instance vision::RepositionResponse :init)))

(setf (get vision::RepositionRequest :md5sum-) "47be5df2ac38fbdb1ce8731a7f11ea4b")
(setf (get vision::RepositionRequest :datatype-) "vision/RepositionRequest")
(setf (get vision::RepositionRequest :definition-)
      "
geometry_msgs/Point Location 

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
---
bool Ack

")

(setf (get vision::RepositionResponse :md5sum-) "47be5df2ac38fbdb1ce8731a7f11ea4b")
(setf (get vision::RepositionResponse :datatype-) "vision/RepositionResponse")
(setf (get vision::RepositionResponse :definition-)
      "
geometry_msgs/Point Location 

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
---
bool Ack

")



(provide :vision/Reposition "47be5df2ac38fbdb1ce8731a7f11ea4b")


