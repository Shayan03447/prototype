import cv2

def start_camera():
    cap=cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open cammera")
        return 
    
    print("camera opened successfully")

    while True:
        ret, frame=cap.read()
        if not ret:
            print("ERROR: Could not read Frame")
            break

        cv2.imshow("TryNStyle - Camera", frame)

        key=cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    start_camera()