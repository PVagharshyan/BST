class Node():
    def __init__(self, value = None):
        self.__left = None;
        self.__right = None;
        self.__value = value;

    def __str__(self):
        return f"value: {self.__value}";

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left_val):
        self.__left = left_val

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right_val):
        self.__right = right_val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

def main():
    print("!Node!")

if __name__ == "__main__":
    main()
