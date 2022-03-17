import base64                  
import requests
from PIL import Image

response = requests.get('https://codepannu-disney.herokuapp.com/')
x = [i['_id'] for i in response.json()]
print(x)
for n,i in enumerate(x):
  with open(f'{i}.jpg','wb') as f:
    f.write(base64.b64decode(response.json()[n]['img']))
    print('wrote')


##########################################################################################
######################## Getting by name and saving the image ############################
##########################################################################################

mickey = requests.get(f'https://codepannu-disney.herokuapp.com/name/micKeyMoUse',params={'apiKey':'codepannustudent'})
print(mickey.json())
with open('mickeyy.png','wb') as f:
  f.write(base64.b64decode(mickey.json()[0]['img']))

im = Image.open('./mickeyy.png')
im.show()

##################################################################
################ Getting by gender ###############################
##################################################################

mini = requests.get(f'https://codepannu-disney.herokuapp.com/gender/female',params={'apiKey':'codepannustudent'})
print(mini.json())
with open('mini.png','wb') as f:
  f.write(base64.b64decode(mini.json()[0]['img']))
  print('wrote')



#####################################################################
###################### posting data #################################
#####################################################################

##Data alreadt exists


# character = {
#   'name':'MinnieMouse',
#   'designedby':'Walt Disney,',
#   'img':'',
#   'firstAppeared': 'Steamboat Willie',
#   'gender':'Female'
#   }

# with open('Minnie_Mouse.png','rb') as f:
#   character['img'] = base64.b64encode(f.read()).decode("utf8")


# response = requests.post('http://localhost:3000',params={'apiKey':'codepannustudent'},data=character)
# print(response.json())



