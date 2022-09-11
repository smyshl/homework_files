# Домашняя работа по теме «Открытие и чтение файла, запись в файл»
# Часть про файлы

with open('files\\1.txt', encoding='utf-8') as f_1:

    with open('files\\2.txt', encoding='utf-8') as f_2:

        with open('files\\3.txt', encoding='utf-8') as f_3:

            file_list_1 = f_1.readlines()
            file_list_2 = f_2.readlines()
            file_list_3 = f_3.readlines()

            files_list = [(len(file_list_1), f_1.name, file_list_1), (len(file_list_2), f_2.name, file_list_2),
                          (len(file_list_3), f_3.name, file_list_3)]

            files_list.sort()

            with open('result_file.txt', 'w', encoding='utf-8') as f_result:

                for file in files_list:
                    f_result.write(file[1].strip(('files\\')) + '\n')
                    f_result.write(str(file[0]) + '\n')
                    f_result.writelines(file[2])
                    f_result.write('\n')

