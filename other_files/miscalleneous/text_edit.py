
import re

def write_output_file():
    linelist = []
    with open("C:/Users/vajravel/Desktop/Eethalview/other_files/miscalleneous/struct.txt", 'r', encoding='cp1252') as file:  # windows
        linelist = file.readlines()

    # 
    nof_lines = len(linelist)
    for i in range(0, nof_lines):
        line = linelist[i]
        print(line)

        splitted = line.split(':')
        print(splitted[0])
        print(splitted[1])

        first = splitted[0]
        second = splitted[1]

        second_split = second.split(', ')
        #print("second_split", second_split)

        new_second = ""
        for item in second_split:
            new_second += "'" + item + "'" + ", "

        # remove first comma
        new_second = new_second[3:]
        new_second = "['" + new_second
        new_second = new_second[:-3]

        print("first: ", first)
        print("new_second: ", new_second)

        line = first + ': ' + str(new_second)
        #print(line)

        # if line.isdigit() == False:
        #     line = ''

        # replace â€ with :
        #line = line.replace("â€”", ":")
        # splitted = line.rsplit()
        #print(splitted)

        # remove spaces and form a string
        # newline = ""
        # for item in splitted:
        #     if(item != '.'):
        #         newline += item + ' '
        #print(newline)

        # remove last space
        # newline = newline[:-1]

        # remove last char, if it is dot
        # if(newline[len(newline)-1] == '.'):
        #     newline = newline[:-1]

        # remove space bw element and number
        # twostr = newline.split(':', 1)
        # twostr[0] = twostr[0].replace(' ', '')
        # twostr[1] = (twostr[1])[1:]
        # newstr = '\'' + twostr[0] + '\'' + ' : ' + '\'' + twostr[1] + '\'' + ','

        # remove comma in last line manually

        linelist[i] = line

    txtfile = open("C:/Users/vajravel/Desktop/Eethalview/other_files/miscalleneous/structee.txt", 'w')
    for line in linelist:
        txtfile.write(line)
    txtfile.close()

def main():
    write_output_file()

main()