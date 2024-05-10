import math

def calculate_mean(data):
    """
    Calculate the mean of a list of numbers.
    
    Parameters:
        data (list): A list of numerical values.
        
    Returns:
        float: The mean of the data.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(data) / len(data)

def calculate_variance(data):
    """
    Calculate the variance of a list of numbers.
    
    Parameters:
        data (list): A list of numerical values.
        
    Returns:
        float: The variance of the data.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate variance of an empty list")
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

def calculate_standard_deviation(variance):
    """
    Calculate the standard deviation from variance.
    
    Parameters:
        variance (float): The variance of a dataset.
        
    Returns:
        float: The standard deviation.
        
    Raises:
        ValueError: If the variance is negative.
    """
    if variance < 0:
        raise ValueError("Variance cannot be negative")
    return math.sqrt(variance)

def calculate_probability(favorable_outcomes, total_outcomes):
    """
    Calculate the probability of an event.
    
    Parameters:
        favorable_outcomes (float): The number of favorable outcomes.
        total_outcomes (float): The total number of possible outcomes.
        
    Returns:
        float: The probability of the event.
        
    Raises:
        ValueError: If the total outcomes is non-positive.
    """
    if total_outcomes <= 0:
        raise ValueError("Total outcomes must be a positive number")
    return favorable_outcomes / total_outcomes

def calculate_mode(data):
    """
    Calculate the mode(s) of a list of numbers.
    
    Parameters:
        data (list): A list of numerical values.
        
    Returns:
        list: The mode(s) of the data.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate mode of an empty list")

    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_frequency = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_frequency]

    if len(modes) == len(data):
        return "No unique mode"
    else:
        return min(modes)  # Return the smallest mode if multiple modes exist

def calculate_median(data):
    """
    Calculate the median of a list of numbers.
    
    Parameters:
        data (list): A list of numerical values.
        
    Returns:
        float: The median of the data.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate median of an empty list")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        # If even number of elements, average the two middle values
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        # If odd number of elements, return the middle value
        return sorted_data[n // 2]

def calculate_range(data):
    """
    Calculate the range of a list of numbers.
    
    Parameters:
        data (list): A list of numerical values.
        
    Returns:
        float: The range of the data.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate range of an empty list")
    return max(data) - min(data)

# Example usage and testing
data = [10, 20, 30, 40, 50]
favorable_outcomes = 3
total_outcomes = 10

try:
    mean = calculate_mean(data)
    variance = calculate_variance(data)
    std_deviation = calculate_standard_deviation(variance)
    mode = calculate_mode(data)
    median = calculate_median(data)
    data_range = calculate_range(data)
    probability = calculate_probability(favorable_outcomes, total_outcomes)

    print("Data:", data)
    print("Mean:", mean)
    print("Variance:", variance)
    print("Standard Deviation: {:.3f}".format(std_deviation))
    print("Mode:", mode)
    print("Median:", median)
    print("Range:", data_range)
    print("Probability of an event:", probability)

except ValueError as ve:
    print("Error:", ve)
