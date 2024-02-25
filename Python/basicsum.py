
        # Main function
def main():

    print("\nEnter Two Value Below\n");
        # Taking input from the user
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
        # Function to add two numbers
    def add_numbers(a, b):
        return a +b 
        # Adding the numbers
    result = add_numbers(a, b)
        # Displaying the result
    print("\nResult for Addition of the value:\n\nwhere", ("A is"),[a], "and", ("B is"),[b], "\nand the result C", "is:", result)

    print("\nJajakallah Khair for using this program")
    
if __name__ == "__main__":
    main()