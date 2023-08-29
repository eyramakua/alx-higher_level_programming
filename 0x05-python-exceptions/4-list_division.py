#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    m_list = []
    for i in range(list_length):
        try:
            b = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            b = 0
        except ZeroDivisionError:
            print("division by 0")
            b = 0
        except IndexError:
            print("out of range")
            b = 0
        finally:
            m_list.append(b)
    return m_list
