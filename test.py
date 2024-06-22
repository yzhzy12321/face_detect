import cv2

# 加载人脸级联分类器
face_cascade = cv2.CascadeClassifier('config/haarcascade_frontalface_alt.xml')

# 从默认摄像头（索引0）捕获视频
cameraCapture = cv2.VideoCapture(0)

while True:
    success, frame = cameraCapture.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

    if len(faces) > 0:
        # 检测到人脸！在此处处理它们。
        for (x, y, w, h) in faces:
            # 在这里执行您现有的人脸识别逻辑
            print('检测到人脸')
            pass
    else:
        print("未检测到人脸。")

    cv2.imshow("摄像头", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cameraCapture.release()
cv2.destroyAllWindows()
