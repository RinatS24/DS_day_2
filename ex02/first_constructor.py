import sys


class Research:
    def __init__(self,file_path):
        self.file_path = file_path
    
    def file_reader(self):
        file = open(self.file_path)
        array_class = file.readlines()
        flag = len(array_class) > 1
        for current_index in range(len(array_class)):
            array_class[current_index] = array_class[current_index].replace("\n","")

            split_line_array = array_class[current_index].split(',')
            if current_index == 0:
                if len(split_line_array) == 2 and not(split_line_array[0].isdigit()) and not(split_line_array[1].isdigit()):
                    flag += 1
            else:
                if len(split_line_array) == 2 and int(split_line_array[0]) != int(split_line_array[1]):
                    flag += 1
        if flag == len(array_class) + 1:
            return array_class
        return []
    
def main(file_path):
    object_class = Research(file_path).file_reader()
    if len(object_class) != 0:
        for current_object in object_class:
            print(current_object)
    



if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])