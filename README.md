# ffmpeg_thumbnail
 This is a python script for using ffmpeg to create screenshots from a collection of videos at one specified time(in the videos)(variable *time*) for all the videos in a source folder(variable *path*) and using them as thumbnail in the same video sent to another location(variable *destination*).
 ------------
 
All of these variables can be replaced in the main() function.

To install ffmpeg refer https://www.wikihow.com/Install-FFmpeg-on-Windows. Sometimes after adding path a restart is needed and sometimes a "\\" is needed at the end that is in the path variable change it from c:\FFmpeg\bin to c:\FFmpeg\bin\\.


This is not yet complete but works ok, some of the work remaining off the top of my head are:

 #TODO Create a try except block for if the filename contains "."

 #TODO Auto rename the files if they have "." in them to change them to "-".

 #TODO Auto create a folder in the home directory to store the newly thumbnailed videos.

 #TODO Split the engine function to two separate functions so that this script can be used as a module to either get thumbnails from video or thumbnail videos.

 #TODO Add a control for number of files so that if only the file is given as input then only one file gets thumbnailed.

 #TODO Add GUI too advanced for me now.

Sources
"""
 https://stackoverflow.com/questions/42438380/ffmpeg-in-python-script
 https://trac.ffmpeg.org/wiki/Create%20a%20thumbnail%20image%20every%20X%20seconds%20of%20the%20video
 https://stackoverflow.com/questions/54717175/how-do-i-add-a-custom-thumbnail-to-a-mp4-file-using-ffmpeg
"""
