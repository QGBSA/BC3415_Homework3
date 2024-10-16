import torch
from stable_diffusion_videos.stable_diffusion_pipeline import StableDiffusionWalkPipeline

# Load the pipeline once globally
pipeline = StableDiffusionWalkPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,
    revision="fp16"
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image_from_prompt(prompt):
    """
    Generates an image from a text prompt using Stable Diffusion.
    
    Args:
    - prompt (str): The input text prompt to generate an image.

    Returns:
    - str: The file path of the generated image.
    """
    image_path = f"static/generated_images/{prompt[:10]}_image.png"
    
    # Generate image (for simplicity, we'll reuse the video pipeline for now)
    image = pipeline(prompt).images[0]
    
    # Save the image locally
    image.save(image_path)
    
    return image_path

def generate_video_from_prompts(prompts, seeds, fps=5, num_interpolation_steps=5):
    """
    Generates a video by interpolating between multiple text prompts.

    Args:
    - prompts (list of str): The text prompts to interpolate between.
    - seeds (list of int): The random seeds corresponding to each prompt.
    - fps (int): Frames per second for the video.
    - num_interpolation_steps (int): Number of interpolation steps between each prompt.

    Returns:
    - str: The file path of the generated video.
    """
    video_path = f"static/generated_videos/{prompts[0][:10]}_to_{prompts[-1][:10]}.mp4"
    
    # Generate the video using the stable diffusion pipeline
    pipeline.walk(
        prompts=prompts,
        seeds=seeds,
        fps=fps,
        num_interpolation_steps=num_interpolation_steps,
        height=512,
        width=512,
        output_dir='static/generated_videos',
        video_name=video_path.split('/')[-1]
    )
    
    return video_path
