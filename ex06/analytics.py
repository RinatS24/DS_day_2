from random import randint
import logging
import requests
from config import telegram_api_url, telegram_token, telegram_chat_id

logging.basicConfig(
    level = logging.INFO,
    filename = "analytics.log",
    format = "%(asctime)s %(message)s",
    filemode="w"
)


class Research:
    def __init__(self,file_path):
        self.file_path = file_path
        logging.info("Launching constructor of Research")
    
    def file_reader(self):
        file = open(self.file_path)
        array_class = file.readlines()

        logging.info("Successful open and read the file")

        split_line_array = array_class[0].split(',')
        
        has_header = not(split_line_array[0].isdigit()) and not(split_line_array[1].isdigit())
        result = [0]*(len(array_class) - has_header)

        for current_index in range(has_header,len(array_class)):
            result[current_index-has_header] = array_class[current_index].replace("\n","")
            split_line_array = array_class[current_index].split(',')

            if int(split_line_array[0]) != int(split_line_array[1]):
                result[current_index-has_header] = [int(split_line_array[0]),int(split_line_array[1])]
        logging.info("Successful read lines")
        return result

    def send_telegram_message(self, message):
        url = f"{telegram_api_url}/bot{telegram_token}/sendMessage"
        data = {
            "chat_id": telegram_chat_id,
            "text": message
        }
       
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            logging.info("Successful to sent Telegram message")
        else:
            logging.error("Failed to send Telegram message")
        

    class Calculations:
        def __init__(self,data):
            self.data = data
            logging.info("Launching constructor of Calculations")

        def counts(self):
            logging.info("Counting the number of heads and tails")
            return sum(arr[0] for arr in self.data), sum(arr[1] for arr in self.data)

        @staticmethod
        def fractions(heads,tails):
            total = heads + tails
            logging.info("Counting fractions")
            return (heads/total) * 100, (tails/total) * 100

class Analytics(Research.Calculations):
    def __init__(self,data):
       super().__init__(data)
       logging.info("Launching constructor of Analytics")

    @staticmethod
    def predict_random(num_of_steps):
        predict = []
        for _ in range(num_of_steps):
            if randint(0, 1) == 0:
                predict.append([1,0])
            else:
                predict.append([0,1])
        logging.info("Counting random throws")
        return predict
    
    def predict_last(self):
        logging.info("Output of the last element")
        return self.data[-1]
    
    @staticmethod
    def save_file(data, name_of_file, extension = "txt"):
        with open(f"{name_of_file}.{extension}", "w") as file:
            file.write(data)
            logging.info(f"Successful writing of a message to a {name_of_file}.{extension}")