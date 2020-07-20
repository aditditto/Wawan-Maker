import bs4
import csv
import pdfkit

import os
dirname = os.path.dirname(__file__)
path_wkhtmltopdf = os.path.join(dirname, r'wkhtmltox\bin\wkhtmltopdf.exe')
print(path_wkhtmltopdf)

with open('data.csv') as csvfile:
    data_csv = csv.reader(csvfile, delimiter=';')
    data_orang = []
    for row in data_csv:
        data_orang.append(row)

data_orang.pop(0)
html_id = ['nam', 'nim', 'jur', 'keu', 'fim']
for row in data_orang:
    with open("template.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
        for i in range(5):
            soup.find(id=html_id[i]).string += row[i]
    # path_wkhtmltopdf = r'wkhtmltox\bin\wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_string(soup.prettify(), f'16519346_{row[1]}.pdf', configuration=config)




# # jurusan = soup.find(id='jur')
# # jurusan.string += 'ppek'

# # with open('result.html', 'w') as target:
# #     target.write(soup.prettify())


# # pdfkit.from_file('result.html', 'out.pdf')