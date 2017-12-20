# -*- coding: UTF-8 -*-

from io import StringIO
import random
from PIL import Image

img = Image.new('RGB', (512, 512))
base = random.randint(0, 16777216)
pixels = [base+i*j for i in range(512) for j in range(512)]
img.putdata(pixels)
output = StringIO()
bebe = output.getvalue()
img.save('image.png')
print(bebe)
print('sending image')
