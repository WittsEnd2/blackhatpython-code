def sum(one, two):
    one_int = convert_integer(one)
    two_int = convert_integer(two)
    
    result = one_int + two_int
    
    return result;
def convert_integer(number_string):
    converted_integer = int(number_string)
    return converted_integer

answer = sum("1", "2")