import os
import cv2
import numpy as np
import pyautogui
import PIL.ImageGrab as ImageGrab
import imutils
import time
import psutil
from zipfile import ZipFile

realScreen_x = 720
realScreen_y = 1440

box = (1,33,492,1016) #Android screen coordinates

try:
	# Create a ZipFile Object and load sample.zip in it
	with ZipFile('scrcpy-win64.zip', 'r') as zipObj:
		# Extract all the contents of zip file in current directory
		zipObj.extractall()
		print('>> "scrcpy-win64" Extraction complete')
except Exception as e:
	pass

def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def convert_time(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def adbShell(cmd):
	try:
		os.chdir(adb_dir)
		tap_coordinates = cmd
		os.system(tap_coordinates) #x,y
		os.chdir(orig_dir)
	except Exception as e:
		print(e)
		cv2.destroyAllWindows()
		input('>> adb failed, press Enter to continue')

# 205 147
def tap_once(x,y):
	try:
		os.chdir(adb_dir)
		tap_coordinates = 'adb shell input tap '+str(x)+' '+str(y)
		os.system(tap_coordinates) #x,y
		os.chdir(orig_dir)
	except Exception as e:
		print(e)
		cv2.destroyAllWindows()
		input('>> adb failed, press Enter to continue')

def input_once(text):
	try:
		os.chdir(adb_dir)
		tap_coordinates = 'adb shell input text '+str(text)
		os.system(tap_coordinates) #x,y
		os.chdir(orig_dir)
	except Exception as e:
		print(e)
		cv2.destroyAllWindows()
		input('>> adb failed, press Enter to continue')

#Excluding from running two mirrors of android screen
if checkIfProcessRunning('scrcpy-noconsole.exe'):
	print('>> Android screen already mirrored')
else:
	print('>> Mirroring android screen')
	os.system('start scrcpy-win64/scrcpy-noconsole.exe')

#initializing program
run_status = 1
st = time.time()

#Reading paths
orig_dir = os.getcwd()
adb_dir = os.path.join(os.getcwd(), "scrcpy-win64")

#getting started
input('>> Press Enter to continue')

search_bar_left_temp = cv2.imread("./flag_img/search_bar_left.png")
search_bar_right_temp = cv2.imread("./flag_img/search_bar.png")
keyboard_bar_temp = cv2.imread("./flag_img/type_page_keyboard.png")
type_bar_left_temp = cv2.imread("./flag_img/type_page_left.png")
type_bar_right_temp = cv2.imread("./flag_img/type_page_right.png")

timeline = 0
startTimepoint = 0
startTimepoint2 = 0

while True:
	#Reading frames from screen
	screen = ImageGrab.grab(box)
	screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
	cv2.imwrite("page_search.png",screen)
	# screen = imutils.resize(screen, height=985)

	
	# search "search bar"
	res = cv2.matchTemplate(screen,search_bar_left_temp,cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	if(max_val > 0.8):
		if(timeline - startTimepoint > 30):
			tap_once(int((top_left[0] + bottom_right[0])/2),int((top_left[1] + bottom_right[1])/2))
			startTimepoint = timeline
			print("tap tap tap tap " + str(int((top_left[0] + bottom_right[0])/2)) + " " + str(int((top_left[1] + bottom_right[1])/2)))
		print("now in main page")
		# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
		top_left = max_loc
		res = cv2.matchTemplate(screen,search_bar_right_temp,cv2.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
		bottom_right = (max_loc[0] + search_bar_right_temp.shape[1], max_loc[1] + search_bar_right_temp.shape[0])
		cv2.putText(img=screen, text='SearchBar', org=(top_left[0],top_left[1]-8), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=1)
		cv2.rectangle(screen,top_left, bottom_right, 255, 2)
	else:
		startTimepoint = timeline
	
	res = cv2.matchTemplate(screen,type_bar_left_temp,cv2.TM_CCOEFF_NORMED)
	min_val, max_val_type, min_loc, max_loc = cv2.minMaxLoc(res)
	if max_val_type > 0.8:
		if ( timeline - startTimepoint2 ) > 30:
			input_once("tizhicheng")
			time.sleep(1)
			tap_once(70,700)
			startTimepoint2 = timeline
		# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
		top_left = (max_loc[0] + type_bar_left_temp.shape[1],max_loc[1])
		res = cv2.matchTemplate(screen,type_bar_right_temp,cv2.TM_CCOEFF_NORMED)
		min_val, max_val_type, min_loc, max_loc = cv2.minMaxLoc(res)
		# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
		bottom_right = (max_loc[0] + type_bar_right_temp.shape[1], max_loc[1] + type_bar_right_temp.shape[0])
		cv2.putText(img=screen, text='TypeBar', org=(top_left[0],top_left[1]-8), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=1)
		cv2.rectangle(screen,top_left, bottom_right, 255, 2)
		res = cv2.matchTemplate(screen,keyboard_bar_temp,cv2.TM_CCOEFF_NORMED)
		min_val, max_val_type2, min_loc, max_loc = cv2.minMaxLoc(res)
		# print(str(min_val) + " " + str(max_val) + " " + str(min_loc) + " " + str(max_loc))
		top_left = max_loc
		bottom_right = (max_loc[0] + keyboard_bar_temp.shape[0],max_loc[1] + keyboard_bar_temp.shape[1])
		cv2.rectangle(screen,top_left, bottom_right, 255, 2)
		print("now is type page")
	else:
		startTimepoint2 = timeline
 
	#reading time elapsed
	et = time.time()
	elapsed_time = et-st
	elapsed_time = round(elapsed_time)

	#performing fps calculation, till first 30 seconds to get an idea
	try:
		if elapsed_time < 30:
			fps = run_status/elapsed_time
			fps = round(fps)
	except Exception as e:
		print(e)
		fps = 0

	#printing information
	elapsed_time = convert_time(elapsed_time)
	frame_info = 'FPS: ' + str(fps) + ' , Time: ' + str(elapsed_time)
	cv2.putText(screen, "{}".format(frame_info), (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
	os.system('cls')
	print(frame_info)

	#Showing frames
	#cv2.imwrite('temp/game_screen'+str(run_status)+'.png',screen)
	cv2.imshow('Screen', screen)

	#tapping somewhere on screen
	# if run_status == 5:
	# 	x,y = (360,360) #coordinate according to your android phone screen
	# 	tap_once(x,y)

	#Program End Handling Block
	# run_status +=1
	timeline += 1
	key = cv2.waitKey(1)
	if key == ord("q"):
		cv2.destroyAllWindows()
		break
