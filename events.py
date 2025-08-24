import json
import datetime
import os

#Try open json file and get data
def openJSON(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Events script try open JSON file, but did not find the JSON file in the script directory")
    except UnicodeDecodeError:
        print("Events script cannot decode JSON file using UTF-8 encoding")
    except Exception as exception:
        print(f"Events script try open JSON file, but got an error: {exception}")
    else: return data

#Checking for event in calendar and print event
def handlingEvent(data):
    #Get date
    fullDate = datetime.datetime.now()
    mKey = fullDate.strftime("%b").lower()
    dKey = fullDate.strftime("%d")
    #Print event, if not report the absence
    try:
        print(data[mKey][dKey])
    except Exception:
        print("Today nothing")

#Main part
def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "calendar.json")
    data = openJSON(path)
    handlingEvent(data)

if __name__ == "__main__":
    main()