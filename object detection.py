import cv2
image=input("image:")
classfile=input("classfile:") #you can assign directly filename
configpath=input("config path:") #you can assign directly filename
weightspath=("Weights path:") #you can assign directly filename
img=cv2.imread(image)
classnames=[]

with open(classfile,'rt') as f:
    classnames=f.read().rstrip('\n').split('\n')

net=cv2.dnn_Detectionmodel(weightspath,configpath)
net.SetInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean(127.5,127.5,127.5)
net.setInputSwanpRB(True)

classıd,confs,bbox=net.detect(img,confThreshold=0.5)

print(classId,bbox)
for classıd,confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
    cv2.rectange(img,box,color=(0,255,0),thickness=3)
    cv2.putText(img,classnames[classıd-1].upper(),(box[0]+10,box[1]+30),
                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


cv2.imshow("output",img)
cv2.WaitKey(0)
