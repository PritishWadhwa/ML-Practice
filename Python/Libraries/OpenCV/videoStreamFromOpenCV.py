import cv2

# capture the device
cap = cv2.VideoCapture(0)  # 0: Default Webcam
while True:
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ret = False: frame not captured
    if ret == False:
        continue
    cv2.imshow('Video Frame', frame)
    cv2.imshow('Gray Frame', grayFrame)

    # wait for user input: q to quit
    # program wait for 1 ms b4 next iteration
    keyPressed = cv2.waitKey(1) & 0xFF  # get the last 8 bits
    if keyPressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
