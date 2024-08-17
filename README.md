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

### Method 2: Using the Executable
1. Place the executable (images_metadata_cleaner.exe) in the folder containing your images.
2. Double-click the executable to run it.
3. The tool will automatically clean the metadata from all .jpg, .jpeg, and .png files in the folder.
4. A command prompt window will display messages indicating the progress. Press Enter to close the window when the process is complete.

## Requirements
- **Python 3.6+ (if using the Python script)**:
- **Pillow and piexif Python libraries**:

Installation
To install the required Python libraries, run:
   
    ```bash
     pip install pillow piexif





### Building the Standalone Executable

To create a standalone executable version of the tool, follow these steps:

1. **Open Command Prompt (CMD):**
   - Press `Win + R`, type `cmd`, and hit `Enter`.

2. **Navigate to the Folder Containing the Code:**
   - Use the `cd` command to change to the directory where your code is located:
     ```bash
     cd %Full_Path%\Image-Metadata-Eraser
     ```
     Replace `%Full_Path%` with the actual path to the `Image-Metadata-Eraser` folder.

3. **Install PyInstaller:**
   - If you haven't installed `PyInstaller` yet, run the following command:
     ```bash
     pip install pyinstaller
     ```

4. **Build the Executable:**
   - To create the standalone executable, run the following command:
     ```bash
     pyinstaller --onefile Metadata-Eraser.py
     ```
   - This process takes about a minute. Once completed, you'll find the executable in the `dist` folder.

5. **Locate the Executable:**
   - Navigate to the `dist` folder, where you'll see the `Metadata-Eraser.exe` file.

6. **Use the Executable:**
   - Copy the `Metadata-Eraser.exe` file into the folder containing the images you want to clean.
   - Double-click the `.exe` file to run it. The tool will automatically remove the metadata from all the images in that folder.

7. **Verify Metadata Removal:**
   - After the process completes, check the images to confirm that their metadata has been successfully removed.





