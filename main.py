import time
ifmain = False
ver_a = ""
ver_b = ""
ver_c = ""
ver_d = ""
ver_e = ""
ver_f = ""
ver_g = ""
ver_h = ""
int_a = 0
int_b = 0
int_c = 0
int_d = 0
def oper():
    pass

ad = input('Dosya Adı:')
with open(ad + '.eg') as dosya:
    print('Çalıştırılıyor........\n---------------------------------------------------')
    read = dosya.readlines()
    i = 0
    while True:
        try:
            rood = read[i]
            rood = rood.replace('&a',ver_a)
            rood = rood.replace('&b',ver_b)
            rood = rood.replace('&c',ver_c)
            rood = rood.replace('&d',ver_d)
            rood = rood.replace('&e',ver_e)
            rood = rood.replace('&f',ver_f)
            rood = rood.replace('&g',ver_g)
            rood = rood.replace('&h',ver_h)
            
            
            
            


            if rood == 'EG_start:\n' :
                ifmain = True

            if rood == 'eg_STOP':
                print("eg_STOP!!")
                
            if 'print: ' in rood and ifmain == True:
                rood = rood.replace('print: ','')
                rood = rood.replace('\n','')
                rood = rood.replace('""','')
                print(rood)

            if 'str: ' in rood and ifmain == True:
                rood = rood.replace('str: ','')
                rood = rood.replace('\n','')
                rooda = rood.split('=')
                if rooda[0] == 'a':
                    ver_a = rooda[1]
                if rooda[0] == 'b':
                    ver_b = rooda[1]
                if rooda[0] == 'c':
                    ver_c = rooda[1]
                if rooda[0] == 'd':
                    ver_d = rooda[1]
                if rooda[0] == 'e':
                    ver_e = rooda[1]
                if rooda[0] == 'f':
                    ver_f = rooda[1]
                if rooda[0] == 'g':
                    ver_g = rooda[1]
                if rooda[0] == 'h':
                    ver_h = rooda[1]


                    
                    
                

            if 'print.var(str):' in rood and ifmain == True:
                rood = rood.replace('print.var(str):','')
                rood = rood.replace('\n','')
                rooda = rood.split(',')
                if rooda[0] == 'a':
                    print(ver_a)
                if rooda[0] == 'b':
                    print(ver_b)
                if rooda[0] == 'c':
                    print(ver_c)
                if rooda[0] == 'd':
                    print(ver_d)
            
        
            if 'int: ' in rood and ifmain == True:
                rood = rood.replace('int: ','')
                rood = rood.replace('\n','')
                rooda = rood.split('=')
                if rooda[0] == 'a':
                    ver_a = int(input(rooda[1]))
                if rooda[0] == 'b':
                    ver_b = int(input(rooda[1]))
                if rooda[0] == 'c':
                    ver_c = int(input(rooda[1]))
                if rooda[0] == 'd':
                    ver_d = int(input(rooda[1]))
                if rooda[0] == 'e':
                    ver_e = int(input(rooda[1]))
                if rooda[0] == 'f':
                    ver_f = int(input(rooda[1]))
                if rooda[0] == 'g':
                    ver_g = int(input(rooda[1]))
                if rooda[0] == 'h':
                    ver_h = int(input(rooda[1]))
                
                    
        

            if 'print.var(int):' in rood and ifmain == True:
                rood = rood.replace('print.var(int):','')
                rood = rood.replace('\n','')
                rooda = rood.split(',')
                if rooda[0] == 'a':
                    print(int_a)
                if rooda[0] == 'b':
                    print(int_b)
                if rooda[0] == 'c':
                    print(int_c)
                if rooda[0] == 'd':
                    print(int_d)
            
                    
        
            #if 'event.kerem.msg' in rood and ifmain == True:
             #   rood = rood.replace('event.kerem.msg','')
              #  rood = rood.replace('\n','')
               # print("'ünlü olurum inş' -- KEREM")

        

                        
        
            if '/*' in rood :
                rood = rood.replace('/*','')
                rood = rood.replace('\n','')

            if 'event.kerem.math:' in rood and ifmain == True:
                oper()

            if 'event.eg.version' in rood and ifmain == True:
                print("HELLLO EG-LANG V1.4 -- ELSE - MATH - LİST")
                
            if 'event.input :' in rood and ifmain == True:
                rood = rood.replace('event.input :','')
                rood = rood.replace('\n','')
                rooda = rood.split(',')
        
                if rooda[0] == 'a':
                    ver_a = input(rooda[1])
                if rooda[0] == 'b':
                    ver_b = input(rooda[1])
                if rooda[0] == 'c':
                    ver_c = input(rooda[1])
                if rooda[0] == 'd':
                    ver_d = input(rooda[1])

                if rooda[0] == 'int_a':
                    int_a = int(input(rooda[1]))
                if rooda[0] == 'int_b':
                    ver_b = int(input(rooda[1]))
                if rooda[0] == 'int_c':
                    int_c = int(input(rooda[1]))
                if rooda[0] == 'int_d':
                    ver_d = int(input(rooda[1]))
                    

                



            if 'a += ' in rood:
                rood = rood.replace('a += ','')
                int_a += int(rood)
            if 'b += ' in rood:
                rood = rood.replace('b += ','')
                int_b += int(rood)
            if 'a -= ' in rood:
                rood = rood.replace('a += ','')
                int_a += int(rood)
            if 'b -= ' in rood:
                rood = rood.replace('b += ','')
                int_b -= int(rood)

            if 'var a ?' in rood:
                print(ver_a)
            if 'var b ?' in rood:
                print(ver_b)

            if 'var int_a ?' in rood:
                print(int_a)
            if 'var int_b ?' in rood:
                print(int_b)
                
            if 'var c ?' in rood:
                print(ver_c)
            if 'var d ?' in rood:
                print(ver_d)

            if 'var int_c ?' in rood:
                print(int_c)
            if 'var int_d ?' in rood:
                print(int_d)

            if 'event.eg.sleep ' in rood and ifmain == True:
                rood = rood.replace('event.eg.sleep ','')
                rood = rood.replace('\n','')
                rooda = rood.split(':')
                time.sleep(int(rooda[1]))
            
            if 'math: ' in rood and ifmain == True:
                rood = rood.replace('math: ','')
                rood = rood.replace('\n','')
                rooda = rood.split(' ')
                #a ile operatörler
                if rooda[1] == "a +":
                    if rooda[2] == "a":
                        print(int_a + int_a)
                    if rooda[2] == "b":
                        print(int_a + int_b)
                    if rooda[2] == "c":
                        print(int_a + int_c)
                    if rooda[2] == "d":
                        print(int_a + int_d)
                if rooda[1] == "a -":
                    if rooda[2] == "a":
                        print(int_a - int_a)
                    if rooda[2] == "b":
                        print(int_a - int_b)
                    if rooda[2] == "c":
                        print(int_a - int_c)
                    if rooda[2] == "d":
                        print(int_a - int_d)
                if rooda[1] == "a *":
                    if rooda[2] == "a":
                        print(int_a * int_a)
                    if rooda[2] == "b":
                        print(int_a * int_b)
                    if rooda[2] == "c":
                        print(int_a * int_c)
                    if rooda[2] == "d":
                        print(int_a * int_d)
                if rooda[1] == "a /":
                    if rooda[2] == "a":
                        print(int_a / int_a)
                    if rooda[2] == "b":
                        print(int_a / int_b)
                    if rooda[2] == "c":
                        print(int_a / int_c)
                    if rooda[2] == "d":
                        print(int_a / int_d)
                # b ile operatörler
                if rooda[1] == "b +":
                    if rooda[2] == "a":
                        print(int_b + int_a)
                    if rooda[2] == "b":
                        print(int_b + int_b)
                    if rooda[2] == "c":
                        print(int_b + int_c)
                    if rooda[2] == "d":
                        print(int_b + int_d)
                if rooda[1] == "b -":
                    if rooda[2] == "a":
                        print(int_b - int_a)
                    if rooda[2] == "b":
                        print(int_b - int_b)
                    if rooda[2] == "c":
                        print(int_b - int_c)
                    if rooda[2] == "d":
                        print(int_b - int_d)
                if rooda[1] == "b *":
                    if rooda[2] == "a":
                        print(int_b * int_a)
                    if rooda[2] == "b":
                        print(int_b * int_b)
                    if rooda[2] == "c":
                        print(int_b * int_c)
                    if rooda[2] == "d":
                        print(int_b * int_d)
                if rooda[1] == "b /":
                    if rooda[2] == "a":
                        print(int_b / int_a)
                    if rooda[2] == "b":
                        print(int_b / int_b)
                    if rooda[2] == "c":
                        print(int_b / int_c)
                    if rooda[2] == "d":
                        print(int_b / int_d)
                #c ile operatörler
                if rooda[1] == "c +":
                    if rooda[2] == "a":
                        print(int_c + int_a)
                    if rooda[2] == "b":
                        print(int_c + int_b)
                    if rooda[2] == "c":
                        print(int_c + int_c)
                    if rooda[2] == "d":
                        print(int_c + int_d)
                if rooda[1] == "c -":
                    if rooda[2] == "a":
                        print(int_c - int_a)
                    if rooda[2] == "b":
                        print(int_c - int_b)
                    if rooda[2] == "c":
                        print(int_c - int_c)
                    if rooda[2] == "d":
                        print(int_c - int_d)
                if rooda[1] == "c *":
                    if rooda[2] == "a":
                        print(int_c * int_a)
                    if rooda[2] == "b":
                        print(int_c * int_b)
                    if rooda[2] == "c":
                        print(int_c * int_c)
                    if rooda[2] == "d":
                        print(int_c * int_d)
                if rooda[1] == "c /":
                    if rooda[2] == "a":
                        print(int_c / int_a)
                    if rooda[2] == "b":
                        print(int_c / int_b)
                    if rooda[2] == "c":
                        print(int_c / int_c)
                    if rooda[2] == "d":
                        print(int_c / int_d)
                #d ile operatörler
                if rooda[1] == "d +":
                    if rooda[2] == "a":
                        print(int_d + int_a)
                    if rooda[2] == "b":
                        print(int_d + int_b)
                    if rooda[2] == "c":
                        print(int_d + int_c)
                    if rooda[2] == "d":
                        print(int_d + int_d)
                if rooda[1] == "d -":
                    if rooda[2] == "a":
                        print(int_d - int_a)
                    if rooda[2] == "b":
                        print(int_d - int_b)
                    if rooda[2] == "c":
                        print(int_d - int_c)
                    if rooda[2] == "d":
                        print(int_d - int_d)
                if rooda[1] == "d *":
                    if rooda[2] == "a":
                        print(int_d * int_a)
                    if rooda[2] == "b":
                        print(int_d * int_b)
                    if rooda[2] == "c":
                        print(int_d * int_c)
                    if rooda[2] == "d":
                        print(int_d * int_d)
                if rooda[1] == "d /":
                    if rooda[2] == "a":
                        print(int_d / int_a)
                    if rooda[2] == "b":
                        print(int_d / int_b)
                    if rooda[2] == "c":
                        print(int_d / int_c)
                    if rooda[2] == "d":
                        print(int_d / int_d)




            if 'if :' in rood and ifmain == True:
                rood = rood.replace('if :','')
                rood = rood.replace('\n','')
                rooda = rood.split(',')
                if rooda[1] == '==' and rooda[0] != rooda[2] :
                    ifmain = False
                if rooda[1] == '!=' and rooda[0] == rooda[2] :
                        ifmain = False
                if rooda[1] == '>' :
                    if rooda[0] < rooda[2] or rooda[0] == rooda[2]:
                        ifmain = False
                if rooda[1] == '<':
                    if rooda[0] < rooda[2] or rooda[0] == rooda[2]:
                        ifmain = False
                if rooda[1] == '=>' and rooda[0] < rooda[2] :
                    ifmain = False
                if rooda[1] == '<=' and rooda[0] > rooda[2] :
                    ifmain = False

            if rood == 'if.end()\n':
                ifmain = True

                
            if rood == 'Loop.Reolad\n' and ifmain == True:
                while True:
                    i -= 1
                    if read[i] == "Loop.Start\n":
                        break

            if rood == 'Loop.Break\n' and ifmain == True:
                while True:
                    i += 1
                    if read[i] == "Loop.Reolad\n":
                        break
                
            time.sleep(0.1)
            i += 1
        except:
            pass
