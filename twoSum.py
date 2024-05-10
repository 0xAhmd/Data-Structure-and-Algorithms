def two_sum(nums, target):
    """
    Given an array of integers 'nums' and an integer 'target', 
    return indices of the two numbers such that they add up to 'target'.
    """
    num_dict = {}  # Create an empty dictionary to store numbers and their indices
    for i, num in enumerate(nums):  # Loop through each number in the array along with its index
        complement = target - num  # Calculate the complement needed to reach the target
        if complement in num_dict:  # If the complement is already in the dictionary
            return [num_dict[complement], i]  # Return the indices of the complement and current number
        num_dict[num] = i  # Store the current number and its index in the dictionary
    return None  # If no solution is found, return None

# Example usage:
nums = [2, 4, 5, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1] (indices of 2 and 7 add up to 9)
