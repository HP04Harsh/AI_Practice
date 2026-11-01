chai_types = ["Black", "Green", "White", "Earl Grey","kadak", "Masala", "Chamomile", "Jasmine", "Peppermint", "Lemongrass"]

strong_chai = filter(lambda chai: chai=="kadak" or chai=="Masala", chai_types)

print(list(strong_chai))