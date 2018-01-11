"""Static methods have very limited use case, because like class methods or any other methods within a class,
they cannot access properties of the class itself.
However, when you need a utility function that doesn't access any properties of a class but makes sense that
it belongs to the class, we use static functions."""


class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")