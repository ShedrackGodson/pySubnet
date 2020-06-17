# A function to convert dotted decimal value to binary value
def to_binary(decimal_value):
    new_decimal = decimal_value.split('.')
    value_list = []
    result_decimals_list = []
    for value in new_decimal:
        new_value = bin(int(value))
        new_value = new_value.replace('b', '')

        if len(new_value) < 8:
            for i in new_value:
                value_list.append(i)
            for x in range(8-len(new_value)):
                value_list.insert(0, '0')
            value_list = ','.join(value_list)
            value_list = value_list.replace(',', '')
            result_decimals_list.append(value_list)
            value_list = []
        # elif len(new_value) > 8:
        #     for i in range(8-len())
        else:
            result_decimals_list.append(new_value)
    
    result_decimals = ' '.join(result_decimals_list)

    return print(result_decimals)

to_binary('129.11.11.239')