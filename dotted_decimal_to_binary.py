# A function to convert dotted decimal value to binary value
def to_binary(decimal_value: str):
    """ Returns Binary format of the decimal value param """
    new_decimal = decimal_value.split('.')
    value_list = []
    result_decimals_list = []
    try:
        for value in new_decimal:
            try:
                if value[0] == '0' and len(value) > 1:
                    return print("No Decimal With Leading 0\nYou entered:-",value)
            except Exception:
                return print("IP address has missing values. Enter a valid IP address.")
            if len(value) > 3:
                return print("No Dotted-Decimal IP address with {} values\nYou entered:-{}".format(len(value), value))
            if int(value) > 255:
                return print("Enter a valid IP Address.\nShould not exceed 255.")
            if int(value) < 0:
                return print("Non-positive values are not valid IP's")
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
            else:
                result_decimals_list.append(new_value)
    except Exception:
        return print("Invalid IP address")

    final_values = []
    final_decimals = []

    for ss in result_decimals_list:
        if ss[1] and len(ss) == 9:
            for yy in ss:
                final_values.append(yy)
            final_values.pop(0)
            final_values = ''.join(final_values)
            final_decimals.append(final_values)
            final_values = []
        else:
            final_decimals.append(ss)
    result_decimals = ' '.join(final_decimals)

    return result_decimals

# to_binary('128.56.7.91')