import csv
import json
import os
import time
import subprocess
from typing import Type
#import yaml
from glob import glob





endelement = []

rawmeet = []
rawfish =[[[]]]
rawfruits = []
indexlist = []
fdata =[]

global ary
ary = []

jsondata = {}
jsondate = {}


checker = False

path = "lem/lem6.csv"

cnt = 0
cntt = 0
cnnt = 0
global connt
cnnnt = 0


try:
    cmd = ["mkdir","./lem/csvoutput"]
    subprocess.run(cmd)
    cmd2 = ["mkdir","./lem/tmpo!"]
    subprocess.run(cmd2)
    cmd3 = ["mkdir","./lem/turbochrger!"]
    subprocess.run(cmd3)
    cmd4 = ["mkdir","./lem/jsondata"]
    subprocess.run(cmd4)
except:
    None



def rawfish1(name,weight,persent,ary):
    print("---------in define Raw fish------------")
    print(name,weight)
    per = dilution(ary[4])
    indexname = name + str((names(weight)))
    if name in ary and persent == per:
        if indexname not in indexlist:
            indexlist.append(indexname)
            checker = False
            #テキストファイル作成時
            maketmp(ary,checker)
            # #YAMLファイル作成時
            # makeyaml(ary,checker)
        elif indexname in indexlist:
            checker = True
            #テキストファイル作成時
            maketmp(ary,checker)
            # #YAMLファイル作成時
            # makeyaml(ary,checker)
    else:
        print("WFT !?")
        
    return


def replace(data):
    g = [0.0 if value == '' else value for value in data]
    return g

def dilution(weight):
    if weight == "1/10":
        persent = 1/10
    elif weight == "1/100":
        persect = 1/100
    elif weight == "1/1,000":
        persent = 1/1000
    elif weight == "1/10,000":
        persent = 1/10000
    elif weight == "1/100,000":
        persent = 1/100000
    elif weight == "1/1,000,000":
        persent = 1/1000000
    elif weight == "1/10,000,000":
        persent = 1/10000000
    elif weight == "1/100,000,000":
        persent = 1/100000000
    elif weight == "1/1,000,000,000":
        persent = 1/1000000000

    return persent 




def names(weight):
    if weight == "1/10":
        names = 10
    elif weight == "1/100":
        names = 100
    elif weight == "1/1,000":
        names = 1000
    elif weight == "1/10,000":
        names = 10000
    elif weight == "1/100,000":
        names = 100000
    elif weight == "1/1,000,000":
        names = 1000000
    elif weight == "1/10,000,000":
        names = 10000000
    elif weight == "1/100,000,000":
        names = 100000000
    elif weight == "1/1,000,000,000":
        names = 1000000000

    return names 



def maketmp(date,check):

    print("--------------- in to def maketmp ------------------")

    try:
        bunshipath = "/Users/ozaki/Desktop/table1 2/bunshi2/"+date[3]+".txt"

        with open(bunshipath,"r") as f:
            a =f.readline()
            shiki = a.strip()
            inchi = f.readline()
            print(shiki)
            print(inchi)
    except:
        shiki = "none"
        inchi = "none"

    namekuzi = names(date[4])
    SDAT = {}
    data = replace(date)

    #値の型をstrからfloatに変更
    fdata =[]

    for i in range(18,38):
        fdata.append(float(data[i]))

    SDAT  = {
                        "mol_name":data[3],
                        "dilution":data[4],
                        "mol_formula":shiki,
                        "cas_no":data[0],
                        "inchi_no":inchi,
                        "id" : data[5],
                        "exp":{
                            "EDIBLE":fdata[0],
                            "BAKERY":fdata[1],
                            "SWEET":fdata[2],
                            "FRUIT":fdata[3],
                            "FISH":fdata[4],
                            "GARLIC":fdata[5],
                            "SPICES":fdata[6],
                            "COLD":fdata[7],
                            "SOUR":fdata[8],
                            "BURNT":fdata[9],
                            "ACID":fdata[10],
                            "WARM":fdata[11],
                            "MUSKY":fdata[12],
                            "SWEATY":fdata[13],
                            "AMMONIA/URINOUS":fdata[14],
                            "DECAYED":fdata[15],
                            "WOOD":fdata[16],
                            "GRASS":fdata[17],
                            "FLOWER":fdata[18],
                            "CHEMICAL":fdata[19]}}

    
    if check == True:
        print("found it")
        pathsss = "lem/tmpo!/" + data[3] + str(namekuzi) +".txt"
        with open(pathsss,"a") as d:
            d.write(json.dumps(SDAT))
            d.write("\n")
        d.close
    elif check == False:
        print("Failed")
        pathss = "lem/tmpo!/" + data[3] + str(namekuzi) +".txt"
        with open(pathss,"w") as c:
            c.write(json.dumps(SDAT))
            c.write("\n")
        c.close()




def makeyaml(date,check):
    print("------------define make yaml--------------")
    uzimushi = names(date[4])
    obj = replace(date)
    SDAT = {}
    SDAT [obj[3]] = {"C.A.S":obj[0],
                    "element":obj[3],
                    "dilution":obj[4],
                            "character":{
                                "EDIBLE":obj[18],
                                "BAKERY":obj[19],
                                "SWEET":obj[20],
                                "FRUIT":obj[21],
                                "FISH":obj[22],
                                "GARLIC":obj[23],
                                "SPICES":obj[24],
                                "COLD":obj[25],
                                "SOUR":obj[26],
                                "BURNT":obj[27],
                                "ACID":obj[28],
                                "WARM":obj[29],
                                "MUSKY":obj[30],
                                "SWEATY":obj[31],
                                "AMMONIA/URINOUS":obj[32],
                                "DECAYED":obj[33],
                                "WOOD":obj[34],
                                "GRASS":obj[35],
                                "FLOWER":obj[36],
                                "CHEMICAL":obj[37]
                            } 
                     }

    if check == True:
        pathsss1 = "lem/turbochrger!/" + obj[3] + str(uzimushi) + ".yaml"
        print(type(SDAT))
        with open(pathsss1,"r") as h:
            before = yaml.load(h)
            before["{}".format(obj[3])].update(SDAT)
        with open(pathsss1,"w") as e:
            yaml.safe_dump(before,e)

    elif check == False:
        pathsss = "lem/turbochrger!/" + obj[3] + str(uzimushi) + ".yaml"

        with open(pathsss,"w") as e:
            yaml.safe_dump(SDAT,e)
        e.close()


    return


def makejson(data):
    print("-----------In Define Make Json----------")
    # print(type(data))
    edit = replace(data)
    # print(type(edit))
    # ary.append(edit)
    # print(len(ary))
    # print(ary[-1])

    SDAT = {}


    name = edit[3] + " " + edit[4]
    print(name)

    SDAT [name] = {"C.A.S":edit[0],
                        "element":edit[3],
                        "dilution":edit[4],
                        "character":{
                            "EDIBLE":edit[18],
                            "BAKERY":edit[19],
                            "SWEET":edit[20],
                            "FRUIT":edit[21],
                            "FISH":edit[22],
                            "GARLIC":edit[23],
                            "SPICES":edit[24],
                            "COLD":edit[25],
                            "SOUR":edit[26],
                            "BURNT":edit[27],
                            "ACID":edit[28],
                            "WARM":edit[29],
                            "MUSKY":edit[30],
                            "SWEATY":edit[31],
                            "AMMONIA/URINOUS":edit[32],
                            "DECAYED":edit[33],
                            "WOOD":edit[34],
                            "GRASS":edit[35],
                            "FLOWER":edit[36],
                            "CHEMICAL":edit[37]}}










    tmp = "".join(map(str,edit[4]))
    dilution_1 = tmp.replace("/","_")

    secter = names(edit[4])


    



    # ///Json make

    if name not in endelement:
        paths = []
        jsondata ={}
        print(edit)
        paths = "lem/csvoutput/" + edit[3] + str(secter) + ".json"
        #JSON 新規作成
        jsondata [name] = {"C.A.S":edit[0],
                           "element":edit[3],
                           "dilution":edit[4],
                           "character":{
                               "EDIBLE":edit[18],
                               "BAKERY":edit[19],
                               "SWEET":edit[20],
                               "FRUIT":edit[21],
                               "FISH":edit[22],
                               "GARLIC":edit[23],
                               "SPICES":edit[24],
                               "COLD":edit[25],
                               "SOUR":edit[26],
                               "BURNT":edit[27],
                               "ACID":edit[28],
                               "WARM":edit[29],
                               "MUSKY":edit[30],
                               "SWEATY":edit[31],
                               "AMMONIA/URINOUS":edit[32],
                               "DECAYED":edit[33],
                               "WOOD":edit[34],
                               "GRASS":edit[35],
                               "FLOWER":edit[36],
                               "CHEMICAL":edit[37]}}


        with open (paths,"w") as w:
            json.dump(jsondata,w,ensure_ascii=False,indent=4)
        w.close()

        endelement.append(name)
        c =0
        print("-----------inside endelement------------")
        for t in endelement:
            print(endelement[c])
            c =c+1

    elif name in endelement:
        paths = []
        jsondate = {}
        paths = "lem/csvoutput/" + edit[3] + str(secter) + ".json"
        print(edit)
        #JSON追記
        jsondate [name] = {"C.A.S":edit[0],
                           "element":edit[3],
                           "dilution":edit[4],
                           "character":{
                               "EDIBLE":edit[18],
                               "BAKERY":edit[19],
                               "SWEET":edit[20],
                               "FRUIT":edit[21],
                               "FISH":edit[22],
                               "GARLIC":edit[23],
                               "SPICES":edit[24],
                               "COLD":edit[25],
                               "SOUR":edit[26],
                               "BURNT":edit[27],
                               "ACID":edit[28],
                               "WARM":edit[29],
                               "MUSKY":edit[30],
                               "SWEATY":edit[31],
                               "AMMONIA/URINOUS":edit[32],
                               "DECAYED":edit[33],
                               "WOOD":edit[34],
                               "GRASS":edit[35],
                               "FLOWER":edit[36],
                               "CHEMICAL":edit[37]}}

        print(paths)
        with open(paths)as r:
            jsonupdate = json.load(r)
        r.close()
        writedata = [jsonupdate,jsondate]

        print("update")
        print(paths)

        with open(paths,"w") as u:
            json.dump(writedata,u,ensure_ascii=False,indent=4)
        u.close()

        jsondate = {}

    # JSON make end


    # name = rawmeet[cnt][3] +"   "+ rawmeet[cnt][4]
    # # jsondata [name] = {"CAS":rawmeet[cnt][0]}
    # jsondata [name] = {"C.A.S":rawmeet[cnt][0],"element":rawmeet[cnt][3],"dilution":rawmeet[cnt][4],"character":{"EDIBLE":rawmeet[cnt][18],"BAKERY":rawmeet[cnt][19],"SWEET":rawmeet[cnt][20],"FRUIT":rawmeet[cnt][21],"FISH":rawmeet[cnt][22],"GARLIC":rawmeet[cnt][23],"SPICES":rawmeet[cnt][24],"COLD":rawmeet[cnt][25],"SOUR":rawmeet[cnt][26],"BURNT":rawmeet[cnt][27],"ACID":rawmeet[cnt][28],"WARM":rawmeet[cnt][29],"MUSKY":rawmeet[cnt][30],"SWEATY":rawmeet[cnt][31],"AMMONIA/URINOUS":rawmeet[cnt][32],"DECAYED":rawmeet[cnt][33],"WOOD":rawmeet[cnt][34],"GRASS":rawmeet[cnt][35],"FLOWER":rawmeet[cnt][36],"CHEMICAL":rawmeet[cnt][37]}}
    # print("--------aaa------")
    # print(jsondata)
    # cnt = cnt + 1

    return


with open (path,"r") as f:
    data = csv.reader(f)
    for i in data:
        
        rawmeet.append(i)

        # print(rawmeet)
        # print(rawmeet[cnt][3])
 
        print(len(rawmeet))
        # if lname in rawfish and lweigt in rawfish:
        #     rawfruits.append(f)

        # print(rawfruits)
        #  # print(len(rawfruits)
        


for h in rawmeet:
    lname = str(h[3])
    lweigt = str(h[4])
    per = dilution(lweigt)
    print(lname)
    print("-------------H-----------")

    rawfish1(lname,lweigt,per,h)
    cnnt = cnnt +1


    print("sleeping Zzzzzz....")
    print("cnnt = {}".format(cnnt))
    # if cnnt == 55000:
    #     break
    # time.sleep(3)



        

textpath = "lem/tmpo!/"
for file in glob(textpath + '/*.txt'):
    jsondata =[]
    with open(file,"r") as f :
        for i in f:
            jsondata.append(eval(i))
    filrename2 = os.path.basename(file)
    outpath = "./lem/jsondata/" + filrename2 + ".json"

    with open(outpath,"w") as h:
        json.dump(jsondata,h,indent=4)
    h.close()
