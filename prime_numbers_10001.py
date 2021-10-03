a = list(range(0,3,1))
b= list( range(0, 3,1))
#a=[0,1,2]
#b=[0,1,2]
philosophy =[]
university = []
for item in a:
    for items in b:
        philosophy.append(item)
        philosophy.append(items)
        #print(item,items)     
        university.append(philosophy)
        philosophy =[]

difficulty = []
abscess = 0
#print(university)

artificial = 0

cancer = 1
for disease in university:
         verification = university.index(disease)
         while disease[0] != university[len(university)-1][0]:
                  print(disease, university [verification -1])
                  artificial += cancer
                  disease [0] += cancer

                 # print(artificial , 210012210)

      
      


print((abscess , artificial ))