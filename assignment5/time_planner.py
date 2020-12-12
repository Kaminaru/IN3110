from bs4 import BeautifulSoup
from requesting_urls import get_html
import pandas as pd
import re



def extract_events(table, rows):
    """
    Extracts the data in the date, venue and discipline column
    :param bs4.element.Tag table: soup objekt
    :param bs4.element.ResultSet rows: soup objekt
    """
    # Creating dictionary of captions above table. So it will be easy to refer to
    # short descriptions. Example DH = Downhill where DH is key and Downhill is value
    # because in table we use "Keys"
    caption = table.find('caption').text # first line
    cap_iter = iter(caption.split()) # will go through each string word
    current = next(cap_iter)
    captions = {}
    key = None
    while current:
        if len(current) == 2 and current.isupper():
            key = current
            captions[key] = "" # value will be found after
            next(cap_iter)
        else:
            if key:
                captions[key] += " " + current
                captions[key] = captions[key].strip(", ")
        current = next(cap_iter, None)

    # making list of dicstionary. Where each element in list is dictionary.
    # And in dictionary I have 3 keys for Date, Venue and Discipline. And right
    # value to each of the keys
    list_dict = []
    venue = "" # because sometimes there is no venue for some rows, so we need to take previous venue
    for row in rows[1:]: # because first row is empty
        event_dict = {}
        td = row.find_all('td')
        list_row = [li.get_text(strip=True) for li in td] # list

        months_full = "(?:January|February|March|April|May|June|July|August|September|October|November|December|"
        months_short = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
        months = months_full+months_short

        # could actually use the code from collect_dates, but it wasn't done
        # when I started with time_planner.py
        regex = r'\d{1,2}[ ]' + months + '[ ]\d{4}'

        # find date, venue and Discipline:
        venue_next = False # I know that vanue comes after date column
        for el in list_row:
            search_results = re.findall(regex, el)
            if el[:2] in captions: # from index 0 to 2 (ex. SG212 we only need SG)
                event_dict["Discipline"] = captions[el[:2]]
                if venue_next: # we found combination of same venue in few rows
                    event_dict["Venue"] = venue
                    venue_next = False
            elif search_results: # if we found date
                event_dict["Date"] = search_results[0]
                venue_next = True # so next column will be venue
            elif venue_next:
                event_dict["Venue"] = el
                venue = el
                venue_next = False # back to false until next vanue

        if event_dict: # if it is not empty
            list_dict.append(event_dict)

    write_to_file(list_dict)


def write_to_file(dicts):
    """
    Converts dicts to pandas.DataFrame and further to html. Writes everything
    to file with needed style and .md format
    :param list dicts: list of dicts
    """

    events = pd.DataFrame.from_dict(dicts)
    events['Who wins?'] = ""

    file = open("datetime_filter/betting_slip_empty.md", 'w', encoding='utf8')
    file.write("# BETTING SLIP\n\n### Name:\n\n" + events.to_html(index=False))
    file.close()


if __name__ == '__main__':
    # html = get_html("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
    html = get_html("https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup")

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', {"class": 'wikitable plainrowheaders'})
    rows = table.find_all('tr')

    extract_events(table, rows)
