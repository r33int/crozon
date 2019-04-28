import codecs

enb = input('Enter eNb ID: ')
print("eNb:", enb)

tac = input('Enter TAC: ')
print("TAC:", tac)

lat = input('Enter lat: ')
print("lat:", lat)

lon = input('Enter lon: ')
print("lon:", lon)

pci = input('Enter s0 pci (cid 9,12,15,700cid1,27): ')
print("pci:", pci)
pci1= int(pci)
pci2= int(pci) + int(1)
pci3= int(pci) + int(2)
print (pci1)
print (pci2)
print (pci3)

name = input('Enter name: ')
print("name:", name)

#lines to gen

#2600
line4= ("4G;208;20;9;{0};{1};{2};{3};{4};{5} [2600][S1];3175\n".format(tac, enb, pci1, lat, lon, name))
line5= ("4G;208;20;10;{0};{1};{2};{3};{4};{5} [2600][S2];3175\n".format(tac, enb, pci2, lat, lon, name))
line6= ("4G;208;20;11;{0};{1};{2};{3};{4};{5} [2600][S3];3175\n".format(tac, enb, pci3, lat, lon, name))

#1800
line1= ("4G;208;20;12;{0};{1};{2};{3};{4};{5} [1800][S1];1850\n".format(tac, enb, pci1, lat, lon, name))
line2= ("4G;208;20;13;{0};{1};{2};{3};{4};{5} [1800][S2];1850\n".format(tac, enb, pci2, lat, lon, name))
line3= ("4G;208;20;14;{0};{1};{2};{3};{4};{5} [1800][S3];1850\n".format(tac, enb, pci3, lat, lon, name))

#800
line7= ("4G;208;20;15;{0};{1};{2};{3};{4};{5} [800][S1];6200\n".format(tac, enb, pci1, lat, lon, name))
line8= ("4G;208;20;16;{0};{1};{2};{3};{4};{5} [800][S2];6200\n".format(tac, enb, pci2, lat, lon, name))
line9= ("4G;208;20;17;{0};{1};{2};{3};{4};{5} [800][S3];6200\n".format(tac, enb, pci3, lat, lon, name))

#700
line10= ("4G;208;20;700cid1;{0};{1};{2};{3};{4};{5} [700][S1];9385\n".format(tac, enb, pci1, lat, lon, name))
line11= ("4G;208;20;700cid2;{0};{1};{2};{3};{4};{5} [700][S2];9385\n".format(tac, enb, pci2, lat, lon, name))
line12= ("4G;208;20;700cid3;{0};{1};{2};{3};{4};{5} [700][S3];9385\n".format(tac, enb, pci3, lat, lon, name))

#2100
line13= ("4G;208;20;27;{0};{1};{2};{3};{4};{5} [2100][S1];251\n".format(tac, enb, pci1, lat, lon, name))
line14= ("4G;208;20;28;{0};{1};{2};{3};{4};{5} [2100][S2];251\n".format(tac, enb, pci2, lat, lon, name))
line15= ("4G;208;20;29;{0};{1};{2};{3};{4};{5} [2100][S3];251\n".format(tac, enb, pci3, lat, lon, name))

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(line10)
print(line11)
print(line12)
print(line13)
print(line14)
print(line15)

f= codecs.open("bt.ntm","a+", "utf-8")
f.write(line1)
f.write(line2)
f.write(line3)
f.write(line4)
f.write(line5)
f.write(line6)
f.write(line7)
f.write(line8)
f.write(line9)
f.write(line10)
f.write(line11)
f.write(line12)
f.write(line13)
f.write(line14)
f.write(line15)
f.close()