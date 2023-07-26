# https://www.dropbox.com/s/th0u3mpsl71fxit/CertificateTemplate.jpg

from PIL import Image, ImageDraw, ImageFont
img = Image.open("./MODULE-08/Certi_Template.jpg")

import matplotlib.pyplot as plt
import numpy as np

# image show 
def print_img(img):
    plt.imshow(np.array(img))
    plt.show()

import cv2

img = cv2.imread("./MODULE-08/Certi_Template.jpg")

def generate_certificate(img, name="Enter Name"):
    generated_image = img.copy()  #COPY THE IMAGE
    font = cv2.FONT_HERSHEY_SIMPLEX #FONT IN CV2 LIB

    cordinates = (700,750)
    font_size = 3.5
    font_color = (51,51,51)
    font_thickness = 10
    
    cv2.putText(generated_image,name,cordinates,font,font_size,font_color,font_thickness)
    return generated_image

def save_img(img, name):
    path="./certi_{}.jpg".format(name)
    print(cv2.imwrite(path,img))    

name = input("Enter the name you want on certificate: ")
generated_image = generate_certificate(img, name)
save_img(generated_image, name)
    
