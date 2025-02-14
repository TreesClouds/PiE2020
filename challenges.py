

# Team 35 Coding Challenges


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
    passes, i, lIndex, rIndex = 0, 0, 0, len(animals)
    mIndex = (lIndex + rIndex) // 2
    while i == 0:
        passes += 1
        if checkAnimal(animals[mIndex]) == -1:
            rIndex = mIndex
            mIndex = (lIndex + rIndex) // 2
        elif checkAnimal(animals[mIndex]) == 0:
            i += 1
        else:
            lIndex = mIndex
            mIndex = (lIndex + rIndex) // 2
    return passes * mIndex


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
    return 9 * num + num ** 2 + 2 * num ** 3 + 2 * num ** 4 + num ** 6


# Testing problem 6
print("Testing pie_cals_triangle")
print(pie_cals_triangle(1))  # 15
print(pie_cals_triangle(3))  # 981
print(pie_cals_triangle(8))  # 271496
print("\n")


# Problem 7
def road_trip(num):
    if "roadTime" not in globals():
        global roadTime
        roadTime = 0
    if num <= 0:
        roadTimeF = roadTime
        roadTime = 0
        return roadTimeF
    elif num % 5 == 0:
        num += 3
    else:
        num -= 2
    roadTime += 1
    return road_trip(num)


# Testing problem 6
print("Testing road_trip")
print(road_trip(12))  # 11
print(road_trip(51))  # 48
print(road_trip(104))  # 102
print("\n")


# Problem 8
def convertRoman(num):
    roman = ""
    while num >= 1000:
        num -= 1000
        roman += "M"
    while num >= 900:
        num -= 900
        roman += "CM"
    while num >= 500:
        num -= 500
        roman += "D"
    while num >= 400:
        num -= 400
        roman += "CD"
    while num >= 100:
        num -= 100
        roman += "C"
    while num >= 90:
        num -= 90
        roman += "XC"
    while num >= 50:
        num -= 50
        roman += "L"
    while num >= 40:
        num -= 40
        roman += "XL"
    while num >= 10:
        num -= 10
        roman += "X"
    while num >= 9:
        num -= 9
        roman += "IX"
    while num >= 5:
        num -= 5
        roman += "V"
    while num >= 4:
        num -= 4
        roman += "IV"
    while num >= 1:
        num -= 1
        roman += "I"
    return roman


# Testing problem 6
print("Testing convertRoman")
print(convertRoman(41))  # "XLI"
print(convertRoman(904))  # "CMIV"
print(convertRoman(1050))  # "ML"
