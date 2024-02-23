import doctest
from itertools import product

class First:
    def first():
        """
        >>> First.first()
        6075
        """
        __ = ['Н', 'А', 'С', 'Т', 'Я']
        ___ = []

        for _ in product(__, repeat=6):
            if _.count("А") <= 1 and _.count("Я") <= 1:
                ___.append(_)

        return len(___)
    
class Second:
    def second():
        """
        >>> Second.second()
        43
        """
        __ = 16;___=18;____=4;_____=10;______=46;_______=16
        _=__**___*____**_____-______-_______;________=''
        while _ > 0:________=str(_%4)+________;_=_//4
        return ________.count("3")
    
class Third:
    def third():
        """
        >>> Third.third()
        [452025, 452028, 452029, 452034, 452036]
        """
        ___ = []
        for _ in range(452022, 500000):
            if len(___) != 5:
                for __ in range(2, _):
                    if _ % __ == 0:
                        if (_ // __ + __) % 7 == 3:
                            #print(_ // __ + __, _ , __)
                            ___.append(_)
                            break
            else:
                break
        return ___
if __name__ == "__main__":
    doctest.testmod()