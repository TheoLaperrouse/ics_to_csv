import csv
from icalendar import Calendar

def ics_to_csv(ics_file_path, csv_file_path):
    """Transform a calendar in ics to csv"""
    with open(ics_file_path, 'rb') as ics_file:
        cal = Calendar.from_ical(ics_file.read())

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(['Titre', 'Description', 'Date', 'Lieu'])
           
            for event in cal.walk('vevent'):
                start_time = event.get('dtstart').dt.strftime('%Y-%m-%d %H:%M:%S')
                summary = event.get('summary')
                description = event.get('description', '')
                location = event.get('location', '')
                csv_writer.writerow([summary, description, start_time, location])

if __name__ == "__main__":
    ics_to_csv("calendar.ics", "calendar.csv")
    print("CSV file generated successfully from ics")
