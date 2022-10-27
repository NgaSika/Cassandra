
def search():
    ch = input("index.txtの検索を行います。TimeUUIDから求める場合は１を、分子名から求める場合は２を入力してください。")

    elist =[]
    idlist =[]
    with open("./index.txt")as f:
        for line in f:
            a = line.replace("element name : ", "").replace(" timeuuid " ,"")
            b = a.split(":")
            c = b[1].replace(" ","").replace("\n","")
            
            elist.append(b[0])
            idlist.append(c)


    if ch == "1":
        tid = input("TimeUUIDから分子名を抽出します。TimeUUIDを入力してください。")
        d = idlist.index(tid)
        print(f"TimeUUID{tid}の対応する分子名は{elist[d]}です。")
    elif ch == "2":
        el = input("分子名でTimeUUIDを検索します。分子名を入力してください。また、記号同士が隣り合う場合、間に空白入れないでください。")
        e = elist.index(el)
        print(f"分子名{el}に対応するTineUUIDは{idlist[e]}です。")