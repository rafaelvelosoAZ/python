students_scores = input("Input a list of scores: \n").split()
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)
##MAX FUN using FOR
highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score
print(f"the hieghest score is: {highest_score}")

##MIN FUN using FOR
tall_score = students_scores[n]
for score in students_scores:
    if score < tall_score:
        tall_score = score
print(f"the min score is: {tall_score}")


    

#quantidade de itens no len
#print(n)
#chamar o ultimo item do len
#print(students_scores[n])