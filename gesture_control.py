from utils import calculate_distance
from config import (
    LEFT_CLICK_THRESHOLD,
    RIGHT_CLICK_THRESHOLD
)


class GestureController:

    def __init__(self):

        self.previous_left = False
        self.previous_right = False

    def get_finger_states(self, landmarks):

        # Finger tip and PIP joint positions
        fingers = []

        # Index, middle, ring and pinky
        tips = [8, 12, 16, 20]
        pips = [6, 10, 14, 18]

        for tip, pip in zip(tips, pips):

            is_extended = landmarks[tip].y < landmarks[pip].y

            fingers.append(is_extended)

        return fingers

    def detect_gesture(self, landmarks):

        if landmarks is None:
            return "NO HAND"

        fingers = self.get_finger_states(landmarks)

        index, middle, ring, pinky = fingers

        thumb = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]

        left_distance = calculate_distance(
            thumb,
            index_tip
        )

        right_distance = calculate_distance(
            thumb,
            middle_tip
        )

        # Pause gesture: all four fingers extended
        if all(fingers):
            self.previous_left = False
            self.previous_right = False
            return "PAUSE"

        # Left click
        if left_distance < LEFT_CLICK_THRESHOLD:

            if not self.previous_left:
                self.previous_left = True
                self.previous_right = False
                return "LEFT CLICK"

        else:
            self.previous_left = False

        # Right click
        if right_distance < RIGHT_CLICK_THRESHOLD:

            if not self.previous_right:
                self.previous_right = True
                self.previous_left = False
                return "RIGHT CLICK"

        else:
            self.previous_right = False

        # Scroll
        if index and middle and not ring and not pinky:
            return "SCROLL"

        # Cursor movement
        if index and not middle and not ring and not pinky:
            return "MOVE"

        return "NONE"