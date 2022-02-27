import requests


quotes = [
{"quote":"You should be motivated","category":"Motivation","author":"anonymous","__v":0},
{"quote":"The best is yet to be.","category":"Positivity","author":"anonymous","__v":0},
{"quote":"Try to be a rainbow in someone's cloud.","category":"Positivity","author":"anonymous","__v":0},
{"quote":"Do good and good will come to you.","category":"Positivity","author":"anonymous","__v":0},
{"quote":"A positive mindset brings positive things.","category":"Positivity","author":"Nawf","__v":0},
{"quote":"Positivity always wins","category":"Positivity","author":"Nawf","__v":0},
{"quote":"When things go wrong, don't go with them.","category":"Positivity","author":"Nawf","__v":0},
{"quote":"Live life to the fullest and focus on the positive.","category":"Positivity","author":"Nawf","__v":0},
{"quote":"Keep looking up","category":"Positivity","author":"Nawf","__v":0},
{"quote":"Our greatest glory is not in never falling, but in rising every time we fall","category":"Motivation","author":"Confucius.","__v":0},
{"quote":"Magic is believing in yourself.","category":"Motivation","author":"anonymus","__v":0},
{"quote":"All our dreams can come true, if we have the courage to pursue them","category":"Motivation","author":"Walt_Disney","__v":0},
{"quote":"Education is the most powerful weapon which you can use to change the world","category":"Education","author":"Nelson Mandela","__v":0},
{"quote":"Develop a passion for learning. If you do, you wil never cease to grow","category":"Education","author":"j.DAngelo","__v":0}
{"quote":"Knowledge is power. Information is liberating. Education is the premise of progress, in every society, in every family","category":"Education","author":" Kofi Anna","__v":0},
{"quote":"A person who won’t read has no advantage over one who can’t read.","category":"Education","author":"Mark Twain","__v":0},
{"quote":"Education is the ability to listen to almost anything without losing your temper or your self-confidence.","category":"Education","author":"Robert Frost","__v":0}
]

for quote in quotes:
    response = requests.post('http://localhost:3000/',
        params={'apiKey':'codepannustudent'},
        data={
        'quote':quote['quote'],
        'category':quote['category'],
        'author':quote['author']
    })
    print(response.json())
response = requests.get('http://localhost:3000/')

#print(response.json())
response = requests.get('http://localhost:3000/category/positivity')
#print(response.json())
response = requests.get('http://localhost:3000/random')
#print(response.json())
response = requests.get('http://localhost:3000/author/Nawf')
print('Quotes of nawf are:')
print(response.json())

id_to_delete = '6211f387031787f9757ba34f'#use the id to delete
deleting = requests.delete(f'http://localhost:3000/{id_to_delete}',params={'apiKey':'codepannustudent'})
print(deleting.json())