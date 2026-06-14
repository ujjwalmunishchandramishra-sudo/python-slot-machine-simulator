import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
            
    


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
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
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row],end = " | ")
            else:
                print(column[row],end = "")
        print()

def deposit():  # definining a fuction for  depositing money into the slot machine
    while True:
        amount  = input("what would you like to deposit? $")# asking to enter the amount to be deposited
        if amount.isdigit():# if amount is digit means 10,100,1000 not negative 
            amount = int(amount)# it is to be converted into int form
            if amount > 0:# it is defined to ensure that amount entered is not 0
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")# this else is used in case the amount entered is not a number

    return amount
def get_number_of_lines():
     while True:
        lines  = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")?")# asking to enter the amount to be deposited
        if lines.isdigit():# if amount is digit means 10,100,1000 not negative 
            lines = int(lines)# it is to be converted into int form
            if 1 <= lines <= MAX_LINES:# it is defined to ensure that amount entered is not 0
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a number.")# this else is used in case the amount entered is not a number

     return lines
def get_bet():
    while True:
        amount  = input("what would you like to bet on each line? $")# asking to enter the amount to be deposited
        if amount.isdigit():# if amount is digit means 10,100,1000 not negative 
            amount = int(amount)# it is to be converted into int form
            if MIN_BET <= amount <= MAX_BET:# it is defined to ensure that amount entered is not 0
                break
            else:
                print(f"Amount must between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")# this else is used in case the amount entered is not a number

    return amount

def main():
    balance = deposit()# it is used to call the function
    lines = get_number_of_lines()
    while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
        print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
      else:
        break
    print(f"you are betting $ {bet} on {lines} lines. Total bet is equal to: ${total_bet} ")

    slots = get_slot_machine_spin( ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings , winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"you won $ {winnings}.")
    print(f"You won on lines",*winning_lines)



def spin(balance):
    lines = get_number_of_lines()
    while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
        print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
      else:
        break
    print(f"you are betting $ {bet} on {lines} lines. Total bet is equal to: ${total_bet} ")

    slots = get_slot_machine_spin( ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings , winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"you won $ {winnings}.")
    print(f"You won on lines",*winning_lines)
    return winnings - total_bet




def main():
    balance = deposit()
    while  True:
        print(f"current balance is $ {balance}")
        answer = input("Press eneter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

    #print(balance,lines)

main()

    