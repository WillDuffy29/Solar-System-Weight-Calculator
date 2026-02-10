# Solar System Weight Calculator 🌍

print("Welcome to the Solar System Weight Converter!")

EarthWeight = float(input("What is your weight on earth (in KG)?: "))

print("Our available planets are:")
print("  1. Mercury")
print("  2. Venus")
print("  3. Mars")
print("  4. Jupiter")
print("  5. Saturn")
print("  6. Uranus")
print("  7. Neptune")

# Destination

Destination = int(input("Where would you like to go?: "))

if Destination == 1:           # Variable assignment for destintion choice
  Destination = 1              # This had to be done as lines 8-14 are simply strings and not integers, so the variable assignment is necessary for the weight calculation later on.
elif Destination == 2:
  Destination = 2
elif Destination == 3:
  Destination = 3
elif Destination == 4:
  Destination = 4
elif Destination == 5:
  Destination = 5
elif Destination == 6:
  Destination = 6
elif Destination == 7:
  Destination = 7
else:
  print("Invalid planet number")

# Destination Weight

if Destination == 1:
  EarthWeight = EarthWeight * 0.38
  print("Your destination is Mercury! Your weight will be: ")
  print(EarthWeight)
elif Destination == 2:
  EarthWeight = EarthWeight * 0.91
  print("Your destination is Venus! Your weight will be: ")
  print(EarthWeight)
elif Destination == 3:
  EarthWeight = EarthWeight * 0.38
  print("Your destination is Mars! Your weight will be: ")
  print(EarthWeight)
elif Destination == 4:
  EarthWeight = EarthWeight * 2.53
  print("Your destination is Jupiter! Your weight will be: ")
  print(EarthWeight)
elif Destination == 5:
  EarthWeight = EarthWeight * 1.07
  print("Your destination is Saturn! Your weight will be: ")
  print(EarthWeight)
elif Destination == 6:
  EarthWeight = EarthWeight * 0.89
  print("Your destination is Uranus! Your weight will be: ")
  print(EarthWeight)
elif Destination == 7:
  EarthWeight = EarthWeight * 1.14
  print("Your destination is Neptune! Your weight will be: ")
  print(EarthWeight)