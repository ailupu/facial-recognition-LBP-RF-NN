import numpy as np
import cv2
from matplotlib import pyplot as plt

def compare_pixels(mid,pixels):
    out = []
    for a in pixels:
        if a >= mid:
            out.append(1)
        else:
            out.append(0)
    return out


def binaryToDecimal(n):
    decimal = 0
    multi = [1,2,4,8,16,32,64,128]
    for i in range(0,len(n)):
        decimal = decimal + (multi[i] *n[i])
    return decimal



def get_pixels(image,idx,idy):
    try:
        return image[idx,idy]
    except IndexError:
        return 0



def lbp_7x7(img,img_copy):
    
    matrix = [0,0,0,0,0,0,0,0]
    values = list()
    res = 0
    cnt = 0
    
    
    for i in range(0,len(img),22):
        
        for j in range(0,len(img[0]),22):
            
            for x in range(i,i+22):
                for y in range(j,j+22):
                    
                    try:
                        
                        center = get_pixels(img,x,y)
            
                        top_left =get_pixels(img, x-1, y-1)
                        matrix[0]=top_left
            
                        top_up = get_pixels(img, x, y-1)
                        matrix[1] = top_up
            
                        top_right = get_pixels(img, x+1, y-1)
                        matrix[2]=top_right
            
                        right = get_pixels(img, x+1, y )
                        matrix[3] = right

                        bottom_right = get_pixels(img, x+1, y+1)
                        matrix[4] = bottom_right
            
                        bottom_down = get_pixels(img, x, y+1 )
                        matrix[5]=bottom_down
            
                        bottom_left = get_pixels(img, x-1, y+1)
                        matrix[6]=bottom_left

                        left = get_pixels(img, x-1, y )
                        matrix[7] = left

                        values = compare_pixels(center,matrix)

            
                        res = binaryToDecimal(values)
            
            
                        img_copy.itemset((x,y),res)
                        res = 0
                        values.clear()
                        
                    except:
                        pass
        
       
    return img_copy
