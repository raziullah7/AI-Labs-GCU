# fizz_buzz_game
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

# main function
rounds = int(input("Enter the number of rounds to play: "))
fizz_buzz_game(rounds)
