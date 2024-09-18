from flask import Flask, request, jsonify
import base64
from renderer import Renderer
import numpy as np
import torch

PKL_PATH = 'check_points/stylegan2_lions_512_pytorch.pkl'
IMAGE_RESOLUTION = 512
DIST_THRESHOLD = 1.5
MAX_ITER = 1000

app = Flask(__name__)

def base64_string_to_image(base64_string):
    image_data = base64.b64decode(base64_string)
    return image_data

def image_to_base64_string(image_path):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

@app.route('/upload', methods=['POST'])
def process_image():
    data = request.json

    if 'image_data' not in data:
        return jsonify({"error": "No image data provided"}), 400

    base64_string = data['image_data']

    image_data = base64_string_to_image(base64_string)

    p_in_pixels = np.array(data['point_start'])
    t_in_pixels = np.array(data['point_target'])

    image_data = np.frombuffer(image_data, dtype=np.uint8)

    res = {'img_resolution': IMAGE_RESOLUTION, 'num_ws': 16, 'has_noise': True, 'has_input_transform': False}

    renderer = Renderer()
    renderer.init_network(res, pkl = PKL_PATH)

    res_2 = {'img_resolution': IMAGE_RESOLUTION, 'num_ws': 16, 'has_noise': True, 'has_input_transform': False, 'image': image_data, 'w': renderer.w}
    mask = np.ones((IMAGE_RESOLUTION, IMAGE_RESOLUTION), dtype=np.float32)
    mask_tensor = torch.tensor(mask).float()
    drag_mask = 1 - mask_tensor

    flag = True
    count = 0
    while flag:
        renderer._render_drag_impl(
            res_2, 
            p_in_pixels,
            t_in_pixels, 
            drag_mask, 
            20,
            reg=0,
            feature_idx=5,  # NOTE: do not support change for now
            r1=3,
            r2=12,  
            trunc_psi=0.7,
            is_drag=True,
            to_pil=True)
        
        p_in_pixels = np.array(p_in_pixels)
        t_in_pixels = np.array(t_in_pixels)
        dist = np.linalg.norm(p_in_pixels - t_in_pixels)

        count += 1
        if dist < DIST_THRESHOLD or count > MAX_ITER:
            flag = False

    base64_string = image_to_base64_string('test.jpg')

    return jsonify({"image_data": base64_string})


if __name__ == '__main__':
    app.run(debug=True)
