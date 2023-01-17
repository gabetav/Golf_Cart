import ktb
import os
import cv2
import time
import datetime
from PIL import Image
import gluoncv as gcv


#folder_path = "cart_images"
#img_test = cv2.imread("cart_images/road_test.jpg")
    
    # Check if the "cart_images" folder exists, and create it if it doesn't
#if not os.path.exists(folder_path):
 #       os.makedirs(folder_path)
    
    # Create a Kinect object
kinect = ktb.Kinect()
    
    
    # Capture images from the Kinect camera
while True:
    image = kinect.get_frame(ktb.RAW_COLOR)
    kinect.get_frame()
    #current_date = datetime.datetime.now()
    #ts = current_date.timestamp()
        
    if image is not None:
        

        frame = cv2.flip(image, 1)
        #cv2.imshow('cart_image_', frame)
        
        #gray = cv2.cvtColor()

# Use GluonCV's semantic segmentation model to segment the road
        pre_trained_model = gcv.model_zoo.get_model('psp_resnet101_citys', pretrained=True)
        pred = pre_trained_model.predict(frame)

# Get the segmented road mask and use it to find the center of the road
        road_mask = gcv.utils.viz.image.get_colormap_mask(pred, colormap='road_colors')
#road_center = gcv.utils.viz.image.center_of_mass(road_mask)
        cv2.imshow(road_mask)
        too_left = 1
        too_right = 1
        
# Move the golf cart to the center of the road
#golf_cart.move(road_center)
        if too_left == 0:
            print("send signal")
        elif too_right == 1:
            print("send signal")
        else:
            print("send signal")
            
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        #elif key == ord('s'):
         #   print('ss')
cv2.destroyAllWindows()
