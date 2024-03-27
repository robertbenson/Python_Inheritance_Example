
# Inheritance Example using Python
## Description
## Stack class:

`__init__(self):` Initialises an empty stack (private).

`push(self, val):` Adds the value to the top of the stack.

`pop(self):` Removes and returns the top element from the stack.

## SumStack class (inherits from Stack):


`__init__(self):` Initialises an empty stack and sets the sum to 0.

`get_sum(self):` Returns the sum of elements currently in the stack.

`push(self, val):` Overrides the push method of the Stack class to add val to the sum before pushing it onto the stack.

`pop(self):` Overrides the pop method of the Stack class to subtract the popped value from the sum before returning it.


<img src="Assets/Python_inheritance.png" width="300">



### Enhanced functionality

The SumStack class extends the functionality of the Stack class by keeping track of the sum of elements pushed onto or popped from the stack.














# Output
## Name Mangling

`__stack_list --> _Stack__stack_list`

`__sum --> _SumStack__sum`


```python
push: 0{'_Stack__stack_list': [0], '_SumStack__sum': 0}
push: 1{'_Stack__stack_list': [0, 1], '_SumStack__sum': 1}
push: 2{'_Stack__stack_list': [0, 1, 2], '_SumStack__sum': 3}
push: 3{'_Stack__stack_list': [0, 1, 2, 3], '_SumStack__sum': 6}
push: 4{'_Stack__stack_list': [0, 1, 2, 3, 4], '_SumStack__sum': 10}
Total: 10
pop: 4{'_Stack__stack_list': [0, 1, 2, 3], '_SumStack__sum': 6}
pop: 3{'_Stack__stack_list': [0, 1, 2], '_SumStack__sum': 3}
pop: 2{'_Stack__stack_list': [0, 1], '_SumStack__sum': 1}
pop: 1{'_Stack__stack_list': [0], '_SumStack__sum': 0}
pop: 0{'_Stack__stack_list': [], '_SumStack__sum': 0}```
