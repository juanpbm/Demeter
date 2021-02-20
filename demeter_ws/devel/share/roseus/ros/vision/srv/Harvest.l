;; Auto-generated. Do not edit!


(when (boundp 'vision::Harvest)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'Harvest (find-package "VISION")))
(unless (find-package "VISION::HARVEST")
  (make-package "VISION::HARVEST"))
(unless (find-package "VISION::HARVESTREQUEST")
  (make-package "VISION::HARVESTREQUEST"))
(unless (find-package "VISION::HARVESTRESPONSE")
  (make-package "VISION::HARVESTRESPONSE"))

(in-package "ROS")





(defclass vision::HarvestRequest
  :super ros::object
  :slots ())

(defmethod vision::HarvestRequest
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

(defclass vision::HarvestResponse
  :super ros::object
  :slots ())

(defmethod vision::HarvestResponse
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

(defclass vision::Harvest
  :super ros::object
  :slots ())

(setf (get vision::Harvest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::Harvest :datatype-) "vision/Harvest")
(setf (get vision::Harvest :request) vision::HarvestRequest)
(setf (get vision::Harvest :response) vision::HarvestResponse)

(defmethod vision::HarvestRequest
  (:response () (instance vision::HarvestResponse :init)))

(setf (get vision::HarvestRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::HarvestRequest :datatype-) "vision/HarvestRequest")
(setf (get vision::HarvestRequest :definition-)
      "
---
")

(setf (get vision::HarvestResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get vision::HarvestResponse :datatype-) "vision/HarvestResponse")
(setf (get vision::HarvestResponse :definition-)
      "
---
")



(provide :vision/Harvest "d41d8cd98f00b204e9800998ecf8427e")


