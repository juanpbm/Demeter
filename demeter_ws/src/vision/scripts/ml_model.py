
from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import VGG16

 model = VGG16(weights="imagenet")
 image = image_utils.imresize(img_L, size=(224, 224), interpolate='bilinear', channel_first=False, **kwargs)
 image = image_utils.img_to_array(image)
 image = np.expand_dims(image, axis=0)
 image = preprocess_input(image)
 preds = self.model.predict(image)
 P = decode_predictions(preds)[0]
 print(f"the pepper is in the picture with a prob of: {P[['bell_pepper'  in i for i in P].index(True)][2]}")
