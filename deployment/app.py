from fastai.vision.all import *
import gradio as gr
import os
# from pathlib import Path
# import pathlib

# # Force Fastai to use WindowsPath
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

category_levels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'human', 'ship', 'truck']

current_dir = os.getcwd()
model_path = os.path.join(os.path.join(current_dir,"models"),"category_model_v2.pkl")
print(model_path)

model = load_learner(model_path)

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(category_levels, map(float, probs)))

image = gr.Image(width=224, height=224)
label = gr.Label(num_top_classes=5)
example_images = [os.path.join(os.path.join(current_dir,"test_images"),f"{i}.jpg") for i in range(1,9)]
print(example_images)

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=example_images)
iface.launch(inline=False)
