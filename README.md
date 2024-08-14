# Image-Metadata-Eraser


**Image-Meta-Data-Eraser** is a tool designed to remove metadata from image files. The tool can be used in two different ways: as a Python script that can be executed in your IDE, or as a standalone executable (`.exe`) file that you can run directly in a folder containing your images.

## Features

- **Clean Metadata**: Removes all EXIF metadata from `.jpg`, `.jpeg`, and `.png` files.
- **Two Usage Methods**:
  1. **Python Script**: Run the code directly in your Python environment.
  2. **Executable**: Use the standalone `.exe` file to clean metadata from images in a specific folder.

## Usage

### Method 1: Running the Python Script

1. Clone the repository or download the script.
2. Install the required libraries:
   ```bash
   pip install pillow piexif



3. Place your images in the same directory as the script.
4. Run the script using your Python IDE or command line:
   ```bash
   python images_metadata_cleaner.py
5. The script will process all the images in the folder, removing any metadata.
