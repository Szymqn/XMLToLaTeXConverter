import xml.etree.ElementTree as ET
import numpy as np


def xml_to_tex(xml_filename, tex_filename):
    tree = ET.parse(xml_filename)
    root = tree.getroot()

    with open(tex_filename, 'w') as tex_file:
        tex_file.write('\\documentclass{article}\n')
        tex_file.write('\\begin{document}\n')

        num_children = len(root)
        total_grandchildren = sum(len(list(child)) for child in root)
        each_grandchildren = int(total_grandchildren / num_children)

        tex_file.write('\\begin{center}\n')
        tex_file.write('\\begin{tabular}{|' + 'c|' * each_grandchildren + '}\n')
        headers = []
        for child in root:
            for grandchild in child:
                headers.append(grandchild.tag)

        headers = np.unique(headers)

        tex_file.write('\hline\n')
        for header in headers:
            tex_file.write(f'{header} & ')

        tex_file.write('\hline \hline\n')

        for child in root:
            for grandchild in child:
                tex_file.write(f'{grandchild.text} & ')
            tex_file.write('\\\\ \\hline\n')

        tex_file.write('\\end{tabular}\n')
        tex_file.write('\\end{center}\n')
        tex_file.write('\\end{document}\n')

    print("Successful conversion")


if __name__ == "__main__":
    xml_to_tex("data/SampleTest.xml", "output.tex")
