#!/bin/bash -e
user=$(whoami)

fl=$(find /proc -maxdepth 2 -user $user -name environ -print -quit)
while [ -z $(grep -z DBUS_SESSION_BUS_ADDRESS "$fl" | cut -d= -f2- | tr -d '\000' ) ]
do
  fl=$(find /proc -maxdepth 2 -user $user -name environ -newer "$fl" -print -quit)
done

export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS "$fl" | cut -d= -f2-)

if [ $# -gt 0 ]
then
  PICS_PATH=$1
else
  PICS_PATH="/home/mr-robot/Pictures/Wallpapers/"
fi

IMG=$(find -L $PICS_PATH -name "*.jpg" -o -name "*.png" | shuf -n1)
gsettings set org.gnome.desktop.background picture-uri "file://${IMG}"
#dconf write "/org/gnome/desktop/background/picture-uri" "'file://${IMG}'"

echo -e "$(date): ${IMG}" >> /tmp/wallch.log
