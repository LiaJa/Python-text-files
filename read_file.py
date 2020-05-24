# Tu zagrabi še prvo vrstico - tega ne sme!!!
# with open("tabela.csv", "r") as tabela_file:
#     tabela_lines = tabela_file.readlines()
#     for line in tabela_lines:
#         tabela = line.split(",")
#         name = tabela[0]
#         gender = tabela[1]
#         age = tabela[2]
#         print(name + " is " + gender + " and " + age + " years old.")

with open("tabela.csv", "r") as file:
    lines = file.readlines()
    lines.pop(0)
    for line in lines:
        line_list = line.split(",")
        name = line_list[0]
        gender = line_list[2]
        age = line_list[1]
        print(name + " is " + gender + " and " + age + " years old.")