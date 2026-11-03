import cv2


def main():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Webcam not found!")
        return

    while True:

        success, frame = cap.read()

        if not success:
            print("Failed to capture frame")
            break

        frame = cv2.flip(frame, 1)

        cv2.imshow("Camera Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()