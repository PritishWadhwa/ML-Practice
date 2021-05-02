import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read()
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue

    # params: greyFrame, scalingFactor, noOfNbrs (more detail can be found at documentation of haarcascade)
    # the method return the starting coordinates of each frame along with height and width in form of tuples
    faces = faceCascade.detectMultiScale(greyFrame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Video Frame", frame)

    keyPressed = cv2.waitKey(1) & 0xFF
    if keyPressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
