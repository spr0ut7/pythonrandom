import random

def get_random_number():
    try:
        # Prompt user for upper limit
        upper_limit = int(input("Enter an upper limit (whole number greater than 2): "))
        
        # Validate input
        if upper_limit <= 2:
            print("Error: Please enter a number greater than 2.")
            return
        
        # Generate random number
        random_num = random.randint(1, upper_limit)
        
        # Output result
        print(f"Your random number is: {random_num}")
        
    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    get_random_number()