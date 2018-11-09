from __future__ import print_function
import sys
import time
import numpy as np
import cv2 as cv
def is_grayscale(my_image):
    return len(my_image.shape) < 3

def main(argv):
    filename = "src.png"
    img_codec = cv.IMREAD_COLOR
    if argv:
        filename = sys.argv[1]
        if len(argv) >= 2 and sys.argv[2] == "G":
            img_codec = cv.IMREAD_GRAYSCALE
    src = cv.imread(filename, img_codec)
    if src is None:
        print("Can't open image [" + filename + "]")
        print("Usage:")
        print("mat_mask_operations.py [image_path -- default ../../../../data/lena.jpg] [G -- grayscale]")
        return -1
    cv.namedWindow("Input", 0)
    cv.resizeWindow("Input",600,600)
    cv.namedWindow("Output", 0)
    cv.resizeWindow("Output",600,600)
    cv.imshow("Input", src)

    t = round(time.time())
    #类高斯模糊模板
    kernel1 = np.array([[1/10,1/10,1/10],
                       [1/10,1/5,1/10],
                       [1/10,1/10,1/10]], np.float32) 
    #拉普拉斯锐化图像
    kernel2=np.array([[0,-1,0],
                      [-1,5,-1],
                      [0,-1,0]],np.float32)
    
    dst1 = cv.filter2D(src, -1, kernel1)
    # ddepth = -1, means destination image has depth same as input image
    
    t = (time.time() - t) / 1000
    print("Built-in filter2D time passed in seconds:     %s" % t)
    cv.imshow("Output", dst1)
    dst1=cv.bilateralFilter(dst1,d=30,sigmaColor=50,sigmaSpace=40)
    #dst1=cv.bilateralFilter(dst1,d=30,sigmaColor=50,sigmaSpace=40)
    while cv.waitKey(0)==' ':
        pass
    cv.imshow('Output',dst1)
    dst1 = cv.filter2D(dst1, -1, kernel2)
    while cv.waitKey(0)==' ':
        pass
    cv.imshow('Output',dst1)

    dst1=cv.bilateralFilter(dst1,d=30,sigmaColor=50,sigmaSpace=40)
    while cv.waitKey(0)==' ':
        pass
    cv.imshow('Output',dst1)
    
    cv.waitKey()
    cv.destroyAllWindows()
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
