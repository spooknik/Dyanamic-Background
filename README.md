# Dynamic-Background
### A simple Python script to change wallpapers and GTK themes throughout the day.

Inspired by Mac OS X Mojave's Dynamic Wallpapers, I wrote my own simple Python script and Systemd service to change the wallpapers and GTK theme throughout the day. 

It works even if the computer is put to sleep, but it doesn't work retroactively. (i.e. The background is suppose to change at 12 and you start the script at 12:15.)

To install simply run 'install.sh'. Do not run as sudo. Everything will be installed to your home directory. It will also enable and start a user systemd service for running the script in the background. If the python script is changed, you need to stop the service (systectl --user stop Dynamic-Background) and then reload (systectl daemon-reload) then start the service again (systectl --user start Dynamic-Background). The status can always be checked using: 'systectl --user status Dynamic-Background'

GTK Themes can also be changed, you just need to know the name of the theme, and schedule it in the python script.

I encourage people to customize this script to their own liking, the current setup is done just as a template for people to understand and see how the script works. 

Please note, this script isn't very advanced, it only changes wallpapers based on the hour of the day, meaning as the seasons change the days and nights may need to be adjusted. I couldn't think of an elegant way to do this, I'll incorporate this function. 

