# Raspberry Pi AI Camera Object Tracking

AIcam is a Raspberry Pi-based application that captures video using the IMX500 camera module, performs real-time object detection to identify people, and tracks them by adjusting a servo-controlled camera mount. The project integrates computer vision and hardware control to create an autonomous tracking camera system.

## Features
- **Camera Capture**: Uses the IMX500 camera module to capture video streams.
- **Object Detection**: Detects people in the video feed using pre-trained AI models stored in the `imx500-models/` folder.
- **Camera Mount Control**: Adjusts the camera's pan and tilt using servo motors to track detected objects.
- **Visualization**: Draws bounding boxes and labels around detected objects on the video feed.

## Prerequisites
- Raspberry Pi (e.g., Raspberry Pi 4) with Raspbian OS.
- IMX500 camera module connected to the Raspberry Pi.
- Two servo motors connected to GPIO pins (default: GPIO18 for pan, GPIO19 for tilt).
- Model files in the `imx500-models/` folder (e.g., `imx500_network_ssd_mobilenetv2_fpnlite_320x320_pp.rpk`).
- Label file in the `assets/` folder (e.g., `coco_labels.txt`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mmandernach13/AIcam.git
   cd AIcam
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the `imx500-models/` and `assets/` folders are in the repository root with the required model and label files.

## Usage
1. Connect the IMX500 camera module and servo motors to your Raspberry Pi.
2. Run the main script:
   ```bash
   python object_tracking.py
   ```
3. The camera will capture video, detect people, and adjust the mount to track them. Bounding boxes and labels will be displayed on the video feed. The object tracked can be changed in the object_tracking.parse_detections method by changing the label(s) that get added to the detection list.
4. Press `Ctrl+C` to stop the program and safely detach the servos.

### Optional Arguments
You can customize the script with command-line arguments:
- `--model`: Path to the model file (default: `/usr/share/imx500-models/imx500_network_ssd_mobilenetv2_fpnlite_320x320_pp.rpk`).
- `--threshold`: Detection confidence threshold (default: 0.5).
- `--iou`: Intersection over union threshold for non-max suppression (default: 0.65).
- `--max-detections`: Maximum number of detections per frame (default: 10).
- `--fps`: Set frames per second for capture.
- `--labels`: Path to a custom labels file.

Example:
```bash
python object_tracking.py --threshold 0.6 --max-detections 5
```

## Dependencies
See `requirements.txt` for a complete list of dependencies, including:
- `opencv-python`: For image processing and visualization.
- `numpy`: For numerical operations.
- `picamera2`: For Raspberry Pi camera control with IMX500 support.
- `gpiozero`: For servo motor control.

## Folder Structure
- `imx500-models/`: Contains pre-trained model files for object detection.
- `assets/`: Contains label files (e.g., `coco_labels.txt`) for detected object categories.

## License
This project is licensed under the MIT License.
