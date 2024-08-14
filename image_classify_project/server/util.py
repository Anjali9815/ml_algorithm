import cv2, base64
from wavelet import w2d
import numpy as np
import json, pickle, joblib


__class_name_to_number = {}
__class_number_to_name = {}
__model = None

def class_number_to_name(class_num):
    return __class_number_to_name[class_num]

def classify_image(image_base64data, file_path = None):
    imgs = get_cropped_img(file_path, image_base64data)
    result = []
    for image in imgs:
        scaled_raw_img = cv2.resize(image, (32, 32))
        img_haar = w2d(image, 'db1', 5)
        scaled_img_haar = cv2.resize(img_haar, (32, 32))
        # combined_img = np.vstack((scaled_raw_img.reshape(32*32*3, 1), scaled_img_haar.reshape(32*32, 1)))
        combined_img = np.vstack((scaled_raw_img.reshape(32*32*3,1),scaled_img_haar.reshape(32*32,1)))
        len_of_image = 32 * 32 * 3 + 32 * 32

        final_img = combined_img.reshape(1, len_of_image).astype(float)
        # result.append(__model.predict(final_img)[0])
        result.append({
            'class': class_number_to_name(__model.predict(final_img)[0]),
            'class_probability': np.around(__model.predict_proba(final_img)*100,2).tolist()[0],
            'class_dictionary': __class_name_to_number
        })
    return result

def get_cv2_image_base64(base64str):
    # this function converts base64 to encoded string 
    
    encoded_data = base64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_cropped_img(image_path, base64_path):
    face_cascade = cv2.CascadeClassifier("D:/Workspace/ML_ALGO/image_classification/model/opencv/haarcascade/haarcascade_frontalface_default.xml")

    eyes_cascade = cv2.CascadeClassifier("D:/Workspace/ML_ALGO/image_classification/model/opencv/haarcascade/haarcascade_eye.xml")

    if image_path:
        img = cv2.imread(image_path)
    else:
        img = get_cv2_image_base64(base64_path)
    cropped_faces = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyes_cascade.detectMultiScale(roi_gray)
        if len(eyes) >=2:
            cropped_faces.append(roi_color)
    return cropped_faces

def get_base64():
    with open("D:/Workspace/ML_ALGO/image_classification/model/test_images/bs64_kiara.txt.txt") as f:
        return f.read()

def load_saved_artifact():
    print("loading saved artifacts...start")
    global __class_name_to_number
    global __class_number_to_name

    with open("D:/Workspace/ML_ALGO/image_classification/server/artifacts/class_dictionary.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}

    global __model
    if __model is None:
        with open('D:/Workspace/ML_ALGO/image_classification/server/artifacts/saved_model.pkl', 'rb') as f:
            __model = joblib.load(f)
    print("loading saved artifacts..done")


if __name__ == "__main__":
    load_saved_artifact()
    print(classify_image(get_base64(), None))
    print(classify_image(None, 'D:/Workspace/ML_ALGO/image_classification/model/dataset/kohli/2c06edccfb.jpg'))
    print(classify_image(None, 'D:/Workspace/ML_ALGO/image_classification/model/dataset/selena/53cc1d13093f4ab989262e10a99d7e33.jpg'))
    print(classify_image(None, 'D:/Workspace/ML_ALGO/image_classification/model/dataset/maria/184-1847379_download-maria-sharapova-wallpaper-2013-wallpaper-hd-full.jpg'))
    print(classify_image(None, 'D:/Workspace/ML_ALGO/image_classification/model/dataset/messi/5de5fed30f25441e5823254c.jpg'))
