def main():
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure.")
    road = input("You're at a cross road.Where do you wnat to go? Type 'left' or 'right'. ").lower()
    if road == "left":
        decision = input("You come to a lake. There is an island in the middle of the lake. \nType 'wait' to wait for a boat. Type 'swim' to swim across : ").lower()
        if decision == "wait":
            door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? : ").lower()
            if door == "yellow":
                print("You found the treasure. You Win The Game!!!")
            elif door == "red":
                print("You have entered the room of fire. Game Over!")
            elif door == "blue":
                print("You have entered the room of beast. Game Over!")
            else:
                print("Game over!")
        else:
            print("You are drown. Game Over!")
            
    else:
        print("You fell into a hole. Game Over!")
    
    
main()