op1 = 0     # Global Variable for candidate 1
op2 = 0     # Global Variable for candidate 2


# Function that counts the votes (Takes a parameter that checks who was voted for)
def count(vote):
    global op1, op2     # Makes the two candidate variables visible
    if vote == 1:       # Checks which candidate was chosen
        op1 += 1        # Increases the vote for candidate 1
    elif vote == 2:     # Checks which candidate was chosen
        op2 += 1        # Increases the vote for candidate 2
    print(op1)          # Prints the votes for candidate 1
    print(op2)          # Prints the votes for candidate 1
