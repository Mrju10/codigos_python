import random
import io
import PIL.Image
import numpy as np

def generate_image(width, height):
  image = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(random.randint(0, 255))
    image.append(row)
  return image

def save_image(image, filename):
  buffer = io.BytesIO()
  image = np.array(image, dtype=np.uint8)
  image = PIL.Image.fromarray(image, 'RGB')
  image.save(buffer, 'PNG')
  buffer.seek(0)
  with open(filename, 'wb') as f:
    f.write(buffer.read())

if __name__ == "__main__":
  image = generate_image(28, 28)
  print(image)
  save_image(image, 'imaging.png')
