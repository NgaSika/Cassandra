import os
from cassandra.cluster import Cluster, Session
from cassandra.query import dict_factory
import table1_req
import table2_main

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('odorDB')
session.row_factory = dict_factory

def req_tb2_1():
    inchi = input("Inchiを入力してください。")
    # anchi = input("inchi_noを入力してね")
    # out = session.execute("SELECT inchi_no FROM calcfreq WHERE inchi_no = %s;", (anchi,))

    # tmp = out.current_rows
    # tmp2 = tmp[0]
    # inchi = tmp2["inchi_no"]
    out = session.execute("SELECT mol_name, mol_formula, exp FROM odorDB.MOESM1_BY_INCHI WHERE inchi_no = %s",[inchi])
    formats = input("アウトプット形式を選択してください。標準出力で表示させるには１を、テキストおファイルで保存させるには２を,  入力してください。")
    if formats == "1" or formats == "１":  
        print("//////////////////////   OUTPUT DATA   //////////////////////\n")
        for i in out:
            print(i)
    elif formats == "2" or formats == "２":
        with open("(os.path.dirname(__file__))"+ "/"+inchi+".txt","w") as f:
            f.writelines(out)
            f.close()

        
def req_tb1_2():
    print("Table1の要素でTable2を検索します。\n入力するパラメータを指定してください。")
    ch = input("mol_nameで検索する場合は１を、mol_formulaで検索する場合は２を、Inchiナンバーで検索する場合は３を 入力してください。")
    if ch == "1" or ch =="１":
        d = input("mol_nameを入力してください。")
        out = session.execute("SELECT inchi_no FROM odorDB.MOESM1_BY_NAME WHERE mol_name = %s",[d])
        tmp = out.current_rows
        tmp2 = tmp[0]
        inchi = tmp2["inchi_no"]
        out1 = session.execute("SELECT mol_name, mol_formula, exp FROM odorDB.MOESM1_BY_INCHI WHERE inchi_no = %s",[inchi])
        formats = input("アウトプット形式を選択してください。標準出力で表示させるには１を、テキストおファイルで保存させるには２を,  入力してください。")
        if formats == "1" or formats ==  "１":  
            print("//////////////////////   OUTPUT DATA   //////////////////////\n")
            for i in out1:
                print(i)
        elif formats == "2" or formats == "２":
            with open("(os.path.dirname(__file__))"+ "/"+inchi+".txt","w") as f:
                f.writelines(out1)
                f.close()
    elif ch =="2" or ch == "２":
        d  = input("mol_formulaを入力してください。")
        out =  session.execute("SELECT inchi_no FROM odorDB.MOESM1_BY_FORMULA WHERE mol_formula = %s",[d])
        tmp = out.current_rows
        tmp2 = tmp[0]
        inchi = tmp2["inchi_no"]
        out1 = session.execute("SELECT mol_name, mol_formula, exp FROM odorDB.MOESM1_BY_INCHI WHERE inchi_no = %s",[inchi])
        formats = input("アウトプット形式を選択してください。標準出力で表示させるには１を、テキストおファイルで保存させるには２を,  入力してください。")
        if formats == "1" or formats == "１":  
            print("//////////////////////   OUTPUT DATA   //////////////////////\n")
            for i in out1:
                print(i)
        elif formats == "2" or formats == "２":
            with open("(os.path.dirname(__file__))"+ "/"+inchi+".txt","w") as f:
                f.writelines(out1)
                f.close()
    elif ch == "3" or  ch == "３":
        inchi = input("Inchiナンバーを入力してください。")
        out1 = session.execute("SELECT mol_name, mol_formula, exp FROM odorDB.MOESM1_BY_INCHI WHERE inchi_no = %s",[inchi])
        formats = input("アウトプット形式を選択してください。標準出力で表示させるには１を、テキストおファイルで保存させるには２を,  入力してください。")
        if formats == "1" or formats == "１":  
            print("//////////////////////   OUTPUT DATA   //////////////////////\n")
            for i in out1:
                print(i)
        elif formats == "2" or formats ==  "２":
            with open("(os.path.dirname(__file__))"+ "/"+inchi+".txt","w") as f:
                f.writelines(out1)
                f.close()


        




#メイン部分

def requests():
    ch = input("Table1のデータを抜き出すには１を、Table2のデータを抜き出すには２を、Table１の要素で関連データを抜き出すには３を、Table2の要素で関連データを抜き出すには４を入力してください。")
    

    #選択部分
    if ch == "1" or ch == "１":
        table1_req.req()
    elif ch == "2" or ch == "２":
        table2_main.request()
    elif ch == "3" or ch ==  "３":
        req_tb1_2()
    elif ch == "4" or ch =="４":
        req_tb2_1()

