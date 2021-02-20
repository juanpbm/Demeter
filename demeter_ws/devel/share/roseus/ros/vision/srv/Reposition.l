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





(defclass vision::RepositionRequest
  :super ros::object
  :slots ())

(defmethod vision::RepositionRequest
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

(defclass vision::RepositionResponse
  :super ros::object
  :slots ())

(defmethod vision::RepositionResponse
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

(defclass vision::Reposition
  :super ros::object
  :slots ())

(setf (get vision::Reposition :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Reposition :datatype-) "vision/Reposition")
(setf (get vision::Reposition :request) vision::RepositionRequest)
(setf (get vision::Reposition :response) vision::RepositionResponse)

(defmethod vision::RepositionRequest
  (:response () (instance vision::RepositionResponse :init)))

(setf (get vision::RepositionRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::RepositionRequest :datatype-) "vision/RepositionRequest")
(setf (get vision::RepositionRequest :definition-)
      "
---
")

(setf (get vision::RepositionResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::RepositionResponse :datatype-) "vision/RepositionResponse")
(setf (get vision::RepositionResponse :definition-)
      "
---
")



(provide :vision/Reposition "d41d8cd98f00b204e9800998ecf8427e")


