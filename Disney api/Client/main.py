import base64                  
import requests
from PIL import Image
#######################################################################
#########################Getting and saving image data ################
#######################################################################

response = requests.get('http://localhost:3000')
x = [i['_id'] for i in response.json()]
print(x)
filename = input("Enter the filename with extention: ")
with open(filename,'wb') as f:
  f.write(base64.b64decode(response.json()[-1]['img']))
  print('wrote')

#####################################################################
###################### posting data #################################
#####################################################################

character = {
  'name':'Minnie Mouse',
  'designedby':'Walt Disney,',
  'img':'',
  'firstAppeared': 'Steamboat Willie',
  'gender':'Female'
  }

with open('Minnie_Mouse.png','rb') as f:
  character['img'] = base64.b64encode(f.read()).decode("utf8")


response = requests.post('http://localhost:3000',params={'apiKey':'codepannustudent'},data=character)
print(response.json())



#######################################################################
###########################Deleting####################################
#######################################################################
id_to_delete = '62149c240a428e01b5d5fd21'
deleting = requests.delete(f'http://localhost:3000/{id_to_delete}',params={'apiKey':'codepannustudent'})
#print(deleting.json())


#####################################################################
######################## Getting by name ############################
#####################################################################

mickey = requests.get(f'http://localhost:3000/name/micKeyMoUse',params={'apiKey':'codepannustudent'})
print(mickey.json())
with open('mickeyy.png','wb') as f:
  f.write(base64.b64decode(mickey.json()[0]['img']))

im = Image.open('./mickeyy.png')
im.show()


mini = requests.get(f'http://localhost:3000/gender/female',params={'apiKey':'codepannustudent'})
print(mini.json())
with open('mini.png','wb') as f:
  f.write(base64.b64decode(mini.json()[0]['img']))
  print('wrote')

