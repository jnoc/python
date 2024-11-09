tableOut = ""
fTCount = 0
pTCount = 0
jobArray = []

def main():
    print("Jobs Tracker\n" + ("=" * 30))
    while True:
        try: # do this, if wrong value catch error
            jobsAdd = int(input("How many jobs would you like to add? "))
            break
        except ValueError:
            print("Enter a correct value!")
    if jobsAdd > 0:
        writeToFile("#") # write top line of .txt files
        for i in range(jobsAdd): # run loop for amount input
            obj = details(i) # handles input
            writeToFile(obj) # writes each job object to line
        print("\n" + tableOut) # prints nice formatted table out after input
    else:
        pass
    #print(jobArray)
    summary()
    return

def details(i):
    writeFile = ""
    line = "\nEnter the details of job %s\n" % (i + 1) # fstring var in string
    print(line + ("-" * 30))
    while True:
        try:
            jobTitle = titleHandle()
            location = locationHandle()
            fileType = fileTypeHandle()
            if fileType == 1: # if full time
                writeFile = "ft"
                experience = experienceHandle()
                hours = 40 # set hours for full time
                payRate = payHandle()
                break
            else: # else fileType == 2 therefore part time
                writeFile = "pt"
                experience = experienceHandle()
                hours = hourHandle()
                payRate = payHandle()
                break
        except ValueError: # catch any errors thrown from the handle defs
            print("Incorrect value detected please start this job input again!\n")

    # format [jobID, jobTitle, location, experience, payRate, hours, ]
    job = [(i + 1), jobTitle, location, experience, payRate, hours, round((payRate * hours),2)]
    obj = [writeFile, job] # smack together in a list object to handle in other defs
    jobArray.append(job) # added to global variable for use later on in summary()
    return obj

def titleHandle(): # handles the title question if empty string not accepted
    jobTitle = str(input("What is the job title: "))
    if len(jobTitle) <= 0:
        print("Job title cannot be empty, try again!")
        return titleHandle() # recursively call if empty string
    else:
        return jobTitle

def locationHandle(): # handles the company question if empty string not accepted
    location = str(input("What is the company name: "))
    if len(location) <= 0:
        print("Company name cannot be empty, try again!")
        return locationHandle() # recursively call if empty string
    else:
        return location

def fileTypeHandle(): # handles the file that the output is going in, 1 for full time 2 for part time, else if not those values repeat question
    set = [1, 2]
    fileType = int(input("Please specify the type of employment\n1. Full time\n2. Part time\n==> "))
    while True:
        if fileType in set:
            return fileType
        else:
            fileType = int(input("Please specify the correct type of employment\n1. Full time\n2. Part time\n==> "))

def experienceHandle(): # this handles the experience question for yes or no specifically only wanting ["y", "Y", "n", "N"]
    set = ["y", "Y", "n", "N"] # accepted only
    experience = str(input("Does the job require experience (y/n)? "))
    while True:
        if experience in set:
            if experience == ("y" or "Y"):
                return "yes"
            else:
                return "no"
        else:
            experience = str(input("Please enter a correct value for experience: "))

def hourHandle(): # this handles the hours question and only accepts positive integers or if error thrown from incorrect value details() is restarted
    hours = int(input("How many hours per week? "))
    if hours <= 0:
        print("Hours cannot be a negative or 0 value, try again!")
        return hourHandle() # recursively call if negative int 
    else:
        return hours
    
def payHandle(): # this handles the pay per hour question and only accepts positive integers or if error thrown from incorrect value details() is restarted
    payRate = round(float(input("Enter the rate paid per hour? ")),2) # round correctly
    if payRate <= 0:
        print("Pay per hour cannot be a negative or 0 value, try again!")
        return payHandle() # recursively call if negative int 
    else:
        return payRate

def writeToFile(obj):
    global tableOut
    global fTCount
    global pTCount
    # handles defined input specified in main() so you can write this line to the top of your files
    if obj == "#":
        data = ["ID", "JOB TITLE", "LOCATION", "EXP", "RATE(€)", "HOURS", "EARNINGS"]
        writeStr = '{:<4}{:<20}{:<16}{:<5}{:<10}{:<8}{:<8}'.format(data[0], data[1], data[2], data[3], data[4], data[5], data[6]) + "\n" + ("=" * 71)
        tableOut += writeStr + "\n"
        file = open("fulltime.txt", "a")
        file.write("%s\n" % (writeStr))
        file.close
        file = open("parttime.txt", "a")
        file.write("%s\n" % (writeStr))
        file.close
    else:
        first = obj[0]
        last = obj[1]
        # splitting up and writing to file
        data = last
        # {:<num}.format(data) <- handles spacing, and also can handle 2 decimal places properly after rounded (for printing)
        writeStr = '{:<4}{:<20}{:<16}{:<5}{:<10}{:<8}{:>8}'.format(data[0], data[1], data[2], data[3], "{:.2f}".format(data[4]), data[5], "{:.2f}".format(data[6]))
        tableOut += writeStr + "\n"
        # obj[0] handled
        if first == "ft":
            fTCount += 1 # counter for amount added to file
            file = open("fulltime.txt", "a")
            file.write("%s\n" % (writeStr))
            file.close()
        else:
            pTCount += 1 # counter for amount added to file
            file = open("parttime.txt", "a")
            file.write("%s\n" % (writeStr))
            file.close()

def summary():
    print("Summary\n" + ("=" * 10))
    # global variable used to keep count of amount changed when running the program
    print("%s full time post(s) – fulltime.txt has been updated" % fTCount)
    print("%s part time post(s) – parttime.txt has been updated\n" % pTCount)
    
    payArray = [] # build all the jobs pays into an array to handle calculations
    for i in range(len(jobArray)):
       item = jobArray[i][4]
       payArray.append(item) 

    # working out of hourly range and average pay using the built arrray
    hourRang = "Hourly pay rate ranges from €%s to €%s" % ("{:.2f}".format(min(payArray)), "{:.2f}".format(max(payArray)))
    avgPay="Average pay is €%s" % ("{:.2f}".format(round(sum(payArray) / len(payArray), 2)))

    # working out of the highest paying job (fetching the index for highest pay value then using that index against the jobArray to grab title and location)
    highPayIndex = payArray.index(max(payArray))
    highPayTitle = jobArray[highPayIndex][1]
    highPayLocation = jobArray[highPayIndex][2]

    # output for details
    highPayDeets = "Details of highest pay rate: %s at %s" % (highPayTitle, highPayLocation)

    print("%s\n%s\n%s\n" % (hourRang, avgPay, highPayDeets))

if __name__ == "__main__":
    main()