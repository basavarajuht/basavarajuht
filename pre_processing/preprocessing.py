import cv2
import matplotlib.pyplot as plt
image = cv2.imread('C:/Users/Lenovo/Downloads/Object-Detection-using-cvlib-main/object detection/image.jpg')
print('Input size is:', image.shape)
plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
r=image[:,:,0]
g=image[:,:,1]
b=image[:,:,2]
plt.figure()
plt.imshow(r,cmap="gray")
plt.title('red')
plt.figure()
plt.imshow(g,cmap="gray")
plt.title('green')
plt.figure()
plt.imshow(b,cmap="gray")
plt.title('blue')
cv2.imshow('input', image)
cv2.imshow('red', r)
cv2.imshow('green', g)
cv2.imshow('blue', b)
im_re = cv2.resize(b, (256, 256))
print('blue image', im_re.shape)
#ret, bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#plt.imshow(bw_img,cmap="gray")
plt.show()
cv2.waitKey(0)  # delay 0
cv2.destroyAllWindows()
