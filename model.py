import tensorflow as tf
import cv2 as cv
from keras.models import load_model
import pandas as pd
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model

class Model:

    def __init__(self):
        self.f = tf.gfile.GFile('detector/detector.pb', 'rb')
        self.sess = tf.Session()
        self.graph = tf.get_default_graph()
        self.graph_def = tf.GraphDef()
        self.graph_def.ParseFromString(self.f.read())
        set_session(self.sess)

        self.model = load_model('model/VGG16.h5')
        self.model.load_weights('model/VGG16_weights.h5')

    def detect_roi(self, image):
        # Read and preprocess an image.
        original_img = cv.imread(image, 1)
        height, width, channels = original_img.shape

        # scale factor for preprocessing (resize)
        picSize = 200
        ratio = picSize / height
        resized_image = cv.resize(original_img, None, fx=ratio, fy=ratio)
        inp = resized_image[:, :, [2, 1, 0]]  # BGR2RGB

        # Restore session
        with self.sess.graph.as_default():
            tf.import_graph_def(self.graph_def, name='')

        # Run the model
        out = self.sess.run([self.sess.graph.get_tensor_by_name('num_detections:0'),
                            self.sess.graph.get_tensor_by_name('detection_scores:0'),
                            self.sess.graph.get_tensor_by_name('detection_boxes:0'),
                            self.sess.graph.get_tensor_by_name('detection_classes:0')],
                           feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})

        # Visualize detected bounding boxes.
        num_detections = int(out[0][0])
        croped_image = None
        detected = False
        i = 0
        while i < num_detections:
            score = float(out[1][0][i])
            bbox = [float(v) for v in out[2][0][i]]
            if score > 0.4:
                detected = True
                x = bbox[1] * width
                y = bbox[0] * height
                right = bbox[3] * width
                bottom = bbox[2] * height
                croped_image = original_img[int(y):int(bottom), int(x):int(right)]
                cv.rectangle(original_img, (int(x), int(y)), (int(right), int(bottom)), (125, 255, 51), thickness=2)
            if detected:
                i = num_detections

        cv.imwrite('result.jpg', original_img)
        cv.waitKey(500)
        return croped_image

    def predict_result(self, img):
        with self.graph.as_default():
            set_session(self.sess)
            prediction = self.model.predict(img)
        return prediction

    def preprocess_image_for_model(self, image):
        resized_image = cv.resize(image, (150, 150))
        return resized_image

    def predict_emotion(self, prediction):
        d = {'emotion': ['Alarmed', 'Annoyed', 'Curious', 'Relaxed'], 'prob': prediction[0]}
        df = pd.DataFrame(d, columns=['emotion', 'prob'])
        df = df.sort_values(by='prob', ascending=False)
        emotion = df['emotion'].values[0]
        prob = str(round((df['prob'].values[0]) * 100, 2))

        return emotion, prob
