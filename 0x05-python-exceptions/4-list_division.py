#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        new_list.append(0)
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except LookupError:
            print("out of range")
        finally:
            pass
        return new_list
