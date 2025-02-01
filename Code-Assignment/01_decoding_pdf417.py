
# import cv2
# import numpy as np
# import subprocess
# import os

# # Paths to required files
# javase_jar = "javase-3.5.0.jar"
# core_jar = "core-3.5.0.jar"
# jcommander_jar = "jcommander-1.82.jar"
# barcode_image = "pdf417.jpg"

# # Validate required files
# for file in [javase_jar, core_jar, jcommander_jar, barcode_image]:
#     if not os.path.exists(file):
#         print(f"Error: {file} not found!")
#         exit(1)

# # Docker command to detect the barcode and get its position
# docker_command = [
#     "docker", "run", "--rm",
#     "-v", f"{os.getcwd()}:/app",
#     "openjdk:17",
#     "java", "-cp",
#     f"/app/{javase_jar}:/app/{core_jar}:/app/{jcommander_jar}",
#     "com.google.zxing.client.j2se.CommandLineRunner",
#     f"/app/{barcode_image}"
# ]

# try:
#     # Run the Docker command to get the decoding and position
#     result = subprocess.run(docker_command, capture_output=True, text=True, check=True, encoding='utf-8')
#     output = result.stdout.strip() if result.stdout else ""
#     print("Decoded Output:")
#     print(output)
# except subprocess.CalledProcessError as e:
#     print("Error during decoding:")
#     print(e.stderr)
#     exit(1)

# # Parse the ZXing output for barcode position
# points = []
# if output:
#     for line in output.splitlines():
#         if line.startswith("  Point"):
#             parts = line.split(":")[1].strip().replace("(", "").replace(")", "").split(",")
#             points.append((int(float(parts[0])), int(float(parts[1]))))

#     # If points are found, draw a bounding polygon
#     if len(points) >= 4:
#         # Load the image with OpenCV
#         image = cv2.imread(barcode_image)
#         if image is None:
#             print("Error: Unable to read the image!")
#             exit(1)

#         # Draw a polygon connecting the points
#         points_array = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
#         print(f"Drawing polygon with points: {points}")

#         cv2.polylines(image, [points_array], isClosed=True, color=(0, 255, 0), thickness=2)

#         # Save and display the annotated image
#         annotated_image_path = "annotated_barcode.png"
#         cv2.imwrite(annotated_image_path, image)
#         print(f"Annotated image saved as {annotated_image_path}")

#         # Display the image
#         cv2.imshow("Detected Barcode", image)
#         print("Press any key to close the window.")
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         print("No bounding box points detected.")
# else:
#     print("No output from decoding.")
# from PIL import Image as PIL
# from pdf417decoder import PDF417Decoder

# # Load the image containing the barcode
# image = PIL.open("pdf417.jpg")

# # Initialize the PDF417 decoder with the image object
# decoder = PDF417Decoder(image)

# # Attempt to decode the barcode
# if decoder.decode() > 0:
#     decoded = decoder.barcode_data_index_to_string(0)
#     print("Decoded data:", decoded)
# else:
#     print("No PDF417 barcode found.")
from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image
image = cv2.imread("pdf417.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load the image.")
    exit()

# Decode the barcode
barcodes = decode(image)

if len(barcodes) == 0:
    print("No barcodes found.")
else:
    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        print(f"Barcode Data: {data}")

        # Draw a rectangle around the barcode
        points = barcode.polygon
        points = [(point.x, point.y) for point in points]
        cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

        # Annotate the decoded data beside the bounding box
        x, y = points[0]  # Take the first point of the bounding box
        cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Green text

    # Display the image with the barcode highlighted and annotated
    cv2.imshow("Barcode with Annotation", image)

    # Wait for a key press
    key = cv2.waitKey(0)

    # Save the annotated image when a key is pressed
    output_file = "decoded_barcode.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")

    cv2.destroyAllWindows()
