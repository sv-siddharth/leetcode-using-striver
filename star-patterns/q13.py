def pattern(N):
        
    num = 0
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        
        # For printing the numbers in each row
        for j in range(i+1):
            num=num+1
            print(num, end='')
        # Move to the next line after printing each row
        print()



def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 3

  pattern(N)

if __name__ == "__main__":
  main()
