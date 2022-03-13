import base64                  
import requests
from PIL import Image


emotions = ['happy','sad','angry','adorable']
for emotion in emotions:
	with open(f'{emotion}.png','rb') as f:
		response = requests.post(f'http://localhost:3000/{emotion}',params={'apiKey':'codepannustudent'},data={'img':base64.b64encode(f.read()).decode("utf8")})
	print(response.json())	


response = requests.get('http://localhost:3000/angry',params={'apiKey':'codepannustudent'})
#print(response.json())
with open('emotion.png','wb') as f:
	f.write(base64.b64decode(response.json()['img']))


im = Image.open('./emotion.png')
im.show()