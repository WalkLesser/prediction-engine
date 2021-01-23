import predictor as p
import json

def getData(term, week, day):
    #First trys to get data from file, if not found calls generator function
    #Makes sure bad data is not given (probably not needed)
    if term > 4 or day > 5:
        return "Give me proper data you nong"
    f = open("days.json")
    days = json.load(f)
    dayID = str(term)+'-'+str(week)+'-'+str(day)
    for key in days:
        if key == dayID:
            return days[dayID]["Overall"]
    #This will get the data
    return p.callData(term, week, day)["Overall"]