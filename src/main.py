import cv2
import requests
import gradio as gr
import numpy as np
from ultralytics import YOLO
from pyzbar.pyzbar import decode
from PIL import Image
import time
from src.api import lookup_product  # Import the API function
from config import MODEL_PATH

# Load YOLOv8 model (for barcode detection)
''''
MODEL_PATH = 'models/best.onnx'
'''
model = YOLO(MODEL_PATH)  # YOLOv8 nano (lightweight & fast)

#barcode_data = decode(Image.open(testimagepath)) 

def process_frame(image):
    start_time = time.time()
    """Detects a barcode using YOLOv8 and extracts numbers using Pyzbar."""
    # Convert image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Run YOLOv8 for barcode detection
    results = model(image)
    detected_barcodes = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box

            # Crop the barcode region
            barcode_region = image[y1:y2, x1:x2]

            # Decode barcode using Pyzbar
            barcodes = decode(barcode_region)
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                if barcode_data:
                  barcode_number = barcode_data  # First detected text
                  response_time = time.time() - start_time
                  response_text=f"Response Time: {response_time:.4f} seconds"
                  return lookup_product(barcode_number), response_text
    
    # Show detected barcode numbers
    return detected_barcodes if detected_barcodes else "No barcode detected. Try again!"

if __name__ == "__main__":
    from frontend.app import interface
    interface.launch(share=True)