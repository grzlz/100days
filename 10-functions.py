# Functions with outputs

def format_name(f_name, l_name):
    f_name = f_name.lower()
    l_name = l_name.lower()

    f_name = [i for i in f_name]
    l_name = [i for i in l_name]

    f_name[0] = f_name[0].upper()
    l_name[0] = l_name[0].upper()

    f_name = "".join(f_name)
    l_name = "".join(l_name)

    name = f"{f_name} {l_name}"
    return name

print(format_name("JUANITO", "JONES"))

