import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    total_months = 0
    for months in reader:
        total_months+= 1
    print(total_months)







import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    total_amount = 0
    for row in csvreader:
        profit_loss = int(row[1])
        total_amount += profit_loss
    print(f"The total amount of Profit/Losses is {total_amount}")








import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    total_change = 0
    num_changes = 0
    prev_value = None
    for row in csvreader:
        value = int(row[1])
        if prev_value is not None:
            change = value - prev_value
            total_change += change
            num_changes += 1
        prev_value = value
    average_change = total_change / num_changes
    print(f"The average change in Profit/Losses is ${round(average_change, 2)}")


   





import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    greatest_increase = 0
    greatest_increase_date = ""
    prev_value = None
    for row in csvreader:
        date = row[0]
        value = int(row[1])
        if prev_value is not None:
            change = value - prev_value
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
        prev_value = value
    print(f"The greatest increase in profits was ${greatest_increase} on {greatest_increase_date}")


   




import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    greatest_decrease = 0
    greatest_decrease_date = ""
    prev_value = None
    for row in csvreader:
        date = row[0]
        value = int(row[1])
        if prev_value is not None:
            change = value - prev_value
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        prev_value = value
    print(f"The greatest decrease in profits was ${greatest_decrease} on {greatest_decrease_date}") 



    




    with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
        text_file.write(str(total_months))


    with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
        text_file.write(str(total_amount))

    with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
        text_file.write(str(average_change))

    with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
        text_file.write(str(greatest_increase))

    with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
        text_file.write(str(greatest_decrease))