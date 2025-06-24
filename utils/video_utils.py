import cv2
import os

def extract_frames(video_path, interval_sec=1):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    saved_paths = []
    os.makedirs("frames", exist_ok=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % (fps * interval_sec) == 0:
            filename = f"frames/frame_{frame_count}.jpg"
            cv2.imwrite(filename, frame)
            saved_paths.append(filename)

        frame_count += 1

    cap.release()
    return saved_paths
