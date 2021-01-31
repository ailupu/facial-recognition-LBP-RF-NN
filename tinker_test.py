# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils
import dlib
import os
import glob
import copy
import random
import ast
import lbp_7x7
import calc_hist_7x7
from imutils import face_utils
import random

global folder


def select_image():
    curent_dir = os.getcwd()
    img_dir = os.path.join(curent_dir,"antrenare")
    
    etichete = 0
    l_hist_imag = list()
    etichete_total = list()

    folder = []
    lbp_antrenare = list()
    etichete_antrenare = list()
    a = list()

    
	# grab a reference to the image panels
    global panelA, panelB
	# open a file chooser dialog and allow the user to select an input
	# image

	
    path = filedialog.askopenfilename()
    folder = dict()
    curent_dir = os.getcwd()
    img_dir = os.path.join(curent_dir,"antrenare")
    cnt = 0
    for subfolder in os.listdir(img_dir):
        cnt+=1
        folder[subfolder]=cnt

        
# ensure a file path was selected
    if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect

        	# edges in it
        img = cv2.imread(path)
        #cv2.imshow("img",img)
        image = cv2.imread(path,0)
        
        detector = dlib.get_frontal_face_detector()
        rects = detector(image,1)
        for (i,rect) in enumerate(rects):
            #if image.endswith(".jpg"):
            (x, y, w, h) = face_utils.rect_to_bb(rect)
            b = cv2.rectangle(image, (x, y), (x + w, y + h),10,0)
            c = b[y:y+h,x:x+w]
            try:
                c = cv2.resize(c,(154,154))
                c1 = copy.deepcopy(c)
                lbp = lbp_7x7.lbp_7x7(c,c1)
                histograma = calc_hist_7x7.calc_hist_7x7(lbp)
            except Exception as eroare:
                print(eroare)
        l_hist_imag.append(histograma)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        
        for subfolder in os.listdir(img_dir):
            
            os.chdir(os.path.join(img_dir,subfolder))
            etichete += 1
    
            etichete_imagini = list()
            for h_text in os.listdir("."):
                
                if h_text.endswith('txt'):
                    with open(h_text,'r') as f:
                        h = f.readline().rstrip()
                        h = ast.literal_eval(h)
                        #lista_toate.append(h)
                        a.append(list(map(float,h)))
            
                        etichete_imagini.append(etichete)
                                        
                           
            etichete_antrenare.append(etichete_imagini)
    for i in range(len(etichete_antrenare)):
        for j in range(len(etichete_antrenare[i])):
            etichete_total.append(etichete_antrenare[i][j])

    #print(folder)
    lbp_antrenare = np.array(a)
    etichete_antrenare = np.array(etichete_total)
    histograma = np.array(histograma)
    clf = RandomForestClassifier(max_depth=22, random_state=2, n_estimators = 420, bootstrap = False)

    clf.fit(lbp_antrenare, etichete_total)

    b = clf.predict(l_hist_imag)

    b = np.array(b).tolist()
    for i in b:
        val = i

    for key, value in folder.items():
        if value == val:
            f = key
    #print(f)

    path1 = os.path.join(curent_dir,"antrenare",f)
    files = os.listdir(path1)
    for file in os.listdir(path1):
        if file.endswith (".jpg"):
            index = random.randrange(0,len(file))

    d = str(files[index])
    #print(type(d))
    path1 = os.path.join(curent_dir,"antrenare",f,d)

    
    edged = cv2.imread(path1)
    edged = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)
    edged = Image.fromarray(edged)
    edged = ImageTk.PhotoImage(edged)
    
    # if the panels are None, initialize them
    if panelA is None or panelB is None:
			# the first panel will store our original image
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)
			# while the second panel will store the edge map
        panelB = Label(image=edged)
        panelB.image = edged
        panelB.pack(side="right", padx=10, pady=10)
		# otherwise, update the image panels
    else:
			# update the pannels
        panelA.configure(image=img)
        panelB.configure(image=edged)
        panelA.image = img
        panelB.image = edged


# initialize the window toolkit along with the two image panels

root = Tk()
panelA = None
panelB = None
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()
