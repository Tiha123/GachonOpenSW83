import cv2

def cutf(image_path, output_path):
    cascade = cv2.CascadeClassifier('/Users/hyobin/Desktop/pythonProject2/team83/cutpaste/haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    cv2.imshow("origgin",img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        face_region = img[y:y+h, x:x+w]
        cv2.imwrite(output_path, face_region)
        print("Face extracted and saved successfully.")
    else:
        print("No faces detected in the provided image.")

if __name__ == "__main__":
    input_image_path = "/Users/hyobin/Desktop/pythonProject2/team83/asian.jpg"
    output_face_path = "/Users/hyobin/Desktop/pythonProject2/team83/cutpaste/profile.jpg"
    cut(input_image_path, output_face_path)
