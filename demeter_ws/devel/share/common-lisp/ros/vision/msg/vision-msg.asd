
(cl:in-package :asdf)

(defsystem "vision-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "image_Pair" :depends-on ("_package_image_Pair"))
    (:file "_package_image_Pair" :depends-on ("_package"))
  ))