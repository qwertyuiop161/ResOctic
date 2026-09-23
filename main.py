import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
import os

folder = 'images'
os.makedirs('speckle', exist_ok=True)

file_names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
print("type 1 to customize params")
x = int(input(""))
se = 0.01
if (x==1):
    se=float(input("enter speckle intensity 0-1: "))

for item in file_names:
    image = cv2.imread(os.path.join(folder, item))
    
        
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_float = image / 255.0
    
    speckle = random_noise(image_float, mode='speckle', var=se)
    noisy_uintse = np.clip(speckle * 255, 0, 255).astype(np.uint8)
    noisy_se = cv2.cvtColor(noisy_uintse, cv2.COLOR_RGB2BGR)
    
    cv2.imwrite('speckle/' + os.path.splitext(item)[0] + '.jpg', noisy_se)
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    axes[0].imshow(image_float)
    axes[0].set_title('Original')
    axes[0].axis('off')
    
    axes[1].imshow(speckle)
    axes[1].set_title(f'Speckle (var={se})')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
