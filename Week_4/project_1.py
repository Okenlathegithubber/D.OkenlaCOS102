g_Names = ["Evelyn", "Jessica", "Somtom", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
g_Age = [17,16,17,18,16,18,17,20,19,17]
g_Height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
g_Scores = [80,85,70,60,76,66,87,95,50,49]

b_Names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
b_Age = [19,16,18,17,20,19,16,18,17,19]
b_Height = [5.7,5.9,5.8,6.1,5.9,5.5,61,5.4,5.8,5.7]
b_Scores = [74,87,75,68,66,78,87,98,54,60]

print("Data of Boys and Girls")
print("\t\tGirls")
print("\tNames\t  |Age \t|Height\t  |Scores")
for i in range(10):
    print(f"\t{g_Names[i]}\t  |{g_Age[i]} \t|{g_Height[i]}\t |{g_Scores[i]}")

print("\n")

print("\t\tBoys")
print("\tNames\t  |Age \t|Height\t  |Scores")
for k in range(10):
    print(f"\t{b_Names[k]}\t  |{b_Age[k]} \t|{b_Height[k]}\t |{b_Scores[k]}")
