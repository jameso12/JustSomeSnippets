# this is to follow along the intermidiate python 3 video from freecodecamp
# python collections and python itertools are one the things not
# practiced when viewed 
# but they seemed to have very specific and interesting applications
# should learn more about collections and itertools

l= list(((1,3), (2,1), (3, 0), (10, -1), (11, 4)))
l.sort(key = lambda l: l[1]*-1)
print(l)
a = list(range(10))
print(a)
y = 0

li = [(x + 1, y := y + 1) for x in a if x % 2 == 0] 
# notice how the walrus operator makes an assignment statement pass a an expression
print(li)
la = [(x*2, y := y + 1) for x in a] 

print(la)
var = 0
if (var := var + 1) == 1 :
    print("yes") 

test_list = list(range(7))
print(f"Original list\n{test_list}")
# now
# map(func, iterable)
"""
it is like a for loop in that it takes each element of iterable and passses it as 
argument to the function
"""
print('Map')
test_f = map(lambda x: x + 1, test_list)
print(list(test_f))

#filter(func, iterable)
"""
similar to map, but for this one, the function must return either true or false(bools)
and the filter function will add or return the elements to which the function passed as argument
returns to be true
"""
print("Filter")
test_f = filter(lambda x: x % 2 == 0, test_list)
print(list(test_f))

# reduce(func, iterable)
"""
repeatedly applies function to elements and returns single value
"""
from functools import reduce
test_f = reduce(lambda x, y: x+y, test_list)
print(test_f)

try:
    print(int('d'))
except (ValueError, FileNotFoundError) as er: # the 'er' var stores the message
    print('oops', er)

# tou can also raise an exception 
try:
    raise Exception("Git gud") # if this exception is not handled, it will print thi message
except:
    print('Casul')

# there is an assertion function or statement more like
# lets say
try:
    u = 1
    assert(u == 2), ' u is not 2!!'
    # this will trhpw an assertion error
except AssertionError as er1:
    print("See?!, assertion massage:\n", er1)
# you can define your own exceptions!!
class MyError(Exception):
    pass

fi = 2
try:
    if fi > 1:
        raise MyError("Greater than 1!!")
except Exception as e:
    print(e)

"""
input: a list of numbers
output: max number in the list

e.g: [2, 3, 8, 1, 15, 10] => 15

base case: [x] => x
otherwise: 

[2, 3, 8, 1, 15, 10] => max(10, 15) => 15
[2, 3, 8, 1, 15] => 15

  max_from_list([2, 3, 8, 1, 15, 10])
= max(2, max_from_list([3, 8, 1, 15, 10]))
= max(2, max(3, max_from_list([8, 1, 15, 10])))
= ...
= max(2, max(3, ... , max(15, max_from_list([10]))))
= max(2, max(3, ... , max(15, 10))))
= max(2, max(3, ... ,max(1, 15)))
= max(2, max(3, ... ,max(8, 15)))
"""

'''
def max_from_list(l):
  if len(l) == 1:
    return l[0]
  else:
    max_leftovers = max_from_list(l[1:])
    if l[0] >= max_leftovers:
      return l[0]
    else:
      return max_leftovers
    #return max(l[0], max_from_list(l[1:]))

'''

def max_from_list(l):
  if len(l) == 1:
    return l[0]
  else:
    max_leftovers = max_from_list(l[1:])
    print('before is statement',max_leftovers)
    if l[0] >= max_leftovers:
      print('l[0] after if statement',l[0])
      return l[0]
    else:
      print('on the else statement',max_leftovers)
      return max_leftovers
    # return max(l[-1], max_from_list(l[:-1]))# this is the simple and efficient implementation

print(max_from_list([2, 3, 20,8, 1, 15, 10]))


def longest_str(l): # l is list strs 
  if len(l) == 1:
    return l[0]
  else:
    return max(l[0], longest_str(l[1:]))


print("recursive max string in list solver")
print(longest_str(['l', 'llll','yes', 'yujssjfhgf', 'ddff', 'yujssjfhga']))

def another_implementation(l):
  longest_str = None
  for string in l:
    if longest_str is None:
      longest_str = string
    elif len(longest_str) < len(string):
      longest_str = string
  return longest_str

print(another_implementation(['l', 'llll','yes', 'yujssjfhgf', 'ddff']))

### collections
import collections
a = "lllllllaaaaaaattttttiiiiiieeeerrrraaaa" # a is an iterable
CC = collections.Counter(a)
print(CC)

print(CC.most_common(2)) # 2 arg tells that we want the 2 most common
# it has some more methods

james = collections.namedtuple('my', "y x a")
simon = james(1, 2, 3)
print(isinstance(simon,james))

