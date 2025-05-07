


          
# Freepix

Freepix is a Python tool for generating high-quality images using the F-Lite text-to-image diffusion model from Freepik. This tool provides a simple command-line interface for creating images from text prompts with various customization options.

## Features

- Generate high-quality images from text prompts
- Support for negative prompts to exclude unwanted elements
- Customizable image dimensions
- Adjustable generation parameters (guidance scale, steps, etc.)
- Support for multiple image generation in a single run
- Automatic device selection (CUDA/CPU)
- Memory optimization with CPU offloading

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Freepix.git
   cd Freepix
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can generate images using the command-line interface:

```bash
python generate.py --prompt "Your detailed text prompt here" --output_file output.png
```

### Basic Parameters

- `--prompt`: Text prompt describing the image you want to generate (required)
- `--output_file`: Path where the generated image will be saved (required)
- `--negative_prompt`: Text describing elements you want to exclude from the image
- `--num_images`: Number of images to generate (default: 1)

### Advanced Parameters

- `--model`: HuggingFace model ID (default: "Freepik/F-Lite")
- `--seed`: Random seed for reproducible generation (default: 0)
- `--guidance_scale`: Controls how closely the image follows the prompt (default: 6)
- `--steps`: Number of inference steps (default: 30, more steps = higher quality but slower)
- `--width`: Width of the generated image (default: 1344)
- `--height`: Height of the generated image (default: 896)
- `--cpu_offload`: Whether to offload models to CPU when not in use (default: True)
- `--device`: Device to use for inference ("cuda" or "cpu")

## Examples

### Basic Image Generation

```bash
python generate.py --prompt "A beautiful sunset over mountains with vibrant colors" --output_file sunset.png
```
![Sunset example](sunset.png)

### Using Negative Prompts

```bash
python generate.py --prompt "A professional portrait of a woman" --negative_prompt "blurry, low quality, distorted" --output_file portrait.png
```
![Portrait example](portrait.png)

### Generating Multiple Images

```bash
python generate.py --prompt "Abstract digital art with geometric shapes" --output_file abstract.png --num_images 3
```
<img src="abstract.png" alt="Abstract 1" width="200" style="margin-right:10px"/><img src="abstract-1.png" alt="Abstract 2" width="200" style="margin-right:10px"/><img src="abstract-2.png" alt="Abstract 3" width="200"/>

### Custom Dimensions

```bash
python generate.py --prompt "A futuristic cityscape at night" --output_file cityscape.png --width 500 --height 500
```
![Cityscape example](cityscape.png)



## Credits
This work is based on the F-Lite model as described in the article: F Lite: Freepik & Fal.ai unveil an open-source image model trained on licensed data

Special thanks to Freepik and Fal.ai for developing and open-sourcing this innovative model.

## License

Please refer to the original F-Lite model license for usage terms and conditions.
See [LICENSE](LICENSE) for the full license details.

## Acknowledgements

This project uses the F-Lite model developed by Freepik.