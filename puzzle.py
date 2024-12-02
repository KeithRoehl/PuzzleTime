import random

def alien_loop():
    while True:
        code = random.choice([
            "x = 5",
            "y = x + 2",
            "print('Alien server running...')",
            "z = y * 10"
        ])
        exec(code)

# Uncomment this to start the chaos!
# alien_loop()
