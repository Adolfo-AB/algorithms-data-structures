animals = [
    {'class': 'amphibia', 'species': 'Bombina bombina', 'name': 'European fire-bellied toad'},
    {'class': 'amphibia', 'species': 'Atelopus zeteki', 'name': 'Panamanian golden frog'},
    {'class': 'amphibia', 'species': 'Litoria tyleri', 'name': 'Tyler\'s tree frog'}
]

sorted_animals = sorted(animals, key=lambda animal: animal['name'], reverse=True)
print(sorted_animals)