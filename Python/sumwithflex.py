def main():

    print("\n\nThis Program is Created By\n\n-----------------------------------------------------\n\nMd. Mahfuzur Rahman\nDepartment of Mechanical Technology\n5th Semester | 2nd Shift | Group: A | Roll: 188335\nRajshahi Polytechnic Institute\n\n-----------------------------------------------------\n\nProgram Name: \nAddition of Two Value Program Using Python Programming Language\n\nEnter Two Value Below\n\n---------------------------\n")
    
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))

    def add_numbers(a, b):
        return a + b
    result = add_numbers(a, b)

    print("\nResult for Addition of the value:\n\nwhere", ("A is"),[a], "and", ("B is"),[b], "\nand the result C", "is:", result)

    print("\nJajakallah Khair for using this program")
    
if __name__ == "__main__":
    main()