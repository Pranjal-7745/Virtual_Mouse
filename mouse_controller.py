import pyautogui

from config import SMOOTHING


class MouseController:

    def __init__(self):

        self.screen_width, self.screen_height = pyautogui.size()

        self.previous_x = 0
        self.previous_y = 0

        # Keep PyAutoGUI's emergency fail-safe enabled.
        pyautogui.FAILSAFE = True

    def move_mouse(self, x, y):

        # Smooth mouse movement
        current_x = self.previous_x + (
            x - self.previous_x
        ) / SMOOTHING

        current_y = self.previous_y + (
            y - self.previous_y
        ) / SMOOTHING

        self.previous_x = current_x
        self.previous_y = current_y

        pyautogui.moveTo(
            int(current_x),
            int(current_y)
        )

    def left_click(self):

        pyautogui.click()

    def right_click(self):

        pyautogui.rightClick()

    def scroll(self, amount):

        pyautogui.scroll(amount)