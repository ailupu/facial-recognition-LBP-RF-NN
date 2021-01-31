import numpy as np
import cv2
from matplotlib import pyplot as plt
from imutils import face_utils
import argparse
import imutils
import dlib
import os
import copy
import lbp_7x7
from PIL import Image
import calc_hist_7x7
import NN


detector = dlib.get_frontal_face_detector()

lbp_imagini = []
l_imag = list()
l_hist_imag = list()

curent_dir = os.getcwd()
img_dir = os.path.join(curent_dir,"gt_db")

folder = ""
cnt_imagini_total = 0
for subfolder in os.listdir(img_dir):
   
   print(subfolder)
   
   os.chdir(os.path.join(img_dir,subfolder))
   
   for imagini in os.listdir("."):
      
      if imagini.endswith('jpg'):
         
         print (imagini)

         folder += subfolder
         folder += " "
         folder += imagini
         
         img_data = cv2.imread(os.path.join(img_dir,subfolder,imagini),0)

         
         rects = detector(img_data,1)
         histograma = 0
       
         for (i,rect) in enumerate(rects):
            
            if imagini.endswith(".jpg"):
               
               
               (x, y, w, h) = face_utils.rect_to_bb(rect)
               b = cv2.rectangle(img_data, (x, y), (x + w, y + h),10,0)
               c = b[y:y+h,x:x+w]
               
               try:
                  c = cv2.resize(c,(154,154))
                  c1 = copy.deepcopy(c)
                  cv2.imshow("copy",c1)

                  
                  lbp = lbp_7x7.lbp_7x7(c,c1)
                  
                  cv2.imshow("lbp calc",lbp)
                  
                  cnt_imagini_total += 1
                  
                  histograma = calc_hist_7x7.calc_hist_7x7(lbp)
                  
                  l_imag.append(folder)
                  l_hist_imag.append(histograma)
                  
                  f = open(subfolder+"_"+imagini[0:-4]+"_"+"hist.txt", "w+")
                  f.write(str(list(histograma)))
                  f.close()

                  lbp = 0
                  folder = ""

                                  
               except Exception as eroare:
                  print(img_data)
                  print(eroare)
  
        
   

media = list()
for i in range(len(l_hist_imag)):
   media.append(NN.NN(l_hist_imag[i],l_hist_imag))

   
mminim = 0
m = list()
index = list()
for i in range(len(media)):
   for j in range(len(media[i])):
      
      if media[i][j] == 0 :
         media[i][j] = 99999999999
   
   minim = min(media[i])
   index.append(media[i].index(minim))
   
   
   m.append(minim)
   

lista_imagini_asociate = list()
for i in index:
   lista_imagini_asociate.append(l_imag[i])


cnt_imag_bune = 0
for i in range(len(l_imag)):
   try:
      if l_imag[i][0:3] == lista_imagini_asociate[i][0:3]:
         cnt_imag_bune += 1
   except Exception as eroare:
      print("Nu gaseste")

            
total = (cnt_imag_bune/cnt_imagini_total)*100
print(total,"%")
