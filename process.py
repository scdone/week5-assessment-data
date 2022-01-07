log_file = open("um-server-01.txt")

#the statement above is opening the txt file here so the data inside can be manipulated


# def sales_reports(log_file):
#     for line in log_file:
#         line = line.rstrip()
#         day = line[0:3]
#         if day == "Tue":
#             print(line)

#The function above is going through the txt file we opened. It defines where day is in the data. If the "day" is "Tue" (for tuesday), it then prints that line of data.
# 
# the function below was changed to display data from monday instead of tuesday 

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#the statement below invokes the function above with the data from the txt file
sales_reports(log_file)


