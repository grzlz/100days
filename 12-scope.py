# Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 3
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")