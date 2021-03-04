from server import bot_server

print("(c) 2020 using Python 3.8 https://www.python.org")
print("Multiplicative Persistence Number Tester (Auto) by DepthStrider\n")
print("  - Multiplicative persistence is where you multiply all of the digits of an interger together, and you repeat that process until you get a one digit number.")
print("The list of current smallest numbers that return incremental steps:")
print("  - 10 - persistence of 1")
print("  - 25 - persistence of 2")
print("  - 39 - persistence of 3")
print("  - 77 - persistence of 4")
print("  - 679 - persistence of 5")
print("  - 6788 - persistence of 6")
print("  - 68889 - persistence of 7")
print("  - 2677889 - persistence of 8")
print("  - 26888999 - persistence of 9")
print("  - 3778888999 - persistence of 10")
print("  - 277777788888899 - persistence of 11\n")

serverstart = str(input("Do you want to start the web server for this repl? y/n ")).lower().strip()
if serverstart == "y":
  bot_server()
else:
  print("")

command = int(input("What method do you want to use? 1-auto 2-manual "))
if command == 1:
  steps = 0

  goal = int(input('What step amount do you want to find? '))
  startnumber = int(input("What number do you want to start testing at? "))
  c = startnumber
  d = startnumber
  while steps < goal:
    product = 1
    steps = 0
    print(c)
    while c > 9:
      for digit in range(0, len(str(c))):
          product *= int(str(c)[digit])
      print(product)
      steps += 1
      c = product
      product = 1
    print("Steps:", steps)
    print("")
    c *= 0
    d += 1
    c += d
  print(" ** ALERT **   NUMBER FOUND!!!   ** ALERT **")
  dontpause = 1
  blankvar = 0
  while dontpause == 1:
    blankvar += 1
elif command == 2:

  print("Type per(yournumber) to evaluate the number of your choice.")
  
  errormsg = ('Not enough digits in your interger.  Please try again.')
  
  def per(n, steps=0):
    if len(str(n)) == 1:
        print(n)
        print("Total Steps: " + str(steps))
        return (errormsg)

    steps += 1
    digits = [int(i) for i in str(n)]

    result = 1
    for j in digits:
        result *= j
    print(result)
    per(result, steps)
