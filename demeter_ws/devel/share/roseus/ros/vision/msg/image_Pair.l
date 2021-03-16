;; Auto-generated. Do not edit!


(when (boundp 'vision::image_Pair)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'image_Pair (find-package "VISION")))
(unless (find-package "VISION::IMAGE_PAIR")
  (make-package "VISION::IMAGE_PAIR"))

(in-package "ROS")
;;//! \htmlinclude image_Pair.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass vision::image_Pair
  :super ros::object
  :slots (_coordinates _Left_Img _Right_Img ))

(defmethod vision::image_Pair
  (:init
   (&key
    ((:coordinates __coordinates) (make-array 4 :initial-element 0.0 :element-type :float))
    ((:Left_Img __Left_Img) (instance sensor_msgs::CompressedImage :init))
    ((:Right_Img __Right_Img) (instance sensor_msgs::CompressedImage :init))
    )
   (send-super :init)
   (setq _coordinates __coordinates)
   (setq _Left_Img __Left_Img)
   (setq _Right_Img __Right_Img)
   self)
  (:coordinates
   (&optional __coordinates)
   (if __coordinates (setq _coordinates __coordinates)) _coordinates)
  (:Left_Img
   (&rest __Left_Img)
   (if (keywordp (car __Left_Img))
       (send* _Left_Img __Left_Img)
     (progn
       (if __Left_Img (setq _Left_Img (car __Left_Img)))
       _Left_Img)))
  (:Right_Img
   (&rest __Right_Img)
   (if (keywordp (car __Right_Img))
       (send* _Right_Img __Right_Img)
     (progn
       (if __Right_Img (setq _Right_Img (car __Right_Img)))
       _Right_Img)))
  (:serialization-length
   ()
   (+
    ;; float32[4] _coordinates
    (* 4    4)
    ;; sensor_msgs/CompressedImage _Left_Img
    (send _Left_Img :serialization-length)
    ;; sensor_msgs/CompressedImage _Right_Img
    (send _Right_Img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[4] _coordinates
     (dotimes (i 4)
       (sys::poke (elt _coordinates i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; sensor_msgs/CompressedImage _Left_Img
       (send _Left_Img :serialize s)
     ;; sensor_msgs/CompressedImage _Right_Img
       (send _Right_Img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[4] _coordinates
   (dotimes (i (length _coordinates))
     (setf (elt _coordinates i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; sensor_msgs/CompressedImage _Left_Img
     (send _Left_Img :deserialize buf ptr-) (incf ptr- (send _Left_Img :serialization-length))
   ;; sensor_msgs/CompressedImage _Right_Img
     (send _Right_Img :deserialize buf ptr-) (incf ptr- (send _Right_Img :serialization-length))
   ;;
   self)
  )

(setf (get vision::image_Pair :md5sum-) "3be3bcf9d563c8bf7eb1783df2858352")
(setf (get vision::image_Pair :datatype-) "vision/image_Pair")
(setf (get vision::image_Pair :definition-)
      "float32[4] coordinates
sensor_msgs/CompressedImage Left_Img
sensor_msgs/CompressedImage Right_Img

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

")



(provide :vision/image_Pair "3be3bcf9d563c8bf7eb1783df2858352")


