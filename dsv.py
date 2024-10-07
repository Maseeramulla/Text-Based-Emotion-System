import numpy as np
import matplotlib.pyplot as plt

# Create a sample grayscale image (a gradient from black to white)
image = np.linspace(0, 255, 256).astype(np.uint8)
image = np.tile(image, (256, 1))

# Display the image with a gray colormap
plt.imshow(image, cmap='gray')
plt.colorbar()
plt.title('Grayscale Image with Gray Colormap')
plt.axis('off')
plt.show()
