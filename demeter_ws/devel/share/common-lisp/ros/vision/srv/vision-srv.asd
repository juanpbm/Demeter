
(cl:in-package :asdf)

(defsystem "vision-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "Harvest" :depends-on ("_package_Harvest"))
    (:file "_package_Harvest" :depends-on ("_package"))
    (:file "Recognition_Rec" :depends-on ("_package_Recognition_Rec"))
    (:file "_package_Recognition_Rec" :depends-on ("_package"))
    (:file "Reposition" :depends-on ("_package_Reposition"))
    (:file "_package_Reposition" :depends-on ("_package"))
    (:file "Stereo_Rec" :depends-on ("_package_Stereo_Rec"))
    (:file "_package_Stereo_Rec" :depends-on ("_package"))
    (:file "Take_Img" :depends-on ("_package_Take_Img"))
    (:file "_package_Take_Img" :depends-on ("_package"))
  ))