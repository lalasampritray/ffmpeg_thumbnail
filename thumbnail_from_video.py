#! python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:28:40 2020

@author: Lala Samprit Ray
This is a python script for using ffmpeg to create screenshots from a collection of videos at one specified time and using them as thumbnail in the same video.
"""

import os


def engine(time, path, destination):
    """This function creates thumbnails with same name as videos in the same place as the source path and creates new thumbnailed videos in the destination path
        The filename should not have "." (dot) in them.
    Parameters
    ----------
    time : [string]
        In the form "00:00:04" signifying the point at which thumbnail frame has to be taken
    path : [string]
        If windows os is to be used then another backlash has to be added wherever there is a backslash in the path and in the end a double backslash has to be added
        example: "C:\\Users\\myname\\Videos\\python\\Python\\Python\\"
    destination : [string]
        preferrably in the home folder and folder should be empty. Same conditions as path applies.
        example : "C:\\Users\\myname\\videoJatra\\"
    """
    i = 0
    for filename in os.listdir(path):
        if (filename.endswith(".mp4")):  # or .avi,  .mpeg,  whatever.
            # sends commands to command prompt to create a thumbnail image at the time given
            os.system("ffmpeg -i {0}{1} -ss {2} -vframes 1 {3}{4}.png".format(
                path, filename, time, path, filename.split(".")[0]))
            os.system("ffmpeg -i {0}{1} -i {2}{3}.png -map 1 -map 0 -c copy -disposition:0 attached_pic {4}{5}.mp4".format(
                path, filename, path, filename.split(".")[0], destination, i))  # this line adds thumbnail to video
            i += 1
        else:
            continue


def main():
    time = "00:00:04"
    path = "C:\\Users\\myname\\Videos\\python\\Python\\Python\\"
    destination = "C:\\Users\\myname\\videoJatra\\"
    engine(time, path, destination)


if __name__ == "__main__":
    main()

"""
 https://stackoverflow.com/questions/42438380/ffmpeg-in-python-script
 https://trac.ffmpeg.org/wiki/Create%20a%20thumbnail%20image%20every%20X%20seconds%20of%20the%20video
 https://stackoverflow.com/questions/54717175/how-do-i-add-a-custom-thumbnail-to-a-mp4-file-using-ffmpeg
"""
