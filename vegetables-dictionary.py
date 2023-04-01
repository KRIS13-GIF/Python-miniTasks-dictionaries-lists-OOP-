"""A menu of vegetable and price {key:value}
A menu which : 1. Display all the list of vegetables which are stored in dictionary
            2. Change the price of the vegetable
            3. Add a new vegetable
            4. Delete an existing
            5. save to a file in txt when exists
            6. Pickle
            7. Each time that we start the program unpickle it """


import  pickle




input_file=open("fruits.txt", "wb")
vegetables={"banana":50.0, "mango":70.0, "ananas":120.0}
pickle.dump(vegetables,input_file)
print("Done")
input_file.close()


    # Adding a new fruit
def add_fruit():
        input_file=open("fruits.txt", "ab")
        fruit = input("Enter a new fruit:  ")
        if fruit in vegetables.keys():
            print("This fruit exists!")
        else:
            price = float(input("Enter the price for this fruit: "))
            vegetables[fruit] = price
            pickle.dump(vegetables, input_file)
            print(vegetables.items())


def delete_fruit():
        input_file=open("fruits.txt", "wb")
        # Deleting a fruit from the dictionary
        delete_fruit = input("Which fruit are you going to delete: ")
        if delete_fruit in vegetables.keys():
            vegetables.pop(delete_fruit)
            pickle.dump(vegetables,input_file)
            print("Fruit deleted")
        else:
            print("This fruit is not found in the list")
            print(vegetables.items())


def change_price():
        input_file = open("fruits.txt", "wb")
        # change the price of the vegetable
        change_price_name = input("Enter the name of the fruit you are going to change price: ")

        if change_price_name in vegetables.keys():
            price = float(input("Enter the price of the fruit: "))
            vegetables[change_price_name] = price
            print("Price updated !")
            pickle.dump(vegetables, input_file)
            print(vegetables.items())
        else:
            print("Fruit not found ")

def main():
            i=int(input("Enter 1 to show the fruits, 2 to add fruits, 3 to delete fruits, 4 to change price, 0 to exit: "))
            while i!=0:
                if i==1:
                    input2_file=open("fruits.txt", "rb")
                    vegetables=pickle.load(input2_file)
                    print(vegetables)
                    input2_file.close()

                elif i==2:
                    add_fruit()

                elif i==3:
                    delete_fruit()

                elif i==4:
                    change_price()

                elif i==0:
                    print("Value not in range 1~4")
                    exit()
                i = int(input(
                "Enter 1 to show the fruits, 2 to add fruits, 3 to delete fruits, 4 to change price, 0 to exit: "))


main()

#Each time you create an operation , we do need to open dhe file and close it for each method
