#!/opt/pyenv/shims/python

def array_of_names(names):
    full_names = []
    for first_name, last_name in names.items():
        full_names.append(f"{first_name.capitalize()} {last_name.capitalize()}")
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier",
}

print(array_of_names(persons))
