from stacks import is_balanced
from sequences import remove_duplicates
from dictionaries import word_frequency

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
