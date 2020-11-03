
(cl:in-package :asdf)

(defsystem "kinematics-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "data_3D" :depends-on ("_package_data_3D"))
    (:file "_package_data_3D" :depends-on ("_package"))
  ))