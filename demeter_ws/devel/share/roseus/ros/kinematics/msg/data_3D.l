;; Auto-generated. Do not edit!


(when (boundp 'kinematics::data_3D)
  (if (not (find-package "KINEMATICS"))
    (make-package "KINEMATICS"))
  (shadow 'data_3D (find-package "KINEMATICS")))
(unless (find-package "KINEMATICS::DATA_3D")
  (make-package "KINEMATICS::DATA_3D"))

(in-package "ROS")
;;//! \htmlinclude data_3D.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass kinematics::data_3D
  :super ros::object
  :slots (_center _top _bottom ))

(defmethod kinematics::data_3D
  (:init
   (&key
    ((:center __center) (instance geometry_msgs::Point :init))
    ((:top __top) (instance geometry_msgs::Point :init))
    ((:bottom __bottom) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _center __center)
   (setq _top __top)
   (setq _bottom __bottom)
   self)
  (:center
   (&rest __center)
   (if (keywordp (car __center))
       (send* _center __center)
     (progn
       (if __center (setq _center (car __center)))
       _center)))
  (:top
   (&rest __top)
   (if (keywordp (car __top))
       (send* _top __top)
     (progn
       (if __top (setq _top (car __top)))
       _top)))
  (:bottom
   (&rest __bottom)
   (if (keywordp (car __bottom))
       (send* _bottom __bottom)
     (progn
       (if __bottom (setq _bottom (car __bottom)))
       _bottom)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _center
    (send _center :serialization-length)
    ;; geometry_msgs/Point _top
    (send _top :serialization-length)
    ;; geometry_msgs/Point _bottom
    (send _bottom :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _center
       (send _center :serialize s)
     ;; geometry_msgs/Point _top
       (send _top :serialize s)
     ;; geometry_msgs/Point _bottom
       (send _bottom :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _center
     (send _center :deserialize buf ptr-) (incf ptr- (send _center :serialization-length))
   ;; geometry_msgs/Point _top
     (send _top :deserialize buf ptr-) (incf ptr- (send _top :serialization-length))
   ;; geometry_msgs/Point _bottom
     (send _bottom :deserialize buf ptr-) (incf ptr- (send _bottom :serialization-length))
   ;;
   self)
  )

(setf (get kinematics::data_3D :md5sum-) "6ac37e820af93783df7652e7b435f796")
(setf (get kinematics::data_3D :datatype-) "kinematics/data_3D")
(setf (get kinematics::data_3D :definition-)
      "geometry_msgs/Point center
geometry_msgs/Point top
geometry_msgs/Point bottom

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :kinematics/data_3D "6ac37e820af93783df7652e7b435f796")


