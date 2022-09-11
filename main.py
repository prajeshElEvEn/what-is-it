import cv2

feed = cv2.VideoCapture(0)
objectList = []
objectFile = './assets/coco.names'

with open(objectFile, 'rt') as f:
    objectList = f.read().rstrip('\n').split('\n')

weightsPath = "./weights/yolov4-tiny.weights"
configPath = "./model/yolov4-tiny.cfg"

net = cv2.dnn.readNet(weightsPath, configPath)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(480, 480), scale=1/255)

while True:
    check, frame = feed.read()
    # mirrorFeed = cv2.flip(frame, 1)

    (classIds, scores, bboxes) = model.detect(frame, confThreshold=0.5)

    for classId, score, bbox in zip(classIds, scores, bboxes):
        (x, y, w, h) = bbox
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
