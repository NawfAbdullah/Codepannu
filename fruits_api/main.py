import requests

fruits_to_add = [{
    "genus": "Malus",
    "name": "Apple",
    "id": 6,
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 11.4,
        "protein": 0.3,
        "fat": 0.4,
        "calories": 52,
        "sugar": 10.3
    },"category":"fruit"
}, {
    "genus": "Musa",
    "name": "Banana",
    "id": 1,
    "family": "Musaceae",
    "order": "Zingiberales",
    "nutritions": {
        "carbohydrates": 22,
        "protein": 1,
        "fat": 0.2,
        "calories": 96,
        "sugar": 17.2
    },"category":"fruit"
}, {
    "genus": "Rubus",
    "name": "Blackberry",
    "id": 64,
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 9,
        "protein": 1.3,
        "fat": 0.4,
        "calories": 40,
        "sugar": 4.5
    },"category":"fruit"
}, {
    "genus": "Ficus",
    "name": "Fig",
    "id": 68,
    "family": "Moraceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 19,
        "protein": 0.8,
        "fat": 0.3,
        "calories": 74,
        "sugar": 16
    },"category":"fruit"
}, {
    "genus": "Vitis",
    "name": "Grapes",
    "id": 47,
    "family": "Vitaceae",
    "order": "Vitales",
    "nutritions": {
        "carbohydrates": 18.1,
        "protein": 0.72,
        "fat": 0.16,
        "calories": 69,
        "sugar": 15.48
    },"category":"fruit"
}, {
    "genus": "Psidium",
    "name": "Guava",
    "id": 37,
    "family": "Myrtaceae",
    "order": "Myrtales",
    "nutritions": {
        "carbohydrates": 14,
        "protein": 2.6,
        "fat": 1,
        "calories": 68,
        "sugar": 9
    },"category":"fruit"
}, {
    "genus": "Apteryx",
    "name": "Kiwi",
    "id": 66,
    "family": "Actinidiaceae",
    "order": "Struthioniformes",
    "nutritions": {
        "carbohydrates": 15,
        "protein": 1.1,
        "fat": 0.5,
        "calories": 61,
        "sugar": 9
    },"category":"fruit"
}, {
    "genus": "Citrus",
    "name": "Lemon",
    "id": 26,
    "family": "Rutaceae",
    "order": "Sapindales",
    "nutritions": {
        "carbohydrates": 9,
        "protein": 1.1,
        "fat": 0.3,
        "calories": 29,
        "sugar": 2.5
    },"category":"fruit"
}, {
    "genus": "Citrus",
    "name": "Lime",
    "id": 44,
    "family": "Rutaceae",
    "order": "Sapindales",
    "nutritions": {
        "carbohydrates": 8.4,
        "protein": 0.3,
        "fat": 0.1,
        "calories": 25,
        "sugar": 1.7
    },"category":"fruit"
}, {
    "genus": "Litchi",
    "name": "Lychee",
    "id": 67,
    "family": "Sapindaceae",
    "order": "Sapindales",
    "nutritions": {
        "carbohydrates": 17,
        "protein": 0.8,
        "fat": 0.44,
        "calories": 66,
        "sugar": 15
    },"category":"fruit"
}, {
    "genus": "Mangifera",
    "name": "Mango",
    "id": 27,
    "family": "Anacardiaceae",
    "order": "Sapindales",
    "nutritions": {
        "carbohydrates": 15,
        "protein": 0.82,
        "fat": 0.38,
        "calories": 60,
        "sugar": 13.7
    },"category":"fruit"
}, {
    "genus": "Citrus",
    "name": "Orange",
    "id": 2,
    "family": "Rutaceae",
    "order": "Sapindales",
    "nutritions": {
        "carbohydrates": 8.3,
        "protein": 1,
        "fat": 0.2,
        "calories": 43,
        "sugar": 8.2
    },"category":"fruit"
}, {
    "genus": "Carica",
    "name": "Papaya",
    "id": 42,
    "family": "Caricaceae",
    "order": "Caricacea",
    "nutritions": {
        "carbohydrates": 11,
        "protein": 0,
        "fat": 0.4,
        "calories": 43,
        "sugar": 1
    },"category":"fruit"
}, {
    "genus": "Pyrus",
    "name": "Pear",
    "id": 4,
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 15,
        "protein": 0.4,
        "fat": 0.1,
        "calories": 57,
        "sugar": 10
    },"category":"fruit"
}, {
    "genus": "Ananas",
    "name": "Pineapple",
    "id": 10,
    "family": "Bromeliaceae",
    "order": "Poales",
    "nutritions": {
        "carbohydrates": 13.12,
        "protein": 0.54,
        "fat": 0.12,
        "calories": 50,
        "sugar": 9.85
    },"category":"fruit"
}, {
    "genus": "Prunus",
    "name": "Plum",
    "id": 71,
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 11.4,
        "protein": 0.7,
        "fat": 0.28,
        "calories": 46,
        "sugar": 9.92
    },"category":"fruit"
}, {
    "genus": "Rubus",
    "name": "Raspberry",
    "id": 23,
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 12,
        "protein": 1.2,
        "fat": 0.7,
        "calories": 53,
        "sugar": 4.4
    },"category":"fruit"
}, {
    "genus": "Fragaria",
    "name": "Strawberry",
    "id": 3,
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 5.5,
        "protein": 0.8,
        "fat": 0.4,
        "calories": 29,
        "sugar": 5.4
    },"category":"fruit"
}, {
    "genus": "Solanum",
    "name": "Tomato",
    "id": 5,
    "family": "Solanaceae",
    "order": "Solanales",
    "nutritions": {
        "carbohydrates": 3.9,
        "protein": 0.9,
        "fat": 0.2,
        "calories": 74,
        "sugar": 2.6
    },"category":"fruit"
}, {
    "genus": "Citrullus",
    "name": "Watermelon",
    "id": 25,
    "family": "Cucurbitaceae",
    "order": "Cucurbitales",
    "nutritions": {
        "carbohydrates": 8,
        "protein": 0.6,
        "fat": 0.2,
        "calories": 30,
        "sugar": 6
    },"category":"fruit"
}]

###########################run the loop only once########
for fruit in fruits_to_add:
    reponse = requests.post('http://localhost:3000/new',
    params={'apiKey':'codepannustudent'},
    data=fruit)
    print(reponse.json())

#########################post data##################################
reponse = requests.post('http://localhost:3000/new',
	params={'apiKey':'codepannustudent'},
	data={
		"genus": "Malus",
    	"name": "Dummyhtggdf",
    	"id": 6,
    	"family": "Rosaceae",
    	"order": "Rosales",
    	"carbohydrates": 11.4,
        "protein": 0.3,
        "fat": 0.4,
        "calories": 52,
        "sugar": 10.3,
        "category":"fruit"})
print(reponse.json())
id_to_delete = reponse.json().get('result')['_id']
print(id_to_delete)

########################################Getting all fruits#########################
all_fruits = requests.get('http://localhost:3000/')
#print(all_fruits)

###########################################GET by Id##########################

response = requests.get('http://localhost:3000/object/620b51965b3d92516b78355f')
print(response.json())

#############################################################################
############################## Getting by hierarchy #########################
#############################################################################

response = requests.get('http://localhost:3000/name/banana')
print(response.json())

response = requests.get('http://localhost:3000/genus/Mangifera')
print(response.json())


response = requests.get('http://localhost:3000/family/Rosaceae')
print(response.json())

response = requests.get('http://localhost:3000/order/Sapindales')
print(response.json())


###################################################################################
############################# Delete Request #######################################
###################################################################################
deleting = requests.delete(f'http://localhost:3000/{id_to_delete}',params={'apiKey':'codepannustudent'})
print(deleting.json())