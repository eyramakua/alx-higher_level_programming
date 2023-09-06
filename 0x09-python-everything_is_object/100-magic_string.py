def magic_string():
    magic_string.number = getattr(magic_string, 'number', 0) + 1
    return "BestSchool" + (", BestScool" * (magic_string.number - 1))
