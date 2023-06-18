import cv2
from pyzbar import pyzbar


def detect_qr_code(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the image
    qr_codes = pyzbar.decode(gray)

    # Iterate over detected QR codes
    for qr_code in qr_codes:
        (x, y, w, h) = qr_code.rect
        data = qr_code.data.decode("utf-8")
        qr_code_type = qr_code.type

        # Print the decoded information
        print("QR Code Type:", qr_code_type)
        print("QR Code Data:", data)
        print()
    # Display the image with QR code detection
    cv2.imshow("QR Code Detection", image)
    cv2.waitKey(0)


image_path = "QRcode tests/QRcode1.png"

detect_qr_code(image_path)
