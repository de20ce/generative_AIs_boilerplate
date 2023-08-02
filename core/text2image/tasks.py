from random import random
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

import os
from io import BytesIO
from PIL import Image
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

import json
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)



TG_TOKEN = os.getenv('TG_TOKEN')
MODEL_DATA = os.getenv('MODEL_DATA', 'runwayml/stable-diffusion-v1-5')
LOW_VRAM_MODE = (os.getenv('LOW_VRAM', 'true').lower() == 'true')
USE_AUTH_TOKEN = (os.getenv('USE_AUTH_TOKEN', 'true').lower() == 'true')
SAFETY_CHECKER = (os.getenv('SAFETY_CHECKER', 'true').lower() == 'true')
HEIGHT = int(os.getenv('HEIGHT', '512'))
WIDTH = int(os.getenv('WIDTH', '512'))
NUM_INFERENCE_STEPS = int(os.getenv('NUM_INFERENCE_STEPS', '50'))
STRENTH = float(os.getenv('STRENTH', '0.75'))
GUIDANCE_SCALE = float(os.getenv('GUIDANCE_SCALE', '7.5'))

revision = "fp16" if LOW_VRAM_MODE else None
torch_dtype = torch.float16 if LOW_VRAM_MODE else None

channel_layer = get_channel_layer()
# loading the text2imagepipeline
stable_diff_pipe = StableDiffusionPipeline.from_pretrained(MODEL_DATA, revision=revision, torch_dtype=torch_dtype, use_auth_token=USE_AUTH_TOKEN)


def img2bytes(img):
    byte_io = BytesIO()
    byte_io.name = 'dummy_img.jpeg'
    img.save(byte_io, 'JPEG')
    byte_io.seek()
    return byte_io

def generate_image_from_text(prompt, seed=None, height=HEIGHT, width=WIDTH, num_inference_steps=NUM_INFERENCE_STEPS, strength=STRENTH, guidance_scale=GUIDANCE_SCALE, photo=None):
    seed = seed if seed is not None else random.randint(1, 100)
    generator = torch.cuda.manual_seed_all(seed)
    stable_diff_pipe.to("cuda")
    with autocast("cuda"):
        image = stable_diff_pipe(prompt=[prompt],
                        generator=generator,
                        strength=strength,
                        height=height,
                        width=width,
                        guidance_scale=guidance_scale,
                        num_inference_steps=num_inference_steps)["images"][0]
    
    return image, seed

def dummy_response(input):
    if input['text'] != "":
        return input['text'] + " again"
    else:
        return  "Please, you should enter a text"

@shared_task
def get_response(channel_name, input_data):
    logging.info(f'channel: {channel_name}, input: {input_data}')
    logging.info(f'input keys in get_Response : {input_data.keys()}')
    text_response = dummy_response(input_data)
    
    text_response_data = text_response # should be serialized if object
    img, seed = generate_image_from_text(prompt=input_data)
    bytes_img_data = img2bytes(img)
    
    async_to_sync(channel_layer.send)(
        channel_name,
        {
            "type": "chat_message",
            "text": [{"msg": text_response_data, "source": "bot"}],
            "bytes": bytes_img_data,
        },
    )
    logging.info(f'after sending channel step  : {channel_name}, input: {text_response_data}')