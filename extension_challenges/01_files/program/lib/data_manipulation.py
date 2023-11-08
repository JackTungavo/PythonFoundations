import os

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    return os.path.exists(filename)

# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
def get_file_contents(filename):
    if os.path.exists(filename) == False:
        return "This file cannot be found!"
    else:
        checkFile = os.open(filename,"r")
        listLines = checkFile.readlines().copy()
        checkFile.close()
        return listLines


# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def GetListFromString(string):
    return string.split(";")

def christmas_day_air_quality(filename, include_header_row):
    checkFile = os.open(filename,"r")
    ##30/12/2004
    dataToReturn = []
    data = checkFile.readlines()
    for row in data:
        if GetListFromString(str(row))[0] == '25/12/2004':
            if include_header_row == True: dataToReturn.append(data[0]) ##add headers to data to show
            dataToReturn.append(row)
        ##end
    ##end
##end

# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
##0     1   2       3           4
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    totalAirQuality = 0
    timesChecked = 0

    currentFile = os.open(filename,"r")
    data = currentFile.readlines()
    for row in data:
        if GetListFromString(str(row))[0]== '25/12/2004':
            timesChecked =+ 1
            totalAirQuality =+ float(GetListFromString(str(row))[4])
        ##end
    #end
    currentFile.close()

    return totalAirQuality / timesChecked ##returns back AverageAirQuality

# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    allAvererages = { ##1 = Jan, 2 = Feb ...
        "01": 0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
    }

    ##01/34/00
    currentFile = os.open(filename,"r")
    data = currentFile.readlines()
    for Month in range(1,12,1):
        totalAverage = 0
        timesCounted = 0
        targetMonth = "0"

        if Month >= 10: 
            targetMonth = str(Month) 
        else :
            targetMonth = targetMonth + str(Month)
        ##end
        
        for row in data:
            if GetListFromString(str(row))[0][3:5] == targetMonth:
                totalAverage+= float(GetListFromString(str(row))[4])
                timesCounted+=1
            ##end
        ##end
        allAvererages[targetMonth] = totalAverage / timesCounted
    ##end

    return allAvererages

# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"

def create_march_data(filename):
    oldFile = os.open(filename,"r")
    data = oldFile.readlines()
    newData = []
    newData.append(data[0])
    for row in data:
        if GetListFromString(str(row))[0][3:5] == '03': newData.append(row)
    ##end

    with open("AirQualityMarch.csv","+w") as currentFile:
        currentFile.writelines(newData)
        currentFile.close()
    ##end
##end

# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    dirName = "monthly_responses"
    os.mkdir(os.path.join("/Users/jacktungavo/Projects/PythonFoundations/python_foundations/extension_challenges/01_files/program/"),dirName)
    currentFile = os.open(filename,"r")
    data = currentFile.readlines().copy()
    currentFile.close()
    currentMonth = ""
    linesToAdd = []
    for row in data:
        if GetListFromString(str(row))[0][3:9] != currentMonth:
            if currentMonth != "": 
                currentFile.writelines(linesToAdd)
                linesToAdd = []
                currentFile.close() 
            currentMonth = GetListFromString(str(row))[0][3:9]
            currentFile = os.open(currentMonth.replace("/","-")+".csv","w")
            linesToAdd.append(row)
        else:
            linesToAdd.append(row)
        ##end
    ##end
##end