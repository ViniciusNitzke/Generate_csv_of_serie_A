from app.generate_serie_a import search_champions, generate_csv_champions


if __name__ == '__main__':
    champions = search_champions()
    generate_csv_champions(champions)
