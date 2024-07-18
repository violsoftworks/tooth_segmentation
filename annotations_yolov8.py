import os
import json

def convert_to_yolo(json_file, output_directory):
    with open(json_file, 'r') as f:
        data = json.load(f)

    yolo_annotations = []
    for annotation in data['annotations']:
        x_center = annotation['bounding_box']['x']
        y_center = annotation['bounding_box']['y']
        width = annotation['bounding_box']['w']
        height = annotation['bounding_box']['h']
        class_value = annotation['class']
        yolo_annotations.append(f"{class_value} {x_center} {y_center} {width} {height}\n")  # Assuming class label is 0

    yolo_file = os.path.splitext(os.path.basename(json_file))[0] + '.txt'
    output_path = os.path.join(output_directory, yolo_file)
    with open(output_path, 'w') as f:
        f.writelines(yolo_annotations)

    print(f"Converted annotations written to {output_path}")

json_directory = r'C:\\Users\\AMET\\DocGaid\\yolov8\\data\\annotations_classes'
output_directory = r'C:\\Users\\AMET\\DocGaid\\yolov8\\data\\labels'

os.makedirs(output_directory, exist_ok=True)

# Iterate through JSON files in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        json_file = os.path.join(json_directory, filename)
        convert_to_yolo(json_file, output_directory)
