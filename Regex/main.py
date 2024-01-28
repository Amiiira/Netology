import ast
import csv
import re
from pprint import pprint

with open("Regex/phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


for contact in contacts_list:
    fullname = contact[0].split()
    lastname = " ".join(fullname[0].split())
    firstname = " ".join(contact[1].split())
    surname = " ".join(contact[2].split())

    if firstname == "":
        firstname = fullname[1]

    if len(fullname) == 3:
        surname = fullname[2]

    if len(firstname.split()) > 1:
        first_sur = firstname.split()
        firstname = " ".join(first_sur[0].split())
        surname = " ".join(first_sur[1].split())

    contact[0] = lastname
    contact[1] = firstname
    contact[2] = surname

pattern = re.compile(
    r"(\+7|8)[\s]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})([\s]?\(?(доб.)[\s](\d{4})\)?)?"
)
subst_pattern = r"+7(\2)\3-\4-\5 \7\8"
result = pattern.sub(subst_pattern, str(contacts_list))

data_list = ast.literal_eval(result)
merged_data = {}

for person in data_list[1:]:
    key = (person[0], person[1])
    if key not in merged_data:
        merged_data[key] = person
    else:
        for i, field in enumerate(person):
            if field and not merged_data[key][i]:
                merged_data[key][i] = field

merged_data = list(merged_data.values())


with open("Regex/phonebook.csv", "w", encoding="utf-8") as f:
    datawiter = csv.writer(f, delimiter=",")
    datawiter.writerows(merged_data)
