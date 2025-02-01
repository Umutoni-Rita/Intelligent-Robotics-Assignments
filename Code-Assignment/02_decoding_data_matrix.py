import numpy as np
import cv2
from pylibdmtx import pylibdmtx

if __name__ == '__main__':

    image = cv2.imread('data_matrix.png', cv2.IMREAD_UNCHANGED);

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    msg = pylibdmtx.decode(thresh)
    print(msg)

# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np

# # Load the image containing the Data Matrix or QR code
# image = cv2.imread('data_matrix.png')

# # Check if the image is loaded properly
# if image is None:
#     print("Error: Unable to read the image!")
#     exit(1)

# # Decode the Data Matrix or QR code(s) in the image
# decoded_objects = decode(image)

# # Loop through the decoded objects
# for obj in decoded_objects:
#     # Print the decoded data
#     print("Decoded Data:", obj.data.decode('utf-8'))

#     # Draw a rectangle around the detected QR code or Data Matrix
#     points = obj.polygon
#     if len(points) == 4:
#         # Create a bounding box around the QR code/Data Matrix
#         pts = [tuple(point) for point in points]
#         cv2.polylines(image, [np.array(pts, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)
    
#     # Display the decoded data on the image
#     cv2.putText(image, str(obj.data.decode('utf-8')), (points[0].x, points[0].y-10), 
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# # Save and display the result
# cv2.imwrite("decoded_output.png", image)

# # Show the image with the decoded QR/Data Matrix
# cv2.imshow("Decoded Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


