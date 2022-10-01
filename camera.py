# importing cv2 library
import cv2
# opening camera as a variable
video = cv2.VideoCapture(0)
while True:
    rate , frame = video.read()
    # show the frame as camera picture
    cv2.imshow("Video is playing", frame)
    # break the loop and out
    # you can use any letter to command quitting
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        print("Quitted")
        break

video.release()
cv2.destroyAllWindows()