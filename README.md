# 🌙 Smart Low-Light Image Enhancement System for Mobile Cameras

## 📌 Overview
This project presents a smart and adaptive low-light image enhancement system designed for mobile camera applications. The system improves visibility, reduces noise, and preserves natural colors in images and videos captured under poor lighting conditions.

Unlike traditional methods, this system intelligently analyzes brightness, motion, and content to produce high-quality enhanced output in real time.

---

## 🚀 Key Features

### 🔹 1. Adaptive Illumination Enhancement
- Automatically analyzes image brightness
- Adjusts enhancement strength dynamically
- Uses CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Prevents overexposure and unnatural brightness

---

### 🔹 2. Motion-Selective Frame Fusion ⭐ (Core Innovation)
- Detects motion using optical flow
- Separates static and moving regions
- Applies strong denoising for static areas and minimal processing for moving objects
- Prevents motion blur and ghosting artifacts

---

### 🔹 3. Hybrid Noise Reduction
- Adapts noise reduction based on image condition
- Uses bilateral filtering and multi-frame averaging
- Preserves fine details while reducing noise

---

### 🔹 4. Face-Aware Enhancement
- Detects human faces using Haar Cascade
- Applies controlled enhancement on faces
- Prevents over-bright skin and color distortion
- Maintains natural appearance

---

### 🔹 5. Temporal Smoothing (For Video) ⭐
- Reduces flickering in video frames
- Blends current and previous frames
- Produces stable and consistent brightness

---

### 🔹 6. Edge-Aware Sharpening
- Enhances fine details and textures
- Uses sharpening filters
- Avoids halo artifacts

---

### 🔹 7. Real-Time Processing
- Works on images, videos, and live camera feed
- Optimized for performance

---

### 🔹 8. Interactive GUI Interface
- Built using Tkinter
- Features:
  - Open Image
  - Open Video
  - Live Camera
  - Save Output
  - Enhancement Strength Slider

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- NumPy  
- Tkinter  
- Pillow  

---

## 📂 Project Structure
low_light_project/
│── main.py        # Main UI and controller  
│── enhance.py     # Image enhancement logic  
│── motion.py      # Motion detection & fusion  
│── face.py        # Face detection module  
│── utils.py       # Helper functions  
│── config.py      # Parameters and settings  
│── output/        # Saved results  

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
pip install opencv-python numpy pillow

### 2️⃣ Run the Project
python main.py

### 3️⃣ Use Features
- Open Image → Enhance photo  
- Open Video → Process video  
- Live Camera → Real-time enhancement  
- Adjust slider for intensity  
- Save Output → Save result  

---

## 📷 Output Results
- Improved brightness and visibility  
- Reduced noise  
- Natural color preservation  
- Flicker-free video output  

---

## 🧠 Novelty of the Project
This system introduces a combined adaptive framework integrating:
- Motion-selective enhancement  
- Content-aware processing  
- Temporal stability  
- Lightweight real-time execution  

This combination is not commonly found in traditional low-light enhancement systems.

---

## 📈 Applications
- Mobile photography  
- Surveillance systems  
- Night vision enhancement  
- Automotive camera systems  
- Security monitoring  

---

## 👨‍💻 Developed By
Ajith S  
B.Tech Computer Science Engineering

---

## 📌 Future Improvements
- Deep learning-based enhancement  
- Android app deployment  
- GPU acceleration  
- Real-time HDR fusion  

---

## ⭐ Conclusion
This project demonstrates a smart, adaptive, and efficient solution for enhancing low-light images and videos, suitable for real-world mobile applications.
