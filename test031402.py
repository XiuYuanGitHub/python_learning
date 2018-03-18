"""
Example 1-4
===========================
Filtering Python Lists
"""

sample_list = [ 25, 'A', 34, 'B', 45, 'C']

def filter_marks(lst):
    '''
      Filter integers from list and returns a tuple
    '''
    integers = []
    rest = []

    for ele in lst:
        if type(ele) is int:
            integers.append(ele)
        else:
            rest.append(ele)

    return integers,rest

integers, rests = filter_marks(sample_list)

print('Integers:',','.join([ str(x) for x in integers]))
print('Others:',','.join(rests))

print( str(x) for x in integers)
