def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # If my_list_1 or my_list_2 is too short
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            # If the elements are not integer or float
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            # If the division can't be done (/0)
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
