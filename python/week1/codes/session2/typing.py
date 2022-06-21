## Typing can help with dynamic code analysis in an IDE like vscode
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

print(get_full_name("john", 2)) ## this will raise error but vscode doesn't warn

def get_full_name_v1(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name_v1("john", "doe"))

print(get_full_name_v1("john", 3)) ## dynamic code analysis, vscode gives warning

def get_name_with_age_v2(name: str, age: int):
    name_with_age = name + " is this old: " + age ## dynamic checks
    return name_with_age

def get_name_with_age_v3(name: str, age: int):
    name_with_age = name + " is this old: " + str(age) ## dynamic checks
    return name_with_age

