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
    'Estatuto da Criança e Adolescente',
    'Direitos individuais', 
    'Direito coletivo', 
    'Constituição', 
    'Constituição cidadã',
    'Estatuto da Criança e Adolescente',
    'Direitos individuais', 
    'Direito coletivo', 
    'Constituição', 
    'Constituição cidadã'
    ]
    
h = 842/2
w = 595

size('A4')


columns = math.ceil(math.sqrt(len(terms)))
# for the middle cell to be a “free space” there needs to be at least one word
# less than cells! (and this only works when there are an odd number of columns)
free_spaces = columns * columns - len(terms)

margin = 30
if w < h:
    small = w
else:
    small = h
    
s_w = s_h = (small - margin * 2) / columns
margin_x = (w - s_w * columns) / 2
margin_y = (h - s_h * columns) / 2

n_cards = 10
cell_margin = s_w * 0.05


for card in range(n_cards):
    if card % 2 == 0:
        offset_y = height() / 2
    else:
        offset_y = 0
    aux_terms = terms.copy()
    random.shuffle(aux_terms)
    if columns % 2 != 0 and free_spaces > 0:
        i_term = round(columns * columns / 2)
        aux_terms.insert(i_term, 'Espaço Livre')
    for c in range(columns):
        for l in range(columns):
            x = s_w * c + margin_x
            y = s_h * l + margin_y + offset_y
                        
            fill(None)
            stroke(0)
            rect(x, y, s_w, s_h)
            
            i = c * columns + l
            if i < len(terms):
                current_term = aux_terms[i]
            else:
                current_term = "Termo faltante"
                
            can_print = False
            fs = 11
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
            cell_offset_y = (th - text_height) / 2
            textBox(current_term, (tx, ty - cell_offset_y, tw, th), align="center")

    if card > 0 and card % 2 != 0 and card < n_cards-1:
        newPage()