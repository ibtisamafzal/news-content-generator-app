from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe.to("cpu")  # Force CPU if GPU is unavailable
    image = pipe(prompt, guidance_scale=7.5).images[0]  # Use guidance scale to adjust quality
    return image
