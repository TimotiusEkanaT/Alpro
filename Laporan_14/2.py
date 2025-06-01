def list_ke_set(data_list):
    print(set(data_list))

def set_ke_list(data_set):
    print(list(data_set))

def tuple_ke_set(data_tuple):
    print(set(data_tuple))

def set_ke_tuple(data_set):
    print(tuple(data_set))

list_awal = [1, 2, 3, 4, 5, 3, 2]
set_awal = {10, 20, 30, 40, 50}
tuple_awal = (100, 200, 300, 200, 100)

set_dari_list = list_ke_set(list_awal)
list_dari_set = set_ke_list(set_awal)
set_dari_tuple = tuple_ke_set(tuple_awal)
tuple_dari_set = set_ke_tuple(set_awal)

