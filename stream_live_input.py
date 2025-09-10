"""
Live Streaming from Intel RealSense Camera
------------------------------------------
Handles 'No device connected' error gracefully.
"""

import pyrealsense2 as rs
import numpy as np
import cv2
import sys

# ------------------- Configure RealSense -------------------
pipeline = rs.pipeline()
config = rs.config()

# Enable both color and depth streams
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Try to start pipeline
try:
    pipeline.start(config)

except RuntimeError as e:
    if "No device connected" in str(e):
        print("[ERROR] No Intel RealSense device detected. Please check USB connection.")
        sys.exit(1)
    else:
        raise  # re-raise other unexpected errors

try:
    print("[INFO] Streaming live from Intel RealSense... Press ESC to quit.")
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image for visualization
        depth_colormap = cv2.applyColorMap(
            cv2.convertScaleAbs(depth_image, alpha=0.03),
            cv2.COLORMAP_JET
        )

        # Stack color and depth images side by side
        images = np.hstack((color_image, depth_colormap))

        cv2.imshow("RealSense Live Stream (Color | Depth)", images)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
