from pyscript import document, display

class ClassMate():
    def __init__(self, name, section, fav_sub):
        self.name = name
        self.section = section
        self.fav_sub = fav_sub

    def introduce(self):
        return f"Hello! I'm {self.name} from {self.section}. My favorite subject is {self.fav_sub}"

students = [
    {"name":"Allen Daradal", "section":"Topaz", "fav_sub":"ICT"},
    {"name": "Sean Matthew Cotioco", "section":"Topaz", "fav_sub":"ICT"},
    {"name":"Sang-heon Choi", "section":"Topaz", "fav_sub":"Science"},
    {"name":"Ramon Niccolo Santos", 'section':"Topaz", "fav_sub":"Social Studies"},
    {"name":"Beatrix Vilale", "section":"Topaz", "fav_sub":"Social Studies"}
]


def show_list(e):
    document.getElementById("output").innerHTML = ""
    for stud in students:
        new_classmate = ClassMate(**stud)

        display(new_classmate.introduce(), target="output")


def add_item(e):
    name = document.getElementById("name").value
    sect =document.getElementById("sect").value
    sub = document.getElementById("sub").value
    students.append(
        {
            "name":name,
            "section":sect,
            "fav_sub":sub
        }
    )
    document.getElementById("name").value = ""
    document.getElementById("sect").value = ""
    document.getElementById("sub").value  = ""

    