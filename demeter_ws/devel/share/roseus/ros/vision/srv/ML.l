;; Auto-generated. Do not edit!


(when (boundp 'vision::ML)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'ML (find-package "VISION")))
(unless (find-package "VISION::ML")
  (make-package "VISION::ML"))
(unless (find-package "VISION::MLREQUEST")
  (make-package "VISION::MLREQUEST"))
(unless (find-package "VISION::MLRESPONSE")
  (make-package "VISION::MLRESPONSE"))

(in-package "ROS")

(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))




(defclass vision::MLRequest
  :super ros::object
  :slots (_Left_Img ))

(defmethod vision::MLRequest
  (:init
   (&key
    ((:Left_Img __Left_Img) (instance sensor_msgs::CompressedImage :init))
    )
   (send-super :init)
   (setq _Left_Img __Left_Img)
   self)
  (:Left_Img
   (&rest __Left_Img)
   (if (keywordp (car __Left_Img))
       (send* _Left_Img __Left_Img)
     (progn
       (if __Left_Img (setq _Left_Img (car __Left_Img)))
       _Left_Img)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/CompressedImage _Left_Img
    (send _Left_Img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/CompressedImage _Left_Img
       (send _Left_Img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/CompressedImage _Left_Img
     (send _Left_Img :deserialize buf ptr-) (incf ptr- (send _Left_Img :serialization-length))
   ;;
   self)
  )

(defclass vision::MLResponse
  :super ros::object
  :slots (_Percentage ))

(defmethod vision::MLResponse
  (:init
   (&key
    ((:Percentage __Percentage) 0.0)
    )
   (send-super :init)
   (setq _Percentage (float __Percentage))
   self)
  (:Percentage
   (&optional __Percentage)
   (if __Percentage (setq _Percentage __Percentage)) _Percentage)
  (:serialization-length
   ()
   (+
    ;; float32 _Percentage
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _Percentage
       (sys::poke _Percentage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _Percentage
     (setq _Percentage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass vision::ML
  :super ros::object
  :slots ())

(setf (get vision::ML :md5sum-) "4972fcc8dd87e24ab9b33086558f9dc5")
(setf (get vision::ML :datatype-) "vision/ML")
(setf (get vision::ML :request) vision::MLRequest)
(setf (get vision::ML :response) vision::MLResponse)

(defmethod vision::MLRequest
  (:response () (instance vision::MLResponse :init)))

(setf (get vision::MLRequest :md5sum-) "4972fcc8dd87e24ab9b33086558f9dc5")
(setf (get vision::MLRequest :datatype-) "vision/MLRequest")
(setf (get vision::MLRequest :definition-)
      "sensor_msgs/CompressedImage Left_Img

================================================================================
MSG: sensor_msgs/CompressedImage
# This message contains a compressed image

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image

string format        # Specifies the format of the data
                     #   Acceptable values:
                     #     jpeg, png
uint8[] data         # Compressed image buffer

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
---
float32 Percentage

")

(setf (get vision::MLResponse :md5sum-) "4972fcc8dd87e24ab9b33086558f9dc5")
(setf (get vision::MLResponse :datatype-) "vision/MLResponse")
(setf (get vision::MLResponse :definition-)
      "sensor_msgs/CompressedImage Left_Img

================================================================================
MSG: sensor_msgs/CompressedImage
# This message contains a compressed image

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image

string format        # Specifies the format of the data
                     #   Acceptable values:
                     #     jpeg, png
uint8[] data         # Compressed image buffer

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
---
float32 Percentage

")



(provide :vision/ML "4972fcc8dd87e24ab9b33086558f9dc5")


