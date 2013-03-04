#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures
denom=0
CC={}  ##dictionary for candidate counter
############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        # Gini Index
        #row[cand_nm], row[contbr_zip]
        if not row[cand_nm] in CC:
        	CC[row[cand_nm]]=1
        else:
        	CC[row[cand_nm]]+=1
        denom+=1

        ##/
print denom
print CC

###
# TODO: calculate the values below:
gini =  1-sum(CC[cand_nm}]) # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/


print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
