'''
Created on 10 Oct. 2015
@author: Karishma
The use of this function is to display the GUI of the application. This code allows the user to select image file and show the 
loaded file 
'''
#!/usr/bin/env python

#gui.py
import pygtk
pygtk.require('2.0')
import gtk

#Base constructor needed to give the default functions
class Base:
    #when user presses a red cancel button 
    def destroy(app,widget,data=None):
        gtk.main_quit()
    
    #when window loads for first time    
    def __init__(app):
        app.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        app.window.set_position(gtk.WIN_POS_CENTER)
        app.window.set_size_request(600,600)
       
        #button1
        app.button1=gtk.Button("EXIT")
        app.button1.connect("clicked",app.destroy)        
        
        #file chooser
        dialog = gtk.FileChooserDialog("Choose an Image",
                None,gtk.FILE_CHOOSER_ACTION_OPEN,
                (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
                 gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        filter= gtk.FileFilter()
        filter.set_name("Images")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        filter.add_pattern("*.png")
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.jpeg")
        dialog.add_filter(filter)
        
        response=dialog.run()
        if response == gtk.RESPONSE_OK:
            app.pix=gtk.gdk.pixbuf_new_from_file(dialog.get_filename())
            app.pix=app.pix.scale_simple(200,100,gtk.gdk.INTERP_BILINEAR)
            app.image=gtk.image_new_from_pixbuf(app.pix) 
        elif response == gtk.RESPONSE_CANCEL:
            print ("No file selected")
        dialog.destroy()
        
        #container for button, image     
        app.box1=gtk.HBox()
        app.box1.pack_start(app.button1)
        app.box1.pack_start(app.image)
        
        app.window.add(app.box1)
        app.window.show_all()
        app.window.connect("destroy",app.destroy)
    
    #calling the main    
    def main(app):
        gtk.main()

#calling the constructor         
if __name__=="__main__":
    base = Base()
    base.main() 