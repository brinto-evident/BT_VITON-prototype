from PIL import Image
import os
from os import path

Source_Path = "E:\\dataset\\New folder\\cloth-mask"
Destination = "E:\\dataset\\New folder\\cloth-mask"
#dst_folder = os.mkdir(Destination)


def main():
    for filename in os.listdir(Source_Path):
        im1 = Image.open(os.path.join(Source_Path, filename)).convert('L')
        print(filename)
        conv_filename, _ = os.path.splitext(filename)
        conv_filename = conv_filename+'.jpg'
        dst = os.path.join(Source_Path, conv_filename)
        print(dst)
        # im1 = Image.open(os.path.join(Source_Path, filename)).convert('L')
        im1.save(dst)
        os.remove(os.path.join(Source_Path, filename))


# Driver Code
if __name__ == '__main__':
    main()
