import math

l = 10 # learning rate
t_6 = 0 #expected output
# initial values
o_6 = 0.8387
# Setup hidden node 5
o_1 = 1 ; w_13 = -3 ; w_14=2 ; w_15 = 4
o_2 = 2 ; w_23 = 2 ; w_24=-3 ; w_25 = 0.5
o_3 = 0.7311 ; w_36 = 0.2
o_4 = 0.0179 ; w_46 = 0.7
o_5 = 0.9933 ; w_56 = 1.5

for i in range(0,1):
	# Output Error -0.11346127339699999
	err_6 = o_6*(1-o_6)*(t_6-o_6)
	#Errors for hidden layer
	# Error for node 5 = -0.0011326458827956695
	err_3 = o_3*(1-o_3)*(err_6*w_36)
	err_4 = o_4*(1-o_4)*(err_6*w_46)
	err_5 = o_5*(1-o_5)*(err_6*w_56)
	#new weights
	w_36 = w_36 + l*err_6*o_3
	w_46 = w_46 + l*err_6*o_4
	w_56 = w_56 + l*err_6*o_5
	w_13 = w_13 + l*err_3*o_1
	w_14 = w_14 + l*err_4*o_1
	w_15 = w_15 + l*err_5*o_1
	w_23 = w_23 + l*err_3*o_2
	w_24 = w_24 + l*err_4*o_2
	w_25 = w_25 + l*err_5*o_2
	weights = [err_5, err_4, err_3,err_6, w_25,w_23,w_24,w_13,w_14,w_15,w_36,w_46,w_56]
	#calculate new outputs
	o_3 = 1/(1+math.exp(-(o_1*w_13+o_2*w_23)))
	o_4 = 1/(1+math.exp(-(o_1*w_14+o_2*w_24)))
	o_5 = 1/(1+math.exp(-(o_1*w_15+o_2*w_25)))
	o_6 = 1/(1+math.exp(-(o_3*w_36+o_4*w_46+o_5*w_56)))
	print "iteration %d" % (i)
	print "o_6 %s" % o_6
	print "weights " , weights

