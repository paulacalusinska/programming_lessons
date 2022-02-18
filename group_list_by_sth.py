# z podanych imion i nazwisk znajdź rodziny
# (zakładamy, że rodzina posiada takie same nazwiska i pogrupuj ludzi rodzinami)
def group_by_family(list_of_people):
    families = {}
    for e in list_of_people:
        names = e.split()
        name = names[0]
        surname = names[1]
        if surname not in families:
            families[surname] = [name]
        else:
            family_members = families[surname]
            family_members.append(name)
    return families


list_of_poeple = ["Michał Kochanowski", "Jan Kowalski",  "Marek Kowalski", "Kuba Kochanowski", "Wojtek Kot", "Paweł Kowalski"]
print(group_by_family(list_of_poeple))