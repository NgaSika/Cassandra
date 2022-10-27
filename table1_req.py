import os
from cassandra.cluster import Cluster
from cassandra.query import dict_factory



def req():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('odorDB')
    session.row_factory = dict_factory

    session.execute("use odorDB")
    
    print("You must input some data.\nPlease choose parameter.\n1: 分子名\n2: 分子式\n3: Inchiナンバー\n ")
    reqdata = input()
    if reqdata == "1" or reqdata == "１":
        d = input("please input mol_name.")

        #inchino = session.execute("SELECT inchi_no FROM odorDB.MOESM1_ESM WHERE mol_name=%s",[d])
        inpt = input("濃度をパラメータに存在含めますか？ [y or n]: ")
        if inpt == 'y' or inpt == "ｙ":
            fromtable1 = session.execute("SELECT dilution, mol_formula, inchi_no, exp FROM odorDB.MOESM1_BY_NAME WHERE mol_name = %s",[d])
        elif inpt == 'n' or inpt == "ｎ":
            fromtable1 = session.execute("SELECT mol_formula, inchi_no, exp FROM odorDB.MOESM1_BY_NAME WHERE mol_name = %s",[d])
            

        #fromtable2 = session.execute("SELECT * FROM odorDB.calcfreq WHERE inchi_no = %s",[inchino[0]])

        outputex = input("Select the desired data output format.\n1: Standard I/O\n2: Text Format\n")

        if outputex == "1" or outputex =="１":

            print("//////////////////////   OUTPUT DATA   //////////////////////\n")
            print("\n")
            print("----------------------   FROM Table 1 ----------------------\n")
            for i in fromtable1:
                print(i)
            #print("----------------------   FROM Table 2 ----------------------\n")
            #for j in fromtable2:
            #    print(j)
        elif outputex == "2" or outputex == "２":
            with open("(os.path.dirname(__file__))"+ "/"+d+".txt","w") as f:
                f.writelines(fromtable1)
            f.close()
            #with open("(os.path.dirname(__file__))"+ "/"+d+".txt","a") as f:
            #    f.writelines(fromtable2)
            #    f.close()
        else:
            print("選択肢以外が選択されました。再度実行してください。")

    elif reqdata == "2" or reqdata == "２":
        d = input("please input mol_formula.")

        #inchino = session.execute("SELECT inchi_no FROM odorDB.MOESM1_ESM WHERE mol_formula=%s",[d])

        fromtable1 = session.execute("SELECT mol_name, exp FROM odorDB.MOESM1_BY_FORMULA WHERE mol_formula = %s",[d])
        #fromtable2 = session.execute("SELECT * FROM odorDB.calcfreq WHERE inchi_no = %s",[inchino[0]])

        outputex = input("Select the desired data output format.\n1: Standard I/O\n2: Text Format\n")

        if outputex == "1" or outputex == "１":

            print("//////////////////////   OUTPUT DATA   //////////////////////\n")
            print("\n")
            print("----------------------   FROM Table 1 ----------------------\n")
            for i in fromtable1:
                print(i)
            #print("----------------------   FROM Table 2 ----------------------\n")
            #for j in fromtable2:
            #    print(j)
        elif outputex == "2" or outputex == "２":
            with open("(os.path.dirname(__file__))"+ "/"+d+".txt","w") as f:
                f.writelines(fromtable1)
            f.close()
            #with open("(os.path.dirname(__file__))"+ "/"+d+".txt","a") as f:
            #    f.writelines(fromtable2)
            #    f.close()
        else:
            None

    elif reqdata == "3" or reqdata == "３":
        d = input("please input Inchi Number.")

        #inchino = session.execute("SELECT  FROM odorDB.MOESM1_ESM WHERE inchi_no=%s",[d])

        fromtable1 = session.execute("SELECT mol_name, mol_formula, exp FROM odorDB.MOESM1_BY_INCHI WHERE inchi_no = %s",[d])
        #fromtable2 = session.execute("SELECT * FROM odorDB.calcfreq WHERE inchi_no = %s",[inchino[0]])

        
        outputex = input("Select the desired data output format.\n1: Standard I/O\n2: Text Format\n")

        if outputex == "1" or outputex =="１":

            print("//////////////////////   OUTPUT DATA   //////////////////////\n")
            print("\n")
            print("----------------------   FROM Table 1 ----------------------\n")
            for i in fromtable1:
                print(i)
            #print("----------------------   FROM Table 2 ----------------------\n")
            #for j in fromtable2:
            #    print(j)
        elif outputex == "2" or outputex == "２":
            with open("(os.path.dirname(__file__))"+ "/"+d+".txt","w") as f:
                f.writelines(fromtable1)
            f.close()
            #with open("(os.path.dirname(__file__))"+ "/"+d+".txt","a") as f:
            #    f.writelines(fromtable2)
            #    f.close()
        else:
            None 
   
    else:
        None


    return        

