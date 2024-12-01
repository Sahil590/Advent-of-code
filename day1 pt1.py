with open("Inputs/day1.txt", "r") as file:
    list1 = []
    list2 = []
    for line in file:
        num1, num2 = line.split("   ")
        list1.append(int(num1))
        list2.append(int(num2))
    list1.sort()
    list2.sort()
    differences = [abs(a - b) for a, b in zip(list1, list2)]
total_difference = sum(differences)
print(total_difference)
