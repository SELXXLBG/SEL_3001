nbm_de_notes = int (10)
notes = []

for i in range(10) :
    note = float(input("met une de tes moyenne de matière (sur 20) n'importe laquelle : "))
    notes.append(note)
moyenne_gnrl = sum(notes) / nbm_de_notes

print(f" ta moyenne générale est donc de {moyenne_gnrl: .2f14} ! ")
