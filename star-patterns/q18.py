def pattern(N):
    # Outer loop for the number of rows.
        # Outer loop for the number of rows.
    for i in range(N):
        # Inner loop for printing the alphabets from
        # 'A' + N - 1 - i (i is row number) to 'A' + N - 1 (E in this case).
        for ch in range(ord('A') + N - 1 - i, ord('A') + N):
            print(chr(ch), end=' ')
        
        # Move to the next line after printing each row.
        print()
        

def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.1
  N = 3

  pattern(N)

if __name__ == "__main__":
  main()                          
   