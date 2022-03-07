import csv

articles = []
for (filename, filecode) in [('legislatie/ro/codul_penal', 'ro_cp'),
                             ('legislatie/ro/codul_civil', 'ro_cc')]:
    with open(filename) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for lines in tsv_file:
            for line in lines:
                articles.append((filecode, line))


with open('legislatie/legislatie_completa.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    for (id, article) in enumerate(articles):
        writer.writerow([id, article[0], article[1]])
