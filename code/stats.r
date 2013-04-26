
#NOTE: This is R code. I ran out of time to learn Python in addition to Unix and Github. Next week, hopefull.

#CREATE FUNCTION TO COMPUTE ALL STATISTICS

stats=function(d) #computes all statistics
{
	print(paste("Minimum = ",round(min(d),4), sep=""))
	print(paste("Maximum = ",round(max(d),4), sep=""))
	print(paste("Mean = ",round(mean(d),4), sep=""))
	print(paste("Median = ",round(median(d),4), sep=""))
	print(paste("Standard deviation = ",round(sd(d),4), sep=""))
	print(paste("Mean = ",round(mean(d),4), sep=""))
}

######READ IN FILE

toDir="/Volumes/NO NAME/Grad school_112212/Grad school/Class/Data mining"
setwd(toDir)
filename="P00000001-CA.csv"
F=read.csv(filename, header=T, row.names=NULL) #read in file

d=D$contbr_occupation ##had some file input difficulty, so column names are shifted
		##contbr-occupation corresponds to the contb_receipt_amt column 
d=d[which(d>0)] #drop 8120 data points with negative contributions.

#GET STATS
stats(d)
print (sort(unique(D$cand_id))) #Prints the names of different candidates. again, column names are shifted. 
range=abs(min(d))+abs(max(d)) #range of data
f=(d-min(d))/range #normalize data, which is very right-skewed due to a few very large donations
print(f)

###EXTRA CREDIT
print("EXTRA CREDIT")

##z-scores
print("Z-scores") 
z=(d-mean(d))/sd(d)
print(z)

#stats by candidate
cands=sort(unique(D$cand_id))
for (i in i:length(cands))
{
temp=subset(D, cand_id==as.character(cands[i]))
d=temp$contbr_occupation
d=d[which(d>0)] #drop data points with negative contributions.
print(paste("For candidate ", as.character(cands[i]),":",sep=""))
stats(d)
}





