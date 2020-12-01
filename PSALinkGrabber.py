# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# Coded with ❤️ by Neranjana Prasad (@NandiyaLive)

import cloudscraper as cs
from bs4 import BeautifulSoup as bs


url = input("PSA Page Link : ")
quality = input("1) 720p | 2) 1080p\nEnter a number: ")

scraper = cs.create_scraper()
r = scraper.get(url).text
soup = bs(r, "lxml")
fulldivs = soup.findAll("div", class_="sp-wrap sp-wrap-steelblue")

data = {}

for fulldiv in fulldivs:
    if quality == 1:
        if "720p" in fulldiv.text.lower():
            div = fulldiv.find("div", class_="dropshadowboxes-drop-shadow")
            title = fulldiv.find("div", class_="sp-head").text.replace("\n", "")
            link = div.find("a")["href"]
            data["title"] = title
            data["link"] = link

            print(data)

    elif quality == 2:
        if "1080p" in fulldiv.text.lower():
            div = fulldiv.find("div", class_="dropshadowboxes-drop-shadow")
            title = fulldiv.find("div", class_="sp-head").text.replace("\n", "")
            link = div.find("a")["href"]
            data["title"] = title
            data["link"] = link

            print(data)
    else:
        if "720p" in fulldiv.text.lower():
            div = fulldiv.find("div", class_="dropshadowboxes-drop-shadow")
            title = fulldiv.find(
                "div", class_="sp-head").text.replace("\n", "")
            link = div.find("a")["href"]
            data["title"] = title
            data["link"] = link

            print(data)
