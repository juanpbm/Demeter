;; Auto-generated. Do not edit!


(when (boundp 'vision::Action)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'Action (find-package "VISION")))
(unless (find-package "VISION::ACTION")
  (make-package "VISION::ACTION"))
(unless (find-package "VISION::ACTIONREQUEST")
  (make-package "VISION::ACTIONREQUEST"))
(unless (find-package "VISION::ACTIONRESPONSE")
  (make-package "VISION::ACTIONRESPONSE"))

(in-package "ROS")





(defclass vision::ActionRequest
  :super ros::object
  :slots (_Action ))

(defmethod vision::ActionRequest
  (:init
   (&key
    ((:Action __Action) nil)
    )
   (send-super :init)
   (setq _Action __Action)
   self)
  (:Action
   (&optional (__Action :null))
   (if (not (eq __Action :null)) (setq _Action __Action)) _Action)
  (:serialization-length
   ()
   (+
    ;; bool _Action
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _Action
       (if _Action (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _Action
     (setq _Action (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass vision::ActionResponse
  :super ros::object
  :slots (_Ack ))

(defmethod vision::ActionResponse
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

(defclass vision::Action
  :super ros::object
  :slots ())

(setf (get vision::Action :md5sum-) "48a9460ec0cc64685337f3762768aa1d")
(setf (get vision::Action :datatype-) "vision/Action")
(setf (get vision::Action :request) vision::ActionRequest)
(setf (get vision::Action :response) vision::ActionResponse)

(defmethod vision::ActionRequest
  (:response () (instance vision::ActionResponse :init)))

(setf (get vision::ActionRequest :md5sum-) "48a9460ec0cc64685337f3762768aa1d")
(setf (get vision::ActionRequest :datatype-) "vision/ActionRequest")
(setf (get vision::ActionRequest :definition-)
      "bool Action 
---
bool Ack 

")

(setf (get vision::ActionResponse :md5sum-) "48a9460ec0cc64685337f3762768aa1d")
(setf (get vision::ActionResponse :datatype-) "vision/ActionResponse")
(setf (get vision::ActionResponse :definition-)
      "bool Action 
---
bool Ack 

")



(provide :vision/Action "48a9460ec0cc64685337f3762768aa1d")


