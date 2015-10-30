import sys
import gen_data as gd
import glob, time

file1=open('label.txt','w')
file2=open('image_arr.txt','w')
file1.write("")
file2.write("")
file1.close()
file2.close()
array_folder = ["training/a/*.png","training/b/*.png","training/c/*.png","training/d/*.png","training/e/*.png",
           "training/f/*.png","training/g/*.png","training/h/*.png","training/i/*.png","training/k/*.png",
           "training/l/*.png","training/m/*.png","training/n/*.png","training/o/*.png","training/p/*.png",
           "training/r/*.png","training/s/*.png","training/t/*.png","training/u/*.png","training/v/*.png",
           "training/w/*.png","training/x/*.png","training/y/*.png","training/z/*.png"]
for item in array_folder:
    files = glob.glob(item)
    for file in files:
        gd.generate_data(file, ord(item.split("/")[1]))
        
print "training complete"
time.sleep(1)

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

#dir_path=""
class Handler:
    def __init__(self):
        self.dir_path = ""
        self.probability = ""
    def handExit(self, *args):
        print "exit"
        gtk.main_quit(*args)
        
    def handReset(self, *args):
        print "reset"
        lb_show.set_text("")
        
    def handCrack(self, *args):
        print "cracked"
        if self.dir_path == "":
            print "Cannot Crack captcha !!!"
            
    def handChooseFile(self, *args):
        print "choose"
        
        if (file_choose.get_filename().split("/")[-1]).split(".")[1] == "png":
            print "start cracking captcha..."
            self.dir_path = file_choose.get_filename()
            img1.set_from_file(file_choose.get_filename())
        else:
            print "sorry, it is not image png"
            
        
builder = gtk.Builder()
builder.add_from_file("captcha.glade")    
builder.connect_signals(Handler())

lb_show = builder.get_object("label1")
file_choose = builder.get_object("filechooserbutton1")
img1 = builder.get_object("image1")
img2 = builder.get_object("image2")

window = builder.get_object("window1")
window.show_all()

gtk.main()