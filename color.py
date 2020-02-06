import pandas as pd
import numpy as nu
import cv2
import argparse

clicked = False
r = g = b = xpos = ypos = 0

#ceateing draw_fuction
def draw_fuction(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked=True
        xpos=x
        ypos =y
        b,g,r=img[x, y]
        b=int(b)
        g=int(g)
        r=int(r)

#d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
#calculte nearest color or distance
def getColorName(R, G, B):
    min=1000
    for i in range(len(csv)):
        d=abs(R-int(csv.loc[i, "R"]))+abs(G-int(csv.loc[i, "G"]))+abs(B-int(csv.loc[i, "B"]))
        if(d<=min):
            min=d
            cname=csv.loc[i, "color_name"]
    return cname


ag=argparse.ArgumentParser()
ag.add_argument('-i', '--image', required=True, help="Image path")
args=vars(ag.parse_args())
img_path=args['image']

#read image
img=cv2.imread(img_path)

#read csv file
index=['color', 'color_name', 'hex', 'R', 'G', 'B']
csv=pd.read_csv('colors.csv', names=index, header=None)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_fuction)

#display image
while(1):
    cv2.imshow("image", img)
    if(clicked):
        cv2.rectangle(img, (20,20), (760, 60), (b,g,r), -1)
        text=getColorName(r, g, b)+' R='+str(r)+' G='+str(g)+' B='+str(b)
        cv2.putText(img, text, (50,50), 2, 0.8,(255,255,255), 2, cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text, (50,50), 2, 0.8,(255,255,255), 2, cv2.LINE_AA)

        clicked=False
    if cv2.waitKey(20) & 0xFF==27:
        break

cv2.destroyAllWindows()