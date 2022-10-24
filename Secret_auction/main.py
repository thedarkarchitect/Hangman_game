from art import logo

print(logo)
bid_log = []

print("Welcome to the secret auction program.")

def add_log():
    bid_per_person = {}
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bid_per_person["name"] = name
    bid_per_person["bid"] = bid

    bid_log.append(bid_per_person)

def checker():
    counter = 0

    for i in bid_log:
        if i["bid"] > counter:
            counter = i["bid"] 
            name = i["name"]
    print(f"The winner is {name} with a bid of {counter}")

is_true  = True
add_log()

while is_true:
    
    if input("Are there any other bidder? 'yes' or 'no'") == "yes":
        add_log()
    else:
        print(bid_log)
        checker()
        is_true = False

