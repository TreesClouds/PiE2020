

# Team 35 Coding Challenges - "Oven Password"


# Problem 1
def convert_time(num):
    hour = num // 100
    minute = num % 100
    if hour > 12:
        hour -= 12
    return [hour, minute]


# Testing problem 1
print("Testing Convert Time")
print(convert_time(1738))  # [5, 38]
print(convert_time(0))  # [0, 0]
print(convert_time(2359))  # [11,59]
print("\n")


# Problem 2
def eta(num):
    return (((num[0] - 5)**2 + (num[1] - 14)**2)**(1/2)) // 3


# Testing problem 2
print("Testing eta")
print(eta([0, 0]))  # 4
print(eta([5, 38]))  # 8
print(eta([40, 40]))  # 14
print("\n")


# Problem 3
def wacky_numbers(num):
    for i in range(20):
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 5 + 3
    return num


# Testing problem 3
print("Testing wacky_numbers")
print(wacky_numbers(10))  # 1249
print(wacky_numbers(0))  # 0
print(wacky_numbers(39))  # 39
print("\n")


# Problem 4
def num_increases(num):
    increases = 0
    while num % 100 // 10 != 0:
        num1 = num % 10
        num2 = num % 100 // 10
        if num1 > num2:
            increases += 1
        num //= 10
    return increases


# Testing problem 4
print("Testing num_increases")
print(num_increases(12345))  # 4
print(num_increases(1211119))  # 2
print(num_increases(9123444534))  # 5
print(num_increases(987654))  # 0
print("\n")


# Problem 5
def wheresArmadillo(animals):
    passes, i, lIndex, rIndex, mActualIndex = 0, 0, 0, len(animals), 0
    mIndex = (lIndex + rIndex) // 2
    mActualIndex = mIndex
    while i == 0:
        passes += 1
        if checkAnimal(animals[mIndex]) == -1:
            rIndex = mIndex
            mIndex = (lIndex + rIndex) // 2
            mActualIndex = mActualIndex - mIndex
        elif checkAnimal(animals[mIndex]) == 0:
            i += 1
        else:
            lIndex = mIndex
            mIndex = (lIndex + rIndex) // 2
            mActualIndex = mActualIndex + mIndex
    return passes * mActualIndex


def checkAnimal(animal):
    """
    DO NOT TOUCH THIS FUNCTION
    :type animal: String representing the name of the animal
    :output: a 1 if the armadillo is heavier than the input animal,
             a -1 if the armadillo is lighter than the input animal,
             a 0 if the armadillo is the input animal.
    """
    weights={"mouse":0.01, "frog":0.1, "dove":1, "chicken":3, "cat":5, "koala":10, "dog":15, "turkey":20, "armadillo":27, "alligator":50, "leopard":100, "wolf":150, "pig":200, "deer":250, "lion":300,"cow":310, "buffalo":400, "elephant":500, "dinosaur":1000}
    animalWeight=weights.get(animal)
    armadilloWeight=weights.get("armadillo")
    if animalWeight>armadilloWeight:
        return -1
    elif animalWeight<armadilloWeight:
        return 1
    elif animalWeight==armadilloWeight:
        return 0


# Testing problem 5
print("Testing wheresArmadillo")
print(wheresArmadillo(["mouse", "frog","chicken","cat","dog","armadillo","pig","cow","dinosaur"])) # 15
print(wheresArmadillo(["mouse", "frog","chicken","turkey","cat","dog","armadillo","pig","cow","buffalo","dinosaur"])) # 18
print(wheresArmadillo(["dog","armadillo","pig","cow","buffalo","dinosaur"])) # 2
print("\n")


# Problem 6
def pie_cals_triangle(num):
  """
  :type num: positive integer representing the starting number of your triangle
  :output: the sum of the first five rows of the triangle shown in the coding challenges
  """
  return()


# Testing problem 6
print("Testing pie_cals_triangle")
print(pie_cals_triangle(1)) # 15
print(pie_cals_triangle(3)) # 981
print(pie_cals_triangle(8)) # 271496
print("\n")


# Problem 7
def road_trip(num):
  """
  :type num: positive integer re
  :type output: integer representing the time traveled rounded to the nearest time if everytimme the distance left is a multiple of five you add three units of distance, otherwise subtract two units of distance.
  :RESTRICTION YOU MUST USE RECURSION
  """
  return()


# Testing problem 6
print("Testing road_trip")
print(road_trip(12)) # 11
print(road_trip(51)) # 48
print(road_trip(104)) # 102
print("\n")


# Problem 8
def convertRoman(num):
  """
  :type num: a positive integer
  :type output: the roman numeral representation of the input num
  """
  return()


# Testing problem 6
print("Testing convertRoman")
print(convertRoman(41))  # "XLI"
print(convertRoman(904))  # "CMIV"
print(convertRoman(1050))  # "ML"

