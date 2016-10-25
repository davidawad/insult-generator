import random 
import os
import yaml
import json

config = yaml.load(open(os.path.dirname(__file__) + 'insults.yml'))

pref = 'Thou'

# algorithm simply makes a random choice from three different columns and concatenates them. 

col1 = random.choice(config['column1'])

col2 = random.choice(config['column2'])

col3 = random.choice(config['column3'])

# print generated insult for the 'user' 
print( pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '.' )

