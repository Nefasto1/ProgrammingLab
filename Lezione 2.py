#------------------------------------------------------------------
my_file = open("shampoo_Sales.csv", "r");
print(my_file.read());
my_file.close();



stringa[0:50]    #dal primo al cinquantesimo carattere
stringa[3]       #il terzo carattere (da 0)
stringa[0:-1]    #dal primo al penultimo



my_file = open("shampoo_Sales.csv", "r");
print(my_file.read()stringa[0:50]);
my_file.close();


#------------------------------------------------------------------
# Apro il file
my_file = open("shampoo_sales.txt", "r")
# Leggo il contenuto
my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) >50:        #len = lenght
    print(my_file_contents[0:50])
else:
    print(my_file_contents)
# Chiudo il file
my_file.close()

#------------------------------------------------------------------
#ERRATO
my_file = open("shampoo_sales.csv", "r")
print(my_file.readline())
print(my_file.readline())  #legge singola riga
my_file.close()

#CORRETTO
my_file = open("shampoo_sales.csv", "r")
for line in my_file:
    print(line)
my_file.close()


#------------------------------------------------------------------
my_file = open("saluti.txt", "w")
my_file.write("Ciao mondo!")
my_file.close()

#------------------------------------------------------------------
#Split

stringa = "Ciao, come va?";
lista = stringa.split(",");

#------------------------------------------------------------------
#conversione

stringa = "5.5";
num = float(stringa);

#------------------------------------------------------------------
#aggiungi elementi a lista

lista = [1, 2, 3];
lista.append(4);

#------------------------------------------------------------------
#Lettura file csv

# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r")
for line in my_file:
 # Faccio lo split di ogni riga sulla virgola
 elements = line.split(',')
 # Se NON sto processando l’intestazione...
 if elements[0] != 'Date':
 # Setto la data e il valore
 date = elements[0]
 value = elements[1]
 # Aggiungo alla lista dei valori questo valore
 values.append(float(value))