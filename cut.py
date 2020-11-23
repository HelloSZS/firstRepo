import cv2
import os

img=cv2.imread(r'C:\\Users\\Nelson\\Desktop\\cut\\1.jpg')

filename=0
filenum=1

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#分割图片大小
b=400 #数字块大小为400×400

#步长除数 可看成卷积核大小
c = 3

#步长为b//3 也即是400//3
bc = b // c

# //为整除
# 得出将要分割出的图片数量m*n
m = img.shape[0]//b * c - 2
n = img.shape[1]//b * c - 2
print(m,n)

#图片:4032*3024

for i in range(m):
    offsetRow=i*bc

    if i%5==0 and i !=0:
        # filename+=1
        filenum=0
    #   可以释放内存
    # del filename
    path="C:\\Users\\Nelson\\Desktop\\cut\\cut1\\"+str(filename)
    if not os.path.exists(path):
        os.makedirs(path)

    for j in range(n):
        offsetCol=j*bc
        filepath = path+"\\"+str(filenum)+".jpg"
        filenum+=1
        im=img[offsetRow:offsetRow+b-1,offsetCol:offsetCol+b-1]
        cv2.imwrite(filepath,im, [int( cv2.IMWRITE_JPEG_QUALITY), 100])

print(filename,filenum)
print(path)