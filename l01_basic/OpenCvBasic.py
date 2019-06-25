import cv2

cap = cv2.VideoCapture(0)
while (True):
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
print(cv2.__version__)

img = cv2.imread('pic/test01.jpg',0) # 0, IMREAD_GRAYSCALE ขาวดำ  :: 1 IMREAD_COLOR สี
cv2.imshow('Show Result',img) # อ่าน
cv2.imwrite('result.png',img) # เขียน
cv2.waitKey(0)  # รอกดปุ่ม
cv2.destroyAllWindows() # ปิดโปรแกรม

