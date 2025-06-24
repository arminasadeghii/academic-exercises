import random 
# in module baraye entekhab random computere


def bazi_dobare() : 
    darkhast = input("shurue bazi (yes or click on enter) ?")
    if darkhast == "" or darkhast.lower() == "yes" : 
        return True
    
    else : 
        print("lotfan javab monsaeb vared konid")
        return False
# in function baraye darkhast bazi dobaras
i = [["1","2","3"]
    ,["4","5","6"]
    ,["7","8","9"]] 
l1 = ["1","2","3","4","5","6","7","8","9"]

def shart_bazi(i, c, d):
    
    vaziat_barande = [
        [(0, 0), (0, 1), (0, 2)],  
        [(1, 0), (1, 1), (1, 2)],  
        [(2, 0), (2, 1), (2, 2)],  
        [(0, 0), (1, 0), (2, 0)],  
        [(0, 1), (1, 1), (2, 1)],  
        [(0, 2), (1, 2), (2, 2)],  
        [(0, 0), (1, 1), (2, 2)],  
        [(0, 2), (1, 1), (2, 0)]   
    ]

    for vaziat in vaziat_barande :
        if all(i[row][col] == c for row, col in vaziat):
            print(f"{d} Winnn !!! ")
            return True
    return False
# in function baraye sharayet bord va bakhte

def startgame() : 
    noe_bazi = input("bazi ba (computer) ya bazi (do nafare) : ")
    #dar inja az karbar mikhaym noe bazi ro entekhab kone
    tedad_round = int(input("tedad round haro vared konin : "))
    player1_wins = 0
    player2_wins = 0
    ties = 0
    
    for c in range(tedad_round) : 
    
        if noe_bazi == "computer" : 
   
            name = input("esm bazikon : ")
            #inja az karbar mikhaym ke esm khodesho vared kone
    

            b = input("beyn x va o entekhab kon : ")
            if b == "x" :
                computer = "o"
            else : 
                computer = "x"

            i = [["1","2","3"]
            ,["4","5","6"]
            ,["7","8","9"]] 

            l1 = ["1","2","3","4","5","6","7","8","9"]

            history = [ ]

            while  len(l1) > 0  : 

                rand = random.randint(0,len(l1)-1)
                computer_choice = l1[rand]
                # inja az sintax module random estefade mikonim 
        
                print(i[0])
                print(i[1])
                print(i[2])
                print("baraye bargasht be marhale ghabl undo bejaye entekhab bezarid")

                entekhab_b = input(f"{name},entekhab kon : ") 
                # az f"{} baraye inke esm karbar o neshon bede estefade mishe
                history.append((i,l1[:]))

            

                for x in i[0] :
                    if x == entekhab_b:
                        x_p = i[0].index(x)
                        i[0][x_p] = b
                        l1.remove(entekhab_b)
             
                for x in i[1] : 
                    if x == entekhab_b:
                        x_p = i[1].index(x)
                        i[1][x_p] = b
                        l1.remove(entekhab_b)
                
                for x in i[2] : 
                    if x == entekhab_b:
                        x_p = i[2].index(x)
                        i[2][x_p] = b
                        l1.remove(entekhab_b)

                if shart_bazi(i,b,name) : 
                    player1_wins += 1
                    break 

                print(i[0])
                print(i[1])
                print(i[2])
        
                for x in i[0] : 
                    if x == computer_choice :
                        x_p = i[0].index(computer_choice)
                        i[0][x_p] = computer
                        l1.remove(computer_choice)
            
                for x in i[1] : 
                    if x == computer_choice :
                        x_p = i[1].index(computer_choice)
                        i[1][x_p] = computer
                        l1.remove(computer_choice)
            
            
                for x in i[2] : 
                    if x == computer_choice :
                        x_p = i[2].index(computer_choice)
                        i[2][x_p] = computer
                        l1.remove(computer_choice)
    
                if shart_bazi(i,computer,"computer"):
                    player2_wins += 1 
                    break

                if entekhab_b == 'undo' : 
                    print(history)
            if len(l1) == 0 and not any(shart_bazi(i, b, name) or shart_bazi(i, computer,"computer") for b in ["x", "o"]):
                print("MOSAVI SHOD!!!")
     #in shart baraye zamanie ke tamom khone ha por shode va kasi barande nashode

            print(f"\nNatayej bazi: {name} {player1_wins} - computer {player2_wins}")  

            print(i[0])
            print(i[1])
            print(i[2])
        
    

    
        if noe_bazi == "do nafare":
            name_1 = input("esm bazikon 1 : ")
            name_2 = input("esm bazikon 2 : ")
    # inja az 2 karbar be sorat joda mikhaym ke esmeshono vared konan
            b_1 = input("beyn x va o entekhab kon : ")
            if b_1 == "x" :
                b_2 = "o"
            else : 
                b_2 = "x" 
    # inja az do karbar mikhaym beyn x va o entekhab konan
            i = [["1","2","3"]
             ,["4","5","6"]
             ,["7","8","9"]]
    # inja yek matris tashkil midim 
            l1 = ["1","2","3","4","5","6","7","8","9"]
            history = []
    
    
            while len(l1)>0 : 

                print(i[0])
                print(i[1])
                print(i[2])
                print("baraye bargasht be marhale ghabl undo bejaye entekhab bezarid")

                entekhab_b_1 = input(f"{name_1},entekhab kon  :") 
                history.append((i,l1[:]))

                for y in i[0] :
                    if y == entekhab_b_1:
                        y_p = i[0].index(y)
                        i[0][y_p] = b_1
                        l1.remove(entekhab_b_1)

                for y in i[1] : 
                    if y == entekhab_b_1:
                        y_p = i[1].index(y)
                        i[1][y_p] = b_1
                        l1.remove(entekhab_b_1)
                
            
                for y in i[2] : 
                    if y == entekhab_b_1:
                        y_p = i[2].index(y)
                        i[2][y_p] = b_1
                        l1.remove(entekhab_b_1)

                if shart_bazi(i,b_1,name_1) :
                    player1_wins += 1
                    break  
                if entekhab_b_1 == 'undo' : 
                    print(history)      
        # in halghe ha baraye jaygozini x ya o dar jaygaha anjam mishe
                print(i[0])
                print(i[1])
                print(i[2])
            
                entekhab_b_2 = input(f"{name_2},entekhab kon :")
                history.append((i,l1[:]))
        
                for y in i[0] : 
                    if y == entekhab_b_2:
                        y_p_2 = i[0].index(y)
                        i[0][y_p_2] = b_2
                        l1.remove(entekhab_b_2)
            # inja ba estefade az index shomare jayi k mikhad jaygozin she o migirim
            #bad mosavi x ya o gharar midim
        
                    for y in i[1] : 
                        if y == entekhab_b_2:
                            y_p_2 = i[1].index(y)
                            i[1][y_p_2] = b_2
                            l1.remove(entekhab_b_2)
            
                    for q in i[2] : 
                        if q == entekhab_b_2:
                            q_p_2 = i[2].index(q)
                            i[2][q_p_2] = b_2
                            l1.remove(entekhab_b_2)
         
                    if shart_bazi(i,b_2,name_2):
                        player2_wins += 1
                        break
                    if entekhab_b_2 == 'undo' : 
                        print(history)      
        # dar nahayat inja esm bazikon be hamrah bord ya bakhtesh namayesh dade mishe
            if len(l1) == 0 and not any(shart_bazi(i, b_1,name_1) or shart_bazi(i,b_2,name_2)for b in ["x", "o"]):
                print("MOSAVI SHOD!!!")
            # in shart baraye sharayet mosavi bodane
            print(f"\nNatayej bazi: {name_1} {player1_wins} - {name_2} {player2_wins}")
    

if bazi_dobare():
    startgame()

# in shart baraye dobare bazi kardane