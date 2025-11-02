from PIL import Image as PILImage
from urllib.request import urlopen
from IPython.display import Image, display

def add(im1: PILImage.Image, im2: PILImage.Image, x, y):
  #note that im1 should be the background or other image such that
  #each cell is 80*80.
  i = x * 80
  j = y * 80
  xSize, ySize = im1.size
  if xSize-80 < i or ySize-80 < j:
    raise Exception("Invalid coordinate for input image size");
  else:
    im1.paste(im2, (i,j))
