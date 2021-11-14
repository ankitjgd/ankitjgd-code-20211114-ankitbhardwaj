This package open up provided data file, 
reads data from it and 
return the number of overweight people it finds in data.

example usage:

from bmiCalculator import calculator

obj = calculator('data.json')
own = obj.get_overweight_number()
print(own)