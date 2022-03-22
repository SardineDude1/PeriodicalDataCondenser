# This script reads all the items in a csv with the following format:
# bib title, item call number, item total checkouts, item total number of renewals, item location
# and outputs the total number of checkouts and renewals for each matching title.

# The purpose of the script is to condense circultion information on bibliographic
# titles which have serialized items (e.g. magazines).

file_name = 'MagazineHoldings.txt'

location_code = 'location-code'

file = open(file_name, 'r', encoding="UTF-8")
Lines = file.readlines()

TITLES = []
STATS = []

for line in Lines:
    if line == Lines[0]:
        pass
    else:
        stats = {}
        l = line.split(",")
        
        BibTitle = l[0]
        CallNo = l[-4]
        TotalChk = l[-3].strip("\"").strip("'")
        Renew = l[-2]
        location = l[-1].replace('"', "").replace(" ", "")

        if location[0:len(location_code)] == location_code and TotalChk != '':
            if BibTitle not in TITLES:
                TITLES.append(BibTitle)
                stats[BibTitle] = int(TotalChk)
                STATS.append(stats)
            else:
                for i in STATS:
                    for key in i:
                        if key == BibTitle:
                            i[key] = int(i[key]) + int(TotalChk)

with open("CleanData.txt", "a") as newfile:
    for i in STATS:
        for key in i:
            newfile.write(key + " : " + str(i[key]))
            newfile.write("\n")

