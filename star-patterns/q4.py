def pattern1(N):
  # This is the outer loop which will loop for the rows.
  for i in range(N,0):
    # This is the inner loop which here, loops for the columns
    # as we have to print a rectangular pattern.
    for j in range(0,i+1):
      print("*", end="")
    
    # As soon as N stars are printed, we move to the
    # next row and give a line break otherwise all stars
    # would get printed in 1 line.
    print()

def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 5

  pattern1(N)

if __name__ == "__main__":
  main()
