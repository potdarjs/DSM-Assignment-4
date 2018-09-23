
# Assingment 4 - Data Science Masters

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula. area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# class to take the sides of the triangle
class Polygon:
    def __init__ (self, no_of_sides):
        self.n = no_of_sides
        self.side=[0 for i in range(self.n)]
    def inputSides (self):
        self.side = [float(input('enter side' + str(i+1) + ":" )) for i in range(self.n)]
        
class Triangle(Polygon):
    # this class takes the instances from the parent class ; Polygon
    def __init__ (self):
        Polygon.__init__(self,3)
    # function to calculate area of triangle
    def area (self):
        a, b, c=self.side
        s = ( a + b + c ) / 2
        area = ((s*(s-a)*(s-b)*(s-c))**0.5)
        print('area of the triangle is % 0.2f' % area + ' unit cude') # Print the area
        
T = Triangle()
T.inputSides()
T.area()
# -----------------------------------------
        # 1.2 Write a function filter_long_words() that takes a list of words and an integer n
        # and returns the list of words that are longer than n
import re

def filter_long_words(list_of_words, n):
    """ 
    Function filter_long_words takes a list of words and an integer 
    n as arguments and returns the list of words which are longer than n.
    """
    result = []
    for item in list_of_words :
        item = item.strip()
        if len(item) > n :
            result.append(item)
    return result

def main():
    words = input("Please enter list of words : ")
    patterns = r"[,\[ \] \'\"]"
    pattern = re.compile(patterns)
    words = re.split(pattern,words)
    n = int(input("Please enter an integer : "))
    
    output = filter_long_words(words, n)
    
    print("\nList of words which are longer than integer {} are : [{}]".format(n,','.join(output)))
        
# ---------------------------------------
    # 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns 
    # True if it is a vowel, False otherwise
    
def vowel_check(char) :
    """
    This function takes a character (i.e. a string of length 1) and
    returns True if it is a vowel, False otherwise.
    """  
    
    try :
        if len(char) > 1 :
            print("Plase enter a string of length 1.")
            return "None"
            
        if char in 'aeiou' :
            return 'TRUE'
        else :
            return 'FALSE'
    except :
        pass
    
def main():
    ch = input("Enter a character : ")
    
    output = vowel_check(ch)
    
    print("Vowel check for '{}' returns '{}'".format(ch,output))
 
if __name__ == '__main__':
    main()