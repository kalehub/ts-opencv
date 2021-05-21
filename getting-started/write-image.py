'''
saving (writing) image in OpenCV

'''
import cv2
import os

def main():
    img_dir = 'imgs/dies57.png'
    save_dir = 'saved-imgs/'

    # read the image first but grayscale
    img = cv2.imread(img_dir, 0)
    os.chdir(save_dir)

    cv2.imwrite('savedBG.png', img)

    
    






if __name__ == '__main__':
    main()







