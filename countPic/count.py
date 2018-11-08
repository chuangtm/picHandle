import cv2 as cv

old=cv.imread(r"ranseti.png")
src=old
cv.namedWindow("image")
cv.imshow("image", src)

#高斯平滑处理
def blur(image):
    dst=cv.blur(image,(2,2))
    cv.imwrite("blur.jpg",dst)
    cv.namedWindow('blur',0)
    cv.resizeWindow('blur',600,600)
    cv.imshow('blur',dst)

    return dst

#中值滤波
def gaussblur(image):
    dst=cv.GaussianBlur(image,(3,3),0)
    cv.imwrite("gaussblur.jpg",dst)
    cv.namedWindow('gaussblur',0)
    cv.resizeWindow('gaussblur',600,600)
    cv.imshow('gaussblur',dst)
    return dst

#双边滤波处理
def bilaterFilt(image):
    dst=cv.bilateralFilter(src=image,d=10,sigmaColor=110,sigmaSpace=40)
    cv.imwrite("bilateralFilter.jpg",dst)
    cv.namedWindow('bilaterFilted',0)
    cv.resizeWindow('bilaterFilted',600,600)
    cv.imshow('bilaterFilted',dst)
    return dst

def canny(image):
    edge=cv.Canny(image,50,150)
    cv.imwrite("canny.jpg",edge)
    cv.namedWindow('edge',0)
    cv.resizeWindow('edge',600,600)
    cv.imshow('edge',edge)
    return edge

def threshold(image):
    (_,dst)=cv.threshold(image,180,255,cv.THRESH_BINARY)
    cv.imwrite("threshold.jpg",dst)
    cv.namedWindow('threshold',0)
    cv.resizeWindow('threshold',600,600)
    cv.imshow('threshold',dst)
    return dst

def erode_dilate(image):
    g=cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
    dst=cv.erode(image,g,iterations=2)
    dst=cv.dilate(dst,g,iterations=3)
    cv.imwrite("erode_dilate.jpg",dst)
    cv.namedWindow('erode_dilate',0)
    cv.resizeWindow('erode_dilate',600,600)
    cv.imshow('erode_dilate',dst)
    return dst

def draw_contours(image):
    num=0
    result=cv.findContours(src,cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
    for i in range(1,50):
        if len(result[1][i])>8:
            cv.drawContours(old,result[1][i],-1,(0,0,255),1)
            path=r'ceshi\{}.jpg'.format(i)
            cv.imwrite(path,old)
            num+=1
    cv.imwrite("result.jpg",old)
    cv.namedWindow('contours',0)                
    cv.resizeWindow('contours',1000,1000)
    cv.imshow('contours',old)
    return num

#src=gaussblur(src)
src=blur(src)
src=bilaterFilt(src)
src=cv.cvtColor(src, cv.COLOR_RGB2GRAY)
src=threshold(src)
src=erode_dilate(src)
num=draw_contours(src)
edge=canny(src)
print("the number is  ",num)











