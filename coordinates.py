import cv2

# Initialize a list to store clicked points
coordinates = []

# Mouse callback function that records coordinates when the image is clicked
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        coordinates.append((x, y))
        print(f"Clicked at: {x}, {y}")

# Load the image
image = cv2.imread('assignment-001-given.jpg')

# Create a named window
# cv2.namedWindow('Image')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  # Allow window resizing
# Set the mouse callback to capture coordinates on click
cv2.setMouseCallback('Image', get_coordinates)

# Display the image in a window

cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()

# Print all the clicked coordinates
print("Coordinates clicked:", coordinates)
