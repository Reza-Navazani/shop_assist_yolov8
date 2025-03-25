import gradio as gr
from src.main import process_frame

interface = gr.Interface(
    fn=process_frame,
    inputs=gr.Image(type="pil"),  # Remove 'source' argument
    outputs=["text", "text"],
    title="📸 Shop Assist (YOLOv8)",
    description="Upload an image containing a barcode to extract the number."
)

if __name__ == "__main__":
    interface.launch(share=True)