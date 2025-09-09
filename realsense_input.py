import pyrealsense2 as rs
import numpy as np

class RealSenseMotion:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, width, height, rs.format.z16, 30)
        self.pipeline.start(config)

    def get_motion_position(self, threshold=1000):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            return None

        depth_image = np.asanyarray(depth_frame.get_data())
        motion_mask = (depth_image < threshold) & (depth_image > 0)

        if np.any(motion_mask):
            indices = np.argwhere(motion_mask)
            avg_pos = np.mean(indices, axis=0)
            y, x = int(avg_pos[0]), int(avg_pos[1])
            return (x, y)  # Pygame uses (x, y)
        return None

    def stop(self):
        self.pipeline.stop()
