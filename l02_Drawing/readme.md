# Drawing

```python 
import cv2
print(cv2.__version__)

img = cv2.imread('test01.jpg',1)
# สี BGR
# เส้นตรง (รูปภาพ,จุดเริ่ม,จุดจบ,สี,ความหนา)
img = cv2.line(img,(0,0),(255,255),(0,0,255),10)
# ลูกศร (รูปภาพ,จุดเริ่ม,จุดจบ,สี(BGR),ความหนา)
img = cv2.arrowedLine(img,(0,0),(400,400),(255,0,0),10)
# สี่เหลี่ยม (รูปภาพ,จุดเริ่ม,จุดจบ,สี,ความหนา)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),10)
# วงกลม (รูปภาพ,จุดกลาง,เส้นรอบวง,สี,ความหนา)
img = cv2.circle(img,(447,63),63,(0,255,0),10) # 1 มีแต่เส้น   -1 พื้นที่ของวงกลม
# ตัวหนังสือ (รูปภาพ,ตัวหนังสือ,จุดเริ่ม,FONT,ขนาดตัวอักษร,สี,ความหนา)
img = cv2.putText(img,'TESTTEXT',(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cv2.imshow('Show Result',img) # อ่าน
cv2.imwrite('result.png',img) # เขียน
cv2.waitKey(0)  # รอกดปุ่ม
cv2.destroyAllWindows() # ปิดโปรแกรม
```