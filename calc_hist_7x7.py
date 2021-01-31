import cv2
from matplotlib import pyplot as plt
def calc_hist_7x7 (img):
    hist = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    list_hist = list()
    cnt =0
    for x in range(0,len(img),22):
        
        for y in range(0,len(img[0]),22):
            hist = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            for i in range(x,x+22):
                for j in range(y,y+22):
                    
                    if ( 0 <= img[i][j] < 20 ):
                        hist[0] += 1
                        
                    if ( 20 <= img[i][j] < 40 ):
                        hist[1] += 1
                        
                    if ( 40 <= img[i][j] < 60 ):
                        hist[2] += 1
                        
                    if ( 60 <= img[i][j] < 80 ):
                        hist[3] += 1
                        
                    if ( 80 <= img[i][j] < 100 ):
                        hist[4] += 1
                        
                    if ( 100 <= img[i][j] < 120 ):
                        hist[5] += 1
                        
                    if ( 120 <= img[i][j] < 140 ):
                        hist[6] += 1
                        
                    if ( 140 <= img[i][j] < 160 ):
                        hist[7] += 1
                        
                    if ( 160 <= img[i][j] < 180 ):
                        hist[8] += 1
                        
                    if ( 180 <= img[i][j] < 200 ):
                        hist[9] += 1
                        
                    if ( 200 <= img[i][j] < 220 ):
                        hist[10] += 1
                        
                    if (220  <= img[i][j] < 240 ):
                        hist[11] += 1
                        
                    if (240 <= img[i][j] < 260 ):
                        hist[12] += 1

            
            
           
                   
            for h in range(len(hist)):           
                list_hist.append(hist[h])

    return list_hist
        
            
"""   

    for z in range(len(hist_plot)):
        
        file = plt.bar(range(0,255,20),hist_plot[z],width = 20)
        
        plt.xlabel("Interval")
        plt.ylabel("Frecveta de aparitie")
        plt.title("Histograma imaginii")

        idx += 1
        savefile = "hist" + str(idx)+".png"

        
        plt.savefig(savefile)
        plt.show()
"""
    

