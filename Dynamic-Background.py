#dyanmic-background
import schedule
import time
import subprocess

schedule.every().day.at("21:31").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_4.jpeg", shell=True)

schedule.every().day.at("3:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_1.jpeg", shell=True)
schedule.every().day.at("6:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_2.jpeg", shell=True)
schedule.every().day.at("7:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_3.jpeg", shell=True)
schedule.every().day.at("8:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_4.jpeg", shell=True)
schedule.every().day.at("9:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_5.jpeg", shell=True)
schedule.every().day.at("11:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_6.jpeg", shell=True)
schedule.every().day.at("12:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_7.jpeg", shell=True)
schedule.every().day.at("13:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_8.jpeg", shell=True)
schedule.every().day.at("15:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_9.jpeg", shell=True)
schedule.every().day.at("17:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_10.jpeg", shell=True)
schedule.every().day.at("18:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_11.jpeg", shell=True)
schedule.every().day.at("19:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_12.jpeg", shell=True)
schedule.every().day.at("20:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_13.jpeg", shell=True)
schedule.every().day.at("22:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_14.jpeg", shell=True)
schedule.every().day.at("0:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_15.jpeg", shell=True)
schedule.every().day.at("1:00").do(subprocess.call, "gsettings set org.gnome.desktop.background picture-uri file:///$HOME/.wallpaper/mojave_dynamic_16.jpeg", shell=True)
schedule.every().day.at("7:00").do(subprocess.call, "gsettings set org.gnome.desktop.interface gtk-theme 'Sierra-light'", shell=True) #You can change the GTK-Theme using this line. The place the name of your theme inside the quotes. 
schedule.every().day.at("20:00").do(subprocess.call, "gsettings set org.gnome.desktop.interface gtk-theme 'Sierra-dark'", shell=True)

while True:
    schedule.run_pending()
    time.sleep(1)

