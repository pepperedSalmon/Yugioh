import numpy as np
import cv2
import requests
import yugiohGameObjects


def retrive_img(name,url):
    img_data = requests.get(url).content
    with open(f'art\{name}.jpg', 'wb') as handle:
        handle.write(img_data)       

def image_2_ascii(file_name):
    ''' Convert Images into ASCII Art '''
    # 1st 
    # Lets import image and and convert it to gray scale
    try: 
        img = cv2.imread(f'art\{file_name}.jpg')
    except FileNotFoundError:
        print("Image not found")
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #-------------------------------------------
        # 2nd
        # Lets Resize the image 
        height, width= gray.shape[:2]
        print(f"height= {height}")
        print(f"width = {width}")
        max_height = 150
        max_width = 150
        # only shrink if img is bigger than required
        if max_height < height or max_width < width:
            # get scaling factor
            scaling_factor = max_height / float(height)
            if max_width/float(width) < scaling_factor:
                scaling_factor = max_width / float(width)
            # resize image
            gray = cv2.resize(gray, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        height, width= gray.shape[:2]
        #-------------------------------------------
        # 3nd
        # Lets place an ascii key in place of an intensity value 
        # "Standard" character ramp for grey scale pictures. 
        # 70 characters long, black -> white.
        ascii_map=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        ascii_map.reverse()
        # 10 characters long, white -> black. 
        ascii_short_map=list(" .:-=+*#%@")
        fiename=f'{file_name}.txt'
        line=''
        ascii_img=''
        for x in range(height):
            for y in range(width):
                         line+=ascii_map[int(gray[x,y]//(256/len(ascii_map)))]
            with open(f"ascii_art\{fiename}",'a') as file_object:
                file_object.write(line+"\n")
            line=''
        print(f"{file_name}")

def setup_art(card): 
    retrive_img(name=card.name,url=card.img_url)
    image_2_ascii(file_name=card.name)
