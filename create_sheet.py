import csv
from collections import defaultdict
from statistics import stdev, mean, median

filepath = "C:/Users/Andy/Desktop/git/bloodsugars/Blood_sugars.csv"

time_seperators=[(0,600),(601,900),(901,1100),(1101,1300),(1301,1500),(1501,1700),(1701,2030),(2031,2359)]
upper_value=[seperators[1] for seperators in  time_seperators]
date_dict= defaultdict(list)

with open(filepath, newline='') as csvfile:
    bloodsugars = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in bloodsugars:
        day = row[0]
        time = row[1]
        b_sugar = row[2]        
        date_dict[day].append((time,b_sugar))
        
date_sorted = {}
date_strings = {}
time_values = {}
for date in date_dict:
    time_sorted = []
    for lower_bound,upper_bound in time_seperators:
        time_sorted.append([ time_bsugar for time_bsugar in date_dict[date] if lower_bound <= int(time_bsugar[0]) <= upper_bound])
        time_sorted[-1].sort()
        date_sorted[date]=time_sorted
    lens = [ len(t) for t in time_sorted ]
    rows = max (lens)
    table_rows=[]
    
    for row in range(0,rows):
        table_row = ""
        for t in range(0,len(time_seperators)):
            if len(time_sorted[t]) <= row :
                # if its empty print an empty spot
                table_row += "|              |"
            else:
                table_row += "|  %4d : %3d  |"%(int(time_sorted[t][row][0]),int(time_sorted[t][row][1]))
                if t not in time_values.keys():
                    time_values[t]=[int(time_sorted[t][row][1])]
                else:
                    time_values[t].append(int(time_sorted[t][row][1]))
            
        table_rows.append(table_row)
    #print (table_rows)
    #print(time_sorted)
    date_strings[date]=table_rows

#Done formatting the data now lets print out the sheet

seperator_row ="======================================================================================================================================="
date_seperator="---------------------------------------------------------------------------------------------------------------------------------------"    
title_row="Date    | [%4d, %4d]"%(time_seperators[0][0],time_seperators[0][1])
mean_row="Mean    |  %8f  |"%(mean(time_values[0]))
median_row="Median  |  %3d         |"%(median(time_values[0]))
stdev_row="Std.Dev.|  %8f  |"%(stdev(time_values[0]))
min_row="Min     |  %3d         |"%(min(time_values[0]))
max_row="Max     |  %3d         |"%(max(time_values[0]))

for i in range(1,len(time_seperators)):
    title_row += " || " + str("[%4d, %4d]"%(time_seperators[i][0],time_seperators[i][1]))
    mean_row += "| " + str(" %8f  |"%mean(time_values[i]))
    median_row += "| " + str(" %3d         |"%median(time_values[i]))
    stdev_row += "| " + str(" %8f   |"%stdev(time_values[i]))
    min_row += "| " + str(" %3d         |"%min(time_values[i]))
    max_row += "| " + str(" %3d         |"%max(time_values[i]))


print(seperator_row)
print (title_row)
print(seperator_row)
print ()

for date in date_strings:
    #print (date)
    for row in range(0,len(date_strings[date])):
        print (date + date_strings[date][row])
    print (date_seperator)

print (mean_row)
print (median_row)
print (stdev_row)
print (min_row)
print (max_row)
print (seperator_row)
