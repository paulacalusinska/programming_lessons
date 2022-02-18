grades = {
    "class": {
        "students": [{
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }, {
             "name": "Ana",
             "marks": {
                "english": 95,
                "history": 90
             }
        }]
    }
}
name = grades["class"]["students"][0]["name"]
print(name)
mark_history = grades["class"]["students"][0]["marks"]["history"]
print(mark_history)
all_history_marks = grades["class"]["students"][1]["marks"]["history"]

students = grades["class"]["students"]
for student in students:
    name = student["name"]
    mark_history = student["marks"]["history"]
    print(name, mark_history)

# wypisać oceny z przedmiotu fiz dla wszystkich studentów jezeli student nie otrzymal oceny z tego przedmiotu
# to wypisać none (użyć do tego met get z obiektu dict)

students = grades["class"]["students"]
for student in students:
    name = student["name"]
    mark_physics = student["marks"].get("physics")
    print(name, mark_physics)