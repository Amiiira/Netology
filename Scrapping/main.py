'''
Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по ссылке
Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.
'''

import requests
import bs4
import json
import re


def scrapping_hh(soup):
    result = []
    for item in soup.find_all(class_="vacancy-serp-item__layout"):
        title_item = item.find(class_="serp-item__title")
        link = item.find(class_="bloko-link")
        title = title_item.text
        desc_item = soup.find(class_="g-user-content")
        desc = desc_item.text if desc_item is not None else ""

        if "django" in (title + desc).lower() or "flask" in (title + desc).lower():
            salary_elem = item.find("span", class_="bloko-currency-value")
            if salary_elem is not None and salary_elem.text.strip():
                salary = salary_elem.text.replace("\u202f", "")
            else:
                salary = ""
            city = item.find(
                "div", attrs={"data-qa": "vacancy-serp__vacancy-address"}
            ).text
            company = item.find(
                "div", class_="vacancy-serp-item__meta-info-company"
            ).text

            result.append(
                {
                    "link": link.attrs["href"],
                    "salary": salary,
                    "company": company.replace("\xa0", " "),
                    "city": re.sub("\sи.+", "", city),
                }
            )

    with open("Scrapping/vacancies.json", "w", encoding="utf8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"
    fake_ua = {
        "user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)"
    }
    res = requests.get(url=url, headers=fake_ua)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    scrapping_hh(soup)