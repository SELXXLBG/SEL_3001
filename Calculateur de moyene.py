nbm_de_notes = 11
notes = []

for i in range (nbm_de_notes) :
    note = float(input("met une de tes moyenne de matière (sur 20) n'importe laquelle : "))
    
    notes.append(note)
moyenne_gnrl = sum(notes) / nbm_de_notes

print(f" ta moyenne générale est donc de {moyenne_gnrl} ! ")
