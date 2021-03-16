
(cl:in-package :asdf)

(defsystem "vision-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "Action" :depends-on ("_package_Action"))
    (:file "_package_Action" :depends-on ("_package"))
    (:file "ML" :depends-on ("_package_ML"))
    (:file "_package_ML" :depends-on ("_package"))
    (:file "Reposition" :depends-on ("_package_Reposition"))
    (:file "_package_Reposition" :depends-on ("_package"))
  ))