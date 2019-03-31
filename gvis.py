import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

food_dic={"apple" : 3,
          "burrito" : 5,
          "pudding" : 10,
          "chocolate" : 100,
          "pizza" : 7,
          "cup noodles" : 365,
          "chicken curry" : 2,
          "burrito" : 3,
          "bread" : 30,
          "banana" : 7,
          "pad thai" : 2,
          "sashimi" : 1,
          "peanut butter" : 80,
          "ice-cream" : 7,
          "french fries" : 4,
          "steak" : 4,
          "cripsy fried chicken" : 6,
          "chocolate chip cookies" : 40,
          "cheesecake" : 7,
          "bacon" : 3,
          "cheeseburger" : 8,
          "cheese" : 42,
          "taco" : 3,
          "brownie" : 4,
          "barbecue" : 4,
          "strawberries" : 6,
          "donuts" : 3,
          "pasta" : 2,
          "cake" : 3,
          "waffles" : 90,
          "pancakes" : 180,
          "salmon" : 2,
          "mangoes" : 7,
          "oranges" : 14,
          "raspberries" : 3,          
          }


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    wordls=[]
    
    for text in texts:
        text=text.description.lower().rstrip('\n')
        if text in food_dic:
            wordls.append((text, str(food_dic[text])))
        #wordls.append(text.description.rstrip('\n'))
        #print('\n{}'.format(text.description))

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
        #           for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))
    print('Google vision sucessfully responded...')
    return wordls;
