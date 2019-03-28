import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('/home/al220/Documents/graph.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y, marker='o',color="green")

plt.title('Data from the CSV File: People and Expenses')

plt.xlabel('Number of People')
plt.ylabel('Expenses')

plt.show()

