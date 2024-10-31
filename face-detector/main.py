#imports
import cv2
import numpy as np

#initialization
face_cascade = cv2.CascadeClassifier('./classifier/faceCascade.xml')
camera = cv2.VideoCapture(0)

#detect face
def face_detection(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(optimized_frame, scaleFactor=1.1, minSize=(50, 50), minNeighbors=5)
    return faces

#infos
def info_text(frame):

    faces = face_detection(frame)
    cv2.putText(frame, f"Face detected: {len(faces) | 0}", (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 225), 1)

    text = "Press Q to exit"
    cv2.putText(frame, text, (500, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 225), 1)



#color check 
def skin_color_classification(face_img):
    if face_img is None or face_img.size == 0:
        return "Unknown"
    
    hsv = cv2.cvtColor(face_img, cv2.COLOR_BGR2HSV)
    avg_color = np.mean(hsv[:, :, 0]) 

    if avg_color < 20:
        return "Nigga"
    elif avg_color < 48:
        return "Cokolat"
    else:
        return "Putih"

#rect around face
def draw_rectangle(frame):
    
    for x, y, w, h in face_detection(frame):
        face_img = frame[ y:y+h, x:x+w]
        skin_color_info = skin_color_classification(face_img)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
        (text_width, text_height), baseline = cv2.getTextSize(skin_color_info, cv2.FONT_HERSHEY_PLAIN, 1, 1 )

        cv2.rectangle(frame, (x, y + h), (x + text_width, y + h + text_height + baseline), (0, 255, ), -1  )
        cv2.putText(
            frame, 
            skin_color_info, 
            (x, y + h + text_height), 
            cv2.FONT_HERSHEY_PLAIN, 
            1, 
            (0, 0, 0), 
            2, 
            cv2.LINE_AA
        )


#clearing
def finish_all():
    camera.release()
    cv2.destroyAllWindows()
    exit()

#main
def main():
    while True:
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)
        draw_rectangle(frame)
        info_text(frame)
        cv2.imshow("What race you are?", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            finish_all()

if __name__ == '__main__':
    main()