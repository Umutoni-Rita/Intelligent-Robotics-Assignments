import cv2  # Import OpenCV library

image = cv2.imread('assignment-001-given.jpg')

# Add text to the image (example: License plate 'RAH972U')
# Text: 'RAH972U', Location (830,180): Above the plate
# Font: FONT_HERSHEY_SIMPLEX, Scale: 3, Color: Green (BGR: (0, 255, 0)), Thickness: 5
cv2.putText(image,  
                'RAH972U',  
                (830, 180),  
                cv2.FONT_HERSHEY_SIMPLEX, 3,  
                (0, 255, 0),  
                5,  
                cv2.LINE_4) 

# Draw a green rectangle around the plate
cv2.rectangle(image, (250, 200), (980, 920), (0, 255, 0), 8)

# Display the image with text in a window
cv2.namedWindow('My Result', cv2.WINDOW_NORMAL)  # Allow window resizing
cv2.imshow('My Result', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the image with text to a new file
cv2.imwrite('my-result.jpg', image)

# Close all OpenCV windows
cv2.destroyAllWindows()
