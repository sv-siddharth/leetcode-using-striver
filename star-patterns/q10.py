def pattern(N):
    # This is the outer loop which will loop for the rows.
    for i in range(1,2*N):
        
        stars = i
        if(i >N):
            stars = 2*N - i
        # For printing the spaces before stars in each row
        for j in range(stars):
            print("*", end='')
            

        # Move to the next line after printing each row
        print()



def main():
  # Here, we have taken the value of N as 5.
  # We can also take input from the user.
  N = 5

  pattern(N)

if __name__ == "__main__":
  main()
