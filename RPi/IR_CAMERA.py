import cv2
import RPi.GPIO as GPIO
import ftplib

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def capture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('cap.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()

def security_upload():
    session = ftplib.FTP('cribblservices.esy.es','u553917010','Clandestine@1996')
    file = open('cap.jpg','rb')
    session.storbinary('STOR photo.jpg', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
    print 'done'

    
def IR():
    ir_state = GPIO.input(4)
    if ir_state == True:
        print 'woah'
        capture()
        security_upload()
        print 'done'
    else:
        print 'still'

while (True):
    IR()
