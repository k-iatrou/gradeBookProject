# creating lists
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# 2D list
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

print(gradebook)

# adding computer class and visual arts grade to gradebook
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# updating the visual arts points from 93 to 98
gradebook[5][1] = 98

# changing from point to pass/fail system for visual arts class
gradebook[5].remove(98)
gradebook[5].append("Pass")
