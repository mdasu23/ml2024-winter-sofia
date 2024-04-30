def main():

  N = int(input("Enter the total number of elements (N): "))

  numbers = []
  for i in range(N):
      num = int(input(f"Enter number {i+1}: "))
      numbers.append(num)

  X = int(input("Enter the number to search for (X): "))

  if X in numbers:
      index = numbers.index(X) + 1 
      print(f"The index of {X} is: {index}")
  else:
      print(f"{X} was not found among the provided numbers. Output: -1")


if __name__ == "__main__":
  main()
