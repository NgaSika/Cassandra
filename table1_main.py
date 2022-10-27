from cassandra.cluster import Cluster
import os
import json

def mktable():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute("CREATE KEYSPACE IF NOT EXISTS odorDB \
       WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'} ")

    session.execute("use odorDB")
    session.execute("CREATE TABLE IF NOT EXISTS MOESM1_ESM (mol_name text, dilution text, mol_formula text, cas_no text, inchi_no text, id text, exp map<text, double>, primary key((inchi_no, mol_name, dilution), id))")

    session.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS MOESM1_BY_INCHI AS SELECT *FROM MOESM1_ESM WHERE inchi_no IS NOT NULL AND mol_name IS NOT NULL AND dilution IS NOT NULL AND id IS NOT NULL PRIMARY KEY (inchi_no, mol_name, dilution, id) ")
    session.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS MOESM1_BY_NAME AS SELECT *FROM MOESM1_ESM WHERE mol_name IS NOT NULL AND inchi_no IS NOT NULL AND dilution IS NOT NULL AND id IS NOT NULL PRIMARY KEY (mol_name, inchi_no, dilution, id)")
    session.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS MOESM1_BY_FORMULA AS SELECT *FROM MOESM1_ESM WHERE mol_formula IS NOT NULL AND inchi_no IS NOT NULL AND mol_name IS NOT NULL AND dilution IS NOT NULL AND id IS NOT NULL PRIMARY KEY (mol_formula, inchi_no, mol_name, dilution, id)")
    session.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS MOESM1_BY_NAME_DILUTION AS SELECT *FROM MOESM1_ESM WHERE mol_name IS NOT NULL AND dilution IS NOT NULL AND inchi_no IS NOT NULL AND id IS NOT NULL PRIMARY KEY ((mol_name, dilution), inchi_no, id)")
  


def insert():
    mktable()

    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute("use odorDB")

    path_ = "./lem/tmpo!/"
    files =os.listdir("./lem/tmpo!")
    fname = [f for f in files if os.path.isfile(os.path.join("./lem/tmpo!", f))]

    cnt=0

    for i in fname:
        filename = path_ + i
        with open(filename) as f:
            for j in f.read().splitlines():         
                t = ""
                if "\'" in j:
                    t = j.replace("\'", "\'\'")
                else:
                    t = j
                k = "\'" + t + "\'"
                print("回数 : "+str(cnt))
                #print(k)
                session.execute("INSERT INTO MOESM1_ESM JSON" + k)
                cnt+=1


def delete():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute("use odorDB")

    #インチナンバーを要求
    inchi = input("Inchiナンバー：  ")
    name = input("分子名： ")
    dilution = input("濃度：  ")
    id = input("id:  ")

    #2種類の濃度を取得
    #選択要求

    #確認
    inpt = input(name+dilution+"のid = "+id+"を削除したいか? [yes, no]: ")
    
    if inpt == 'yes':
        session.execute("DELETE FROM MOESM1_ESM WHERE inchi_no=\'"+ inchi +"\' AND mol_name=\'" + name+ "\' AND dilution=\'" + dilution + "\' AND id=\'" + id + "\'")
    else:
        print("Has failed.")


