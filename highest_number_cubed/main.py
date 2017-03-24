"""This is the entry point of the program."""


def highest_number_cubed(limit):
    val = 0
    for num in range(limit):
        if num**3 <= limit:
            val = num
    
    return val
            

        
