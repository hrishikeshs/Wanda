Wanda
======

The fan favorite Wanda The Fish in your Ubuntu Unity Launcher.


In order to add Wanda to your launcher, create a file called wanda.desktop in your home directory. You can download
a photo of wanda from the internetz.
Save it as wanda.jpg in your home directory.
The contents of wanda.desktop should be:
```
[Desktop Entry]
Version=1.0
Type=Application
Name= Wanda Says...
Comment= Easy access to fortunes
TryExec= <path to wanda.py>
Exec= python <path to wanda.py>
Icon= <path to wanda.jpg>
```
Now chmod +x to wanda.desktop and exit. Double click to execute. Drag and drop it onto your launcher.
