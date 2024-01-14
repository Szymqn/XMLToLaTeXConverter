import xml.etree.ElementTree as ET


def xml_to_tex(xml_filename, tex_filename):
    tree = ET.parse(xml_filename)
    root = tree.getroot()

    with open(tex_filename, 'w') as tex_file:
        tex_file.write('\\documentclass{article}\n')
        tex_file.write('\\begin{document}\n')
        tex_file.write('\\section{Table}\n')

        table_children = root[:3]
        num_children = len(table_children)
        total_grandchildren = sum(len(list(child)) for child in table_children)
        each_grandchildren = int(total_grandchildren / num_children)

        tex_file.write('\\begin{center}\n')
        tex_file.write('\\begin{tabular}{|' + 'c|' * each_grandchildren + '}\n')
        tex_file.write('\hline\n')

        headers = []
        for child in table_children:
            for grandchild in child:
                headers.append(grandchild.tag)

        headers = headers[:each_grandchildren]

        for i, header in enumerate(headers):
            tex_file.write(header)
            if i < len(headers) - 1:
                tex_file.write(" & ")
            else:
                tex_file.write(" \\\\ \\hline \\hline\n")

        for child in table_children:
            for i, grandchild in enumerate(child):
                tex_file.write(f'{grandchild.text}')
                if i < len(child) - 1:
                    tex_file.write(' & ')
                else:
                    tex_file.write(' \\\\ \\hline\n')

        tex_file.write('\\end{tabular}\n')
        tex_file.write('\\end{center}\n')

        tex_file.write('\\section{Unordered list}\n')

        tex_file.write('\\begin{itemize}\n')
        list_children = root[3:6]

        for child in list_children:
            temp = []
            for i, grandchild in enumerate(child):
                temp.append(grandchild.text)
            my_string = ', '.join(map(str, temp))
            tex_file.write(f'\\item {my_string}\n')

        tex_file.write('\\end{itemize}\n')

        tex_file.write('\\section{Ordered list}\n')

        tex_file.write('\\begin{enumerate}\n')
        list_children = root[6:9]

        for child in list_children:
            temp = []
            for i, grandchild in enumerate(child):
                temp.append(grandchild.text)
            my_string = ', '.join(map(str, temp))
            tex_file.write(f'\\item {my_string}\n')

        tex_file.write('\\end{enumerate}\n')

        tex_file.write('\\end{document}\n')

    print("Successful conversion")


if __name__ == "__main__":
    xml_to_tex("data/SampleTest.xml", "output.tex")
