import cv2
import numpy as np
import config

def estimate_brightness(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

def get_clip_limit(brightness):
    if brightness < config.LOW_BRIGHTNESS:
        return config.CLIP_LOW
    elif brightness < config.MID_BRIGHTNESS:
        return config.CLIP_MID
    else:
        return config.CLIP_HIGH

def adaptive_enhance(img, strength=1.0):
    brightness = estimate_brightness(img)
    clip = get_clip_limit(brightness) * strength

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(8,8))
    cl = clahe.apply(l)

    merged = cv2.merge((cl, a, b))
    enhanced = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    # Edge sharpening
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    sharp = cv2.filter2D(enhanced, -1, kernel)

    return sharp