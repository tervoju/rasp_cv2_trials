import cv2
import time
import numpy as np

def frame_diff(prev_frame, cur_frame, diff_thres=20):

    if prev_frame is None:
        return True
    else:

        _diff = cv2.absdiff(prev_frame, cur_frame)

        diff = np.sum(_diff)/prev_frame.shape[0]/prev_frame.shape[1]/3.
        print(diff)

        if diff > diff_thres:
            return True
        else:
            return False

def main():
    while True:
        cap = cv2.VideoCapture(0)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

        # Capture frame
        ret, frame1 = cap.read()
        if ret:
	        cv2.imwrite('image1.jpg', frame1)
        #cap.release()

        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5) 


        #for (x, y width, height) in bodies:
        #    cv2.retangle(frame, (x,y), (x+ width, y + height), (255, 0, 0))

        if len(bodies) + len(faces) > 0:
             if ret:
                cv2.imwrite('image_face.jpg', frame1)
        cap.release()

        time.sleep(5)
        cap = cv2.VideoCapture(0)
        # Capture frame
        ret, frame2 = cap.read()
        if ret:
	        cv2.imwrite('image2.jpg', frame2)
        cap.release()

        if frame_diff(frame1, frame2):
            print("threshold:")
            cv2.imwrite('image_A.jpg', frame2)

        difference = cv2.subtract(frame1, frame2)
        frame3 = cv2.absdiff(frame1, frame2)
        b, g, r = cv2.split(frame3)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
        else:
            #print("changes in the image")
            cv2.imwrite('imagediff.jpg', frame3)
        time.sleep(5)



if __name__=='__main__':
	main()