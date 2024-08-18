import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

print("This model is based on Haar_cascade.")
print("--------------------------------------------")
print("Want to detect face on images or videos")
print("1. Images")
print("2. Videos")
x = input("Enter Your Choice: ").lower()

if x in ['1', 'images', 'image']:
    loc = input("Enter the location of the file: ")
    if not os.path.exists(loc):
         print("Image cannot be found at the specified location.")

    else:
        img = cv.imread(loc)

        if img.shape[1] > 600 or img.shape[0] > 600:
            img = cv.resize(img, (img.shape[1]//3, img.shape[0]//3)) 

        cv.imshow('Image', img)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

        print(f'Number of faces found = {len(faces_rect)}')

        for (x, y, w, h) in faces_rect:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)

        cv.imshow('detected faces', img)

elif x in ['2', 'videos', 'video']:
    print("Get Video From?")
    print("1. Use Camera")
    print("2. Enter location Manually")
    
    o = input("Select a Option: ").lower()

    if o in ['1', 'use camera']:
        capture = cv.VideoCapture(0)
        print("PRESS 'd' TO EXIT. ")
        
        while True:
            isTrue, frame = capture.read()

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x, y, w, h) in faces_rect:
                    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)

            cv.imshow('Camera', frame)

            if cv.waitKey(20) & 0xFF == ord('d') or cv.getWindowProperty('Camera', cv.WND_PROP_VISIBLE) < 1:
                break
    

    if o in ['2', 'enter location manually']:
        loc = input("Enter the location of the video file: ")

        if not os.path.exists(loc):
            print("Video cannot be found at the specified location.")

        else:
            capture = cv.VideoCapture(loc)

            while True:
                isTrue, frame = capture.read()
        
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

                for (x, y, w, h) in faces_rect:
                        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)

                cv.imshow('Camera', frame)

                if cv.waitKey(20) & 0xFF == ord('d') or cv.getWindowProperty('Camera', cv.WND_PROP_VISIBLE) < 1:
                    break

cv.waitKey(0)
