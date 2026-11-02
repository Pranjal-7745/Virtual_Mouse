# 🖱️ Virtual Mouse Gesture Controller

An AI-driven computer vision project that lets you control your computer's mouse cursor, perform clicks, scroll, and pause control using real-time hand gestures captured by a webcam[cite: 1].

---

## 🛠️ Built With

This project relies on four primary technologies[cite: 1]:

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language[cite: 1] |
| **OpenCV** | Captures webcam input and handles image processing[cite: 1] |
| **MediaPipe** | Detects hands and tracks 21 key hand landmarks in real-time[cite: 1] |
| **PyAutoGUI** | Translates hand coordinates into mouse movements and clicks[cite: 1] |

---

## 🔄 System Architecture & Data Flow

1. **Webcam Input:** Captures real-time video stream of your hand[cite: 1].
2. **OpenCV Processing:** Converts and processes video frames for spatial analysis[cite: 1].
3. **MediaPipe Landmark Detection:** Identifies 21 3D hand keypoints (finger tips and joints)[cite: 1].
4. **Gesture Calculation:** Python computes spatial distances and movement vectors between landmarks[cite: 1].
5. **System Execution:** PyAutoGUI executes the corresponding mouse action on your operating system[cite: 1].

---

## 🖐️ Supported Gesture Mapping

* ☝️ **Move Index Finger** $\rightarrow$ Move mouse cursor[cite: 1]
* 🤏 **Bring Index Finger & Thumb Together** $\rightarrow$ Left-click[cite: 1]
* 🤌 **Pinch Middle Finger & Thumb** $\rightarrow$ Right-click[cite: 1]
* ✌️ **Move Two Fingers Up/Down** $\rightarrow$ Scroll[cite: 1]
* ✋ **Show Open Palm** $\rightarrow$ Pause mouse control[cite: 1]

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have Python installed on your system.

### 2. Install Required Dependencies
Run the following command in your terminal to install the necessary libraries:
```bash
pip install opencv-python mediapipe pyautogui
