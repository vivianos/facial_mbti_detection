import cv2
import dlib
import numpy as np
import os
import pandas as pd

# loading detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

types = ['ESTJ', 'ESFJ', 'ISTP', 'ESTP', 'ESFP', 'INTJ', 'INTP', 'ENTJ', 'INFJ', 'INFP', 'ENFJ', 'ENFP']
data = []
for type in types:
    # get all files in a directory
    files = os.listdir(type)

    for file in files:
        if file[-3:] != 'png':
            continue

        print(type + '/' + file)
        # read the image
        img = cv2.imread(type + '/' + file)
        #convert to grayscale
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

        #Use detector
        faces = detector(gray)

        faceArr = np.zeros(shape=(68,2))

        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            landmarks = predictor(image=gray, box=face)
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                faceArr[n] = [x, y]

                cv2.circle(img=img, center=(x,y), radius=2, color=(0, 255, 0), thickness=-1)
                
        # inside eye seperation
        inside_eye = np.linalg.norm(faceArr[39] - faceArr[42])
        # outside eye seperation
        outside_eye = np.linalg.norm(faceArr[36] - faceArr[45])
        # jaw length
        jaw = np.linalg.norm(faceArr[7] - faceArr[11])
        # temple distance
        temple = np.linalg.norm(faceArr[0] - faceArr[16])
        # vertical nose lenght
        vert_nose = np.linalg.norm(faceArr[27] - faceArr[33])

        # Show the image if you want to see it
        # cv2.imshow(winname="Face", mat=img)
        # cv2.waitKey(delay=0)
        # cv2.destroyAllWindows()

        # Append the data to the array
        data.append({'type':type, 'inside_eye':inside_eye, 'outside_eye': outside_eye, 'jaw': jaw, 'temple': temple, 'vert_nose':vert_nose})

df = pd.DataFrame(data)
print(df.head())
df.to_pickle('data.pkl')
