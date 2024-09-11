def pattern(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        
        start = 1

        if(i % 2 == 0):
            start = 1
        else:
            start = 0

        for j in range(i+1):
          print(start, end='')
          start = 1 - start

        # Move to the next line after printing each row
        print()



def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 3

  pattern(N)

if __name__ == "__main__":
  main()
