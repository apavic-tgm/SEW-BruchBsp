"""
Created on 20.10.2016
@author: Markus Limbeck
"""
class Bruch(object):
    def __init__(self, zaehler, nenner=1):
        """
            constructor


            :param zaehler: - Bruch or int
            :param nenner:  - int, default value 1, not 0
            :raises ZeroDivisionError: if nenner = 0
            :raises TypeError: if zaehler and nenner not int
            """
        if type(zaehler) == Bruch:
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        else:
            self.zaehler = zaehler
            self.nenner = nenner

        if self.nenner == 0:
            raise ZeroDivisionError
        if type(self.nenner) != int or type(self.zaehler) != int:
            raise TypeError

    def __float__(self):
        """
            override predefined float() method

            :return float Result
            """
        return self.zaehler / self.nenner

    def __int__(self):
        """
            override predefined int() method

            :return int Result
            """
        return int(self.__float__())

    def __complex__(self):
        """
            override predefined  complex() method

            :return complex Result
            """
        return complex(self.__float__())

    def __invert__(self):
        """
            override predefined invert() method

            :return inverted Bruch
            """
        return Bruch(self.nenner, self.zaehler)

    def __pow__(self, power, modulo=None):
        """
        override predefined pow() method

        :param power: int
        :param modulo: std = None
        :raise TypeError: if power not int
        :return: multiplied Bruch
        """
        if type(power) == int:
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError

    def __abs__(self):
        """
        override predefined abs() method


        :return: absolute Value of Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        override predefined neg() method

        :return: negation of Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __eq__(self, other):
        """
        override predefined eq() method

        :param other: Bruch
        :return: boolean - equal; comparison of two Bruch
        """
        return self.__float__() == other.__float__()

    def __ne__(self, other):
        """
        override predefined ne() method
        :param other: Bruch
        :return: boolean - negativ; comparison of two Bruch
        """
        return self.__float__() != other.__float__()

    def __ge__(self, other):
        """
        override predefined ge() method

        :param other: Bruch
        :return: boolean - greater-equal; comparison of two Bruch
        """
        return self.__float__() >= other.__float__()

    def __le__(self, other):
        """
        override predefined le() method

        :param other: Bruch
        :return: boolean - less-equal; comparison of two Bruch
        """
        return self.__float__() <= other.__float__()

    def __lt__(self, other):
        """
        override predefined lt() method

        :param other: Bruch
        :return: boolean - less; comparison of two Bruch
        """
        return self.__float__() < other.__float__()

    def __gt__(self, other):
        """
        override predefined gt() method

        :param other: Bruch
        :return: boolean - greater; comparison of two Bruch
        """
        return self.__float__() > other.__float__()

    def __str__(self):
        """
        override predefined str() method

        :return: alphanumric Output of Bruch
        """
        if self.nenner == 1:
            return "(%s)" % (abs(self.zaehler))
        else:
            return "(%s/%s)" % (abs(self.zaehler), abs(self.nenner))

    def __add__(self, other):
        """
        override predefined add() method

        :param other: int or Bruch
        :return: summation of two Bruch
        :raise TypeError: if other not int or Bruch
        """
        if type(other) != Bruch and type(other) != int:
            raise TypeError
        else:
            return Bruch(self.zaehler*Bruch(other).nenner + Bruch(other).zaehler*self.nenner,
                         self.nenner * Bruch(other).nenner)

    def __radd__(self, other):
        """
        override predefined radd() method

        right side addition

        :param other: int or Bruch
        :return: summation of two Bruch
        """
        return self.__add__(other)

    def __iadd__(self, other):
        """
        override predefined iadd() method

        intern addition

        :param other: int or Bruch
        :return: summation of two Bruch
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        override predefined sub() method

        :param other: int or Bruch
        :return: subtraction of two Bruch
        :raise TypeError: if other not int or Bruch
        """
        if type(other) != Bruch and type(other) != int:
            raise TypeError
        else:
            return Bruch(self.zaehler*Bruch(other).nenner - Bruch(other).zaehler*self.nenner,
                         self.nenner * Bruch(other).nenner)

    def __rsub__(self, other):
        """
        override predefined rsub() method

        ride side subtract

        :param other: int or Bruch
        :return: subtraction of two Bruch
        :raise TypeError: if other not int or Bruch
        """
        if type(other) != Bruch and type(other) != int:
            raise TypeError
        else:
            return Bruch(Bruch(other).zaehler*self.nenner - self.zaehler*Bruch(other).nenner,
                         self.nenner * Bruch(other).nenner)

    def __isub__(self, other):
        """
         override predefined isub() method

         intern subtract

         :param other: int or Bruch
         :return: subtraction of two Bruch
         """
        return self.__sub__(other)

    def __mul__(self, other):
        """
        override predefined mul() method


        :param other: int or Bruch
        :return: multiplication of two Bruch
        :raise TypeError: if other not in or Bruch
        """
        if type(other) != Bruch and type(other) != int:
            raise TypeError
        else:
            return Bruch(self.zaehler * Bruch(other).zaehler,
                         self.nenner * Bruch(other).nenner)

    def __rmul__(self, other):
        """
        override predefined rmul() method

        right side multiplication

        :param other: int or Bruch
        :return: multiplication of two Bruch
        """
        return self.__mul__(other)

    def __imul__(self, other):
        """
        override predefined imul() method

        intern multiplication

        :param other: int or Bruch
        :return: multiplication of two Bruch
        """
        return int(self.__mul__(other))

    def __truediv__(self, other):
        """
        override predefined div() method
        since Python 3.x --> truediv

        :param other: int or Bruch
        :return: division of two Bruch
        :raises TypeError: (if other not in or Bruch)
        :raises ZeroDivisionError: (if other.nenner = 0)

        """
        if type(other) != Bruch and type(other) != int:
            raise TypeError
        elif Bruch(other).zaehler == 0:
            raise ZeroDivisionError
        else:
            return Bruch(self.zaehler * Bruch(other).nenner,
                         self.nenner * Bruch(other).zaehler)

    def __rtruediv__(self, other):
        """
        override predefined rdiv() method
        since Python 3.x --> rtruediv

        right side division

        :param other: int or Bruch
        :return: division of two Bruch
        :raises TypeError :if other not in or Bruch
        :raises ZeroDivisionError: if other.nenner = 0
        """
        if type(other) != Bruch and type(other) != int:
            raise TypeError
        elif self.zaehler == 0:
            raise ZeroDivisionError
        else:
            return Bruch(self.nenner * Bruch(other).zaehler,
                         self.zaehler * Bruch(other).nenner)

    def __itruediv__(self, other):
        """
        override predefined idiv() method
        since Python 3.x --> itruediv

        intern division

        :param other: int or Bruch
        :return: division of two Bruch
        """
        return self.__truediv__(other)

    def __iter__(self):
        """
         override predefined iter() method

         allows to iterate through the attributes

        :return: orderd attributes (zeahler, nenner)
        """
        return (self.zaehler, self.nenner).__iter__()

    @staticmethod
    def __makeBruch(other):
        """
        creates a new Bruch

        :param other: int or Bruch
        :return: Bruch
        :raise TypeError: if other not int or Bruch
        """
        if type(other) != int or type(other) == Bruch:
            raise TypeError
        else:
            return Bruch(other, 1)
