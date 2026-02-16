My_chip=10
def draw(hand):#一枚ドローする関数
    global deck
    import random
    result=random.choice(deck)
    deck.remove(result)
    print(f"出たカード：{result}")
    if type(result)==int:
        hand.append(result)
    elif result=="A":
        hand.append(11)
    else:
        hand.append(10)

print("ルール説明\n・10枚のチップを100枚にすればゲームクリア。0枚でゲームオーバー。\n・勝てばチップが2倍になるが、Aと10点札が揃ったとき（ブラックジャック）は1.5倍になる。なお小数点は繰り上げになる。")
print("ゲーム進行\n・賭けるチップを入力するとカードを二枚ドローされ、追加で引くかどうかを選択する。(y/n)\n・引かないを選択するとディーラーのターンになり2枚ドローした後17点以上になるまでドローする")
print("・勝負の結果が出た後に再び賭けるチップを入力する。")
startyn="n"
while startyn=="n":
    start=input("始めるには\"start\"と入力してください＞＞")
    if not start=="start":
        print("\"start\"と入力してください")
    else:
        startyn="y"

while 0<My_chip<100:
    print(f"所持チップ：{My_chip}")
    bet_start="n"
    while bet_start=="n":
        bet_chip=input("チップをいくら賭けますか？＞＞")
        try:
            num=int(bet_chip)
            if int(bet_chip)>My_chip:
                print("チップが足りません")
            elif int(bet_chip)<=0:
                print("１以上のチップを賭けてください")
            elif int(bet_chip)<=My_chip:
                bet_start="y"
                My_chip=int(My_chip)-int(bet_chip)
        except ValueError:
             print("整数を入力してください")

    deck=["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
    print("こちらの手札２枚を見ます")
    My_Hand=[]
    for aa in range(2):
        draw(My_Hand)
        print(f"合計：{sum(My_Hand)}")
    if sum(My_Hand)==21:
        print("ブラックジャック！")
    else:
            if sum(My_Hand)==22:
                My_Hand[0]=1
                print("Aを１として扱う")
                print(f"合計：{sum(My_Hand)}")
            else:
                pass
            ppppp="y"
            while ppppp=="y":
                if sum(My_Hand)<=21:
                    addition=input("追加でドローしますか？（y/n）")
                    if addition=="y":
                        print("一枚ドロー")
                        draw(My_Hand)
                        ppppp="y"
                    else:
                        ppppp="n"
                else:
                    if 11 in My_Hand:
                        for data1 in range(len(My_Hand)):
                            if My_Hand[data1]==11 and sum(My_Hand)>21:
                                My_Hand[data1]=1
                            else:
                                pass
                        print("Aを１として扱う")
                    else:
                        print("バスト")
                        break
                print(f"合計：{sum(My_Hand)}")
            
    print("\n続いてディーラーが引きます")
    dealers_Hand=[]
    for aa in range(2):
        draw(dealers_Hand)
    print(f"合計：{sum(dealers_Hand)}")
    if sum(dealers_Hand)==21:
        print("ブラックジャック！")    
    else:
        if sum(dealers_Hand)==22:
            dealers_Hand[0]=1
            print("Aを１として扱う")
            print(f"合計：{sum(dealers_Hand)}")
        else:
            pass
        if sum(dealers_Hand)<17:
            print("17以上になるまで引きます")
            while sum(dealers_Hand)<17:
                draw(dealers_Hand)
                if sum(dealers_Hand)>21:
                    if 11 in dealers_Hand:
                        for data2 in range(len(dealers_Hand)):
                                if dealers_Hand[data2]==11 and sum(dealers_Hand)>21:
                                    dealers_Hand[data2]=1
                                else:
                                    pass
                        print("Ａを１として扱う")
                    else:
                        print("バスト")
                        break
                else:
                    pass
                print(f"合計：{sum(dealers_Hand)}")
                    


    if len(dealers_Hand)==2 and sum(dealers_Hand)==21 and len(My_Hand)>2:
            print("ディーラーのブラックジャックにより負け")
    elif len(My_Hand)==2 and sum(My_Hand)==21 and len(dealers_Hand)>2:
            print("こちらのブラックジャックにより勝ち")
            My_chip+=int(((int(bet_chip)*3/2)*10)/10)
    elif sum(My_Hand)>21 and sum(dealers_Hand)>21:
        print("引き分け（プッシュ）")
        My_chip+=int(bet_chip)
    elif sum(My_Hand)>21:
        print("こちらのバストにより敗北")   
    elif sum(dealers_Hand)>21:
        print("ディーラーのバストにより勝利")
        My_chip+=int(bet_chip)*2
    elif sum(dealers_Hand)>sum(My_Hand):
        print(f"こちらの点：{sum(My_Hand)}\nディーラーの点：{sum(dealers_Hand)}\n負け")
    elif sum(dealers_Hand)<sum(My_Hand):
        print(f"こちらの点：{sum(My_Hand)}\nディーラーの点：{sum(dealers_Hand)}\n勝ち")
        My_chip+=int(bet_chip)*2
    else:
        print("引き分け（プッシュ）")
        My_chip+=int(bet_chip)

print(f"所持チップ：{My_chip}")    
if My_chip==0:
    print("ゲームオーバー")
else:
    print("ゲームクリア")










