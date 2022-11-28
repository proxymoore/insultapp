# Author: Darcie Moore
# Date: 10/14/20
#This is a program that insults you!
# Type insultapp.py into the terminal and follow the instructions

from flask import Flask, render_template, request
import random

# The first lists of insults...
column1 = ('artless'
, 'bawdy'
, 'beslubbering'
, 'bootless'
, 'churlish'
, 'cockered'
, 'clouted'
, 'craven'
, 'currish '
, 'dankish '
, 'dissembling '
, 'droning '
, 'errant'
, 'fawning '
, 'fobbing '
, 'froward '
, 'frothy'
, 'gleeking'
, 'goatish '
, 'gorbellied'
, 'impertinent '
, 'infectious'
, 'jarring '
, 'loggerheaded'
, 'lumpish '
, 'mammering '
, 'mangled '
, 'mewling '
, 'paunchy '
, 'pribbling '
, 'puking'
, 'puny'
, 'qualling'
, 'rank'
, 'reeky '
, 'roguish '
, 'ruttish '
, 'saucy '
, 'spleeny '
, 'spongy'
, 'surly '
, 'tottering '
, 'unmuzzled '
, 'vain'
, 'venomed '
, 'villainous'
, 'warped'
, 'wayward '
, 'weedy '
, 'yeasty' )

# The second list of insults...
column2 = ('base-court'
, 'bat-fowling'
, 'beef-witted'
, 'beetle-headed'
, 'boil-brained'
, 'clapper-clawed'
, 'clay-brained'
, 'common-kissing'
, 'crook-pated'
, 'dismal-dreaming'
, 'dizzy-eyed'
, 'doghearted'
, 'dread-bolted'
, 'earth-vexing'
, 'elf-skinned'
, 'fat-kidneyed'
, 'fen-sucked'
, 'flap-mouthed'
, 'fly-bitten'
, 'folly-fallen'
)

# The third this of insults!!
column3 = ('laggard', 'mugwug', 'plebean', 'mudseller', 'Frenchmen', 'scallywag', 'bear welp', 'wagtail'
           )

app = Flask(__name__)

# Telling the browser where to go
@app.route('/')
def index():
    return render_template('index.html')


# Gathering input from the user & outputting using the random generator to complete the personal insult
@app.route('/insult', methods=['POST'])
def insult():
    yourname = str(request.form['yourname'])
    yourage = str(request.form['yourage'])
    return "*GASP* Youd think youd be better than a " + random.choice(column1) + ' ' + random.choice(column2) + ' ' + random.choice(column3) + " at {0}, {1} <br/> <a href=\"/\">Back Home</a>".format(yourage, yourname, random.choice(column1), random.choice(column2), random.choice(column3))


if __name__ == '__main__':
    app.run(debug=True)