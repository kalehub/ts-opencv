'''
RGB color spaces in OpenCV
'''

import cv2

def main():
    img_dir = 'imgs/dies57.png'

    # read the image first
    img = cv2.imread(img_dir)

    B,G,R = cv2.split(img)

    cv2.imshow('Original', img)
    cv2.waitKey(0)
    cv2.imshow('Red', R)
    cv2.waitKey(0)
    cv2.imshow('Green', G)
    cv2.waitKey(0)
    cv2.imshow('Blue', B)
    cv2.waitKey(0)


    cv2.destroyAllWindows()






if __name__ == '__main__':
    main()




