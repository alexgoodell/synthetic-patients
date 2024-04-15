import requests
import json

import requests
import json
import random


def send_prompt(final_prompt):

    seed = random.randint(0, 1000000000)
    url = "http://localhost:1111/sdapi/v1/txt2img"
    payload = json.dumps({
      "sampler": "DPM++ 2M Karras",
      "model": "pixelwaveturboexcellent_03_f16.ckpt",
      "original_width": 1024,
      "hires_fix": False,
      "seed_mode": "Scale Alike",
      "aesthetic_score": 5,
      "fps": 5,
      "crop_top": 0,
      "mask_blur_outset": 0,
      "target_width": 1024,
      "guiding_frame_noise": 0.019999999552965164,
      "hires_fix_width": 768,
      "crop_left": 0,
      "negative_aesthetic_score": 5,
      "steps": 8,
      "image_prior_steps": 5,
      "original_height": 300,
      "negative_prompt_for_image_prior": True,
      "width": 1024,
      "negative_original_height": 512,
      "refiner_start": None,
      "strength": 1,
      "sharpness": 0,
      "num_frames": 14,
      "negative_original_width": 512,
      "mask_blur": 1,
      "batch_size": 1,
      "height": 1024,
      "seed": seed,
      "guidance_scale": 3,
      "start_frame_guidance": 1,
      "clip_weight": 1,
      "hires_fix_strength": 0.699999988079071,
      "batch_count": 5,
      "hires_fix_height": 768,
      "refiner_model": None,
      "motion_scale": 127,
      "image_guidance": None,
      "negative_prompt": "signature",
      "target_height": 1024,
      "clip_skip": 1,
      "loras": [  {"file": "pixel_art_xl_v1_lora_f16.ckpt", "weight": 1}],
      "prompt": final_prompt,
      "zero_negative_prompt": False
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


personalities = [
    "a 25-year-old Black female with curly hair, wearing a stylish blazer",
    "a 40-year-old Hispanic male with short black hair, wearing a button-down shirt",
    "a 60-year-old white female with shoulder-length grey hair, wearing a cashmere sweater",
    "a 35-year-old Asian male with glasses, wearing a polo shirt",
    "a 50-year-old Middle Eastern female with straight hair, wearing a tailored business suit",
    "a 18-year-old Native American male with medium-length hair, wearing a graphic tee",
    "a 45-year-old South Asian female with wavy hair, wearing a smart casual dress",
    "a 70-year-old East Asian male with a clean shave, wearing a sports jacket",
    "a 30-year-old mixed-race female with shoulder-length straight hair, wearing a trendy top",
    "a 55-year-old white male with a receding hairline, wearing a flannel shirt",
    "a 20-year-old Black male with short hair, wearing a university sweatshirt",
    "a 65-year-old Hispanic female with bobbed hair, wearing a knit top",
    "a 28-year-old Middle Eastern male with a stubble beard, wearing a casual shirt",
    "a 75-year-old South Asian male with thinning hair, wearing a vest over a long-sleeve shirt",
    "a 22-year-old East Asian female with long dyed hair, wearing a chic blouse",
    "a 40-year-old Native American female with long dark hair, wearing a simple dress",
    "a 33-year-old mixed-race male with short curls, wearing a lightweight hoodie",
    "a 29-year-old white female with layered hair, wearing a casual blazer",
    "a 48-year-old Black male with a buzz cut, wearing a casual shirt",
    "a 15-year-old Hispanic female with long straight hair, wearing a tank top",
    "a 38-year-old Middle Eastern female with curly hair, wearing a blazer",
    "a 53-year-old Asian female with short hair, wearing a business suit",
    "a 67-year-old white male with a full beard, wearing a cable knit sweater",
    "a 24-year-old Native American male with a ponytail, wearing a button-up shirt",
    "a 34-year-old South Asian male with slicked-back hair, wearing a suit",
    "a 43-year-old East Asian female with bobbed hair, wearing a casual summer dress",
    "a 19-year-old mixed-race female with long wavy hair, wearing a college hoodie",
    "a 47-year-old Black female with braids, wearing a corporate dress",
    "a 58-year-old Hispanic male with greying hair, wearing a polo shirt",
    "a 27-year-old white male with short blond hair, wearing a casual shirt",
    "a 62-year-old Middle Eastern female with shoulder-length hair, wearing a modern tunic",
    "a 16-year-old South Asian female with long black hair, wearing a bright top",
    "a 51-year-old Native American female with straight hair, wearing a blouse",
    "a 37-year-old East Asian male with medium-length hair, wearing a sweater",
    "a 21-year-old mixed-race male with buzzed hair, wearing a sports jersey",
    "a 44-year-old Black female with short curly hair, wearing a professional skirt suit",
    "a 26-year-old Hispanic female with long wavy hair, wearing a knit sweater",
    "a 39-year-old white male with thinning hair, wearing a sports coat",
    "a 57-year-old Middle Eastern male with a neat beard, wearing a linen shirt",
    "a 31-year-old South Asian female with a lob haircut, wearing a contemporary wrap dress",
    "a 49-year-old East Asian male with glasses, wearing a button-up shirt",
    "a 17-year-old Native American female with braided hair, wearing a casual tee",
    "a 56-year-old mixed-race male with a goatee, wearing a knit polo",
    "a 23-year-old Black male with dreadlocks, wearing a casual suit"
]


prompt_template = (f"A pixel art image depicting a shoulder-level headshot portrait of {{"
                   f"personality}}, against a bright plain monochromatic background")

for personality in personalities:
    final_prompt = prompt_template.format(personality=personality)
    print(final_prompt)
    send_prompt(final_prompt)


