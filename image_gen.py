# Alternative solution if direct model loading fails
# This solution downloads the necessary files from Hugging Face and uses them directly

import os
import sys
import torch
from huggingface_hub import hf_hub_download, snapshot_download
from pathlib import Path

# Define model ID
model_id = "Freepik/F-Lite"

print("Downloading model files...")
# Download the entire repository to a local directory
model_dir = snapshot_download(
    repo_id=model_id,
    local_dir="./F-Lite-model",
    local_dir_use_symlinks=False
)

print(f"Model downloaded to {model_dir}")

# Add the model directory to Python path
sys.path.append(model_dir)

try:
    # Try to import the custom pipeline
    print("Importing custom pipeline...")
    from dit_model.f_lite_pipeline import FLitePipeline
    
    # Initialize the pipeline
    print("Initializing pipeline...")
    pipe = FLitePipeline.from_pretrained(
        pretrained_model_path=os.path.join(model_dir, "dit_model"),
        pretrained_tokenizer_path=os.path.join(model_dir, "tokenizer"),
        torch_dtype=torch.float16
    )
    
    # Move to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    pipe = pipe.to(device)
    
    # Print VRAM info if using GPU
    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name()}")
        print(f"Available VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    
    # Generate an image
    prompt = "A beautiful sunset over mountains with vibrant colors"
    negative_prompt = "low quality, blurry, distorted"
    
    print(f"Generating image with prompt: '{prompt}'")
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    ).images[0]
    
    # Save the image
    output_path = "generated_image.png"
    image.save(output_path)
    print(f"Image saved to {output_path}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nIf the above approach fails, try the following manual steps:")
    print("1. Clone the repository directly:")
    print("   git clone https://huggingface.co/Freepik/F-Lite")
    print("2. Navigate to the directory:")
    print("   cd F-Lite")
    print("3. Create a Python file with the appropriate import:")
    print("   from dit_model.f_lite_pipeline import FLitePipeline")
    print("4. Use the pipeline as shown in the documentation")