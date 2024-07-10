import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "yo.jpg"  # Update the path to your uploaded image
image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print("Error: Unable to load image. Please check the file path.")
else:
    # Convert the image to grayscale
    # This helps in simplifying the image data for further processing
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve edge detection
    # Gaussian blur smoothens the image, which helps in reducing false edges
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection
    # Canny edge detection is used to find edges in the image
    edges = cv2.Canny(blurred_image, 50, 150)

    # Find contours
    # Contours are curves joining all the continuous points along a boundary with the same color or intensity
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Copy the original image to draw contours and display areas
    area_image = image.copy()

    # Define a function to put text on the image with a specified font and color
    def put_text(image, text, position, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        thickness = 1
        cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

    # Calculate and display areas of rectangular contours
    for contour in contours:
        # Approximate the contour to a polygon
        # Approximation helps in reducing the number of points in a contour
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the approximated contour has 4 vertices (indicating a rectangle)
        if len(approx) == 4:
            # Calculate the area of the contour
            area = cv2.contourArea(contour)
            area_text = f"A: {area:.2f}cm^2"
            print(f"Contour area: {area_text}")

            # Get the bounding box of the contour to place the text
            x, y, w, h = cv2.boundingRect(contour)

            # Draw the contour on the image
            # The contour is drawn in green color
            cv2.drawContours(area_image, [contour], -1, (0, 255, 0), 2)

            # Place the text near the contour
            # The area text is placed slightly above the contour
            put_text(area_image, area_text, (x, y - 10), (255, 0, 255))

    # Convert the image from BGR to RGB format for displaying using matplotlib
    # OpenCV uses BGR by default while matplotlib uses RGB, so conversion is needed
    area_image_rgb = cv2.cvtColor(area_image, cv2.COLOR_BGR2RGB)

    # Display the image with contours and area text
    plt.imshow(area_image_rgb)
    plt.axis('off')
    plt.show()
