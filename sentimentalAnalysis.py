import twt
import time
from writetweetsdata import writetweetsdata

ls = ['Donald Trump','Narendra Modi','Rajiv Gandhi']
localtime = time.asctime(time.localtime(time.time()))
for leader in ls:
    data = twt.main(leader)
    print(localtime)
    writetweetsdata(localtime,leader,data)
    print(data)
