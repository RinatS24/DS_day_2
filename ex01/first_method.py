

class Research():
    def file_reader(self):
        file = open("data.csv")
        return file.read() 


def main():
    object_class = Research()
    print(object_class.file_reader())


if __name__ == "__main__":
    main()