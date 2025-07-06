import numpy as np
import math
from detect_circle import detect_circle

# Instructions:
# Review the `detect_circle` function to infer and detect a circle in the image and compute its angle.

def vision_only_distance_calculation(image, camera_fov, object_diameter):
    """
    This function performs object detection and calculates the depth and angle of the detected circle from a camera sensor.

    Args:
        image: The input image from the camera
        camera_fov: The field of view of the camera in radians.
        object_diameter: The expected diameter of the object in meters.

    Returns:
        depth: The depth to the detected object from camera depth estimation in meters.
        angle: the angle of the detected circle in radians.
    """

    ###########################################################################
    # TODO: Student code begins
    ###########################################################################
    
    # locate the object
        # detect_circle gets the
            # x,y and radius of each circle
            # returns none if not found
    if detect_circle(image) is None:
        raise InterruptedError("Detect circle didnt detect an image.")
    list_of_circles = detect_circle(image)
    x, y, radius = list_of_circles[0]
    # pinhole camera model equation to get the depth (focal_length (pixels)) / (depth of image) = (object diameter in image) / (object diameter)
    # depth of image = (object diameter * focal_length) / (object diameter in image)
    image_width = image.shape[1]
    focal_length = (image_width) / (2 * math.tan(camera_fov / 2))
    object_diameter_in_image = radius * 2
    depth = (object_diameter * focal_length) / object_diameter_in_image
        
    ## Get the angle
    angle = camera_fov / 2
    ## to get either it's negative by seeing if its to the left or right
    ## divide the width to get the center. subtract the image center
    
    sign_of_angle = (x- (image_width /2)) / (image_width /2)
    angle = angle * sign_of_angle
    
    ###########################################################################
    # Student code ends
    ###########################################################################
    
    
    return depth, angle



