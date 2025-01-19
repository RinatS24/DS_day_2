import sys


class Research:
    def __init__(self,file_path):
        self.file_path = file_path

    
    def file_reader(self):
        file = open(self.file_path)
        array_class = file.readlines()

        split_line_array = array_class[0].split(',')
        
        has_header = not(split_line_array[0].isdigit()) and not(split_line_array[1].isdigit())
        result = [0]*(len(array_class) - has_header)

        for current_index in range(has_header,len(array_class)):
            result[current_index-has_header] = array_class[current_index].replace("\n","")
            split_line_array = array_class[current_index].split(',')

            if int(split_line_array[0]) != int(split_line_array[1]):
                result[current_index-has_header] = [int(split_line_array[0]),int(split_line_array[1])]
        return result

    
    class Calculations:
        def counts(data):
            return sum(arr[0] for arr in data), sum(arr[1] for arr in data)

        def fractions(heads,tails):
            total = heads + tails
            return (heads/total) * 100, (tails/total) * 100

        
    
def main(file_path):
    object_class = Research(file_path)
    data = object_class.file_reader()
    if len(data) != 0:
        print(data) 
        count = object_class.Calculations.counts(data)
        print(*count)
        print(*object_class.Calculations.fractions(*count))

            

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
