import pyrealsense2 as rs
import numpy as np
import cv2
from pyrealsense2 import playback

bag_path = 'stairs.bag'
# bag_path = 'd435i_walk_around.bag'
# bag_path = 'd435i_walking.bag'
# bag_path = 'depth_under_water.bag'
# bag_path = 'outdoors.bag'

pipeline = rs.pipeline()
config = rs.config()
rs.config.enable_device_from_file(config, bag_path, repeat_playback=True)
profile = pipeline.start(config)

# Optional: slow down playback for debugging
device = profile.get_device()
playback_device = device.as_playback()
playback_device.set_real_time(False)

try:
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            print("No depth frame received.")
            continue

        depth_image = np.asanyarray(depth_frame.get_data())
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)



        cv2.imshow('Simulated Depth Stream', depth_colormap)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
