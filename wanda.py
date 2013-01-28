#!/usr/bin/env python
from gi.repository import Gtk
import os


class Wanda(Gtk.Window):

    label = None

    def __init__(self):
        Gtk.Window.__init__(self, title="Wanda The Fish Says...")
        self.set_default_size(700,300)
        self.label = Gtk.Label()
        self.label.set_line_wrap(False)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.display_fortune()                             #first fortune when it starts up.
        self.set_icon_from_file("wanda.jpg")
     
        table = Gtk.Table(1, 2, True)
        table.set_row_spacings(200)
        table.set_col_spacings(50)
 
        self.add(table)

        button1 = Gtk.Button(label="Speak Again!")
        button1.connect("clicked", self.on_button1_clicked)

        button2 = Gtk.Button(label="Enough Wisdom for Now!")
        button2.connect("clicked", self.on_button2_clicked)

        table.attach(self.label,0,1,0,1)    
        table.attach(button2, 1, 2, 1, 2)
        table.attach(button1, 0, 1, 1, 2)
     
    def on_button1_clicked(self, widget):
         self.display_fortune()

    def on_button2_clicked(self, widget):
        self.display_fortune()
        self.iconify()
 
    def display_fortune(self):
       os.system("fortune -a > .last.txt")
       with open(".last.txt") as f:
         text = str(f.read())
       self.label.set_label(text)
       self.resize(700,300)    
    
win = Wanda()
win.resize(700,300)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
