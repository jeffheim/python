# read a text file, make an ics file
import datetime

from ics import Calendar, Event

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
cal = Calendar()

file = '/home/jeff/gramps/Pauls_birthday_report.txt'

# example

#January
#7
#* (2007) Berger, Annalise Corrin, 14
#* (2007) Berger, Tamarra Katrin, 14
#19
#* (1973) Wood, Andrew Huntington, 48

for line in open(file):
    if line.rstrip() in months:
        month = line.rstrip()
        month_num = months.index(month) + 1
#        print ('month is', month)
    elif line.rstrip()[0].isnumeric():
        date = line.rstrip()
#        print ('date: ' + line.rstrip()[0])
    elif line.rstrip().startswith('*'):
        items = line.split()
        datestr = datetime.datetime(2021, int(month_num), int(date))
        entry = ' '
        entry = entry.join(items[2:])
        # get 3 fields
        fields = entry.split()
        
        short = fields[0] + fields[1] + ' ' + fields[-1]
        print (datestr, ' ', short)
        # make/add the calendar event
        e = Event()
        e.name = short
# e.begin = '2021-01-03 09:00:00'
        e.begin = datestr
        e.make_all_day()
        e.end
        cal.events.add(e)
    else:
        pass
        #print ("skip: ", line.rstrip())
        
    #print(line, end='')

cal.events

# {<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>}

with open('pauls.ics', 'w') as f:

    f.writelines(cal)