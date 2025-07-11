import numpy as np
import math

# 2D point
class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Function for printing a point
    def __str__(self):
        return f"[{self.x}, {self.y}]"

    # Function for printing a list of points
    def __repr__(self):
        return f"[{self.x}, {self.y}]"

"""
SE(2) object that represents 2D pose/transformation containing position and orientation.
It can be used to
    * represent the pose of a coordinate frame, e.g., T^a_b represents the pose of coordinate frame b expressed
        in the coordinate frame a.
    * represent a transformation operation that roates and translates a coordinate frame or a point.
You can implement the class in any way that works best for you. You can add additional attributes to the class,
e.g, a transformation matrix, to suit your needs.
"""
class SE2:
    # Constructor.
    def __init__(self, x, y, h):
        """
        Args:
            * When the SE2 is used to represent a pose:
                * x(float): x coordinate of the pose position.
                * y(float): y coordinate of the pose position.
                * h(float): pose orientation (in radians).
            * When the SE2 is used to represent a transform:
                * x(float): x-component of the translation.
                * y(float): y-component of the translation.
                * h(float): rotation component of the transformation (in radians).
        """
        self.x = x
        self.y = y
        self.h = h
        self.c = math.cos(self.h)
        self.s = math.sin(self.h)
        ######### START STUDENT CODE #########
        # Compute the homogeneous transformation matrix in self.T if you choose to use the it.
        # You won't lose points for not computing or not using the transformation matrix self.T.
    
        ########## END STUDENT CODE ##########

    # Returns the translation component as a point.
    def position(self) -> Point:
        """
        When the SE2 is used to represent a pose, the return value represents the position of the pose.
        When the SE2 is used to represent a transformation, the return value represents the translation.
        """
        return Point(self.x, self.y)

    # Apply transformation to a 2D point.
    def transform_point(self, point: Point) -> Point:
        """
        Apply the transformation (self) to the point.
        Hint:
            * If you use T to represent the transformation matrix, P to represent the point in homogeneous
              coordinate as (x, y, 1), the transformed point expressed in  homogeneous coordinate is T*P.
        Args:
            * point(Point): the point before the transform.
        Return:
            *(Point): the point after the transformation.
        """
        new_x = None
        new_y = None
        ######### START STUDENT CODE #########
        
        ## note self.c = math.cos(self.h) and self.s = math.sin(self.s)
        
        ## x = cos(h) p_x  - sin(h)p_y + x
        ## y = sin(h) p_x + cos(h) p_y + y 
        
        new_x = (self.c*point.x) - (self.s*point.y) + self.x
        new_y = (self.s*point.x) + (self.c*point.y) + self.y

        ########## END STUDENT CODE ##########
        return Point(new_x, new_y)

    # Compose with another transformation.
    def compose(self, other: 'SE2') -> 'SE2':
        """
        Compose the transformation (self) with another transform (other).
        Hint:
            * If you use T_self to represent the transformation matrix of the SE2 (self), T_other to represent
              the transformation matrix of the other SE2 (other), the returning SE2 has the transformation
              matrix T_self * T_other.
        Args:
            * other(SE2): The other SE2 to compose (on the right).
        Return:
            * (SE2): The resulting SE2 after composition.
        """
        new_pose = None
        ######### START STUDENT CODE #########
        
        ## compose the self with other by adding
        
        
        h = self.h + other.h
        x = self.x+self.c * other.x - self.s *other.y
        y = self.y +self.s * other.x +self.c * other.y
        new_pose = SE2(x,y,h)

        ########## END STUDENT CODE ##########
        return new_pose

    # Inverse of the transformation.
    def inverse(self) -> 'SE2':
        """
        Returns the inverse of the transformation.
        Hint:
            * If you use T to represent the transformation matrix of the SE2 (self), the returning SE2
              has the transformation matrix T^{-1}.
        Return:
            * (SE2): the inverse transformation.
        """
        new_x = None
        new_y = None
        new_h = None
        ######### START STUDENT CODE #########
        ## matrix R = [cos -sin][sin cos]
        ## take the rotation matrix R^T = [cos sin][-sin cos]
        ## the inverse of (x,y) is -R^T (x,y)^T
            ## x = - (cos * x + sin * y)
            ## y = - (-sin * x + cos * y)
        
        inverse_h = -self.h
        
        inverse_x = -(self.c * self.x +self.s * self.y)
        inverse_y = -(-self.s * self.x + self.c * self.y)

        return SE2(inverse_x, inverse_y, inverse_h)
        ########## END STUDENT CODE ##########
        #return SE2(new_x, new_y, new_h)

    # Add Gaussian noise to the transformation.
    def add_noise(self, x_sigma: float, y_sigma: float, h_sigma:float) -> 'SE2':
        new_x = self.x + np.random.normal(0, x_sigma)
        new_y = self.y + np.random.normal(0, y_sigma)
        new_h = self.h + np.random.normal(0, h_sigma)
        return SE2(new_x, new_y, new_h)

    # Compute the mean of a list of poses.
    @staticmethod
    def mean(pose_list: list['SE2']) -> 'SE2':
        """
        Computes the mean of multiple poses.
        The average orientation is computed using circular mean.
        """
        x_list = [pose.x for pose in pose_list]
        y_list = [pose.y for pose in pose_list]
        cos_list = [math.cos(pose.h) for pose in pose_list]
        sin_list = [math.sin(pose.h) for pose in pose_list]
        x_mean = np.mean(x_list)
        y_mean = np.mean(y_list)
        cos_mean = np.mean(cos_list)
        sin_mean = np.mean(sin_list)
        h_mean = math.atan2(sin_mean, cos_mean)
        return SE2(x_mean, y_mean, h_mean)

    # Function for printing a transformation. Angle is displayed in degrees.
    def __str__(self):
        deg = math.degrees(self.h)
        return f"[{self.x}, {self.y}, {deg}]"

    # Function for printing a list of transformations. Angle is displayed in degrees.
    def __repr__(self):
        deg = math.degrees(self.h)
        return f"[{self.x}, {self.y}, {deg}]"
