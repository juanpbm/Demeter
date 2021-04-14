;; Auto-generated. Do not edit!


(when (boundp 'vision::Stereo_Rec)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'Stereo_Rec (find-package "VISION")))
(unless (find-package "VISION::STEREO_REC")
  (make-package "VISION::STEREO_REC"))
(unless (find-package "VISION::STEREO_RECREQUEST")
  (make-package "VISION::STEREO_RECREQUEST"))
(unless (find-package "VISION::STEREO_RECRESPONSE")
  (make-package "VISION::STEREO_RECRESPONSE"))

(in-package "ROS")





(defclass vision::Stereo_RecRequest
  :super ros::object
  :slots ())

(defmethod vision::Stereo_RecRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass vision::Stereo_RecResponse
  :super ros::object
  :slots ())

(defmethod vision::Stereo_RecResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass vision::Stereo_Rec
  :super ros::object
  :slots ())

(setf (get vision::Stereo_Rec :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Stereo_Rec :datatype-) "vision/Stereo_Rec")
(setf (get vision::Stereo_Rec :request) vision::Stereo_RecRequest)
(setf (get vision::Stereo_Rec :response) vision::Stereo_RecResponse)

(defmethod vision::Stereo_RecRequest
  (:response () (instance vision::Stereo_RecResponse :init)))

(setf (get vision::Stereo_RecRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Stereo_RecRequest :datatype-) "vision/Stereo_RecRequest")
(setf (get vision::Stereo_RecRequest :definition-)
      "
---
")

(setf (get vision::Stereo_RecResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Stereo_RecResponse :datatype-) "vision/Stereo_RecResponse")
(setf (get vision::Stereo_RecResponse :definition-)
      "
---
")



(provide :vision/Stereo_Rec "d41d8cd98f00b204e9800998ecf8427e")


