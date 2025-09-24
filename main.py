import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            # if we didn’t break, that means all symbols in this line are the same
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols += [symbol] * count

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        row_symbols = []
        for col in columns:
            row_symbols.append(col[row])
        print(" | ".join(row_symbols))


def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid input. Please enter a numeric value.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1 – {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a numeric value.")


def get_bet():
    while True:
        amount = input(f"Enter betting amount between ${MIN_BET} and ${MAX_BET}: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a numeric value.")


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        print(f"Current balance: ${balance}")
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount. Your current balance is ${balance}.")
            continue

        print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}.")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)

        winnings, winning_lines = get_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}.")
        if winning_lines:
            print("You won on line(s):", *winning_lines)
        else:
            print("No winning lines.")

        balance = balance - total_bet + winnings

        print(f"Your balance is now ${balance}.")

        if balance <= 0:
            print("You ran out of money! Game over.")
            break

        play_again = input("Press Enter to play again (or type ‘q’ to quit): ")
        if play_again.lower() == "q":
            print(f"You left with ${balance}. Thanks for playing!")
            break


if __name__ == "__main__":
    main()
