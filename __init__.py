import gen_data
import time
import glob

if __name__=="__main__":
    array_folder = ["training/a/*.png","training/b/*.png","training/c/*.png","training/d/*.png","training/e/*.png",
               "training/f/*.png","training/g/*.png","training/h/*.png","training/i/*.png","training/k/*.png",
               "training/l/*.png","training/m/*.png","training/n/*.png","training/o/*.png","training/p/*.png",
               "training/r/*.png","training/s/*.png","training/t/*.png","training/u/*.png","training/v/*.png",
               "training/w/*.png","training/x/*.png","training/y/*.png","training/z/*.png"]
    for item in array_folder:
        files = glob.glob(item)
        for file in files:
            gen_data.gen_data(file, ord(item.split("/")[1]))
    print "training complete"
    