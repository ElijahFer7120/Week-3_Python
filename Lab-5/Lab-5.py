"""
Week 3 assignment 2

Purpose:
Show that a dictionary stores values by key.

developer notes:
this is the list of items i have in my thomas collections 
"""

diecast_engines = [
    {"name": "thomas", "status": "owned"},
    {"name": "edward", "status": "not_owned"},
    {"name": "henry", "status": "owned"},
    {"name": "gordon", "status": "owned"},
    {"name": "james", "status": "owned"},
    {"name": "percy", "status": "not_owned"},
    {"name": "toby", "status": "not_owned"},
    {"name": "duck", "status": "not_owned"},
    {"name": "diesel", "status": "not_owned"},
    {"name": "oliver", "status": "owned"},
]

for engine in diecast_engines:
    if engine["status"] == "owned":
        status = "owned"
    else:
        status = "not owned"

    print(engine["name"], "is", engine["status"])