from datetime import datetime

origin_file = str(input("Nom du fichier de donnée : "))
export_file = origin_file[:-4] + "_selection.txt"
debut = str(input("Date et heure de début (JJ/MM/AAA HH:MM) : "))  # "08/07/2019 13:24"
fin = str(input("Date et heure de fin (JJ/MM/AAA HH:MM) : "))  # "08/07/2019 13:44"

datetime_debut = datetime.strptime(debut, '%d/%m/%Y %H:%M')
datetime_fin = datetime.strptime(fin, '%d/%m/%Y %H:%M')

moved_line = 0
with open(export_file, "w") as ef:
    with open(origin_file) as f:
        for i, line in enumerate(f):
            if i > 7:  # On ignore les 7 premières lignes du fichier
                line_splitted = line.split("\t")
                date = line_splitted[0]
                datetime = datetime.strptime(date, '%d/%m/%Y %H:%M')
                if datetime_debut <= datetime < datetime_fin:
                    moved_line += 1
                    line = line.replace('\n', '')
                    ef.write(line + "\n")

print(moved_line, " lignes on été copiés dans le fichier ", export_file)

