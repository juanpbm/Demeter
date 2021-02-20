;; Auto-generated. Do not edit!


(when (boundp 'vision::Take_Img)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'Take_Img (find-package "VISION")))
(unless (find-package "VISION::TAKE_IMG")
  (make-package "VISION::TAKE_IMG"))
(unless (find-package "VISION::TAKE_IMGREQUEST")
  (make-package "VISION::TAKE_IMGREQUEST"))
(unless (find-package "VISION::TAKE_IMGRESPONSE")
  (make-package "VISION::TAKE_IMGRESPONSE"))

(in-package "ROS")





(defclass vision::Take_ImgRequest
  :super ros::object
  :slots ())

(defmethod vision::Take_ImgRequest
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

(defclass vision::Take_ImgResponse
  :super ros::object
  :slots ())

(defmethod vision::Take_ImgResponse
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

(defclass vision::Take_Img
  :super ros::object
  :slots ())

(setf (get vision::Take_Img :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Take_Img :datatype-) "vision/Take_Img")
(setf (get vision::Take_Img :request) vision::Take_ImgRequest)
(setf (get vision::Take_Img :response) vision::Take_ImgResponse)

(defmethod vision::Take_ImgRequest
  (:response () (instance vision::Take_ImgResponse :init)))

(setf (get vision::Take_ImgRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Take_ImgRequest :datatype-) "vision/Take_ImgRequest")
(setf (get vision::Take_ImgRequest :definition-)
      "
---
")

(setf (get vision::Take_ImgResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Take_ImgResponse :datatype-) "vision/Take_ImgResponse")
(setf (get vision::Take_ImgResponse :definition-)
      "
---
")



(provide :vision/Take_Img "d41d8cd98f00b204e9800998ecf8427e")


