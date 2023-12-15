import cv2


def cutf(n):
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(n)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray, 1.1, 4)

    result = img[faces[0][1]:faces[0][1]+faces[0][3], faces[0][0]:faces[0][0]+faces[0][2]].copy()

    return result
