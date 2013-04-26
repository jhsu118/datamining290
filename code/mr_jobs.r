setwd("/Users/joannahsu/Documents/Courses/datamining290/code")
allD <- fromJSON(paste(readLines("business_c.json"), collapse=""))
allD <- fromJSON(file="business_c.json")
allD <- fromJSON(paste(readLines("business_c.json")))