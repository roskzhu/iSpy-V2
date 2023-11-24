import cv2
import numpy as np
from PIL import Image
import os

# people dictionary
people = {}

# path to database
path = './dataset'

# define which recognizer algorithm we will use
model = cv2.face.LBPHFaceRecognizer_create()

# load the base classifier
faceCascade = cv2.CascadeClassifier('venv/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def getData(dataset):   
    face_samples = []
    ids = []

    # make list of paths to all images in the dataset
    image_paths_dict = {}
    count = 0
    for person in os.listdir(dataset):
        name_parts = person.split("-")
        formatted_name = " ".join(part.capitalize() for part in name_parts)
        people[count] = formatted_name
        person_directory = os.path.join(dataset, person)
        for img in os.listdir(person_directory):
            image_path = os.path.join(person_directory, img)
            image_paths_dict[image_path] = count
        count += 1
    
    # edit images for training
    for image, num in image_paths_dict.items():
        grayscale_img = Image.open(image).convert('L') # convert to grayscale
        numpy_img = np.array(grayscale_img, 'uint8') # convert to numpy array
        faces = faceCascade.detectMultiScale(numpy_img) # detect faces
        # extract faces and corresponding label
        for (x, y, w, h) in faces:
            face_samples.append(numpy_img[y: y + h, x: x + w])
            ids.append(num)
    
    # open file for kv pairs / edit to make more efficient later
    with open("./pairs.txt", 'w') as f:
        for key, value in people.items():
            f.write(f'{key}: {value}\n')

    return face_samples, ids

# train the model on given dataset and save as a yml file
faces, ids = getData(path)
model.train(faces, np.array(ids))
model.save('./trainer.yml')
