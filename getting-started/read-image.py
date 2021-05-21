'''
Reading an image using OpenCV
'''

import cv2


def main():
    # define the image location
    imgs_dir = 'imgs/dies57.png'

    # reading the image using im.read and it's flag
    read_img = cv2.imread(imgs_dir, cv2.IMREAD_COLOR)

    # showing image
    cv2.imshow('the image', read_img)

    # adding wait key while showing
    cv2.waitKey(0)

    
    # destroying all windows from memory
    cv2.destroyAllWindows()







if __name__ == '__main__':
    main()

