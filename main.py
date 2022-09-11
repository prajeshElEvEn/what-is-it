import cv2

feed = cv2.VideoCapture(0)

while True:
    check, frame = feed.read()
    flipFeed = cv2.flip(frame, 1)
    cv2.imshow('Live', flipFeed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
