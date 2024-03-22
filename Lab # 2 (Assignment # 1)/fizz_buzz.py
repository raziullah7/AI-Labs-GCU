                # fizz_buzz_game

# --------------------------------------------------------
# my implementation according to my output understanding
def fizz_buzz(rounds):
    for i in range(1, rounds + 1):
        # strating round
        print('\n----------------------------------')
        print(f'Round: {i}-th')
        str = input("Enter the next sequence: ")
        
        # casting to string if possible, else its a number
        try:
            theInputNum = int(str)
        except:
            theInputStr = str
        
        # checking if the player's answer if correct
        if i == theInputNum and not(i % 3 == 0 or i % 5 == 0):
            print('Correct sequence entered: ', i)
            continue
        elif i % 3 == 0 and theInputStr.lower() == 'fizz':
            print('Correct sequence entered: fizz')
            continue
        elif i % 5 == 0 and theInputStr.lower() == 'buzz':
            print('Correct sequence entered: buzz')
            continue
        elif i % 3 == 0 and i % 5 == 0 and theInputStr.lower() == 'fizzbuzz':
            print('Correct sequence entered: fizzbuzz')
            continue
        else:
            print("User has entered the wrong sequence, player eliminated!")
            break


# --------------------------------------------------------
# implementation to match the sample output
def fizz_buzz_game(rounds):
    players = ["Player 1", "Player 2"]
    current_player = 0

    for i in range(1, rounds + 1):
        number = i
        message = ""

        if number % 3 == 0:
            message += "Fizz"
        if number % 5 == 0:
            message += "Buzz"
        if not message:
            message = str(number)

        print(players[current_player] + " says:", message)

        # Check if player says the right thing
        if message == "Fizz" and number % 3 != 0 or \
           message == "Buzz" and number % 5 != 0 or \
           message == "FizzBuzz" and (number % 3 != 0 or number % 5 != 0):
            print(players[current_player] + " said the wrong thing and is eliminated!")
            players.pop(current_player)
            if current_player >= len(players):
                current_player = 0

        if len(players) == 0:
            print("No more players remaining!")
            break

        current_player = (current_player + 1) % len(players)


# --------------------------------------------------------
                # main function
rounds = int(input("Enter the number of rounds to play: "))
# fizz_buzz_game(rounds)
fizz_buzz(rounds)
