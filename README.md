# ffmpeg_thumbnail
 This is a python script for using ffmpeg to create screenshots from a collection of videos at one specified time(in the videos)(variable *time*) for all the videos in a source folder(variable *path*) and using them as thumbnail in the same video sent to another location(variable *destination*).
 ------------
 
All of these variables can be replaced in the main() function.

To install ffmpeg refer https://www.wikihow.com/Install-FFmpeg-on-Windows. Sometimes after adding path a restart is needed and sometimes a "\\" is needed at the end that is in the path variable change it from c:\FFmpeg\bin to c:\FFmpeg\bin\\.


This is not yet complete but works ok, some of the work remaining off the top of my head are:

 ~~#TODO Create a try except block for if the filename contains "."~~ not required

 ~~#TODO Auto rename the files if they have "." in them to change them to "-".~~ Done

 ~~#TODO Auto create a folder in the home directory to store the newly thumbnailed videos.~~ not required

 ~~#TODO Split the engine function to two separate functions so that this script can be used as a module to either get thumbnails from video or thumbnail videos.~~ Not required

 ~~#TODO Add a control for number of files so that if only one file is given as input then only one file gets thumbnailed.~~ can just put one file in a folder so not required.

 #TODO Add GUI too advanced for me now.

