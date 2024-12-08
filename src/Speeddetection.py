import cv2
import os

#Path to the video file
video_path=r"D:\Python_Projects\Speed_Detection_122024\data\3\video.hevc"

#Output folder to save images
output_folder =r"D:\Python_Projects\Speed_Detection_122024\Test\Iteration1"
os.makedirs(output_folder, exist_ok=True)

#Open the video file
cap= cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error:Could not open video")
    exit()

#Get the FPS of the vide
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per second: {fps}")
frame_count=0
save_interval =int(fps * 5)

while True:
    #Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        print("End of video or error")
        break
    #Save every nth frame based on the time interval
    if frame_count % save_interval ==0:
        frame_filname = os.path.join(output_folder, f'frame_{frame_count}.jpg')
        cv2.imwrite(frame_filname, frame)
        print(f'saved: {frame_filname}')

    frame_count += 1

    #Display the frame
    cv2.imshow('Video', frame )

    #wait for the user to press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()