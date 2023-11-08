import cv2
import numpy as np

num = 100 # This is to reduce the time taken. According to my approximation, the speed of the program should slow down similar to a 1/x graph with speed on y axis and i value on x axis

image1 = cv2.imread("test7.jpg")
ratio = image1.shape[1]/image1.shape[0]
image1 = cv2.resize(image1, (num, int(num*ratio)))
features = []

num1 = num
num2 = num * ratio

sensitivity = 45.5 #This has to be adjusted a bit or its fine

for i in range(int(num1)):
    for j in range(int(num2)):
        if len(features) != 0:
            nearism = []
            for h in features:
                random = 0
                n = 0
                for x in h:
                    pixelx = image1[x[0], x[1]]
                    pixelij = image1[j, i]
                    distance = ((pixelij[0] - pixelx[0])**2 + (pixelij[1] - pixelx[1])**2 + (pixelij[2] - pixelx[2])**2)**(1/3)
                    random += distance
                    n += 1
                av = random/n
                nearism.append(av)
            minn = min(nearism)
            if minn < 45.5:
                features[nearism.index(minn)].append((j, i))
            else:
                features.append([(j, i)])
        else:
            features.append([(j, i)])
        print(j, i)
            
    
for i in features:
    color = np.random.randint(0, 255)
    for x in i:
        cv2.circle(image1, (x[1], x[0]), 1, (color, color, color), -1)
        
image1 = cv2.resize(image1, (500, int(500 * ratio)))
cv2.imshow("mat", image1)
cv2.imshow("ma", cv2.resize(cv2.imread("test7.jpg"), (num, num)))

cv2.waitKey(0)
