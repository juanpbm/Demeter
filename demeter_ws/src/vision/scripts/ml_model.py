
import cv2
import rospy

from vision.srv import ML 

from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import VGG16

def model(req):
    model = VGG16(weights="imagenet")
    img = decompress(req.Left_Img)#ROS DO NOT CHANGE
   
    image = image_utils.imresize(img_L, size=(224, 224), interpolate='bilinear', channel_first=False, **kwargs)
    image = image_utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    preds = self.model.predict(image)
    P = decode_predictions(preds)[0]
    print(f"the pepper is in the picture with a prob of: {P[['bell_pepper'  in i for i in P].index(True)][2]}")

 def decompress(Left_Img): 
    #to decompress the image from ros srv dont change
    array = np.frombuffer(Left_Img.data, np.uint8)
    img = cv2.imdecode(array,cv2.IMREAD_COLOR)
    img = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
    return(img)

if __name__ == '__main__':
    #rosnode dont change
    rospy.init_node('ML_Model', anonymous=True)
    s = rospy.Service('ML_req', ML, model)#model here has to match the fucntion that will implement the ml model 
    rospy.spin()
