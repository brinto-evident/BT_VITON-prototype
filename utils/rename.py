import os
from os import path

Source_Path = "E:\\dataset\\panjabi\\clothes"
Destination = "E:\\dataset\\New folder\\cloth"
#dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  f"{count+1010:04d}" + ".jpg"
        print(dst)

        # rename all the files
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))


# Driver Code
if __name__ == '__main__':
    main()