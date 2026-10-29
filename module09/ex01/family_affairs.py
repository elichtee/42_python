#!/opt/pyenv/shims/python

def find_the_redheads(family):
    redheads = filter(lambda name: family[name] == "red", family)
    return list(redheads)

family = {
    "jean": "red",
    "marc": "blond",
    "sarah": "red",
    "laura": "brown",
}

print(find_the_redheads(family))