class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def __str__(self):
        if isinstance(self, Time):
            return '{:02d}:{:02d}:{:02d}'.format(self._hour, self._minute, self._second)
        else:
            return '{total time: {:d}}'.format(self)

    def __repr__(self):
        return '{:02d}:{:02d}:{:02d}-{:d}'.format(self._hour, self._minute, self._second, self._total_seconds)

    def __total_seconds(self):
        self._total_seconds = 3600 * self._hour + 60 * self._minute + self._second
        return self._total_seconds

    def __seconds_to_time(self, seconds):
        self._hour = seconds // 3600
        self._minute = seconds % 3600 // 60
        self._second = seconds % 3600 % 60

        if self._hour > 24:
            self._hour -= 24
        elif self._hour < 0:
            self._hour += 24

        return Time(self._hour, self._minute, self._second)

    def __lt__(self, time):
        return self.__total_seconds() < time.__total_seconds()

    def __le__(self, time):
        return self.__total_seconds() <= time.__total_seconds()

    def __gt__(self, time):
        return self.__total_seconds() > time.__total_seconds()

    def __ge__(self, time):
        return self.__total_seconds() >= time.__total_seconds()

    def __eq__(self, time):
        return self.__total_seconds() == time.__total_seconds()

    def __ne__(self, time):
        return self.__total_seconds() != time.__total_seconds()

    def __add__(self, time):
        if isinstance(time, Time):
            self._hour = self._hour + time._hour
            self._minute = self._minute + time._minute
            self._second = self._second + time._second

            return self.__seconds_to_time(self.__total_seconds())

        elif isinstance(time, int):
            self._second = self._second + time

            return self.__seconds_to_time(self.__total_seconds())

        else:
            raise TypeError('invalid type')

    __radd__ = __add__

    def __sub__(self, time):
        if isinstance(time, Time):
            self._hour = self._hour - time._hour
            self._minute = self._minute - time._minute
            self._second = self._second - time._second

            return self.__seconds_to_time(self.__total_seconds())

        elif isinstance(time, int):
            self._second = self._second - time

            return self.__seconds_to_time(self.__total_seconds())

    __rsub__ = __sub__

    def __int__(self):
        return int(3600 * self._hour + 60 * self._minute + self._second)

    def __bool__(self):
        if self._hour == 0 and self._minute == 0 and self._second == 0:
            return False
        else:
            return True

    def __getitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                return self._hour
            elif index == 1:
                return self._minute
            elif index == 2:
                return self._second

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if key == 0:
                self._hour = value
            elif key == 1:
                self._minute = value
            elif key == 2:
                self._second = value


# testing

t1 = Time(22, 10, 24)
print(t1)
result = t1 + 5700
print(result)

t2 = Time(5, 40, 34)
result = t1 + t2
print(result)

result = t1 - t2
print(result)

if t1 > t2:
    print('t1 > t2')
elif t1 < t2:
    print('t1 < t2')
elif t1 == t2:
    print('t1 == t2')

result = int(t1)
print(t1)

print('Zaman sıfır değil' if t1 else 'Zaman sıfır')

t1[0] = 23
print(t1)



