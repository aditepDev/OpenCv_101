import cv2

cap = cv2.VideoCapture('pic/video.avi')
while (True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # ปรับสี Video
    cv2.imshow('frame',gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()