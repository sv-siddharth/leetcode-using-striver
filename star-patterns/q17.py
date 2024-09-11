def pattern(N):
    # Outer loop for the number of rows.
    for i in range(N):
        # For printing the spaces before characters.
        for j in range(N - i - 1):
            print(' ', end='')
        
        # For printing the characters.
        ch = 'A'
        _breakpoint = (2 * i + 1) // 2
        for j in range(1, 2 * i + 2):
            print(ch, end='')
            if j <= _breakpoint:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)
        
        # For printing the spaces after characters.
        for j in range(N - i - 1):
            print(' ', end='')
        
        # Move to the next line after printing each row.
        print()



def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 3

  pattern(N)

if __name__ == "__main__":
  main()
