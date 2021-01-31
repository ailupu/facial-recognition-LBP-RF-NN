from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

import numpy as np
import cv2
from matplotlib import pyplot as plt
from imutils import face_utils
import imutils
import dlib
import os
import glob
import copy
import lbp_7x7
import random
import calc_hist_7x7
import ast


detector = dlib.get_frontal_face_detector()

crop = []
lbp_imagini = []
etichete_imagini = list()
img_dir = "C:\\Users\\Jr\\Desktop\\testare"
folder = ""
etichete = 0
l_hist_imag = list()

#nr = int(random.uniform(1,14))
#print(nr)
nr = 11

etichete_total = list()

lbp_antrenare = list()
etichete_antrenare = list()

lbp_testare = list()
etichete_testare = list()

etichete_random_forest = list()

a = list()
tuplu_random = 0
lista_toate = list()
for subfolder in os.listdir(img_dir):
    print(subfolder)
    os.chdir(img_dir+"\\"+subfolder)
    etichete += 1
    
    etichete_imagini = list()
    for h_text in os.listdir("."):
        if h_text.endswith('txt'):
            
            print(h_text)
            
            with open(h_text,'r') as f:
                h = f.readline().rstrip()
                h = ast.literal_eval(h)
                a.append(list(map(float,h)))
                lista_toate.append(h)
            
                etichete_imagini.append(etichete)
                etichete_total.append(etichete)
               # import sys
               # import code
               # print(f"\n\nEntering in interactive mode.\nFunction: {sys._getframe().f_code.co_name}\n")
               # code.interact(local={**locals(), **globals()}) 
                  
                  
               
    print(len(a))
    tuplu_random = random.sample(list(enumerate(a)),nr)
    #print("tuplu", tuplu_random)

    index = list()
    valori = list()
    for idx, val in tuplu_random:
        index.append(idx)
        lbp_antrenare.append(val)
        etichete_antrenare.append(etichete_imagini[idx])
        #print("eticheta antrenare", etichete_antrenare , "lbp antrenare", lbp_antrenare)
        
    index.sort()
    for x in range(0,15):
        if x not in index:
            etichete_testare.append(etichete_imagini[x])
            lbp_testare.append(a[x])

            
    tuplu_random = list()
    a = list()
    etichete_imagini = list()


#print("etichete antr:",len(etichete_antrenare), etichete_antrenare)

#print("etichete testare:",len(etichete_testare), etichete_testare)



lbp_antrenare = np.array(lbp_antrenare)

lbp_testare = np.array(lbp_testare)

etichete_antrenare = np.array(etichete_antrenare)

etichete_testare = np.array(etichete_testare)


clf = RandomForestClassifier(max_depth=22, random_state=2, n_estimators = 420, bootstrap = False)

clf.fit(lbp_antrenare, etichete_antrenare)

b = clf.predict(lbp_testare)


corect = 0
for i in range(len(b)):
    if b[i] == etichete_testare[i]:
        corect += 1

probabilitate = (corect/len(b)) * 100
print("probabilitate:", probabilitate,"%")





