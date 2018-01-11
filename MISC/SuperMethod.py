class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        super(Dog, self).__init__('Dog')
        print('Dog has four legs.')



d1 = Dog()