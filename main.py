import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_float = image / 255.0
print("customize params? y for yes anything for no")
x = input("")
se=0.01
g=0.01
sp=0.02
if (x=="y"):
  se = float(input("0-1 speckle"))
  g = float(input("0-1 gaussian"))
  sp = float(input("0-1 salt&pepper"))
speckle = random_noise(image_float, mode='speckle', var=se)
gaussian = random_noise(image_float, mode='gaussian', var=g)
sp = random_noise(image_float, mode='s&p', amount=sp)
noisy_uintsp = np.clip(sp * 255, 0, 255).astype(np.uint8)
noisy_uintg = np.clip(gaussian * 255, 0, 255).astype(np.uint8)
noisy_uintse = np.clip(speckle * 255, 0, 255).astype(np.uint8)

noisy_sp = cv2.cvtColor(noisy_uintsp, cv2.COLOR_RGB2BGR)
noisy_se = cv2.cvtColor(noisy_uintse, cv2.COLOR_RGB2BGR)
noisy_g = cv2.cvtColor(noisy_uintg, cv2.COLOR_RGB2BGR)

cv2.imwrite('saltandpepper.jpg', noisy_sp)
cv2.imwrite('speckle.jpg', noisy_se)
cv2.imwrite('guassian.jpg', noisy_g)

fig, axes = plt.subplots(3, 3, figsize=(13, 12))

axes[0, 0].imshow(image_float)
axes[0, 0].set_title('Original')
axes[0, 1].imshow(speckle)
axes[0, 1].set_title('Speckle (var=' + str(se) + ')')

axes[1, 0].imshow(image_float)
axes[1, 0].set_title('Original')
axes[1, 1].imshow(gaussian)
axes[1, 1].set_title('Gaussian (var=' + str(g) + ')')

axes[2, 0].imshow(image_float)
axes[2, 0].set_title('Original')
axes[2, 1].imshow(sp)
axes[2, 1].set_title('S&P (amount=' + str(sp) + ')')

for ax in axes.ravel():
  ax.axis('off')

plt.tight_layout()
plt.show()