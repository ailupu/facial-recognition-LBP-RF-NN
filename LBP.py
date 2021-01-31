import numpy as np
import cv2
from matplotlib import pyplot as plt



def binaryToDecimal(n):
    decimal = 0
    multi = [1,2,4,8,16,32,64,128]
    for i in range(0,len(n)):
        decimal =decimal + (multi[i] * n[i])
    return decimal

def compare(center,pixels):
    out = []
    for a in pixels:
        if a >= center:
            out.append(1)
        else:
            out.append(0)
    return out
def get_pixels(image,idx,idy):
    try:
        return image[idx,idy]
    except IndexError:
        return 0


def LBP(img,img_copy):
    for x in range(0,len(img)):
        for y in range(0,len(img[0])):
            center = img[x,y]
           
            top_left =get_pixels(img, x-1, y-1)
           
            top_up = get_pixels(img, x, y-1)
          
            top_right = get_pixels(img, x+1, y-1)
          
            right = get_pixels(img, x+1, y )
           
            left = get_pixels(img, x-1, y )
            
            bottom_left = get_pixels(img, x-1, y+1)
            bottom_right = get_pixels(img, x+1, y+1)
            bottom_down = get_pixels(img, x, y+1 )
            
            values = compare(center,[top_left, top_up, top_right, right, bottom_right,
bottom_down, bottom_left, left])
            
            res = 0
            res = binaryToDecimal(values)
           
            img_copy.itemset((x,y),res)
        
    return img_copy
    
