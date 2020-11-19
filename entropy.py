import math
import matplotlib.pyplot as plt

# NEW COMMENT
# NEW COMMENT
# NEW COMMENT
# NEW COMMENT
# NEW COMMENT
# Makes every character lowercase and removes spaces
def format_text(text):
    edited_text = text.replace(" ", "").lower()
    return edited_text

# Calculate the occurrence of each character
def char_occurrence(text):
    result = dict((letter,text.count(letter)) for letter in set(text))
    return result

# Calculate the probability of occurrence of each character
def char_probability(text, occurrence_table):
    text_length = len(text)
    probability = dict((letter,occurrence_table[letter]/text_length) for letter in set(text))
    return probability


# Calculate the entropy using the equation
# H = Σp(i)log_2(1/p(i))
def entropy(probability):
    H = 0
    for num in probability:
        H += probability[num]*math.log2(1/probability[num])
    return H

######[Execution]######

input_text = "dqdwqfwqfggqwq"

# Step 1: Format the text
string = format_text(input_text)
print("This is the formated input text: \n" + string)

# Step 2: Calculate the number of occurrences of each letter/character
occurrences = char_occurrence(string)
print(occurrences)
plt.bar(range(len(occurrences)), list(occurrences.values()), align='center')
plt.xticks(range(len(occurrences)), list(occurrences.keys()))
plt.suptitle('Letter occurrences')
plt.show()

# Step 3: Calculate the probability of occurrence of each letter/character
probabilities = char_probability(string, occurrences)
print(probabilities)
plt.bar(range(len(probabilities)), list(probabilities.values()), align='center')
plt.xticks(range(len(probabilities)), list(probabilities.keys()))
plt.suptitle('Probabilities of letter occurrences')
plt.show()

# Step 4: Calculate the entropy of the string
H = entropy(probabilities)
print(H, "bits")