from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from pandas.core.indexes.base import Index
import pubchempy as pup
import os


def insert():
    mktable()

    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.row_factory = dict_factory
    session.execute("use odordb;")

    element = []
    files =os.listdir("/Users/musashimaru/Desktop/table2/edit/am1_outfile")
    element_z = [f for f in files if os.path.isfile(os.path.join("/Users/musashimaru/Desktop/table2/edit/am1_outfile", f))]

    # 分子名取ってくんのに使った
    txt_path = "/Users/musashimaru/Desktop/table2/edit/index.txt"

    for j in element_z:
        a=j.replace(".log","")
        element.append(a)

    num = 0

    for i in element:

            if i != ".DS_Store":
                print(num)
                num = num + 1
                ary_f = [] #freq
                ary_r = [] #ir_inten
                ary_i = [] #inchi_no
                ary_m = [] #method
                ary_t = "" #timeuuid
                ary_o = "" #最適構造データ
                path = "/Users/musashimaru/Desktop/table2/edit/am1_outfile/"+ i + ".log"
                # path_j = "/Users/musashimaru/Desktop/table2/edit/main_out/" + i + ".csv"
                req = ["MolecularFormula","inchi"]

                print(i)
                # index.txtからtimeUUIDみて分子名取ってきてる
                # あとファイル名のtimeUUIDを取ってる
                name = ""
                with open(txt_path, "r") as m:
                    for line in m:
                        if i in line:
                            name = line.replace("element name : ", "").replace(" timeuuid : " + i, "").replace("\n", "")
                            ary_t = i
                
                print(name)

                b_path = "/Users/musashimaru/Desktop/table2/inchi check/comp_bunshi2/"+ name +".txt"
                with open(b_path) as f:
                    for line in f:
                        unchi = line

                    print(unchi)
                    ary_i.append(unchi)

                # logファイルからfreqとir_intenの抜き出し
                with open(path,"r") as d:
                    for i, line in enumerate(d):
                        if 'Frequencies' in line:
                            data = line.replace("Frequencies --","")
                            datas = data.split()
                            for l in datas:
                                ary_f.append(l)
                        elif 'IR Inten' in line:
                            data = line.replace("IR Inten    --","")
                            datas = data.split()
                            for m in datas:
                                ary_r.append(m)   

                ary_f = [float(s) for s in ary_f]
                ary_r = [float(s) for s in ary_r]

                # logファイルからガウシャンの計算手法の抜き出し
                with open(path,"r") as f:
                    for line in f:
                        if "#P" in line:
                            line = line.replace("\n", "")
                            line = line.lstrip()
                            ary_m.append(line)

                # logファイルから最適化構造データの抜き出し
                count = 0
                count2 = 0
                grenade = False

                with open(path, "r") as f:
                    for line in f:
                        # line = line.replace("\"n", "")
                        count = count + 1
                        count2 = count2 + 1
                        a = repr(line)
                        if r"\\1" in a and r"\\Fre\\" in a:
                            print("True{}".format(a))
                            # print(count)
                            grenade = True

                        if grenade == True:
                            ary_o = ary_o + line

                        if "\\Version=" in a or "\\ Version=" in a:
                            # print(count2)
                            grenade = False

                # 以下cassandraに投げたいテーブルのデータ
                # print(ary_t)     #timeuuid
                # print(ary_f[0])  #freq
                # print(ary_i[0])  #inchi_no
                # print(ary_r[0])  #ir_inten
                print(ary_m[0])  #method
                # print(ary_o)     #struct

                session.execute("insert into odordb.calcfreq(timeuuid, freq, inchi_no, ir_inten, method, struct) values (%s, %s, %s, %s, %s, %s);", (ary_t, ary_f, ary_i[0], ary_r, ary_m[0], ary_o))

            else:
                print("DS!")

def mktable():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.row_factory = dict_factory
    session.execute("CREATE KEYSPACE IF NOT EXISTS odorDB WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};")
    session.execute("use odordb;")
    session.execute("CREATE TABLE IF NOT EXISTS calcfreq(timeuuid text , freq list<float>, inchi_no text, ir_inten list<float>, method text, struct text, PRIMARY KEY(inchi_no));")

    session.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS calcfreq_method AS SELECT * FROM calcfreq WHERE method IS NOT NULL AND inchi_no IS NOT NULL PRIMARY KEY (method, inchi_no);")
    # session.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS calcfreq_timeuuid AS SELECT inchi_no, timeuuid FROM calcfreq WHERE timeuuid IS NOT NULL AND inchi_no IS NOT NULL method IS NOT NULL PRIMARY KEY (timeuuid, inchi_no, method);")
    session.execute("CREATE CUSTOM INDEX method_index ON calcfreq(method) USING 'org.apache.cassandra.index.sasi.SASIIndex';")


def delete():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.row_factory = dict_factory
    session.execute("use odorDB;")

    inchi = input("Inchi_no: ")

    kakuninn = input("Inchi_no = " + inchi + " を削除しますか？ [yes, no]: ")
    if kakuninn == 'yes':
        session.execute("DELETE FROM odordb.calcfreq WHERE inchi_no = %s IF EXISTS;", (inchi,))
    else:
        print("WTF!!!!")

def request():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.row_factory = dict_factory
    session.execute("use odorDB;")

    ch=input("inchiで検索する場合は1を、methodで検索する場合は2を：")
    if ch == '1' or ch == '１':
        anchi = input("inchi_noを入力してね：")
        out = session.execute("SELECT inchi_no FROM calcfreq WHERE inchi_no = %s;", (anchi,))
        print(type(out))
        print(out.current_rows)
        a = out.current_rows
        b = a[0].values()
        c = a[0]
        d = c["inchi_no"]
        print(d)
        print(type(d))
        formats = input("outputの形式を指定してね。標準出力の場合は1を、テキストファイルで出力する場合は2を：")
        if formats == "1" or "１":
            print("//////////////////////   OUTPUT DATA   /////////////////////\n")
            print("\n")
            print("----------------------   FROM Table 2 ---------------------\n")
            for i in out:
                print(i)
        elif formats == "2" or "２":
            with open("(os.path.dirname(__file__))"+ "/"+anchi+".txt","w") as f:
                f.writelines(out)
                f.close()
    elif ch == "2" or ch == "２":
        method = input("methodを入力してね：")
        # out = session.execute("SELECT timeuuid FROM calcfreq_method WHERE method = %s;", (method,))
        out = session.execute("SELECT timeuuid FROM calcfreq WHERE method LIKE '%s';",(method))
        formats = input("outputの形式を指定してね。標準出力の場合は1を、テキストファイルで出力する場合は2を：")
        if formats == "1" or "１":
            print("//////////////////////   OUTPUT DATA   /////////////////////\n")
            print("\n")
            print("----------------------   FROM Table 2 ---------------------\n")
            for i in out:
                print(i)
        elif formats == "2" or "２":
            with open("(os.path.dirname(__file__))"+ "/"+method+".txt","w") as f:
                f.writelines(out)
                f.close()

request()

