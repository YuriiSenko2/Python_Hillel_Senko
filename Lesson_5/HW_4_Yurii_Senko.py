from collections import Counter

# Task 1. Find all repeating numbers and print them in ascending order

list_1 = set([16, 23, 20, 28, 2, 4, 8, 19, 17, 10, 9])
list_2 = set([99, 19, 22, 13, 2, 79, 21, 68, 10, 8, 9])
duplicate_values = list_1 & list_2
print(duplicate_values)

# Task 2. Determine the average score and print students with above average performance

student_rating = {
    'Mike': 100,
    'Davide': 66,
    'Malik': 90,
    'Pierre': 89,
    'Fikayo': 78,
    'Theo': 95,
    'Sandro': 77,
    'Ismael': 100,
    'Rafael': 90,
    'Brahim': 70,
    'Olivier': 85
}

average_score = sum(student_rating.values())/len(student_rating)
average_score = average_score.__round__(1)
print(average_score)

for element in student_rating:
    if student_rating[element] > average_score:
        print(element)

# Task 3. Amount of different numbers

integers = [16, 23, 20, 28, 2, 4, 8, 19, 17, 10, 9, 99, 19, 22, 13, 2, 79, 21, 68, 10, 8, 9]
diff_numbers = set(integers)
print(len(diff_numbers))

# Task 4. Find all repeating numbers and print them in ascending order on separate lines

numbers = input('Enter a number in the first list: ')
first_list = []

while numbers != 'Second list':
    numbers = int(numbers)
    first_list.append(numbers)
    numbers = input('Enter a number in the first list: ')

numbers_2 = input('Enter a number in the second list: ')
second_list = []

while numbers_2 != 'Stop':
    numbers_2 = int(numbers_2)
    second_list.append(numbers_2)
    numbers_2 = input('Enter a number in the second list: ')

filter_1 = set(first_list)
filter_2 = set(second_list)
filter_3 = filter_1.intersection(filter_2)
new_list = list(filter_3)
new_list.sort()

for element in new_list:
    print(element)

# Task 5.1. Print all words and their frequency in the text (by Counter)

text = "one two three one four five seven ten seven one"
text = text.split()
words_frequency = Counter(text)
print(words_frequency)

# Task 5.2. Print all words and their frequency in the text (by dictionary and loop)

text_1 = "one two three one four five seven ten seven one"
text_1 = text_1.split()
words_incidence = {}
for i in text_1:
    if i in words_incidence:
        words_incidence[i] += 1
    else:
        words_incidence[i] = 1
print(words_incidence)


