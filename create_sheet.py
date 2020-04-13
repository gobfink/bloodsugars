import csv
from collections import defaultdict

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
 
print (date_dict)
date_sorted = {}
date_strings = {}
for date in date_dict:
    print (date)
    #print (date_dict[date])

    time_sorted = []
    count = 0
    for lower_bound,upper_bound in time_seperators:
        #print ("lower_bound:" + str(lower_bound) + ", upper_bound: " + str(upper_bound))
        time_sorted.append([ time_bsugar for time_bsugar in date_dict[date] if lower_bound <= int(time_bsugar[0]) <= upper_bound])
        time_sorted[-1].sort()
        
        count += 1
    date_sorted[date]=time_sorted
    lens = [ len(t) for t in time_sorted ]
    print (lens)
    rows = max (lens)
    table_rows=[]
    
    for row in range(0,rows):
        table_row = ""
        for t in range(0,len(time_seperators)):
            print ("t - "+ str(t) +" row - "+ str(row) + "len(time_sorted[t]): " + str(len(time_sorted[t])))
            if len(time_sorted[t]) <= row :
                # if its empty print an empty spot
                table_row += "|              |"
            else:
                table_row += "|  %4d - %3d  |"%(int(time_sorted[t][row][0]),int(time_sorted[t][row][1]))
            
        table_rows.append(table_row)
    print (table_rows)
    print(time_sorted)
    date_strings[date]=table_rows
"""
    for time_bsugars in date_dict[date]:
        print(time_bsugars)
        print(time_bsugars[0])
        time=int(time_bsugars[0])

        
        
        if time < upper_value[0]:
            print (str(time) +"<"+ str(upper_value[0]))
        elif time < upper_value[1]:
            print (str(time) +"<" +str(upper_value[1]))
        elif time < upper_value[2]:
            print (str(time) +"<" + str(upper_value[2]))
        elif time < upper_value[3]:
            print (str(time) +"<" + str(upper_value[3]))
        elif time < upper_value[4]:
            print (str(time) +"<" + str(upper_value[4]))
        elif time < upper_value[5]:
            print (str(time) +"<" + str(upper_value[5]))
        elif time < upper_value[6]:
            print (str(time) +"<" + str(upper_value[6]))
        else :
            print (str(time) +"<" + str(upper_value[7]))
"""
title_row="Date    | [%4d, %4d]"%(time_seperators[0][0],time_seperators[0][1])
for i in range(1,len(time_seperators)):
    title_row += " || " + str("[%4d, %4d]"%(time_seperators[i][0],time_seperators[i][1]))
seperator_row ="======================================================================================================================================="
date_seperator="---------------------------------------------------------------------------------------------------------------------------------------"

print(seperator_row)
print (title_row)
print(seperator_row)
print ()

for date in date_strings:
    #print (date)
    for row in range(0,len(date_strings[date])):
        print (date + date_strings[date][row])
    print (date_seperator)

print (seperator_row)
