import time
import cv2
import os
import argparse

def videotoframe(input_loc):
    output_loc="./tmpframes"
    time_start = time.time()
    cap = cv2.VideoCapture(input_loc)
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n")
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count + 1), frame)
        count = count + 1
        if (count > (video_length - 1)):
            time_end = time.time()
            cap.release()
            print("Done extracting frames.\n%d frames extracted" % count)
            print("It took %d seconds for conversion." % (time_end - time_start))
            break
def frametogray(path):
    pass
def g2ftocolor(path):
    pass
def getresvideo(path):
    dir_path = './ansframes'
    ext = 'jpg'
    output = path

    images = []
    for f in os.listdir(dir_path):
        if f.endswith(ext):
            images.append(f)
    # Determine the width and height from the first image
    image_path = os.path.join(dir_path, images[0])
    frame = cv2.imread(image_path)
    # cv2.imshow('video',frame)
    height, width, channels = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output, fourcc, 25.0, (width, height))

    for image in images:
        image_path = os.path.join(dir_path, image)
        frame = cv2.imread(image_path)

        out.write(frame)  # Write out frame to video

        # cv2.imshow('video',frame)
    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()

    #print("The output video is {}".format(output))
