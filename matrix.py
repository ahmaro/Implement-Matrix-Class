import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.is_square() and self.h == 2:
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            det = (a*d)-(c*b)
        elif self.is_square() and self.h == 1:
            det = self[0][0]
        
        return det
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        summ = 0
        # TODO - your code here
        for i in range(self.h):
            summ += self[i][i]
        return summ

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.is_square() and self.h == 2:
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            dett = self.determinant()
            inverse = zeroes(2, 2)
            inverse[0][0] = d/dett
            inverse[0][1] = -b/dett
            inverse[1][0] = -c/dett
            inverse[1][1] = a/dett
        elif self.is_square() and self.h == 1:
            inverse = zeroes(1, 1)
            inverse[0][0] = 1/self.determinant()
        
        
        return inverse
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        width = self.w
        height = self.h
        transpose = zeroes(width, height)
        
        for i in range(height):
            for j in range(width):
                transpose[j][i] = self[i][j]
        
        return transpose        
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        height = self.h
        width = self.w
        
        addm = zeroes(height, width)
        for i in range(height):
            for j in range(width):
                addm[i][j] = self[i][j] + other[i][j]         
         
        return addm
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        height = self.h
        width = self.w
        
        negative = zeroes(height, width)
        for i in range(height):
            for j in range(width):
                negative[i][j] = -self[i][j]
         
        return negative
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        height = self.h
        width = self.w
        
        subtract = zeroes(height, width)
        for i in range(height):
            for j in range(width):
                subtract[i][j] = self[i][j] - other[i][j]
         
        return subtract

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        height = self.h
        width = self.w
        height2 = other.h
        width2 = other.w
        
        k = 0
        r = 0
        
        if width != height2:
            raise(ValueError, "Matrices can not be multiplied")
        
        multiply = zeroes(height, width2)
        
        for k in range(width2):
            for i in range(height):
                for j in range(width):
                    multiply[i][k] += self[i][j] * other[j][k]
         
        return multiply

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            height = self.h
            width = self.w
            
            rmul = zeroes(height, width)
            
            for i in range(height):
                for j in range(width):
                    rmul[i][j] = other*self[i][j]
        return rmul