import cv2

faceCascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('model/haarcascade_eye_tree_eyeglasses.xml')
noseCascade = cv2.CascadeClassifier('model/Nariz.xml')
mouthCascade = cv2.CascadeClassifier('model/Mouth.xml')

# แปลงภาพสีเป็น ดำ และ เรียกใช้ features เพื่อ กีเทคใบหน้า แล้ว ระบุ ตำแหน่ง x,y เพื่อวาดรูป สีเหลี่ยมพืนผ้า
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)

    coords = []

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
        coords = [x, y, w, h]
    return img, coords


# ตรวจจับใบหน้า และ เรียกใช้ draw_boundary
def detect(img, faceCascade, eyeCascade, noseCascade,mouthCascade):
    img, coords = draw_boundary(img, faceCascade, 1.1, 10, (0, 0, 255), "Face")
    img, coords = draw_boundary(img, eyeCascade, 1.1, 12, (255, 0, 0), "Eye")
    img, coords = draw_boundary(img, noseCascade, 1.1, 20, (0, 255, 0), "Nose")
    img, coords = draw_boundary(img, mouthCascade, 1.1, 20, (50, 0, 50), "mouthC")
    return img


cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    frame = detect(frame, faceCascade, eyeCascade, noseCascade,mouthCascade)
    cv2.imshow('frame', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
