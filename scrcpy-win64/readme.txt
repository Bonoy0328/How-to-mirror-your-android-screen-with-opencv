downloaded from: https://github.com/Genymobile/scrcpy

how to connect wirelessly:
step 1: connect via usb

$ adb usb
restarting in USB mode
$ adb devices
List of devices attached
ZX1D63HX9R  device


$ adb tcpip 5555
restarting in TCP mode port: 5555


$ adb connect 192.168.0.102:5556
already connected to 192.168.0.102:5555
$ adb devices
List of devices attached
ZX1D63HX9R  device
192.168.0.102:5556  device

step 2: done, disconnect via usb now

optional info:
realme 3 screen size : 720x1520