      #BDD
# Given a sequence (list or tuple) with duplicates
# When the remove_duplicates function is called with the sequence
# Then the function should return a new sequence with duplicates removed
# And the order of elements in the new sequence should match the original order

     #pseudocode
# Function remove_duplicates(sequence):
 #   Initialize an empty set to track unique elements
 #   Initialize an empty result sequence
 #   For each element in the sequence:
 #       If the element is not in the set:
  #          Add the element to the set
  #          Append the element to the result sequence
  #  Return the result sequence


def remove_duplicates(sequence):
    unique_set = set()
    result_sequence = []

    for element in sequence:
        if element not in unique_set:
            unique_set.add(element)
            result_sequence.append(element)

    return result_sequence

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

