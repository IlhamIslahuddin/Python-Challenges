from datetime import datetime

def calculate_project_duration(start_date, end_date):
    date_format = "%d/%m/%Y"

    try:
        # Convert the string input dates to datetime objects using the new format
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        
        # Check if the end date is earlier than the start date
        if end < start:
            raise ValueError("End date cannot be earlier than start date.")
        
        # Calculate the difference in days
        duration = (end - start).days
        return duration
    
    except ValueError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    start_date = input("Enter the start date (dd/mm/yyyy): ")
    end_date = input("Enter the end date (dd/mm/yyyy): ")

    result = calculate_project_duration(start_date, end_date)
    print(f"Project duration: {result} days")
