import datetime

date = datetime.datetime.now()
date = date.timetuple()

for index in date:
    print(index)
