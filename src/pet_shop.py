# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dict):
    return pet_shop_dict["name"]

def get_total_cash(pet_shop_dict):
    return pet_shop_dict["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_dict, cash):
    pet_shop_dict["admin"]["total_cash"] = pet_shop_dict["admin"]["total_cash"] + cash

def get_pets_sold(pet_shop_dict):
    return pet_shop_dict["admin"]["pets_sold"] 
    
def increase_pets_sold(pet_shop_dict,change_in_pets_sold):
    pet_shop_dict["admin"]["pets_sold"]  = pet_shop_dict["admin"]["pets_sold"]  + change_in_pets_sold

def get_stock_count(pet_shop_dict):
    return len(pet_shop_dict["pets"])

def get_pets_by_breed(pet_shop_dict, breed_to_find):
    # returns a list of pets that match this breed
    found_pets = []
    for pet in pet_shop_dict["pets"]:
        if pet["breed"] == breed_to_find:
            found_pets.append(pet)
    return found_pets

def find_pet_by_name(pet_shop_dict, name_to_search):
    # returns the dictionary relating a pet with this name
    
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == name_to_search:
            return(pet)
    # return "pet not found"

def remove_pet_by_name(pet_shop_dict, pet_name_to_delete):
    # remove from the list of pets the pet whose name matches pet_name_to_delete
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == pet_name_to_delete:
            pet_shop_dict["pets"].remove(pet)

def add_pet_to_stock(pet_shop_dict, pet_to_add):
    pet_shop_dict["pets"].append(pet_to_add)


def get_customer_cash(customer):
    # get return the amount of cash this customer has
    return customer["cash"]

def remove_customer_cash(customer, cash_change):
    customer["cash"]  = customer["cash"]  - cash_change

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    # returns a Boolean on whether or not this customer can afford to buy this pet
    return customer["cash"] >= pet["price"]


def sell_pet_to_customer(pet_shop_dict, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        remove_pet_by_name(pet_shop_dict, pet["name"])
        add_or_remove_cash(pet_shop_dict, pet["price"])
        increase_pets_sold(pet_shop_dict,1)

