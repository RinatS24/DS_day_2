from random import randint

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
        def __init__(self,data):
            self.data = data

        def counts(self):
            return sum(arr[0] for arr in self.data), sum(arr[1] for arr in self.data)

        @staticmethod
        def fractions(heads,tails):
            total = heads + tails
            return (heads/total) * 100, (tails/total) * 100

class Analytics(Research.Calculations):
    def __init__(self,data):
       super().__init__(data)

    @staticmethod
    def predict_random(num_of_steps):
        predict = []
        for _ in range(num_of_steps):
            if randint(0, 1) == 0:
                predict.append([1,0])
            else:
                predict.append([0,1])
        return predict
    
    def predict_last(self):
        return self.data[-1]
    
    @staticmethod
    def save_file(data, name_of_file, extension = "txt"):
        with open(f"{name_of_file}.{extension}", "w") as file:
            file.write(data)