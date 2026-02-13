# 🎮 Intelligent Eye-Controlled Game System  
### Play Temple Run 2 Using Your Eyes 👀

This project allows you to control Temple Run 2 in your browser using real-time eye movement tracking.  
It uses MediaPipe FaceMesh, OpenCV, and PyAutoGUI to detect eye direction and simulate keyboard inputs.

---

## 🚀 Features

- Real-time eye tracking using MediaPipe FaceMesh  
- Smooth eye movement detection using moving average  
- Cooldown system to prevent accidental multiple inputs  
- Automatically opens and controls Temple Run 2  
- Live camera visualization with eye landmark overlay  
- Dynamic screen-based thresholds  

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- MediaPipe  
- PyAutoGUI  
- Webbrowser module  

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/eye-game-control.git
cd eye-game-control
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ How It Works

1. The program opens Temple Run 2 in your browser.
2. Webcam starts capturing your face.
3. MediaPipe FaceMesh detects facial landmarks.
4. Eye center positions are calculated.
5. Movement direction is determined based on screen midpoint.
6. PyAutoGUI simulates arrow key presses.

---

## 🎮 Controls

| Eye Movement | Action |
|--------------|--------|
| Look Left    | Move Left |
| Look Right   | Move Right |
| Look Up      | Jump |
| Look Down    | Slide |

Press **Q** to quit the program.

---

## 🧠 Detection Logic

- Uses extended eye landmarks.
- Calculates average center of both eyes.
- Applies smoothing using deque.
- Uses dynamic threshold (8% of screen width/height).
- 1.5 second cooldown between commands.

---

## 📷 System Requirements

- Python 3.8+
- Webcam
- Good lighting conditions
- Stable head position

---

## ⚠️ Important Notes

- Make sure Temple Run 2 window is active.
- Avoid rapid head movement.
- Ensure proper lighting for better detection.
- Close other applications using keyboard input.

---

## 📈 Future Improvements

- Blink detection for pause/resume  
- Head nod detection  
- Facial expression triggers  
- Voice command integration  
- Calibration mode  
- Sensitivity adjustment UI  

---

## 📄 License

This project is for educational purposes only.

---

## 👨‍💻 Author

Ankur Singh  
BCA Final Year Project  
Intelligent Hands-Free Control System Using Facial and Eye Movement Detection
