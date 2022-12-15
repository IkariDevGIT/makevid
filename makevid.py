import os
import random

import moviepy.video.io.ImageSequenceClip
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path_to_images = os.path.abspath(os.getcwd()).replace(os.sep, '/') + "/"

image_files = []

abc = input("images folder: ")
abc2 = int(input("fps: "))
abc3 = int(input("frames to process: "))

for img_number in range(1,abc3):
    image_files.append(path_to_images + abc + "/" + str(img_number) + '.png')

fps = abc2

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)

endname="export"

if os.path.exists(endname + ".mp4"):
    endname = endname + str(random.randint(0,100000000))

end = endname+".mp4"



clip.write_videofile(path_to_images + end)