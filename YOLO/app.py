import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet(yolov3.weights, yolov3.cfg)
classes = []
with open(coco.names, r) as f
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load image
img = cv2.imread(test.jpg)  # Replace with your test image path
height, width, channels = img.shape

# Detecting objects
blob = cv2.dnn.blobFromImage(img, 1255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Showing info on screen and getting confidence
class_ids = []
confidences = []
boxes = []

for out in outs
    for detection in out
        scores = detection[5]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence  0.5
            center_x = int(detection[0]  width)
            center_y = int(detection[1]  height)
            w = int(detection[2]  width)
            h = int(detection[3]  height)
            x = int(center_x - w  2)
            y = int(center_y - h  2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))

if len(indexes)  0
    for i in indexes.flatten()
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        color = colors[class_ids[i]]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, f{label} {confidence.2f}, (x, y - 5), font, 1, color, 1)

cv2.imshow(Image, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
