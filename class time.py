


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def display(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def __add__(self, other):
        total_seconds = (
            self.__hour * 3600 + self.__minute * 60 + self.__second
            + other.__hour * 3600 + other.__minute * 60 + other.__second
        )

        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60

        return Time(hour, minute, second)


# Creating two time objects
t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)

# Adding two time objects
t3 = t1 + t2

print("Time 1:", t1.display())
print("Time 2:", t2.display())
print("Total Time:", t3.display())
