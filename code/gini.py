#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)

ZIPS={}
totaldonors=0
csv.reader(fileinput.input()):
	    if not fileinput.isfirstline():
	    	if not row[contr_zip] in ZIPS:
				ZIPS[row[contbr_zip]]=[row]
			else:
				ZIPS[row[contbr_zip]].append(row)
			totaldonors+=1

def Gini (list_of_rows):
############### Set up variables
# TODO: declare datastructures
	denom=0
	CC={}  ##dictionary for candidate counter
	############### Read through files
	for row in list_of_rows
	        if not row[cand_nm] in CC:
	        	CC[row[cand_nm]]=1
	        else:
	        	CC[row[cand_nm]]+=1
	        denom+=1

	###
	# TODO: calculate the values below:

	ginipieces = [] ##create list for the individual pieces of Gini Index
	for key in CC:
		ginipieces.append((CC[key]/float(denom))**2) # current Gini Index using candidate name as the class
	return =  1-sum(ginipieces) #.2914 for entire data set

####################DO EVERYTHING

Gini(alldata)

ZipGinis=[] #create list to hold Ginis for all zip codes

for key in ZIPS:
	ZipGinis.append(Gini(ZIPS[key])*len(ZIPS[key])/totaldonors) #Call our function, have it iterate over each dictionary key
	

split_gini = sum(ZipGinis) # weighted average of the Gini Indexes using candidate names, split up by zip code
##/


print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
