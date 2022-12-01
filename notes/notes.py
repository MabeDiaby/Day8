# Functions with inputs
def greet():
    name = input("What is your name?\n")
    print(f"Hello {name} how are you?")
    plan = input("What are your plans for the day?\n")
    print(f"I love {plan}! sounds fun")
    print("Enjoy, talk to you later")
greet()

# Functions with params
def greet_with_name(names):
    print(f"Hello {names}")
    print(f"How do you do {names}")
greet_with_name("David")

# Functions with multiple params
def greet_with(names, location):
    print(f"Hello {names}")
    print(f"What is it like in {location}")
greet_with("Betsy", "Boston")
# Positional Arguments
greet_with("Neverland", "Peter")
# Keyword Arguments
greet_with(location="Neverland", names ="Peter")