import cv2
import numpy as np
from pyzbar import pyzbar


def draw_arrow(image, start_point, end_point):
    arrow_color = (0, 0, 255)

    # Calculate the center point of the QR code
    qr_code_center = ((start_point[0] + end_point[0]) //
                      2, (start_point[1] + end_point[1]) // 2)

    # Calculate the direction vector from the QR code center to the start point
    direction_vector = (
        start_point[0] - qr_code_center[0], start_point[1] - qr_code_center[1])

    # Normalize the direction vector
    norm = np.linalg.norm(direction_vector)
    normalized_direction = (
        direction_vector[0] / norm, direction_vector[1] / norm)

    # Calculate the arrow tip position
    arrow_tip = (int(end_point[0] + normalized_direction[0] * 20),
                 int(end_point[1] + normalized_direction[1] * 20))

    # Draw an arrow from the start point to the arrow tip
    cv2.arrowedLine(image, start_point, arrow_tip,
                    arrow_color, 2, cv2.LINE_AA, tipLength=0.2)


def detect_and_read_qr_codes(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the image
    qr_codes = pyzbar.decode(gray)

    # Iterate over detected QR codes
    for qr_code in qr_codes:
        # Extract the bounding box coordinates
        (x, y, w, h) = qr_code.rect

        # Draw a rectangle around the QR code
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Decode the QR code
        data = qr_code.data.decode("utf-8")
        qr_code_type = qr_code.type

        # Print the decoded information
        print("QR Code Type:", qr_code_type)
        print("QR Code Data:", data)
        print()

        # Draw an arrow pointing towards the center of the QR code
        start_point = (image.shape[1] // 2, image.shape[0] // 2)
        end_point = ((x + x + w) // 2, (y + y + h) // 2)
        draw_arrow(image, start_point, end_point)

    # Display the image with QR code detection
    cv2.imshow("QR Code Detection", image)
    cv2.waitKey(0)

# Example usage


# Example usage
image_path = "QRcode tests/QRcode1.png"

detect_and_read_qr_codes(image_path)
