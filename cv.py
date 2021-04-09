import cv2
import numpy as np
import os
from random import choice
def test():
    back = np.zeros((297*3,210*3,3), np.uint8)
    back.fill(255)
    #im = cv2.imread('./test/img_1.png',cv2.IMREAD_UNCHANGED) 
    #im = im[:, :, 3]
    img = cv2.imread('./test/img_0.png',cv2.IMREAD_UNCHANGED) 
    img = img[:, :, 3]
    h = img.shape[0]
    w = img.shape[1]
    print(img.shape)
    for i in range(h):
        for j in range(w):
            back[i+48,j+346]=img[i,j]
    img = cv2.imread('./test/img_1.png',cv2.IMREAD_UNCHANGED) 
    img = img[:, :, 3]
    h= img.shape[0]
    w = img.shape[1]
    print(img.shape)
    for i in range(h):
        for j in range(w):
            back[i+174,j+199]=img[i,j]
        
        cv2.imshow('image', back)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def loop_write():
    img_all = []
    for filename in os.listdir(r"./image"):
        #print(filename)
        filename = f'./image/{filename}'
        img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        try:
            h,_,_ = img.shape
        except Exception as e:
            print(e)
            print(filename)
            exit()
        img = img[:, :, 3]
        img = 255-img
        img_all.append(img)
    #imgrandom = choice(img_all)
    #cv2.imshow('image', imgrandom)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    marker_all = []
    for filename in os.listdir(r"./2code"):
        filename = f'./2code/{filename}'
        #print(filename)
        marker = cv2.imread(filename)
        x, y = img.shape[0:2]
        marker = cv2.resize(marker,(50,50))
        marker_all.append(marker)
         
    back_all=[]
    for m in range(1000):
        back = np.zeros((297*3,210*3,3), np.uint8)
        back.fill(255)
        #os.mkdir("./label/{}".format(m))
        for mknum in range(1):
            h0 = marker_all[mknum].shape[0]
            w0 = marker_all[mknum].shape[1] 
            for i in range(h0):
                for j in range(w0):
                    back[30+790*mknum+i,j]=marker_all[mknum][i,j]
            h1 = marker_all[mknum+1].shape[0]
            w1 = marker_all[mknum+1].shape[1] 
            for i in range(h1):
                for j in range(w1):
                    back[30+790*mknum+i,580+j]=marker_all[mknum+1][i,j]
        for mknum in range(1):
            h0 = marker_all[mknum+2].shape[0]
            w0 = marker_all[mknum+2].shape[1] 
            for i in range(h0):
                for j in range(w0):
                    back[30+790*(mknum+1)+i,j]=marker_all[mknum+2][i,j]
            h1 = marker_all[mknum+3].shape[0]
            w1 = marker_all[mknum+3].shape[1] 
            for i in range(h1):
                for j in range(w1):
                    back[30+790*(mknum+1)+i,580+j]=marker_all[mknum+3][i,j]
        for n in range(5):
            imgrandom=choice(img_all)
            cv2.imwrite("./label/"+str(m)+"/img_{}.png".format(n),imgrandom)
            h0 = imgrandom.shape[0]
            w0 = imgrandom.shape[1] 
            for i in range(h0):
                for j in range(w0):
                    back[120+150*n+i,140+j]=imgrandom[i,j]
            imgrandom1=choice(img_all)
            cv2.imwrite("./label/"+str(m)+"/img_{}.png".format(n+5),imgrandom1)
            h1 = imgrandom1.shape[0]
            w1 = imgrandom1.shape[1] 
            for i in range(h1):
                for j in range(w1):    
                    back[120+150*n+i,390+j]=imgrandom1[i,j]
                    back = cv2.putText(back,str(m),(300,880),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
            
        cv2.imwrite("./datad/img_{}.png".format(str(m)),back)
        back_all.append(back)
    #print(len(back_all))        
    #cv2.imshow('image', back_all[13232])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()              

def rec():
    rec= cv2.imread("./rec.png")
    rec= cv2.resize(rec,(230,130))
    for m in range(2):
        back = np.zeros((297*3,210*3,3), np.uint8)
        back.fill(255)
        for n in range(5):
            imgrandom=rec
   
            h0 = imgrandom.shape[0]
            w0 = imgrandom.shape[1] 
            for i in range(h0):
                for j in range(w0):
                    back[80+150*n+i,80+j]=imgrandom[i,j]
                   
            imgrandom1=rec
            h1 = imgrandom1.shape[0]
            w1 = imgrandom1.shape[1] 
            for i in range(h1):
                for j in range(w1):    
                    back[80+150*n+i,330+j]=imgrandom1[i,j]
    back = cv2.imwrite("./frame/frame.png",back)        
    #cv2.imshow('image', back)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()  
def main():
    loop_write()
    #back = np.zeros((297*3,210*3,3), np.uint8)
    #back.fill(255)     
    rec()      
    #back = cv2.line(back,(0,int(178*1)),(int(297*3),int(178*1)),(0,0,0),2)
    #back = cv2.line(back,(0,int(178*2)),(int(297*3),int(178*2)),(0,0,0),2)
    #back = cv2.line(back,(0,int(178*3)),(int(297*3),int(178*3)),(0,0,0),2)
    #back = cv2.line(back,(0,int(178*4)),(int(297*3),int(178*4)),(0,0,0),2)
    #back = cv2.line(back,(0,int(178*0)),(int(297*3),int(178*0)),(0,0,0),2)
    #back = cv2.line(back,(0,int(178*5)),(int(297*3),int(178*5)),(0,0,0),2)
    #back = cv2.line(back,(int(210*1.5),0),(int(210*1.5),int(178*5)),(0,0,0),2)
    #back = cv2.imwrite("./frame/frame.png",back)
    #cv2.imshow('image', back)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()  
    
    

if __name__ == '__main__':
    main()
















