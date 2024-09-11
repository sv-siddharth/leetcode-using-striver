def pattern1(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        # For printing the spaces before stars in each row
        for j in range(i):
            print(' ', end='')

        # For printing the stars in each row
        for j in range(2*N - (2*i +1)):
            print('*', end='')

        # For printing the spaces after the stars in each row
        for j in range(i):
            print(' ', end='')

        # Move to the next line after printing each row
        print()


def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 5

  pattern1(N)

if __name__ == "__main__":
  main()
