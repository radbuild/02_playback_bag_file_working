import pyrealsense2 as rs
import numpy as np
import cv2
import sys

pipe = rs.pipeline()
config = rs.config()

width = 640
height = 480
frames_per_sec = 30

config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, frames_per_sec)
config.enable_stream(rs.stream.depth, width, height, rs.format.z16, frames_per_sec)

try:
    pipe.start(config)

except RuntimeError as e:
    if "No device connected" in str(e):
        print("Intel RealSense device not detected.")
        sys.exit(1)
    else:
        raise  # re-raise other unexpected errors

while True:
    frame =  pipe.wait_for_frames()

    depth_frame = frame.get_depth_frame()
    color_frame = frame.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())

    cv2.imshow('Depth', depth_image)
    cv2.imshow('Color', color_image)

    if cv2.waitKey(1) == ord('q'):
        break

pipe.stop()
    