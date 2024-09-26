
import matplotlib.pyplot as plt
import csv

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def read_csv(file_path):
    noten_anzahl =[]
      #open csv file
    with open(file_path) as csvdatei:
        klassenliste = csv.reader(csvdatei)
        noten_str = [row[1]for row in klassenliste]  # sort out names
    noten = [int(n) for n in noten_str if is_number(n)]  #convert to int
    for i in range(1, 7):
        anzahl = noten.count(i)  # count grades
        noten_anzahl.append(anzahl)  # create list of counted grades
    return noten_anzahl


def plot_notenverteilung(noten_anzahl):
    noten = [1, 2, 3, 4, 5, 6]
    plt.bar(noten, noten_anzahl)
    plt.title('Notenverteilung')
    plt.ylabel('Anzahl')
    plt.xlabel('Noten')
    plt.savefig('Files/Notenverteilung_Bargraph.png')
    plt.show()

plot_notenverteilung(read_csv('Files/schueler_noten.csv'))

