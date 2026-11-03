import cv2
import pyautogui

from hand_tracking import HandTracker
from gesture_control import GestureController
from mouse_controller import MouseController

from config import (
    CAMERA_INDEX,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    FRAME_REDUCTION,
    SCROLL_SENSITIVITY
)


def main():

    cap = cv2.VideoCapture(CAMERA_INDEX)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    if not cap.isOpened():
        print("Cannot access webcam!")
        return

    tracker = HandTracker()
    gesture = GestureController()
    mouse = MouseController()

    screen_width, screen_height = pyautogui.size()

    previous_scroll_y = None
    paused = False

    try:

        while True:

            success, frame = cap.read()

            if not success:
                break

            frame = cv2.flip(frame, 1)

            frame = tracker.find_hands(frame)

            landmarks = tracker.get_hand_landmarks()

            gesture_name = gesture.detect_gesture(landmarks)

            height, width, _ = frame.shape

            # Draw active movement region
            cv2.rectangle(
                frame,
                (FRAME_REDUCTION, FRAME_REDUCTION),
                (
                    width - FRAME_REDUCTION,
                    height - FRAME_REDUCTION
                ),
                (255, 0, 255),
                2
            )

            if gesture_name == "PAUSE":

                paused = True

            elif landmarks is not None:

                # Index finger coordinates
                index_tip = landmarks[8]

                x = int(index_tip.x * width)
                y = int(index_tip.y * height)

                if gesture_name == "MOVE" and not paused:

                    screen_x = (
                        (x - FRAME_REDUCTION)
                        * screen_width
                        / (width - 2 * FRAME_REDUCTION)
                    )

                    screen_y = (
                        (y - FRAME_REDUCTION)
                        * screen_height
                        / (height - 2 * FRAME_REDUCTION)
                    )

                    screen_x = max(
                        0,
                        min(screen_width - 1, screen_x)
                    )

                    screen_y = max(
                        0,
                        min(screen_height - 1, screen_y)
                    )

                    mouse.move_mouse(screen_x, screen_y)

                elif gesture_name == "LEFT CLICK" and not paused:

                    mouse.left_click()

                elif gesture_name == "RIGHT CLICK" and not paused:

                    mouse.right_click()

                elif gesture_name == "SCROLL" and not paused:

                    current_y = landmarks[8].y

                    if previous_scroll_y is not None:

                        difference = previous_scroll_y - current_y

                        if abs(difference) > 0.015:

                            amount = int(
                                difference * 100 * SCROLL_SENSITIVITY
                            )

                            if amount != 0:
                                mouse.scroll(amount)

                    previous_scroll_y = current_y

                else:
                    previous_scroll_y = None

            else:

                previous_scroll_y = None

            # Display current gesture
            cv2.putText(
                frame,
                f"Gesture: {gesture_name}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            if paused:

                cv2.putText(
                    frame,
                    "PAUSED - Press R to resume",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

            cv2.imshow("AI Virtual Mouse", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break

            elif key == ord('r'):
                paused = False

    finally:

        cap.release()
        tracker.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()