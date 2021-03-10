
class RubicCube:
    def __init__(self):
        #For debugging purposes, it is interesting that each little face has a different name
        self._top = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        self._left = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
        self._front = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', '!']]
        self._right = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        self._back = [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]
        self._bottom = [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '?']]

    def setStandardSolution(self):
        self._top = [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']]
        self._left = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
        self._front = [['c', 'c', 'c'], ['c', 'c', 'c'], ['c', 'c', 'c']]
        self._right = [['d', 'd', 'd'], ['d', 'd', 'd'], ['d', 'd', 'd']]
        self._back = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
        self._bottom = [['f', 'f', 'f'], ['f', 'f', 'f'], ['f', 'f', 'f']]

    def print(self):
        for i in range(3):
            print("    ", end='')
            for j in range(3):
                print(self._top[i][j], end='')
            print('')

        for i in range(3):
            for j in range(3):
                print(self._left[i][j], end='')
            print('|', end='')
            for j in range(3):
                print(self._front[i][j], end='')
            print('|', end='')
            for j in range(3):
                print(self._right[i][j], end='')
            print('|', end='')
            for j in range(3):
                print(self._back[i][j], end='')
            print('')

        for i in range(3):
            print("    ", end='')
            for j in range(3):
                print(self._bottom[i][j], end='')
            print('')

    def clone(self):
        #TODO: This method should return another instance of RubicCube with the same configuration as self
        pass

    def copy(self, aCube):
        #TODO: This method should copy the configuration of aCube into self
        pass

    def equals(self, aCube):
        #TODO: This method should return True if the configurations of both cubes are the same. False otherwise.
        pass

    def write(self, filename):
        #TODO: It is interesting to have a method that writes the configuration of the cube into a file
        pass

    def read(self, filename):
        #TODO: It is interesting to have a method that reads the configuration of the cube from a file
        pass

    def rotateTopClockwise(self):
        #TODO: This method should modify the configuration of the cube resulting in the rotation of the top face
        # clockwisely
        #He cambido la función por que lo que hacía era rotar la cara frontal
        
        aux = [self._right[0][i] for i in range(3)]

        for i in range(3):
            self._right[0][i] = self._front[0][i]

        for i in range(3):
            self._front[0][i] = self._left[0][i]

        for i in range(3):
            self._left[0][i] = self._back[0][i]

        for i in range(3):
            self._back[0][i] = aux[i]
        

    def rotateTopAntiClockwise(self):
        #TODO....
        pass



#######
#TEST FUNCTIONS
#######

#It is very common to make mistakes in the rotate functions. That's why it is interesting to desing test cases
def rotateTopClockwise_test1():
    c1 = RubicCube()
    c2 = RubicCube()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()

    if not c1.equals(c2):
        print('There is an error rotating top clockwisely')

def rotateTopAnticlockwise_test1():
    c1 = RubicCube()
    c2 = RubicCube()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c2.rotateTopAntiClockwise()

    if not c1.equals(c2):
        print('There is an error rotating top either clockwisely or anticlockwisely')



def runTests():
    rotateTopClockwise_test1()
    rotateTopAnticlockwise_test1()


if __name__=="__main__":
    c = RubicCube()
    c.print()
    print('----------------')
    c.rotateTopClockwise()
    c.print()

    #Checking rotateTopClockwise
    runTests()
