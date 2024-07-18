import os
import shutil
from sklearn.model_selection import train_test_split

# Set the directory containing your images
images_dir = "data/images"

# Get the list of image filenames
image_filenames = os.listdir(images_dir)

# Split the data into train and temp (test + validation)
train_files, temp_files = train_test_split(image_filenames, test_size=0.2, random_state=42)

# Split the temp data into test and validation
test_files, val_files = train_test_split(temp_files, test_size=0.5, random_state=42)

# Define directories for train, test, and validation
train_dir = "data/train"
test_dir = "data/test"
val_dir = "data/validation"

# Create directories if they don't exist
for directory in [train_dir, test_dir, val_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Move images to appropriate directories
for filename in train_files:
    shutil.move(os.path.join(images_dir, filename), os.path.join(train_dir, filename))

for filename in test_files:
    shutil.move(os.path.join(images_dir, filename), os.path.join(test_dir, filename))

for filename in val_files:
    shutil.move(os.path.join(images_dir, filename), os.path.join(val_dir, filename))
