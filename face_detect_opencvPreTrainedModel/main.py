import os
import cv2 as cv
from age_gender_detector import age_gender_detector

print('This model is based on opencv pre-trained face detector.')
print('----------------------------------------------------------')
print('TIP: while entering the location use \\\\ instead of \\ to not get errors.')
print('----------------------------------------------------------')
print("Want to detect face on images or videos")
print("1. Images")
print("2. Videos")
x = input("Enter Your Choice: ").lower()

if x in ['1', 'images', 'image']:
    loc = input("Enter the location of the file: ")
    
    if not os.path.exists(loc):
        print('File does not exists at the specified location.')

    
    else:
        input = cv.imread(loc)

        if input.shape[1] > 600 or input.shape[0] > 600:
            input = cv.resize(input, (input.shape[1]//3, input.shape[0]//3)) 

        output = age_gender_detector(input)
        
        cv.imshow('Image', output)

elif x in ['2', 'videos', 'video']:
    print("Get Video From?")
    print("1. Use Camera")
    print("2. Enter location Manually")
    
    o = input("Select a Option: ").lower()

    if o in ['1', 'use camera']:
        print("Ensure proper lightning to get optimal results. ")
        capture = cv.VideoCapture(0)

        print("PRESS 'd' TO EXIT.")
        while True:
            isTrue, frame = capture.read()
    
            output = age_gender_detector(frame)
    
            cv.imshow('Camera', output)

            if cv.waitKey(20) & 0xFF == ord('d') or cv.getWindowProperty('Camera', cv.WND_PROP_VISIBLE) < 1:
                break
    
    if o in ['2', 'enter location manually']:
        video = input("Enter the Loaction of the vidoeo: ")

        if not os.path.exists(video):
            print('File does not exists at the specified location.')
    
        else:
            capture = cv.VideoCapture(video)

            print("PRESS 'd' TO EXIT.")
            while True:
                isTrue, frame = capture.read()
        
                output = age_gender_detector(frame)
        
                cv.imshow('Camera', output)

                if cv.waitKey(20) & 0xFF == ord('d') or cv.getWindowProperty('Camera', cv.WND_PROP_VISIBLE) < 1:
                    break

cv.waitKey(0)
