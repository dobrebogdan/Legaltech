import csv
articles = []

for (filename, filecode) in [('legislatie/ro/codul_penal', 'ro_cp'),
                             ('legislatie/ro/codul_civil', 'ro_cc')]:
    with open(filename) as f:
        content = f.read()
        lines = content.split("$Articolul ")[1:]
        formated_lines = []
        [formated_lines.append(f"Articolul {line}") for line in lines]
        for line in formated_lines:
            articles.append((filecode, line))

print(articles)

with open('legislatie/legislatie_completa.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    for (id, article) in enumerate(articles):
        writer.writerow([id, article[0], article[1]])
