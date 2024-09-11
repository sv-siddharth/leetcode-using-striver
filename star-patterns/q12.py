def pattern(N):

  # Initial number of spaces in row 1.
  spaces = 2 * (N - 1)
  
    # This is the outer loop which will loop for the rows.
  for i in range(1, N + 1):
          
          # For printing numbers in each row (ascending part)
          for j in range(1, i + 1):
              print(j, end='')
          
          # For printing spaces in each row
          for j in range(spaces):
              print(' ', end='')
          
          # For printing numbers in each row (descending part)
          for j in range(i, 0, -1):
              print(j, end='')
          
          # Move to the next line after printing each row
          print()
          
          # After each iteration, number of spaces decrease by 2
          spaces -= 2


def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 3

  pattern(N)

if __name__ == "__main__":
  main()
