import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')

new_month = []
total_month = 0
total = 0
value = []
month_year = []

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        # print(row[0])

# TO FIND THE TOTAL MONTH AND TOTAL VALUE

        if len(row[0]) > 0:
            month = total_month + 1
            new_month.append(month)
            total_month = total_month + 1
            sum = float(row[1])
            total = total + sum
            value.append(int(row[1]))
            mon_year = row[0]
            month_year.append(mon_year)
#print(month_year)
#print(new_value)
#print(len(value))              
#print(value)

print(f'Total Months: {len(new_month)}')
print(f'Total: ${int(total)}')

# TO POPULATE THE CHANGE LIST

new_diff = []
initial_value = 0
for i in range(len(value)):
    new_value = value[i] - initial_value
    initial_value = value[i]
    new_diff.append(new_value)
# print(new_diff)


# TO FIND THE AVERAGE

sm = 0
for i in range(len(new_diff)):  
    sum = new_diff[i] + sm
    sm = sum 
sm = sm - new_diff[0]
n = len(new_diff)
# print(n)
average = sm / (n - 1)
print(f'Average Change: ${average:.2f}')
# print(sm)


# TO FIND THE GREATEST INCREASE

max = 0
for i in range(len(new_diff)):
    if new_diff[i] > max:
        max = new_diff[i]
    else:
        max = max
        
max_month_index = new_diff.index(max)
# print(max)
# print(max_month_index)
print(f'Greatest Increase in Profits: {month_year[max_month_index]} (${max})')



# TO FIND THE GREATEST DECREASE

min = 0
for i in range(len(new_diff)):
    if new_diff[i] < min:
        min = new_diff[i]
    else:
        min = min

min_month_index = new_diff.index(min)
print(f'Greatest Decrease in Profits: {month_year[min_month_index]} (${min})')


# print(min)
# max_month = row[max_month_index]
# print(max_month)
# # print(max_month_index)



txtpath = os.path.join("PyBank","Analysis", "analysis.txt")
with open(txtpath, 'w') as outfile:
    outfile.write("Financial Analysis \n")
    outfile.write("------------------------- \n")
    outfile.write(f'Total Months: {len(new_month)}' + '\n')
    outfile.write(f'Total: ${int(total)}' + '\n')
    outfile.write(f'Average Change: ${average:.2f}' + '\n')
    outfile.write(f'Greatest Increase in Profits: {month_year[max_month_index]} (${max})' + '\n')
    outfile.write(f'Greatest Decrease in Profits: {month_year[min_month_index]} (${min})' + '\n')
