
import matplotlib.pyplot as plt
import csv


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def plot_notenverteilung(file_path):
    noten_anzahl = []
    schulnoten = [1, 2, 3, 4, 5, 6]
    # open csv file
    with open(file_path) as csvdatei:
        klassenliste = csv.reader(csvdatei)
        noten_str = [row[1]for row in klassenliste]  # sort out names
    noten = [int(n) for n in noten_str if is_number(n)]  # convert to int
    for i in range(1, 7):
        anzahl = noten.count(i)  # count grades
        noten_anzahl.append(anzahl)  # create list of counted grades
    # Durchschnitt berechnen
    gesamtnote = sum(noten)
    gesamtnotenanzahl = sum(noten_anzahl)
    notendurchscnitt = gesamtnote / gesamtnotenanzahl
    print(notendurchscnitt)
    plt.bar(schulnoten, noten_anzahl, label= f'Notendurchscnitt:{notendurchscnitt}')
    plt.title('Notenverteilung')
    plt.ylabel('Anzahl')
    plt.xlabel('Noten')
    plt.legend()
    plt.savefig('Files/Notenverteilung_Bargraph.png')
    plt.show()





plot_notenverteilung('Files/schueler_noten.csv')
