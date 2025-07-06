import math
import numpy as np
from detect_circle import detect_circle

# Instructions:
# Step 1: Review the `detect_circle` function to infer and detect a circle in the image 
#         and compute its angle.
# Step 2: Explore the LiDAR data corresponding to the detected object. Investigate 
#         how to classify the object as either a sphere or a disk. You may reuse 
#         your code from `camera_only.py`.

def camera_and_lidar_calculation(image, camera_fov, object_diameter, lidar_data):
    """
    Performs object detection and classification by combining data from a camera and a LiDAR sensor.

    Args:
        image: The input image captured by the camera.
        camera_fov: The field of view of the camera in radians.
        object_diameter: The expected diameter of the object in meters.
        lidar_data: An array representing LiDAR distance data indexed by angle 
                                  in degrees, where each element corresponds to the distance 
                                  at a specific angle.

    Returns:
        lidar_distance: The distance to the detected object from the LiDAR sensor in meters.
        object_shape: A string indicating the shape of the detected object ("sphere" or "disk").
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
    

    ## get dimension of circle using this height and width, i am able to get the center of the object
    height, width = image.shape[:2]
    center_x = width / 2.0
    center_y = height / 2.0
    pixel_offset_x = x - center_x

    ## turn the pixel offset to radians for example ([-width/2, width/2] -> [-camera_fov/2, camera_fov/2]).
    ## for the LIDAR Data array, i need the degree since it's 0 to 180 degrees (radians to degrees)
    # the lidar distnace is just the index using the angle
    angle_in_rads = (pixel_offset_x / (width / 2.0)) * (camera_fov / 2.0)
    angle_in_degrees = int(np.degrees(angle_in_rads))
    lidar_distance = lidar_data[angle_in_degrees]

    depth_difference_threshold = 0.1

    # get the  expected size in pixels for a sphere
    angular_size = object_diameter / lidar_distance
    pixel_size = (angular_size / camera_fov) * width
    circle_diameter_pixels = 2.0 * radius

    ## USIng the threshold. if there is a 50% difference then it will be a sphere
    size_diff = abs(circle_diameter_pixels - pixel_size)
    
    if size_diff <= depth_difference_threshold * pixel_size:
        object_shape = "disk"
    else:
        object_shape = "sphere"
    return lidar_distance, object_shape



    ###########################################################################
    # Student code ends
    ###########################################################################

