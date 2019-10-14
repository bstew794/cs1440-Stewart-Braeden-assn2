import time
import sys
from Report import Report


rpt = Report()

if len(sys.argv) < 2:
    print("Usage: src/main.py DATA_DIRECTORY")
    sys.exit(1)

print("Reading the databases...", file=sys.stderr)
before = time.time()

areaTitlesPath = sys.argv[1] + "/area_titles.csv"
currentFile = open(areaTitlesPath)
areaTitleDict = {}

for line in currentFile:
    columns = line.split(',"')
    columns[0] = columns[0][1:-1]
    columns[1] = columns[1].rstrip()
    if columns[0].isdigit():
        doAdd = True
        a,b,c,d,e = columns[0]

        if c == "0" and d == "0" and e == "0":
            doAdd = False

        if doAdd:
            areaTitleDict[columns[0]] = columns[1].rstrip('"')

currentFile.close()

dataPath = sys.argv[1] + "/2018.annual.singlefile.csv"
currentFile = open(dataPath)

results = [0, 0, "", 0, 0, "", 0, 0, "", 0, 0, 0, "", 0, 0, "", 0, 0, "", 0]

for line in currentFile:
    columns = line.split(",")

    if areaTitleDict.__contains__(columns[0][1:-1]):
        if (columns[1].strip('"')).rstrip() == "0" and (columns[2].strip('"')).rstrip() == "10":
            results[0] += 1
            results[1] += int(columns[10])

            if int(columns[10]) > results[3]:
                results[2] = areaTitleDict.get(columns[0][1:-1])
                results[3] = int(columns[10])

            results[4] += int(columns[8])

            if int(columns[8]) > results[6]:
                results[5] = areaTitleDict.get(columns[0][1:-1])
                results[6] = int(columns[8])

            results[7] += int(columns[9])

            if int(columns[9]) > results[9]:
                results[8] = areaTitleDict.get(columns[0][1:-1])
                results[9] = int(columns[9])

        if (columns[1].strip('"')).rstrip() == "5" and (columns[2].strip('"')).rstrip() == "5112":
            results[10] += 1
            results[11] += int(columns[10])

            if int(columns[10]) > results[13]:
                results[12] = areaTitleDict.get(columns[0][1:-1])
                results[13] = int(columns[10])

            results[14] += int(columns[8])

            if int(columns[8]) > results[16]:
                results[15] = areaTitleDict.get(columns[0][1:-1])
                results[16] = int(columns[8])

            results[17] += int(columns[9])

            if int(columns[9]) > results[19]:
                results[18] = areaTitleDict.get(columns[0][1:-1])
                results[19] = int(columns[9])

currentFile.close()
after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)


rpt.all.num_areas           = results[0]

rpt.all.gross_annual_wages  = results[1]
rpt.all.max_annual_wage     = (results[2], results[3])

rpt.all.total_estab         = results[4]
rpt.all.max_estab           = (results[5], results[6])

rpt.all.total_empl          = results[7]
rpt.all.max_empl            = (results[8], results[9])


rpt.soft.num_areas          = results[10]

rpt.soft.gross_annual_wages = results[11]
rpt.soft.max_annual_wage    = (results[12], results[13])

rpt.soft.total_estab        = results[14]
rpt.soft.max_estab          = (results[15], results[16])

rpt.soft.total_empl         = results[17]
rpt.soft.max_empl           = (results[18], results[19])


# Print the completed report
print(rpt)
