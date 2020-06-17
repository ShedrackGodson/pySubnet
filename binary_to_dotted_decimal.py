# A function that converts the Binary values to Decimal values
def to_decimal(binary:str):
    """ Returns the Dotted format of the Binary values """
    binary = binary.split(' ')
    new_binary = []
    decimals = []
    for value in binary:
        if len(value) > 8 or len(value) < 8:
            return print("Not a valid binary address.")
        else:
            new_value = int(value, 2)
            new_binary.append(new_value)
    
    # Convert to 255.255.255.255
    dotted_string = str()
    for ss in new_binary:
        if len(dotted_string) == 0:
            dotted_string = dotted_string + str(ss)
        else:
            dotted_string = dotted_string + '.' + str(ss)
    
    return print(dotted_string)


to_decimal('10011110 10000000 00000001 01101100')