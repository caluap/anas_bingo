import math 
import random

terms = ['Cidadão', 
    'Direito Político', 
    'Direito social', 
    'Direito civil', 
    'Direitos individuais', 
    'Direito coletivo', 
    'Constituição', 
    'Constituição cidadã',
    'Estatuto da Criança e Adolescente'
    ]
    
size(595,842/2)    


columns = math.ceil(math.sqrt(len(terms)))
# for the middle cell to be a “free space” there needs to be at least one word
# less than cells! (and this only works when there are an odd number of columns)
free_spaces = columns * columns - len(terms)

margin = 50
if (width() < height()):
    small = width()
else:
    small = height()
    
s_w = s_h = (small - margin * 2) / columns
margin_x = (width() - s_w * columns) / 2
margin_y = (height() - s_h * columns) / 2

n_cards = 1

fill(None)
stroke(0)

for card in range(n_cards):
    aux_terms = terms.copy()
    random.shuffle(aux_terms)
    if columns % 2 != 0 and free_spaces > 0:
        aux_terms.insert(math.floor(len(terms)/2), 'Espaço Livre')
    for c in range(columns):
        for l in range(columns):
            x = s_w * c + margin_x
            y = s_h * l + margin_y
            rect(x, y, s_w, s_h)
            i = c * columns + l
            if (c < len(terms)):
                text = str(i) + ' ' + aux_terms[c * columns + l]
            else:
                text = "Termo faltante"
        