
# Object Detection and Surface Area Calculation

## Overview

This project demonstrates object detection and surface area calculation functionalities using OpenCV in Python. The script detects rectangular objects in an image and calculates their surface areas.

## Approach

1. Image Loading: The image is loaded using OpenCV.
2. Grayscale Conversion: The image is converted to grayscale to simplify processing.
3. Gaussian Blur: A Gaussian blur is applied to reduce noise and improve edge detection.
4. Edge Detection: Canny edge detection is used to find the edges in the image.
5. Contour Detection: Contours are detected from the edge-detected image.
6. Rectangle Detection: Contours are approximated to polygons, and only those with four vertices (rectangles) are processed.
7. Area Calculation: The area of each rectangular contour is calculated.
8. Result Display: Rectangles and their calculated areas are drawn on the image, and the final image is displayed using Matplotlib.

## Assumptions

- The objects in the image are assumed to be flat and lying on a flat surface.
- Only rectangular objects are detected and processed.
- The image provided is of sufficient resolution and clarity for edge detection and contour approximation.

## Output Format

- The output is an image with detected rectangular objects outlined and their areas displayed in cm^2.
- Areas are calculated using the contour area function in OpenCV and displayed near each detected rectangle.

## How to Run

1. Ensure you have OpenCV and Matplotlib installed:
2. I have used my own image for detecting the objects. You can also use the same image to see the output. The sample image is included in the project.
3. Run the detect_rectangles.py file in terminal to see the output 
