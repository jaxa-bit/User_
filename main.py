from tinydb import TinyDB
import tinydb
db = TinyDB('table.json')

data1 = {'name' : 'Samir' , 'age' : '99'}
data2 = {'name' : 'Jakob' , 'age' : '99'}
data3 = {'name' : 'Shea' , 'age' : '99'}
data4 = {'name' : 'Esty' , 'age' : '99'}
data5 = {'name' : 'Jeancarlos' , 'age' : '99'}
data6 = {'name' : 'Rylee' , 'age' : '99'}
data7 = {'name' : 'Amerie' , 'age' : '99'}
data8 = {'name' : 'Lyra' , 'age' : '99'}
data9 = {'name' : 'Ericka' , 'age' : '99'}
data10 = {'name' : 'Kepler' , 'age' : '99'}
data11 = {'name' : 'Izaan' , 'age' : '99'}
data12 = {'name' : 'Van' , 'age' : '99'}
data13 = {'name' : 'Eloise' , 'age' : '99'}
data14 = {'name' : 'Tysen' , 'age' : '99'}
data15 = {'name' : 'Fausto' , 'age' : '99'}
data16 = {'name' : 'Rafael' , 'age' : '99'}
data17 = {'name' : 'Baylor' , 'age' : '99'}
data18 = {'name' : 'Inara' , 'age' : '99'}
data19 = {'name' : 'Sama' , 'age' : '99'}
data20 = {'name' : 'Milliana' , 'age' : '99'}
data21 = {'name' : 'Moises' , 'age' : '99'}
data22 = {'name' : 'Irving' , 'age' : '99'}
data23 = {'name' : 'Omri' , 'age' : '99'}
data24 = {'name' : 'Keziah' , 'age' : '99'}
data25 = {'name' : 'Cameron' , 'age' : '99'}
data26 = {'name' : 'Avalon' , 'age' : '99'}
data27 = {'name' : 'Jeremih' , 'age' : '99'}
data28 = {'name' : 'Destin' , 'age' : '99'}
data29 = {'name' : 'Marlin' , 'age' : '99'}
data30 = {'name' : 'Janice' , 'age' : '99'}
data31 = {'name' : 'Dominique' , 'age' : '99'}
data32 = {'name' : 'David' , 'age' : '99'}
data33 = {'name' : 'Malayna' , 'age' : '99'}
data34 = {'name' : 'Madalyn' , 'age' : '99'}
data35 = {'name' : 'Irena' , 'age' : '99'}
data36 = {'name' : 'Hershel' , 'age' : '99'}
data37 = {'name' : 'Anjali' , 'age' : '99'}
data38 = {'name' : 'Soham' , 'age' : '99'}
data39 = {'name' : 'Kemora' , 'age' : '99'}
data40 = {'name' : 'Zaryah' , 'age' : '99'}
data41 = {'name' : 'Kaydan' , 'age' : '99'}
data42 = {'name' : 'Lenora' , 'age' : '99'}
data43 = {'name' : 'Jamel' , 'age' : '99'}
data44 = {'name' : 'Javion' , 'age' : '99'}
data45 = {'name' : 'Kensi' , 'age' : '99'}
data46 = {'name' : 'Abisai' , 'age' : '99'}
data47 = {'name' : 'Keniel' , 'age' : '99'}
data48 = {'name' : 'Ameer' , 'age' : '99'}
data49 = {'name' : 'Amador' , 'age' : '99'}
data50 = {'name' : 'Analyn' , 'age' : '99'}

db.insert_multiple([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,data31,data32,data33,data34,data35,data36,data37,data38,data39,data40,data41,data42,data43,data44,data45,data46,data47,data48,data49,data50])
print(db.all())
