# Python-Tutorial-LeetCode 

## An journal of Python study 
  - Practice with Leetcode 
  - [Tutorial](https://www.python-course.eu/python3_course.php) 
  
### Identation 
Python use identation as coding blocks 

### Data types & variables 
In C: need to implement data types from scratch, design memory structure, mem arrangement;

Python: dict

Variable names: 

C/C++/Java: declare variable names, as reserving memory 

  int x = 42;
  
Python: can change both value & type  

  i = 42
  
  reason: python variables are references to objects (an arbitary data type)
  
### Naming convention 

### Immutable Strings

>>> s = "Some things are immutable!"

>>> s[-1] = "."
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''


>>> a is b: check the same memory location 
  
>>> a == b: check content only 



### Sequential data types 
6 sequential data types in python: 
Same functions and syntax are used for them; 

i.e. len(country)

- Strings 
- Byte sequences 
- byte arrays 
- lists
- tuples 
- range objects 

>>> lst = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]

>>> print(lst[0])

>>> print(lst[-1]): Print last one 
  
  
### Lists 
list.append(x)
list.remove(x)
list.insert(i, x)

### Heap queue (Heapq)
Heap structure used to represent a priority queue. 

"heapq" module in Python.

pop / heap[0]: returns the smallest element each time;

When elements are pushed or popped, heap structure is maintained. 

Opearations: 

- 1. heapq.heapify(iterable): convert the iterable into a heap data structure 
- 2. heapq.heappush(heap, element): insertion 
- 3. heapq.heappop(heap): remove && return the smallest element 
- 4. heapq.heappushpop(heap, ele)
- 5. heap.heapreplace(heap, ele): first pop, then push 
- 6. heap.nlargest(k, iterable, key = fun)
- 7. heap.nsmallest(k, iterable, key = fun)

### Sets
based on Hash table, check whether an element is present.

Same as {"a", "b","c"} 

normal_set = set(["a", "b","c"]) 


### self: 
The difference between Class Variables v.s. Instance Variables;
Class method && Instance method: 


### sorted: 
Both list.sort() and sorted() have a key parameter to specify a function to be called on each list element prior to making comparisons.

>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

all of the Py2.x versions supported a cmp parameter to handle user specified comparison functions.
>>> def numeric_compare(x, y):
...     return x - y
>>> sorted([5, 2, 4, 1, 3], cmp=numeric_compare) # doctest: +SKIP
[1, 2, 3, 4, 5]




  
