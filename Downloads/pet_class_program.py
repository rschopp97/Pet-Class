import petclass

def main():
    name = input("Please enter the pet's name:")

    animal_type = input("Please enter the pet's animal type:")

    age = input("Please enter the pet's age:")

    pet_info = petclass.Pet(name, animal_type, age)

    print("Here is the pet information that you entered:")
    print("Name:", pet_info.get_name())
    print("Animal Type:", pet_info.get_animal_type())
    print("Age:", pet_info.get_age())

main()