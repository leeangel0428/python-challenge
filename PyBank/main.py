import csv
my_report=open("analysis/report.txt","w") 

data = csv.reader(open('Resources/Xbudget_data.csv'))

#Tasks to do list:
#Find the total number of months 
#Find the net total amount of "Profit/Losses" 
#Find the changes in "Profit/Losses" over the entire period & avg them
#Find the greatest increase in profits (date and amount) 
#Find the greatest decrease in profits (date and amount) 

#Skips header
header = next(data)

#Defining variables 
months= 0
totalProfitAndLosses= 0
Change= 0
total_ch= 0
PrevMos= 0
firstRowFlag= 1
profitIncrease= 0
greatestIncrease= 0
greatestMonth= ""

#These variables are slightly different than the ones above bc they hold two values in the list, nothing and value 0
inc=["",0] 
dec=["",0]

#Loop that'll get all the values I need for tasks above
for row in data:
    #Completes first task: counts all the rows
    months += 1
    #Completes second task: counts all the rows and adds their values
    totalProfitAndLosses += int(row[1]) 
    
    if (firstRowFlag==1):
        PrevMos=int(row[1])
        firstRowFlag=0

    Change=int(row[1])-PrevMos
        
    PrevMos=int(row[1])
    total_ch+= Change 

#Completes fourth task: finding greatest increase & fifth task: finding greatest decrease
    if Change > inc[1]:
        inc[0]=row[0]
        inc[1]= Change

    if Change < dec[1]:
        dec[0]=row[0]
        dec[1]= Change

#Completes task 3: finding average change
AvgChange= total_ch/(months-1)


output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${totalProfitAndLosses:,}
    Average Change: ${AvgChange:,.2f}
    Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
    Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''


print(output)

my_report.write(output)