import tkinter as tk
from tkinter import filedialog
import cv2

from enhance import adaptive_enhance
from motion import get_motion_mask, selective_fusion
from face import protect_faces
from utils import resize_image, convert_to_tk
import config

# ✅ Create root ONLY ONCE (fix for Tkinter error)
root = tk.Tk()
root.title("Smart Low-Light Enhancement System")

prev_frame = None
prev_output = None
strength_val = 1.0


# ---------------- PROCESS FRAME ---------------- #
def process_frame(frame):
    global prev_frame, prev_output

    frame = resize_image(frame)

    # ✅ Motion-safe fusion
    if prev_frame is not None and prev_frame.shape == frame.shape:
        mask = get_motion_mask(prev_frame, frame)
        fused = selective_fusion(prev_frame, frame, mask)
    else:
        fused = frame

    enhanced = adaptive_enhance(fused, strength_val)
    enhanced = protect_faces(frame, enhanced)

    # ✅ Temporal smoothing
    if prev_output is not None:
        enhanced = cv2.addWeighted(
            enhanced, config.TEMPORAL_ALPHA,
            prev_output, 1 - config.TEMPORAL_ALPHA, 0
        )

    prev_output = enhanced
    prev_frame = frame

    return enhanced


# ---------------- DISPLAY ---------------- #
def display(original, enhanced):
    if original is None or enhanced is None:
        return

    img1 = convert_to_tk(original)
    img2 = convert_to_tk(enhanced)

    panelA.config(image=img1)
    panelA.image = img1

    panelB.config(image=img2)
    panelB.image = img2


# ---------------- IMAGE ---------------- #
def open_image():
    global prev_frame, prev_output

    path = filedialog.askopenfilename()
    if not path:
        return

    img = cv2.imread(path)
    img = resize_image(img)

    enhanced = adaptive_enhance(img, strength_val)
    enhanced = protect_faces(img, enhanced)

    display(img, enhanced)

    prev_frame = img
    prev_output = enhanced


# ---------------- VIDEO ---------------- #
def open_video():
    global prev_frame, prev_output

    path = filedialog.askopenfilename()
    if not path:
        return

    cap = cv2.VideoCapture(path)

    prev_frame = None
    prev_output = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        enhanced = process_frame(frame)
        display(frame, enhanced)

        root.update()

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()


# ---------------- CAMERA ---------------- #
def open_camera():
    global prev_frame, prev_output

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # ✅ Check camera
    if not cap.isOpened():
        print("Camera not opening ❌")
        return

    prev_frame = None
    prev_output = None

    global running
    running = True
    while running:
        ret, frame = cap.read()
        if not ret:
            print("Frame not received")
            break

        enhanced = process_frame(frame)
        display(frame, enhanced)

        root.update()

        # Press ESC to exit camera
        running = True

        def stop_camera(event=None):
            global running
            running = False

        root.bind("<Escape>", stop_camera)

    cap.release()


# ---------------- SAVE ---------------- #
def save_output():
    if prev_output is not None:
        cv2.imwrite("output/result.jpg", prev_output)
        print("Saved to output/result.jpg")


# ---------------- SLIDER ---------------- #
def update_strength(val):
    global strength_val
    strength_val = float(val)


# ---------------- UI ---------------- #
tk.Button(root, text="Open Image", command=open_image).pack(pady=5)
tk.Button(root, text="Open Video", command=open_video).pack(pady=5)
tk.Button(root, text="Live Camera", command=open_camera).pack(pady=5)
tk.Button(root, text="Save Output", command=save_output).pack(pady=5)

tk.Label(root, text="Enhancement Strength").pack()

tk.Scale(
    root,
    from_=0.5,
    to=2.0,
    resolution=0.1,
    orient="horizontal",
    command=update_strength
).pack()

panelA = tk.Label(root)
panelA.pack(side="left", padx=10, pady=10)

panelB = tk.Label(root)
panelB.pack(side="right", padx=10, pady=10)


# ---------------- START ---------------- #
root.mainloop()