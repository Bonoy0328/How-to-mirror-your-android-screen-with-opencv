from PIL import Image
import cv2
from paddleocr import PaddleOCR, draw_ocr

# Test Template Match
# search_bar_left_temp = cv2.imread("./flag_img/type_page_left.png")
# search_bar_right_temp = cv2.imread("./flag_img/type_page_right.png")
# keyboard_bar_temp = cv2.imread("./flag_img/type_page_keyboard.png")
# img = cv2.imread("page_search.png")

# res = cv2.matchTemplate(img,search_bar_left_temp,cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
# top_left = (max_loc[0] + search_bar_left_temp.shape[1],max_loc[1])
# res = cv2.matchTemplate(img,search_bar_right_temp,cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
# bottom_right = (max_loc[0] + search_bar_right_temp.shape[1], max_loc[1] + search_bar_right_temp.shape[0])
# cv2.putText(img=img, text='TypeBar', org=(top_left[0],top_left[1]-8), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=1)
# cv2.rectangle(img,top_left, bottom_right, 255, 2)
# res = cv2.matchTemplate(img,keyboard_bar_temp,cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
# top_left = max_loc
# bottom_right = (max_loc[0] + keyboard_bar_temp.shape[0],max_loc[1] + keyboard_bar_temp.shape[1])
# cv2.rectangle(img,top_left, bottom_right, 255, 2)
# cv2.imshow("img",img)
# cv2.waitKey(0)

# Test for Image crop
# img = Image.open("page_search.png")
# croped = img.crop((18,90,50,126))
# croped.save("type_page_left.png")
# croped = img.crop((354,96,388,122))
# croped.save("type_page_right.png")
# croped = img.crop((95,725,381,895))
# croped.save("type_page_keyboard.png")


#Test for baidu orc

# ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# # 

# img_path = 'page_search.png'
# result = ocr.ocr(img_path, cls=True)

# for line in result:
#     print(line)

# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')

# from pyminitouch import safe_connection, safe_device, MNTDevice, CommandBuilder
 
# _DEVICE_ID = 'LKX0218307005327'
 
# device = MNTDevice(_DEVICE_ID)
 
# # print the maximum x and Y coordinates
# print("max x:", device.connection.max_x)
# print("max y:", device.connection.max_y)



import os
import cv2
import numpy as np
import pyautogui
import PIL.ImageGrab as ImageGrab
import imutils
import time
import psutil
from zipfile import ZipFile

# orig_dir = os.getcwd()
# adb_dir = os.path.join(os.getcwd(), "scrcpy-win64")
# def adbShell(cmd):
#     try:
#         os.chdir(adb_dir)
#         tap_coordinates = cmd
#         os.system(tap_coordinates) #x,y
#         os.chdir(orig_dir)
#     except Exception as e:
#         print(e)
#         cv2.destroyAllWindows()
#         input('>> adb failed, press Enter to continue')
  
# while True:
#     # adbShell("adb exec-out screencap -p > s")
#     adbShell("adb shell screencap -p  /sdcard/screen.png")
#     adbShell("adb pull /sdcard/screen.png")
#     adbShell("adb shell rm -rf /sdcard/screen.png")
#     screen = cv2.imread("screen.png")
#     cv2.imshow('Screen', screen)
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         cv2.destroyAllWindows()
#         break
# orig_dir = os.getcwd()
# adb_dir = os.path.join(os.getcwd(), "scrcpy-win64")

# def tap_once(x,y):
#     try:
#         os.chdir(adb_dir)
#         tap_coordinates = 'adb shell input tap '+str(x)+' '+str(y)
#         os.system(tap_coordinates) #x,y
#         os.chdir(orig_dir)
#     except Exception as e:
#         print(e)
#         cv2.destroyAllWindows()
#         input('>> adb failed, press Enter to continue')

# tap_once(310,58)


img = cv2.imread("screen.png")
print(img.shape)

