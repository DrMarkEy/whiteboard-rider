import cv2
import numpy as np

# Function to select 4 points
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point selected: {(x, y)}")
 #       if len(points) == 4:
#            cv2.destroyAllWindows()

# Perspective transformation function
def apply_perspective_transform(image, points):
    # Desired dimensions for the output (rectangular whiteboard)
    width, height = 800, 600  # Set to whatever size you want the final whiteboard to be

    # Points in the output image
    destination_points = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype="float32")

    # Compute the perspective transform matrix and apply it
    matrix = cv2.getPerspectiveTransform(np.array(points, dtype="float32"), destination_points)
    warped = cv2.warpPerspective(image, matrix, (width, height))

    return warped

# Load the image
image = cv2.imread('sample.jpg')

# Display the image and allow the user to select 4 points
points = []
cv2.imshow("Select 4 corners of the whiteboard", image)
cv2.setMouseCallback("Select 4 corners of the whiteboard", select_points)
cv2.waitKey(0)

# Ensure that 4 points were selected
if len(points) == 4:
    cv2.destroyAllWindows()

    # Apply perspective transformation
    warped_image = apply_perspective_transform(image, points)

    # Show the result
    cv2.imshow("Warped Whiteboard", warped_image)
    cv2.waitKey(0)

    # Optionally, save the output
    cv2.imwrite("/Users/marcmendler/workspace/whiteboard-rider/warped_whiteboard.jpg", warped_image)
else:
    print("You need to select exactly 4 points.")
