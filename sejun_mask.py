import numpy as np
import cv2

import os
import shutil

cap = cv2.VideoCapture(0)

real_ir_data_dir = '/Users/sejunsong/PycharmProjects/SaltusDeephand/Real/ir'
real_mask_data_dir = '/Users/sejunsong/PycharmProjects/SaltusDeephand/Real/mask'

index = 0

final_file_number = 1000

isStartCapture = False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    width = cap.get(3)  # float
    height = cap.get(4)  # float

    x = int(width/2)
    y = int(height/2)
    h1 = 195
    h2 = 60
    w1 = 127
    w2 = 128
    crop_img = frame[y-h1:y+h2, x - w1: x + w2]
    cv2.imshow('original', crop_img)
    bk = np.full(crop_img.shape, 255, dtype=np.uint8)  # white bk, same size and type of image

    ret, crop_img_thresh = cv2.threshold(crop_img, 130, 255, cv2.THRESH_BINARY)
    # kernel = np.ones((3,3),np.uint8)
    # crop_img_thresh = cv2.erode(crop_img_thresh,kernel,iterations=1)
    # crop_img_thresh = cv2.dilate(crop_img_thresh, kernel, iterations=1)

    mask = crop_img_thresh

    # get masked foreground
    fg_masked = cv2.bitwise_and(crop_img, crop_img, mask=mask)

    # get masked background, mask must be inverted
    mask = cv2.bitwise_not(mask)
    bk_masked = cv2.bitwise_and(bk, bk, mask=mask)

    ir_image = cv2.bitwise_or(fg_masked, bk_masked)

    crop_img2 = crop_img * crop_img_thresh.astype(crop_img.dtype)

    #flip vertical

    ir_image = cv2.flip(ir_image, 0)
    mask = cv2.flip(mask, 0)
    cv2.imshow('ir_image',ir_image)
    cv2.imshow('mask', mask)

    if isStartCapture :
        index = index + 1

        print("Capture Index : "+str(index))

        cv2.imwrite(real_ir_data_dir + '/' + str(index) + '.png', ir_image)

        cv2.imwrite(real_mask_data_dir + '/' + str(index) + '.png', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        # make dir or remove dir when in directory exist..
        if os.path.exists(real_ir_data_dir):
            shutil.rmtree(real_ir_data_dir)
            os.makedirs(real_ir_data_dir)
        else:
            os.makedirs(real_ir_data_dir)

        if os.path.exists(real_mask_data_dir):
            shutil.rmtree(real_mask_data_dir)
            os.makedirs(real_mask_data_dir)
        else:
            os.makedirs(real_mask_data_dir)

        print("Start Real IR and Mask Capture")
        isStartCapture = True


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()