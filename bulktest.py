import subprocess
import sys
import statistics
from tqdm import tqdm
def subrun(code):
    rslt = subprocess.Popen(code, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return rslt.stdout.read().decode()
def getUserTime(rs):
    splitt = rs.split(" ")[0]
    return float(splitt[:-4])
def avg(list):
    return sum(list)/len(list)
repeat = int(sys.argv[1])
intTimes = []
floatTimes = []
for i in tqdm(range(repeat)):
    rslt = subrun(["time","./int"])
    intTimes.append(getUserTime(rslt))
    rslt = subrun(["time","./float"])
    floatTimes.append(getUserTime(rslt))
print("Integer average time:{} stdev:{}".format(avg(intTimes),statistics.stdev(intTimes)))
print("Float average time:{} stdev:{}".format(avg(floatTimes),statistics.stdev(floatTimes)))