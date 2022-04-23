grades = {
    "class": {
        "students": [{
            "name": "Mike",
            "subjects": {
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
# name = grades["class"]["students"][0]["name"]
# print(name)
# mark_history = grades["class"]["students"][0]["marks"]["history"]
# print(mark_history)
# all_history_marks = grades["class"]["students"][1]["marks"]["history"]

# students = grades["class"]["students"]
# for student in students:
#     name = student["name"]
#     mark_history = student["marks"]["history"]
#     print(name, mark_history)

# wypisać oceny z przedmiotu fiz dla wszystkich studentów jezeli student nie otrzymal oceny z tego przedmiotu
# to wypisać none (użyć do tego met get z obiektu dict)

def get_marks_from_subject(grades, subject):
    students = grades["class"]["students"]
    marks_from_subjects = {}
    for student in students:
        name = student["name"]
        marks = student.get("marks", {})
        mark = marks.get(subject, None)
        marks_from_subjects[name] = mark
    return marks_from_subjects

print(get_marks_from_subject(grades, "history"))