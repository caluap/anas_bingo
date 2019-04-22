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
cell_margin = s_w * 0.10


for card in range(n_cards):
    aux_terms = terms.copy()
    random.shuffle(aux_terms)
    if columns % 2 != 0 and free_spaces > 0:
        aux_terms.insert(math.floor(len(terms)/2), 'Espaço Livre')
    for c in range(columns):
        for l in range(columns):
            x = s_w * c + margin_x
            y = s_h * l + margin_y
            
            fill(None)
            stroke(0)
            rect(x, y, s_w, s_h)
            
            i = c * columns + l
            if (c < len(terms)):
                current_term = aux_terms[c * columns + l]
            else:
                current_term = "Termo faltante"
            can_print = False
            fs = 14
            tx = x + cell_margin
            ty = y + cell_margin
            tw = s_w - cell_margin * 2
            th = s_h - cell_margin * 2
            
            while can_print == False and fs > 0:
                font('Helvetica', fs)
                overflow = textOverflow(current_term,(tx, ty, tw, th),align="center")
                if overflow == "":
                    can_print = True
                else:
                    fs = fs - 1
            
            stroke(None)
            fill(0)
            text_width, text_height = textSize(current_term, align="center", width=tw)
            offset_y = (th - text_height) / 2
            textBox(current_term, (tx, ty - offset_y, tw, th), align="center")
                    
        