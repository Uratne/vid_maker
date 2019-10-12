import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('split.mp4')
success,image = vidcap.read()
count = 100000
success = True
while success:
  cv2.imwrite("./frames/%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print 'Read a new frame: ', success, count
  count += 1