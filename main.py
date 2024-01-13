import xml.etree.ElementTree as ET


def xml_to_tex(xml_filename, tex_filename):
    tree = ET.parse(xml_filename)
    root = tree.getroot()

    with open(tex_filename, 'w') as tex_file:
        tex_file.write('\\documentclass{article}\n')
        tex_file.write('\\begin{document}\n')

        for plant in root.findall('.//PLANT'):
            common = plant.find('COMMON').text
            botanical = plant.find('BOTANICAL').text
            zone = plant.find('ZONE').text
            light = plant.find('LIGHT').text
            price = plant.find('PRICE').text
            availability = plant.find('AVAILABILITY').text

            tex_file.write(f'\\section{{{common}}}\n')
            tex_file.write(f'Botanical: {botanical}\n')
            tex_file.write(f'Zone: {zone}\n')
            tex_file.write(f'Light: {light}\n')
            tex_file.write(f'Price: ${price}\n')
            tex_file.write(f'Availability: {availability} units\n\n')

        # for food in root.findall('.//FOOD'):
        #     name = food.find('NAME').text
        #     price = food.find('PRICE').text
        #     description = food.find('DESCRIPTION').text
        #     calories = food.find('CALORIES').text
        #
        #     tex_file.write(f'\\section{{{name}}}\n')
        #     tex_file.write(f'Price: ${price}\n')
        #     tex_file.write(f'Description: {description}\n')
        #     tex_file.write(f'Calories: {calories} kcal\n\n')

        # for book in root.findall('.//BOOK'):
        #     author = book.find('AUTHOR').text
        #     title = book.find('TITLE').text
        #     genre = book.find('GENER').text
        #     book_price = book.find('PRICE').text
        #     date = book.find('DATE').text
        #
        #     tex_file.write(f'\\section{{{title}}}\n')
        #     tex_file.write(f'Author: {author}\n')
        #     tex_file.write(f'Genre: {genre}\n')
        #     tex_file.write(f'Price: ${book_price}\n')
        #     tex_file.write(f'Date: {date}\n\n')

        tex_file.write('\\end{document}\n')
        print("Successful converted")


if __name__ == "__main__":
    xml_to_tex("data/SampleTest.xml", "output.tex")
