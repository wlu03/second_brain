
import math
import numpy as np
from utils import *
from wall import Wall
from environment import Environment

class LidarSim:
    # Constructor
    def __init__(self, walls:list[Wall], max_range:float, n_rays:float):
         self.walls = walls
         self.max_range = max_range
         self.n_rays = n_rays
         self.resolution = int(360/n_rays)
         self.measurements = math.inf*np.ones(self.resolution)

    # Simulate the lidar sensor reading
    def read(self, pose:SE2) -> np.ndarray:
         '''
         Simulate the lidar sensor readings given the current pose of the robot.

         Parameters:
         pose (SE2): The current pose of the robot, represented as an SE2 object, 
         which includes the x and y coordinates and the heading (orientation) of 
         the robot.

         Returns:
         np.ndarray: An array of simulated lidar measurements, where each element 
         represents the distance to the nearest wall for a specific lidar ray.

         Steps:
         1. Iterate through each lidar ray:
            - For each ray, calculate the angle based on the robot's heading and 
            the resolution of the lidar.
            - Determine the endpoint of the lidar ray based on the maximum range 
            and the calculated angle.

         2. Check for intersections with walls:
            - For each wall, check if the lidar ray intersects with the wall 
            using the line_rectangle_intersect function.
            - If an intersection is detected, calculate the intersection points 
            between the lidar ray and the edges of the wall.
            - Calculate the distances from the robot to these intersection points.

         4. Find the minimum distance:
            - Among all intersection points, find the minimum distance and update 
            the measurements array for the corresponding ray.

         5. Return the measurements:
            - Return the array of simulated lidar measurements.
         '''

         # Reset the measurements
         self.measurements = math.inf*np.ones(self.n_rays) # Webots lidar sensor returns inf for no detection
         
         ######### START STUDENT CODE #########
         # Hint - You may find the following functions in utils.py useful: 
         # line_rectangle_intersect, line_segment_intersect, line_intersection, distance_between_points
         
         ## increment equallygiven 360 degrees by n rays
         angle_increment = 2.0 * math.pi / self.n_rays
         
         robot_position = pose.position()
         robot_h = pose.h
         N = int(self.n_rays)
         
         ## loop overeach lidar ray
         for i in range(N):
            angle = robot_h + (i+0.5) * angle_increment
            x = robot_position.x + self.max_range * math.cos(angle)
            y = robot_position.y + self.max_range * math.sin(angle)
            endpoint = Point(x,y)
            
            min_distance = math.inf ## step 4 find the minimum distance 
            
            # 5 check every wall against the ray
            for wall in self.walls:
               corners = [Point(*wall.top_left),Point(*wall.top_right), Point(*wall.bottom_right),Point(*wall.bottom_left)]
               edges = [(corners[0], corners[1]),(corners[1], corners[2]),(corners[2], corners[3]),(corners[3], corners[0])]
               
               ## for each corner see if ray intersetcts
               for corner1, corner2 in edges:
                  p_int = line_intersection(robot_position, endpoint, corner1, corner2)
                  
                  if p_int is not None:
                     distance = distance_between_points(robot_position, p_int)
                     if distance < min_distance: 
                        min_distance = distance
                        
            self.measurements[i] = min_distance
                  
         ########## END STUDENT CODE ##########

         return self.measurements