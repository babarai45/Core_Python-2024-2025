# well come back Class-4 
###  Class Agenda:
     Python Operaters
     Python Expression
     Python Statement
     Python Comments
     Python Indentation



### Python Operates
     Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
     1. Arithmetic Operators(+, -, *, /, %, **, //)
     2. Comparison (Relational) Operators(==, !=, >, <, >=, <=)
     3. Assignment Operators(=, +=, -=, *=, /=, %=, **=, //=)
     4. Logical Operators(and, or, not)
     5. Bitwise Operators(&, |, ~, ^, <<, >>)
     6. Membership Operators(in, not in)
     7. Identity Operators(is, is not)
     8. Operator Precedence(PEMDAS/BODMAS)
     9. Ternary Operator(Conditional Operator)
     10. Special Operators(//, **, @, _)
     11. Operator Overloading()
     12. Some important points

### Python Expression :
    python Expression is Combination of Values,Varibale ,Operates 
    Basically Python Expression used to solve Mathematicalyy or logically
    Problems and we can say that using Expression we can apply math operations
    on the varibale or values 
     Example:
     

### Python Statement:
     Instructions that a Python interpreter can execute are called statements. For example, a = 1 is an assignment statement. if statement, for statement, while statement, etc. are other kinds of statements which will be discussed later.
     Multi-line statement
     In Python, the end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\). For example:
     total = item_one + \
               item_two + \
               item_three
     This is explicit line continuation. In Python, line continuation is implied inside parentheses ( ), brackets [ ], and braces { }. For instance, we can implement the above multi-line statement as:
     total = (item_one +
                item_two +
                item_three)
     Here, the surrounding parentheses ( ) do the line continuation implicitly. Same is the case with [ ] and { }. For example:
     days = ['Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday']
     This is used in Python to break the line of code in multiple lines

### Python Comments:
     Comments are very important while writing a program. It describes what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out. You might forget the key details of the program you just had written in a month's time. So taking time to explain these concepts in form of comments is always fruitful.
     In Python, we use the hash (#) symbol to start writing a comment.
     It extends up to the newline character. Comments are for programmers for better understanding of a program. Python Interpreter ignores comment.
     Example:
     #This is a comment
     #Write a comment
     #print Hello, world
     print("Hello, world")

### Python Indentation:
     Most of the programming languages like C, C++, Java use braces { } to define a block of code. Python uses indentation.
     A code block (body of a function, loop, etc.) starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.
     Generally, four whitespaces are used for indentation and are preferred over tabs. Here is an example.
     Example:
     for i in range(1,11):
         print(i)
         if i == 5:
             break
     Here, both print(i) and if i == 5: are two separate code blocks. Both these blocks have their own indentation.
     Indentation can be ignored in line continuation. But it's a good idea to always indent. It makes the code more readable. 
     For example:
     if True:
         print('Hello')
     a = 5
     Here, the line a = 5 is not indented and forms a separate block.


### Python Operates one by one:

#### 1. Arithmetic Operators:
     Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
     Operator	Meaning	Example
     +	Addition	x + y
     -	Subtraction	x - y
     *	Multiplication	x * y
     /	Division	x / y
     %	Modulus	x % y
     **	Exponentiation	x ** y
     //	Floor division	x // y
     Example:
     x = 15
     y = 4
     # Output: x + y = 19
     print('x + y =',x+y)
     # Output: x - y = 11
     print('x - y =',x-y)
     # Output: x * y = 60
     print('x * y =',x*y)
     # Output: x / y = 3.75
     print('x / y =',x/y)
     # Output: x % y = 3
     print('x % y =',x%y)
     # Output: x ** y = 50625
     print('x ** y =',x**y)
     # Output: x // y = 3
     print('x // y =',x//y)

#### 2. Comparison Operators:
     Comparison operators are used to compare values. It returns either True or False according to the condition.
     Operator	Meaning	Example
     ==	Equal	x == y
     !=	Not equal	x != y
     >	Greater than	x > y
     <	Less than	x < y
     >=	Greater than or equal to	x >= y
     <=	Less than or equal to	x <= y
     Example:
     x = 10
     y = 12
     # Output: x > y is False
     print('x > y  is',x>y)
     # Output: x < y is True
     print('x < y  is',x<y)
     # Output: x == y is False
     print('x == y is',x==y)
     # Output: x != y is True
     print('x != y is',x!=y)
     # Output: x >= y is False
     print('x >= y is',x>=y)
     # Output: x <= y is True
     print('x <= y is',x<=y)


#### 3. Assignment Operators:
     Assignment operators are used in Python to assign values to variables.
     a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
     There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.
     Operator	Example	Equivalent to
     =	x = 5	x = 5
     +=	x += 5	x = x + 5
     -=	x -= 5	x = x - 5
     *=	x *= 5	x = x * 5
     /=	x /= 5	x = x / 5
     %=	x %= 5	x = x % 5
     //=	x //= 5	x = x // 5
     **=	x **= 5	x = x ** 5
     Example:
     x = 5
     x += 5
     print(x)
     x *= 5
     print(x)
     x /= 5
     print(x)
     x %= 5
     print(x)
     x //= 5
     print(x)
     x **= 5
     print(x)

#### 4. Logical Operators:
     Logical operators are the and, or, not operators.
     Operator	Meaning	Example
     and	Logical AND	x and y
     or	Logical OR	x or y
     not	Logical NOT	not x
     Example:
     x = True
     y = False
     # Output: x and y is False
     print('x and y is',x and y)
     # Output: x or y is True
     print('x or y is',x or y)
     # Output: not x is False
     print('not x is',not x)

#### 5. Bitwise Operators:

     Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.
     For example, 2 is 10 in binary and 7 is 111.
     In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
     Operator	Meaning	Example
     &	Bitwise AND	x & y = 0 (0000 0000)
     |	Bitwise OR	x | y = 14 (0000 1110)
     ~	Bitwise NOT	~x = -11 (1111 0101)
     ^	Bitwise XOR	x ^ y = 14 (0000 1110)
     <<	Bitwise left shift	x << 2 = 40 (0010 1000)
     >>	Bitwise right shift	x >> 2 = 2 (0000 0010)
     Example:
     x = 10
     y = 4
     # Output: x & y = 0
     print('x & y =',x&y)
     # Output: x | y = 14
     print('x | y =',x|y)
     # Output: x ^ y = 14
     print('x ^ y =',x^y)
     # Output: ~x = -11
     print('~x =',~x)
     # Output: x << 2 = 40
     print('x << 2 =',x<<2)
     # Output: x >> 2 = 2
     print('x >> 2 =',x>>2)

#### 6. Membership Operators:
     Membership operators are used to test if a sequence is presented in an object.
     Operator	Meaning	Example
     in	True if value/variable is found in the sequence	x in y, here in results in a 1 if x is a member of sequence y.
     not in	True if value/variable is not found in the sequence	x not in y, here not in results in a 1 if x is not a member of sequence y.
     Example:
     x = 'Hello world'
     y = {1:'a',2:'b'}
     # Output: True
     print('H' in x)
     # Output: True
     print('hello' not in x)
     # Output: True
     print(1 in y)
     # Output: False
     print('a' in y)

#### 7. Identity Operators:
     Identity operators compare the memory locations of two objects. There are two Identity operators explained below:
     Operator	Meaning	Example
     is	True if the operands are identical (refer to the same object)	x is True
     is not	True if the operands are not identical (do not refer to the same object)	x is not True
     Example:
     x = 5
     y = 5
     z = 'Hello'
     # Output: True
     print(x is y)
     # Output: False
     print(x is z)
     # Output: True
     print(x is not z)

#### 8. Operator Precedence:
     The following table lists all operators from highest precedence to lowest.
     Operator	Description
     **	Exponentiation
     ~ + -	Complement, unary plus and minus (method names for the last two are +@ and -@)
     * / % //	Multiply, divide, modulo and floor division
     + -	Addition and subtraction
     >> <<	Right and left bitwise shift
     &	Bitwise 'AND'
     ^ |	Bitwise exclusive `OR' and regular `OR'
     <= < > >=	Comparison operators
     <> == !=	Equality operators
     = %= /= //= -= += *= **=	Assignment operators
     is is not	Identity operators
     in not in	Membership operators
     not or and	Logical operators
     Example:
     x = 10
     y = 12
     # Output: x > y is False
     print('x > y  is',x>y)
     # Output: x < y is True
     print('x < y  is',x<y)
     # Output: x == y is False
     print('x == y is',x==y)
     # Output: x != y is True
     print('x != y is',x!=y)
     # Output: x >= y is False
     print('x >= y is',x>=y)
     # Output: x <= y is True
     print('x <= y is',x<=y)

#### 9. Ternary Operator:
     Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5.
     It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.
     [on_true] if [expression] else [on_false]
     Example:
     x, y = 10, 20
     # Copy value of x in min if x < y else copy value of y
     min = x if x < y else y
     print(min)

#### 10. Special Operators:
     Python language offers some special types of operators like the identity operator or the membership operator. They are described below with examples.
     1. Identity Operators:
     is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal do not imply that they are identical.
     Example:
     x1 = 5
     y1 = 5
     x2 = 'Hello'
     y2 = 'Hello'
     x3 = [1,2,3]
     y3 = [1,2,3]
     # Output: False
     print(x1 is not y1)
     # Output: True
     print(x2 is y2)
     # Output: False
     print(x3 is y3)
     2. Membership Operators:
     in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set, and dictionary).
     In a dictionary we can only test for presence of key, not the value.
     Example:
     x = 'Hello world'
     y = {1:'a',2:'b'}
     # Output: True
     print('H' in x)
     # Output: True
     print('hello' not in x)
     # Output: True
     print(1 in y)
     # Output: False
     print('a' in y)
     3.equality operator
     == and != are the equality operators in Python. They are used to compare two objects. The == operator checks the equality of two objects while the != operator checks the inequality.
     Example:
     x = 5
     y = 5
     z = 'Hello'
     # Output: True
     print(x == y)
     # Output: False
     print(x == z)
     # Output: True
     print(x != z)


#### 11. Operator Overloading:
     Python operators work for built-in classes. But the same operator behaves differently with different types. For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
     This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.
     Example:
     class A:
           def __init__(self, a):
                self.a = a
           def __add__(self, o):
                return self.a + o.a
     ob1 = A(1)
     ob2 = A(2)
     ob3 = A("Geeks")
     ob4 = A("For")
     print(ob1 + ob2)
     print(ob3 + ob4)

     ##output
     3    # 1+2
     GeeksFor  # Geeks+For

#### 12. Some important points:
     1. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     2. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     3. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     4. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     5. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     6. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     7. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     8. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     9. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     10. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     11. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     12. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     13. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     14. The operators are actually functions, and what's more, we can even define our own operators using these functions.
     15. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     16. The operators are actually functions, and what's
     17. The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
     

### Difference  in,is,== vs not in ,is not , in table format
     | Operator | Description | Example |
     | --- | --- | --- |
     | in | True if value/variable is found in the sequence | x in y, here in results in a 1 if x is a member of sequence y. |
     | not in | True if value/variable is not found in the sequence | x not in y, here not in results in a 1 if x is not a member of sequence y. |
     | is | True if the operands are identical (refer to the same object) | x is True |
     | is not | True if the operands are not identical (do not refer to the same object) | x is not True |
     | == | Equality operators | x == y |
     | != | Equality operators | x != y |    

### Difference between == and is operator

