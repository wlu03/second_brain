## WESLEY LU, 903777980, WLU314

from grid import *
from particle import Particle
from utils import *
import setting
import numpy as np
np.random.seed(setting.RANDOM_SEED)
from itertools import product
from typing import List, Tuple

from setting import ODOM_TRANS_SIGMA, ODOM_HEAD_SIGMA


def create_random(count: int, grid: CozGrid) -> List[Particle]:
    """
    Returns a list of <count> random Particles in free space.

    Parameters:
        count: int, the number of random particles to create
        grid: a Grid, passed in to motion_update/measurement_update
            see grid.py for definition

    Returns:
        List of Particles with random coordinates in the grid's free space.
    """
    # TODO: implement here
    # -------------------
    particle_list = []

    for i in range(count):
        x_rand, y_rand = grid.random_place()
        curr_particle = Particle(x_rand, y_rand)
        particle_list.append(curr_particle)
    
    return particle_list
    # -------------------
    

# ------------------------------------------------------------------------
def motion_update(old_particles:  List[Particle], odometry_measurement: Tuple, grid: CozGrid) -> List[Particle]:
    """
    Implements the motion update step in a particle filter. 
    Refer to setting.py and utils.py for required functions and noise parameters
    For more details, please read "Motion update details" section and Figure 3 in "CS3630_Project2_Spring_2025.pdf"


    NOTE: the GUI will crash if you have not implemented this method yet. To get around this, try setting new_particles = old_particles.

    Arguments:
        old_particles: List 
            list of Particles representing the belief before motion update p(x_{t-1} | u_{t-1}) in *global coordinate frame*
        odometry_measurement: Tuple
            noisy estimate of how the robot has moved since last step, (dx, dy, dh) in *local robot coordinate frame*

    Returns: 
        a list of NEW particles representing belief after motion update \tilde{p}(x_{t} | u_{t})
    """
    new_particles = []

    for particle in old_particles:
        # extract the x/y/heading from the particle
        x_g, y_g, h_g = particle.xyh
        # and the change in x/y/heading from the odometry measurement
        dx_r, dy_r, dh_r = odometry_measurement
        
        dx_w =  dx_r * math.cos(h_g) - dy_r * math.sin(h_g)
        dy_w =  dx_r * math.sin(h_g) + dy_r * math.cos(h_g)


        x_new = x_g + dx_w + random.gauss(0, ODOM_TRANS_SIGMA)
        y_new = y_g + dy_w + random.gauss(0, ODOM_TRANS_SIGMA)

        h_new = h_g + dh_r + random.gauss(0, ODOM_HEAD_SIGMA)

        
        new_particle = Particle(x_new, y_new, h_new)
        new_particles.append(new_particle)

        
        # TODO: implement here
        # ----------------------------------
        # align odometry_measurement's robot frame coords with particle's global frame coords (heading already aligned)

        # compute estimated new coordinate, using current pose and odometry measurements. Make sure to add noise to simulate the uncertainty in the robot's movement.

        # create a new particle with this noisy coordinate


        # ----------------------------------

    return new_particles

# ------------------------------------------------------------------------
def generate_marker_pairs(robot_marker_list: List[Tuple], particle_marker_list: List[Tuple]) -> List[Tuple]:
    """ Pair markers in order of closest distance

        Arguments:
        robot_marker_list -- List of markers observed by the robot: [(x1, y1, h1), (x2, y2, h2), ...]
        particle_marker_list -- List of markers observed by the particle: [(x1, y1, h1), (x2, y2, h2), ...]

        Returns: List[Tuple] of paired robot and particle markers: [((xp1, yp1, hp1), (xr1, yr1, hr1)), ((xp2, yp2, hp2), (xr2, yr2, hr2),), ...]
    """
    marker_pairs = []
    while len(robot_marker_list) > 0 and len(particle_marker_list) > 0:
        # TODO: implement here
        # ----------------------------------
        # find the (particle marker,robot marker) pair with shortest grid distance
        
        # add this pair to marker_pairs and remove markers from corresponding lists
        
        smallest_distance = float('inf')
        robot_idx = -1
        particle_idx = -1
        
        for i, robot in enumerate(robot_marker_list): 
            (rx, ry, rh) = robot
            
            for j, particle in enumerate(particle_marker_list):
                (px, py, ph) = particle
                
                dist = grid_distance(px, py, rx, ry)
                if smallest_distance > dist:
                    robot_idx = i
                    particle_idx = j
                    smallest_distance = dist
                
        pair = (particle_marker_list[particle_idx],
                robot_marker_list[robot_idx])
        marker_pairs.append(pair)

        robot_marker_list.pop(robot_idx)
        particle_marker_list.pop(particle_idx)
        
    return marker_pairs

# ------------------------------------------------------------------------
def marker_likelihood(robot_marker: Tuple, particle_marker: Tuple) -> float:
    """ Calculate likelihood of reading this marker using Gaussian PDF. 
        The standard deviation of the marker translation and heading distributions 
        can be found in setting.py
        
        Some functions in utils.py might be useful in this section

        Arguments:
        robot_marker -- Tuple (x,y,theta) of robot marker pose
        particle_marker -- Tuple (x,y,theta) of particle marker pose

        Returns: float probability
    """
    l = 0.0
    # TODO: implement here
    # ----------------------------------
    # find the distance between the particle marker and robot marker

    # find the difference in heading between the particle marker and robot marker

    # calculate the likelihood of this marker using the gaussian pdf. You can use the formula on Page 5 of "CS3630_Project2_Spring_2025.pdf"
    (rx,ry,rtheta) = robot_marker
    (px,py,ptheta) = particle_marker
    distBetweenMarkers = grid_distance(rx, ry, px, py)
    distBetweenMarkers = distBetweenMarkers ** 2
    distBetweenMarkers = distBetweenMarkers / (2 * (setting.MARKER_TRANS_SIGMA**2))
    
    
    angleBetweenMarkers = diff_heading_deg(rtheta, ptheta)
    angleBetweenMarkers = angleBetweenMarkers**2
    angleBetweenMarkers = angleBetweenMarkers / (2 * (setting.MARKER_HEAD_SIGMA**2))
    
    l = math.exp(-(distBetweenMarkers + angleBetweenMarkers))
    
    # ----------------------------------
    return l

# ------------------------------------------------------------------------
def particle_likelihood(robot_marker_list: List[Tuple], particle_marker_list: List[Tuple]) -> float:
    """ Calculate likelihood of the particle pose being the robot's pose

        Arguments:
        robot_marker_list -- List of markers (x,y,theta) observed by the robot
        particle_marker_list -- List of markers (x,y,theta) observed by the particle

        Returns: float probability
    """
    l = 1.0
    marker_pairs = generate_marker_pairs(robot_marker_list, particle_marker_list)
    # TODO: implement here
    # ----------------------------------
    # update the particle likelihood using the likelihood of each marker pair
    # HINT: consider what the likelihood should be if there are no pairs generated

    if len(marker_pairs) == 0:
        return 0.0

    total_likelihood = 1.0
    for (particle_m, robot_m) in marker_pairs:
        total_likelihood *= marker_likelihood(robot_m, particle_m)

    l = total_likelihood
    
    # ----------------------------------
    return l

# ------------------------------------------------------------------------
def measurement_update(particles: List[Particle], measured_marker_list: List[Tuple], grid: CozGrid) -> List[Particle]:
    """ Particle filter measurement update
       
        NOTE: the GUI will crash if you have not implemented this method yet. To get around this, try setting measured_particles = particles.
        
        Arguments:
        particles -- input list of particle represents belief \tilde{p}(x_{t} | u_{t})
                before measurement update (but after motion update)

        measured_marker_list -- robot detected marker list, each marker has format:
                measured_marker_list[i] = (rx, ry, rh)
                rx -- marker's relative X coordinate in robot's frame
                ry -- marker's relative Y coordinate in robot's frame
                rh -- marker's relative heading in robot's frame, in degree

                * Note that the robot can only see markers which is in its camera field of view,
                which is defined by ROBOT_CAMERA_FOV_DEG in setting.py
				* Note that the robot can see mutliple markers at once, and may not see any one

        grid -- grid world map, which contains the marker information,
                see grid.py and CozGrid for definition
                Can be used to evaluate particles

        Returns: the list of particles represents belief p(x_{t} | u_{t})
                after measurement update
    """
    measured_particles = []
    particle_weights = []
    num_rand_particles = 25
    
    if len(measured_marker_list) > 0:
        for p in particles:
            x, y = p.xy
            if grid.is_in(x, y) and grid.is_free(x, y):
                robot_marker_list = measured_marker_list.copy()
                particle_marker_list =  p.read_markers(grid)
                l = particle_likelihood(robot_marker_list, particle_marker_list)
                

                # TODO: implement here
                # ----------------------------------
                # compute the likelihood of the particle pose being the robot's
                # pose when the particle is in a free space

                # ----------------------------------
            else:
                l = 0.0
                # TODO: implement here
                # ----------------------------------
                # compute the likelihood of the particle pose being the robot's pose
                # when the particle is NOT in a free space

                # ----------------------------------

            particle_weights.append(l)
    else:
        particle_weights = [1.]*len(particles)
    
    # TODO: Importance Resampling
    # ----------------------------------
    # if the particle weights are all 0, generate a new list of random particles
    total_weights = sum(particle_weights)
    if total_weights == 0.0:
        return create_random(setting.PARTICLE_COUNT, grid)
    
    # normalize the particle weights
    particle_weights = [weight / total_weights for weight in particle_weights]
            
    # create a fixed number (num_rand_particles) of random particles and add to measured particles
    N = setting.PARTICLE_COUNT
    number_sample = N - num_rand_particles
    
    chosen_indices = random.choices(population=range(len(particles)),weights=particle_weights,k=number_sample)

    measured_particles = []
    for i in chosen_indices:
        old_particle = particles[i]
        measured_particles.append(Particle(old_particle.x, old_particle.y, old_particle.h))

    # add reandom particles
    random_particle_list = create_random(num_rand_particles, grid)
    measured_particles.extend(random_particle_list)

    # ----------------------------------

    return measured_particles


