License Plate Recognition using OpenCV and Tesseract OCR

This project implements a **License Plate Recognition (LPR)** system using **Python**, **OpenCV**, and **Tesseract OCR**. It detects license plates from car images, extracts the license plate region, and recognizes the alphanumeric characters.

---

Features

- Detects license plates from images using contour detection.
- Preprocesses images for better OCR accuracy (grayscale, blurring, edge detection).
- Uses **Tesseract OCR** to extract license plate text.
- Input image can be provided via **terminal** for flexibility.
- Handles errors if the image is not found or the license plate is not detected.

---

Requirements

- Python 3.8+
- OpenCV (`cv2`)
- pytesseract
- Tesseract OCR installed on your system

Install Python packages using pip:


pip install opencv-python pytesseract



NOTE : Paste the selected image path in the terminal to get the number plate recognition.