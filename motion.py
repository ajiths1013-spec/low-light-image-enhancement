import cv2
import numpy as np
import config

def get_motion_mask(prev, curr):
    prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(
        prev_gray, curr_gray, None,
        0.5, 3, 15, 3, 5, 1.2, 0
    )

    mag, _ = cv2.cartToPolar(flow[...,0], flow[...,1])
    mask = mag > config.MOTION_THRESHOLD

    return mask.astype(np.uint8)

def selective_fusion(prev, curr, mask):
    fused = curr.copy()

    static = mask == 0
    fused[static] = (prev[static]*0.5 + curr[static]*0.5)

    return fused.astype('uint8')