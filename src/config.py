from huggingface_hub import hf_hub_download

# Hugging Face model repo details

HF_MODEL_REPO = "RezaNavazani/barcode_detection/ONNX"
MODEL_FILENAME = "yolov8_barcode_detection.onnx"

def get_model_path():
    """Downloads the model from Hugging Face if not available locally."""
    return hf_hub_download(repo_id=HF_MODEL_REPO, filename=MODEL_FILENAME)

MODEL_PATH = get_model_path()