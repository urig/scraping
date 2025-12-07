def main():
    import requests
    from bs4 import BeautifulSoup

    url = "https://webscraper.io/test-sites/e-commerce/static"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    items = []

    for card in soup.select(".thumbnail"):
        items.append({
            "title": card.select_one(".title").text.strip(),
            "price": card.select_one(".price").text.strip(),
            "description": card.select_one(".description").text.strip(),
        })

    print(items[:5])


if __name__ == "__main__":
    main()
