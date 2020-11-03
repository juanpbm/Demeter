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
  :slots (_center _top _bottom _left_Img _right_Img ))

(defmethod vision::image_Pair
  (:init
   (&key
    ((:center __center) (make-array 2 :initial-element 0.0 :element-type :float))
    ((:top __top) (make-array 2 :initial-element 0.0 :element-type :float))
    ((:bottom __bottom) (make-array 2 :initial-element 0.0 :element-type :float))
    ((:left_Img __left_Img) (instance sensor_msgs::CompressedImage :init))
    ((:right_Img __right_Img) (instance sensor_msgs::CompressedImage :init))
    )
   (send-super :init)
   (setq _center __center)
   (setq _top __top)
   (setq _bottom __bottom)
   (setq _left_Img __left_Img)
   (setq _right_Img __right_Img)
   self)
  (:center
   (&optional __center)
   (if __center (setq _center __center)) _center)
  (:top
   (&optional __top)
   (if __top (setq _top __top)) _top)
  (:bottom
   (&optional __bottom)
   (if __bottom (setq _bottom __bottom)) _bottom)
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
    ;; float32[2] _center
    (* 4    2)
    ;; float32[2] _top
    (* 4    2)
    ;; float32[2] _bottom
    (* 4    2)
    ;; sensor_msgs/CompressedImage _left_Img
    (send _left_Img :serialization-length)
    ;; sensor_msgs/CompressedImage _right_Img
    (send _right_Img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[2] _center
     (dotimes (i 2)
       (sys::poke (elt _center i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[2] _top
     (dotimes (i 2)
       (sys::poke (elt _top i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[2] _bottom
     (dotimes (i 2)
       (sys::poke (elt _bottom i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; sensor_msgs/CompressedImage _left_Img
       (send _left_Img :serialize s)
     ;; sensor_msgs/CompressedImage _right_Img
       (send _right_Img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[2] _center
   (dotimes (i (length _center))
     (setf (elt _center i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32[2] _top
   (dotimes (i (length _top))
     (setf (elt _top i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32[2] _bottom
   (dotimes (i (length _bottom))
     (setf (elt _bottom i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; sensor_msgs/CompressedImage _left_Img
     (send _left_Img :deserialize buf ptr-) (incf ptr- (send _left_Img :serialization-length))
   ;; sensor_msgs/CompressedImage _right_Img
     (send _right_Img :deserialize buf ptr-) (incf ptr- (send _right_Img :serialization-length))
   ;;
   self)
  )

(setf (get vision::image_Pair :md5sum-) "b1eeb80bf925ed72664782dd8a9603fe")
(setf (get vision::image_Pair :datatype-) "vision/image_Pair")
(setf (get vision::image_Pair :definition-)
      "float32[2] center
float32[2] top
float32[2] bottom
sensor_msgs/CompressedImage left_Img
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

")



(provide :vision/image_Pair "b1eeb80bf925ed72664782dd8a9603fe")


