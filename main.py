import datetime
import os
import getpass
import table1_main
import table2_main
import req_main
import fromindex


def sysinfo():
    a = os.path.dirname(__file__)
    print(a)
    logpath = a + "log.txt"
    flag = os.path.isfile(logpath)
    osdata = os.uname()
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    user = getpass.getuser()

    return logpath,osdata,now,user,flag


def makelog(logpath,now,osdata,user,flag):
    
    if flag == "True":
        with open(logpath,"w") as l:
            l.writelines("Datetime(UTC +09) : {}\n".format(str(now)))
            l.writelines("system info : {}\n".format(osdata))
            l.writelines("User identifiable : {}\n".format(user))
    else:
        with open(logpath,"a") as l:
            l.writelines("Datetime(UTC +09) : {}\n".format(str(now)))
            l.writelines("system info : {}\n".format(osdata))
            l.writelines("User identifiable : {}\n".format(user))

    return

def choose():
    print("Please select an action.\naction 1 : Request data.\naction 2: Insert Data.\naction 3: Delete Data\naction 4: Search index.txt.\naction 5: Exit This prigram.")
    action = input()
    exitflag = False


    if action in "1" or action in "１":
        print("req data")

        req_main.requests()

        data = sysinfo()
        with open(logpath,"a") as f:
            f.write("{0} has request data.   Time= {1}\n".format(data[3],data[2]))
        error_flag_choose = False
        
    elif action in "2" or action in "２":
        print("insert data")
        data = sysinfo()
        with open(logpath,"a")as f:
            f.write("{0} has Insert data.   Time= {1}\n".format(data[3],data[2]))

        error_flag_choose = False

        table1_main.insert()
        table2_main.insert()

    elif action in "3" or action in "３":
        print ("delete data")
        data = sysinfo()
        with open(logpath,"a") as f:
            f.write("{0} has Delete data.   Time= {1}\n".format(data[3],data[2]))
        error_flag_choose = False

        table1_main.delete()
        table2_main.delete()
        
    elif action in "4" or action in "４":
        fromindex.search()
        
        data = sysinfo()
        with open(logpath,"a") as f:
            f.write("{0} has search in index.txt.   Time= {1}\n".format(data[3],data[2]))
        error_flag_choose = False
        
        
        
    elif action in "5" or action in "５":
        print("exit")
        with open(logpath,"a") as f:
            data = sysinfo()
            f.write("{0} has logout.   Time= {1}\n".format(data[3],data[2]))
            f.write("\n")
        error_flag_choose = False
        exitflag = True
    else:
        print("error")
        error_flag_choose = True

    return error_flag_choose,exitflag



re = sysinfo()
logpath = re[0]
now = re[2]
osdata = re[1]
user = re[3]
flag = re[4]

makelog(logpath,now,osdata,user,flag)


while True:
    out= choose()
    error_flag_choose = out[0]
    exitflag = out[1]

    if exitflag == True:
        
        exit()
    
    if error_flag_choose == True:
        print("again")
        pass
    else:
        print("action fanction")

