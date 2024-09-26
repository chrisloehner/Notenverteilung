import matplotlib
import matplotlib.pyplot as plt
import csv

with open('Files/schueler_noten.csv') as csvdatei:
    notenliste = csv.reader(csvdatei)
    for row in notenliste:
        print(row[1])


def plot_notenverteilung():
    noten = [1, 2, 3, 4, 5, 6]
    noten_anzahl = [4, 7, 10, 2, 1, 0]
    plt.bar(noten, noten_anzahl)
    plt.title('Notenverteilung')
    plt.ylabel('Anzahl')
    plt.xlabel('Noten')
    plt.show()


