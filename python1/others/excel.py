import openpyxl
from datetime import datetime, timedelta

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Set the headers
headers = ["Date", "Day", "Project Name", "Task Name","Total Hour"]
sheet.append(headers)

# Define the date range (from 21 August 2023 to 20 September 2023)
start_date = datetime(2024, 1, 21)
end_date = datetime(2024, 2, 20)
current_date = start_date

# Project name
project_name = "Task Station 23"

# Iterate through the date range and fill in the sheet
while current_date <= end_date:
    # Extract date components
    date = current_date.strftime("%d/%m/%Y")
    day = current_date.strftime("%A")

    # Add a row to the sheet
    sheet.append([date, day, project_name, "", "",'8hr'])
    
    # Move to the next day
    current_date += timedelta(days=1)

# Save the workbook
workbook.save("worklog.xlsx")
