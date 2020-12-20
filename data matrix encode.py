"""from pylibdmtx.pylibdmtx import encode
from PIL import Image
data="hai halo world"
encoded = encode('100')
#encoded=data.encode('Ascii')
#print(encoded)
img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
img.save('test.png')"""
from pylibdmtx.pylibdmtx import encode
from PIL import Image
encoded_data = encode('10022003'.encode('utf-8'))
img = Image.frombytes('RGB', (encoded_data.width, encoded_data.height), encoded_data.pixels)
img.save("test.png")
