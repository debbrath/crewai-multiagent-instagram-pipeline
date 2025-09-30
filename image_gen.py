import torch
from diffusers import StableDiffusionXLPipeline
from IPython.display import display

def generate_images(prompts):
    pipe = StableDiffusionXLPipeline.from_pretrained(
        "segmind/SSD-1B",
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16"
    ).to("cuda")

    results = []
    for p in prompts:
        image = pipe(
            prompt=p,
            negative_prompt="ugly, darkness, blurry, poor quality",
            width=1500 - (1500 % 8),
            height=750 - (750 % 8),
            guidance_scale=7,
            num_inference_steps=28
        ).images[0]
        results.append(image)
        display(image)

    return results