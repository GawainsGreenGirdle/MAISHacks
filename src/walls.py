from PIL import Image as PILImage
from urllib.request import urlopen
from IPython.display import Image, display

def walls(im1: PILImage.Image, listOfRooms):
  url = "https://raw.githubusercontent.com/GawainsGreenGirdle/MAISHacks/main/Tokens/Wall.png"
  wallTile = PILImage.open(urlopen(url))
  wallTileT = wallTile.transpose(PILImage.Transpose.ROTATE_90)
  for room in listOfRooms:
    #assumes that the vertices are listed counterclockwise
    length = room[1][0]-room[0][0]
    height = room[2][1]-room[1][1]
    for j in range(length):
      add(im1, wallTile, room[0][0] + j, room[0][1])
      add(im1, wallTile, room[0][0] + j, room[2][1])
    for j in range(height):
      add(im1, wallTileT, room[0][0], room[0][1] + j)
      add(im1, wallTileT, room[1][0], room[0][1] + j)
