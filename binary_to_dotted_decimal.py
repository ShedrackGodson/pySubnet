# A function to convert dotted decimal value to binary value
def to_binary(decimal_value):
    new_decimal = decimal_value.split('.')
    value_list = []
    result_decimals_list = []
    for value in new_decimal:
        try:
            new_value = bin(int(value))
            new_value = new_value.replace('b', '')
        except Exception as e:
            return "No Binary With Leading 0"

        if len(new_value) < 8:
            for i in new_value:
                value_list.append(i)
            for x in range(8-len(new_value)):
                value_list.insert(0, '0')
            value_list = ','.join(value_list)
            value_list = value_list.replace(',', '')
            result_decimals_list.append(value_list)
            value_list = []
        else:
            result_decimals_list.append(new_value)

    print(result_decimals_list)
    # final_decimals = []
    # final_values = []
    # for ss in result_decimals_list:
    #     if len(ss) == 9:
    #         for values in ss:
    #             final_values.append(values)

    #     final_values.pop(0)
    #     final_values = ''.join(final_values)
    #     print(final_values)
        # final_values = []
    
    result_decimals = ' '.join(result_decimals_list)

    return print(result_decimals)

to_binary('129.011.11.239')