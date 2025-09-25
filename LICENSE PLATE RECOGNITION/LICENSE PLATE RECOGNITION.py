import cv2
import pytesseract

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update to your tesseract.exe location

def recognize_license_plate(image_path):
    """
    Recognizes license plate from an image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Recognized license plate text, or None if recognition fails.
    """
    try:
        # Read the image
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not read image from {image_path}")
            return None

        # Preprocessing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 30, 200)

        # Find contours
        contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        plate_contour = None
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)
            if len(approx) == 4:  # Assuming license plate is a rectangle
                plate_contour = approx
                break

        if plate_contour is None:
            print("License plate not found.")
            return None

        # Extract plate region
        x, y, w, h = cv2.boundingRect(plate_contour)
        plate_roi = gray[y:y + h, x:x + w]

        # Use Tesseract OCR
        plate_text = pytesseract.image_to_string(
            plate_roi,
            config='--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        )
        plate_text = "".join(c if c.isalnum() else "" for c in plate_text).strip()

        if plate_text:
            return plate_text
        else:
            print("License plate text not recognized.")
            return None

    except Exception as e:
        print(f"Error during license plate recognition: {e}")
        return None

# --- Take image path from terminal ---
image_file = input("Enter the full path of the car image: ")

result = recognize_license_plate(image_file)

if result:
    print("License plate:", result)
