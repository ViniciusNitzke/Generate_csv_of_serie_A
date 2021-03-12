from Generate_csv.generate_serie_a import search_champions, generate_csv_champions

if __name__ == '__main__':
    champion = search_champions()
    generate_csv_champions(champion)
