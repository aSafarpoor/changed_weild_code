import cv2
vidcap = cv2.VideoCapture('face1.avi')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  # print(image)
  print('Read a new frame: ', success)
  count += 1
print(count)
# import cv2
# vidcap = cv2.VideoCapture('face1.avi')
# success,image = vidcap.read()
# count = 0
# # while success:
# cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
# success,image = vidcap.read()
  

# print(type(image))
# for i in image:
#   for j in i :
#     print(".",end="")
#   print("---------------")
