
import os
import json
import cv2
import traceback

from camera_and_lidar import camera_and_lidar_calculation

DATA_PATH = '../../data/'

def get_metadata() -> dict:
    with open(os.path.join(DATA_PATH, "metadata.json"), 'r') as f:
        metadata = json.load(f)
    return metadata

def check_distance_accuracy(student_distance: float , sol_distance: float, pct_tol: float = .05) -> bool:
    err = pct_tol * sol_distance
    if abs(sol_distance - student_distance) <= err:
        return True
    return False
        
def check_shape_accuracy(student_shape: str, sol_shape: str) -> bool:
    return student_shape == sol_shape


def test_vision_lidar() -> None:
    print("Running vision_lidar tests!")
    metadata = get_metadata()
    try:
        for image_name, values in metadata.items():
            image_data_path = os.path.join(DATA_PATH, image_name)
            fov = values['fov']
            lidar_data = values['lidar_array']
            student_distance, student_shape = camera_and_lidar_calculation(cv2.imread(image_data_path), fov, 0.058*2, lidar_data)

            
            is_distance_correct = check_distance_accuracy(student_distance, values['vision_lidar_distance'])
            is_shape_correct = check_shape_accuracy(student_shape, values['vision_lidar_shape'])

            print(f"For {image_name}, you calculated the {'correct' if is_distance_correct else 'INCORRRECT'} distance and the {'correct' if is_shape_correct else 'INCORRECT'} shape.")

    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)[-1]
        function_name = tb.name
        line_number = tb.lineno
        raise Exception(f"{function_name}:{line_number} - {e}")


if __name__ == "__main__":
    test_vision_lidar()