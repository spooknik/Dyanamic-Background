#!/bin/bash
#In terminal run: './install.sh'. DO NOT run as sudo. 
echo "Installing backgrounds to home/.wallpapers"
cp -r .wallpaper $HOME/
cp  Dynamic-Background.py /$HOME/.wallpaper/
echo "Installing schedule python module"
pip install schedule
echo "Installing and enabling service."
mkdir -p /$HOME/.config/systemd/user && cp Dynamic-Background.service /$HOME/.config/systemd/user
systemctl --user enable Dynamic-Background
systemctl --user start Dynamic-Background
echo "Finished."


