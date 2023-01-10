class my_list:
    def __init__(self,my_list):
        self.my_list = my_list

    def print_sorted(self):
        print(sorted(self.my_list))

My_List = my_list([3,1,2])
My_List.print_sorted()
