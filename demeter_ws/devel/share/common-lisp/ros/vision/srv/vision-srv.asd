
(cl:in-package :asdf)

(defsystem "vision-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "Rec" :depends-on ("_package_Rec"))
    (:file "_package_Rec" :depends-on ("_package"))
  ))