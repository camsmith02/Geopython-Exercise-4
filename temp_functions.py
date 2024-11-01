def fahr_to_celsius(temp_fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius with two decimal points.
    
    Parameters:
    temp_fahrenheit (float): Temperature in degrees Fahrenheit.
    
    Returns:
    float: Temperature in degrees Celsius, rounded to two decimal places.
    """
    # Convert Fahrenheit to Celsius and round to 2 decimal places
    temp_celsius = round((temp_fahrenheit - 32) * 5 / 9, 2)
    return temp_celsius

def temp_classifier(temp_celsius):
    """
    Classify a temperature in Celsius into categories based on specified criteria.
    
    Parameters:
    temp_celsius (float): Temperature in degrees Celsius.
    
    Returns:
    int: Classification of temperature:
         - 0 for temperatures below -2 degrees Celsius
         - 1 for temperatures equal or warmer than -2 but less than +2 degrees Celsius
         - 2 for temperatures equal or warmer than +2 but less than +15 degrees Celsius
         - 3 for temperatures equal or warmer than +15 degrees Celsius
    """
    if temp_celsius < -2:
        return 0
    elif -2 <= temp_celsius < 2:
        return 1
    elif 2 <= temp_celsius < 15:
        return 2
    else:
        return 3