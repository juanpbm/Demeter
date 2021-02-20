;; Auto-generated. Do not edit!


(when (boundp 'vision::Recognition_Rec)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'Recognition_Rec (find-package "VISION")))
(unless (find-package "VISION::RECOGNITION_REC")
  (make-package "VISION::RECOGNITION_REC"))
(unless (find-package "VISION::RECOGNITION_RECREQUEST")
  (make-package "VISION::RECOGNITION_RECREQUEST"))
(unless (find-package "VISION::RECOGNITION_RECRESPONSE")
  (make-package "VISION::RECOGNITION_RECRESPONSE"))

(in-package "ROS")

(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))




(defclass vision::Recognition_RecRequest
  :super ros::object
  :slots (_left_Img _right_Img ))

(defmethod vision::Recognition_RecRequest
  (:init
   (&key
    ((:left_Img __left_Img) (instance sensor_msgs::CompressedImage :init))
    ((:right_Img __right_Img) (instance sensor_msgs::CompressedImage :init))
    )
   (send-super :init)
   (setq _left_Img __left_Img)
   (setq _right_Img __right_Img)
   self)
  (:left_Img
   (&rest __left_Img)
   (if (keywordp (car __left_Img))
       (send* _left_Img __left_Img)
     (progn
       (if __left_Img (setq _left_Img (car __left_Img)))
       _left_Img)))
  (:right_Img
   (&rest __right_Img)
   (if (keywordp (car __right_Img))
       (send* _right_Img __right_Img)
     (progn
       (if __right_Img (setq _right_Img (car __right_Img)))
       _right_Img)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/CompressedImage _left_Img
    (send _left_Img :serialization-length)
    ;; sensor_msgs/CompressedImage _right_Img
    (send _right_Img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/CompressedImage _left_Img
       (send _left_Img :serialize s)
     ;; sensor_msgs/CompressedImage _right_Img
       (send _right_Img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/CompressedImage _left_Img
     (send _left_Img :deserialize buf ptr-) (incf ptr- (send _left_Img :serialization-length))
   ;; sensor_msgs/CompressedImage _right_Img
     (send _right_Img :deserialize buf ptr-) (incf ptr- (send _right_Img :serialization-length))
   ;;
   self)
  )

(defclass vision::Recognition_RecResponse
  :super ros::object
  :slots (_coordinates ))

(defmethod vision::Recognition_RecResponse
  (:init
   (&key
    ((:coordinates __coordinates) (make-array 4 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _coordinates __coordinates)
   self)
  (:coordinates
   (&optional __coordinates)
   (if __coordinates (setq _coordinates __coordinates)) _coordinates)
  (:serialization-length
   ()
   (+
    ;; float32[4] _coordinates
    (* 4    4)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[4] _coordinates
     (dotimes (i 4)
       (sys::poke (elt _coordinates i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[4] _coordinates
   (dotimes (i (length _coordinates))
     (setf (elt _coordinates i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;;
   self)
  )

(defclass vision::Recognition_Rec
  :super ros::object
  :slots ())

(setf (get vision::Recognition_Rec :md5sum-) "524aec0a2d224648b866e7ced15102d4")
(setf (get vision::Recognition_Rec :datatype-) "vision/Recognition_Rec")
(setf (get vision::Recognition_Rec :request) vision::Recognition_RecRequest)
(setf (get vision::Recognition_Rec :response) vision::Recognition_RecResponse)

(defmethod vision::Recognition_RecRequest
  (:response () (instance vision::Recognition_RecResponse :init)))

(setf (get vision::Recognition_RecRequest :md5sum-) "524aec0a2d224648b866e7ced15102d4")
(setf (get vision::Recognition_RecRequest :datatype-) "vision/Recognition_RecRequest")
(setf (get vision::Recognition_RecRequest :definition-)
      "sensor_msgs/CompressedImage left_Img
sensor_msgs/CompressedImage right_Img

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
float32[4] coordinates 

")

(setf (get vision::Recognition_RecResponse :md5sum-) "524aec0a2d224648b866e7ced15102d4")
(setf (get vision::Recognition_RecResponse :datatype-) "vision/Recognition_RecResponse")
(setf (get vision::Recognition_RecResponse :definition-)
      "sensor_msgs/CompressedImage left_Img
sensor_msgs/CompressedImage right_Img

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
float32[4] coordinates 

")



(provide :vision/Recognition_Rec "524aec0a2d224648b866e7ced15102d4")


