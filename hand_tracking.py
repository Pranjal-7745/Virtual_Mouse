import cv2
import mediapipe as mp

from config import (
    MAX_HANDS,
    DETECTION_CONFIDENCE,
    TRACKING_CONFIDENCE
)


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            max_num_hands=MAX_HANDS,
            min_detection_confidence=DETECTION_CONFIDENCE,
            min_tracking_confidence=TRACKING_CONFIDENCE
        )

        self.results = None

    def find_hands(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        self.results = self.hands.process(rgb_frame)

        if self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame

    def get_landmarks(self, frame):

        landmarks = []

        if self.results and self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            height, width, _ = frame.shape

            for id, landmark in enumerate(hand.landmark):

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                landmarks.append((id, x, y))

        return landmarks

    def get_hand_landmarks(self):

        if self.results and self.results.multi_hand_landmarks:

            return self.results.multi_hand_landmarks[0].landmark

        return None

    def close(self):

        self.hands.close()