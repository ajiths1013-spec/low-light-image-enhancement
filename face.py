import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def protect_faces(original, enhanced):
    faces = face_cascade.detectMultiScale(original, 1.3, 5)

    for (x,y,w,h) in faces:
        enhanced[y:y+h, x:x+w] = (
            original[y:y+h, x:x+w]*0.6 +
            enhanced[y:y+h, x:x+w]*0.4
        )

    return enhanced