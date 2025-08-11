import datetime
from zoneinfo import ZoneInfo

# Define the timezone for IST (Asia/Kolkata)
ist = ZoneInfo('Asia/Kolkata')

# Start date: August 11, 2025 (Monday)
start_date = datetime.date(2025, 8, 11)

# Function to create iCalendar event string for daily weekday recurrences
def create_daily_event(summary, start_time, end_time, description=''):
    dtstart = datetime.datetime.combine(start_date, start_time, tzinfo=ist)
    dtend = datetime.datetime.combine(start_date, end_time, tzinfo=ist)
    
    event = 'BEGIN:VEVENT\n'
    event += f'SUMMARY:{summary}\n'
    event += f'DTSTART;TZID=Asia/Kolkata:{dtstart.strftime("%Y%m%dT%H%M%S")}\n'
    event += f'DTEND;TZID=Asia/Kolkata:{dtend.strftime("%Y%m%dT%H%M%S")}\n'
    event += 'RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR\n'  # Repeat weekly on weekdays
    if description:
        event += f'DESCRIPTION:{description}\n'
    event += f'UID:{summary.replace(" ", "_")}_{dtstart.strftime("%Y%m%dT%H%M%S")}@tradingroutine\n'
    event += 'END:VEVENT\n'
    return event

# Function for weekly day-specific events
def create_weekly_event(summary, start_time, end_time, byday, description=''):
    dtstart = datetime.datetime.combine(start_date, start_time, tzinfo=ist)
    dtend = datetime.datetime.combine(start_date, end_time, tzinfo=ist)
    
    event = 'BEGIN:VEVENT\n'
    event += f'SUMMARY:{summary}\n'
    event += f'DTSTART;TZID=Asia/Kolkata:{dtstart.strftime("%Y%m%dT%H%M%S")}\n'
    event += f'DTEND;TZID=Asia/Kolkata:{dtend.strftime("%Y%m%dT%H%M%S")}\n'
    event += f'RRULE:FREQ=WEEKLY;BYDAY={byday}\n'
    if description:
        event += f'DESCRIPTION:{description}\n'
    event += f'UID:{summary.replace(" ", "_")}_{dtstart.strftime("%Y%m%dT%H%M%S")}@tradingroutine\n'
    event += 'END:VEVENT\n'
    return event

# Function for overnight events (spans to next day)
def create_overnight_event(summary, start_time, end_time_next_day, description=''):
    dtstart = datetime.datetime.combine(start_date, start_time, tzinfo=ist)
    dtend = datetime.datetime.combine(start_date + datetime.timedelta(days=1), end_time_next_day, tzinfo=ist)
    
    event = 'BEGIN:VEVENT\n'
    event += f'SUMMARY:{summary}\n'
    event += f'DTSTART;TZID=Asia/Kolkata:{dtstart.strftime("%Y%m%dT%H%M%S")}\n'
    event += f'DTEND;TZID=Asia/Kolkata:{dtend.strftime("%Y%m%dT%H%M%S")}\n'
    event += 'RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR\n'
    if description:
        event += f'DESCRIPTION:{description}\n'
    event += f'UID:{summary.replace(" ", "_")}_{dtstart.strftime("%Y%m%dT%H%M%S")}@tradingroutine\n'
    event += 'END:VEVENT\n'
    return event

# List of events
events = []

# Daily weekday events (Indian routine)
events.append(create_daily_event(
    'Pre-Market Preparation',
    datetime.time(7, 0),
    datetime.time(9, 15),
    'Review global markets, economic calendar, option chain scan.'
))

events.append(create_daily_event(
    'Opening Session',
    datetime.time(9, 15),
    datetime.time(10, 15),
    'ORB, gaps, high volatility trades.'
))

events.append(create_daily_event(
    'Mid-Morning Monitoring',
    datetime.time(10, 15),
    datetime.time(12, 0),
    'Trend assessment, option chain re-scan.'
))

events.append(create_daily_event(
    'Lunch Hour Check',
    datetime.time(12, 0),
    datetime.time(13, 0),
    'Range trades, European cues.'
))

events.append(create_daily_event(
    'Afternoon Session',
    datetime.time(13, 0),
    datetime.time(14, 30),
    'Swing trades, US pre-market review.'
))

events.append(create_daily_event(
    'Closing Hour Execution',
    datetime.time(14, 30),
    datetime.time(15, 30),
    'Momentum, expiry plays.'
))

events.append(create_daily_event(
    'Post-Market Review',
    datetime.time(15, 30),
    datetime.time(16, 30),
    'Log trades, next-day prep.'
))

# Weekly day-specific overlays
events.append(create_weekly_event(
    'Monday: Gap Focus',
    datetime.time(9, 15),
    datetime.time(10, 15),
    'MO',
    'Gap trading based on weekend news.'
))

events.append(create_weekly_event(
    'Tuesday: Nifty Expiry Focus',
    datetime.time(14, 30),
    datetime.time(15, 30),
    'TU',
    'High gamma, options strategies.'
))

events.append(create_weekly_event(
    'Wednesday: Mid-Week Analysis',
    datetime.time(10, 15),
    datetime.time(12, 0),
    'WE',
    'Sector rotation, range strategies.'
))

events.append(create_weekly_event(
    'Thursday: Sensex Expiry Focus',
    datetime.time(14, 30),
    datetime.time(15, 30),
    'TH',
    'Volatility plays, arbitrage.'
))

events.append(create_weekly_event(
    'Friday: Position Squaring',
    datetime.time(14, 30),
    datetime.time(15, 30),
    'FR',
    'Defensive plays, weekly review.'
))

# Global market sessions (recurring weekdays)
# Asian Overlap
events.append(create_daily_event(
    'Asian Markets Open (Japan, HK, China)',
    datetime.time(5, 30),
    datetime.time(7, 0),
    'Monitor pre-market bias from Asian opens: Japan 5:30-11:30 AM, HK 6:45-1:30 PM, Shanghai 7:00-12:30 PM IST.'
))

# European Overlap
events.append(create_daily_event(
    'European Markets Overlap',
    datetime.time(12, 30),
    datetime.time(14, 30),
    'Mid-session cues: Euronext/Deutsche Börse 12:30 PM-9:00 PM, London 1:30 PM-10:00 PM IST.'
))

# US Markets (overnight)
events.append(create_overnight_event(
    'US Markets (NYSE/NASDAQ)',
    datetime.time(19, 0),
    datetime.time(1, 30),
    'Next-day gap projection: 7:00 PM - 1:30 AM IST.'
))

# Gift Nifty Sessions
events.append(create_daily_event(
    'Gift Nifty Session 1',
    datetime.time(6, 30),
    datetime.time(15, 40),
    'Continuous trading overlap with Indian market.'
))

events.append(create_overnight_event(
    'Gift Nifty Session 2',
    datetime.time(16, 35),
    datetime.time(2, 45),
    'Post-market trend indication.'
))

# MCX Commodity Session
events.append(create_daily_event(
    'MCX Commodity Trading',
    datetime.time(9, 0),
    datetime.time(23, 30),
    'Monitor for sector correlations (energy, metals).'
))

# Build the full ICS content
ics_content = 'BEGIN:VCALENDAR\n'
ics_content += 'VERSION:2.0\n'
ics_content += 'PRODID:-//Trading Routine//EN\n'
ics_content += 'BEGIN:VTIMEZONE\n'
ics_content += 'TZID:Asia/Kolkata\n'
ics_content += 'BEGIN:STANDARD\n'
ics_content += 'TZOFFSETFROM:+0530\n'
ics_content += 'TZOFFSETTO:+0530\n'
ics_content += 'TZNAME:IST\n'
ics_content += 'DTSTART:19700101T000000\n'
ics_content += 'END:STANDARD\n'
ics_content += 'END:VTIMEZONE\n'

for event in events:
    ics_content += event

ics_content += 'END:VCALENDAR\n'

# Output the ICS content (save this to a .ics file)
print(ics_content)