##hw-elasticity

from math import log, exp
from scipy.stats import linregress
import csv
data=csv.reader("price-elasticity.csv")

 
with open('price-elasticity.csv', 'rU') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ')
  for row in reader:
    print row 


slope, intercept, r_value, p_value, std_err = linregress(y, x)