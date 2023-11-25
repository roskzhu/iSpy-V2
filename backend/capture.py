import cv2
from database_interaction import upload

# determines if numpy image contains a face, crops, preprocesses and uploads to gcs db
def capture(name, image, num):
    """
        :type name: str
              image: List[List[List[int]]] (numpy array)
              num: int
        :rtype: 0 (fail, no faces detected)
                1 (success)
                2 (fail, more than one face on screen)
    """
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        bw_image,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    
    if len(faces) < 1:
        return 0
    elif len(faces) == 1:
        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        cropped = image[y: y + h, x: x + w]
        resized = cv2.resize(cropped, (224, 224))
        # upload(name, resized, num)
        return 1
    else:
        return 2

capture("name", cv2.imread("in.jpg"), 1)