import cv2
import random
import os
from tqdm import tqdm

video_path = './input/'
input_videos = os.listdir(video_path)

# remove .DS_Store


print(input_videos)

p = 0.5  # Probability of selecting a frame

# Define output video properties
frame_rate = 12
width = 1920
height = 1080

# Loop through input video files
frames = []
total_frames_read = 0  # Separate variable to count total frames read

print(f'Selecting frames with probability {p}')
for input_video in input_videos:
    cap = cv2.VideoCapture(video_path + input_video)
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    with tqdm(total=num_frames) as pbar: 
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                total_frames_read += 1
                if random.random() < p:
                    frames.append(frame)
            else:
                break
            pbar.update(1)
    cap.release()

print(f'\nSelected {len(frames)} frames from a total of {total_frames_read} frames!')

print("\nNow shuffling frames")
random.shuffle(frames)
print("\nShuffling Complete!\n")

# Create new video file from selected frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('baddie.mp4', fourcc, frame_rate, (width, height)) # dependendo do formato de input, acho que pode dar erro aqui

print('Saving Video')
with tqdm(total=len(frames)) as pbar_write: 
    for frame in frames:
        out.write(frame)
        pbar_write.update(1)
out.release()
print('Video Saved!')