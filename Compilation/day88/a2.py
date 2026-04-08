import statistics

daily_sales = [150,200,150,300,250,150,400]


average_sales = statistics.mean(daily_sales)


median_sales = statistics.mode(daily_sales)



print(f"Average Sales:{average_sales}")
print(f"Meidan Sales:  {median_sales}")
print(f"Most Common Sales Amount: {mode_sales}")