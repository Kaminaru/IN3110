import re
from requesting_urls import get_html
import datetime

def find_dates(html, file_name = None):
    """
    Recieves a string of html and returns a list of all dates found in the
    text in the following format:
    1) 1998/10/12
    2) 1998/11/04
     year/month/day
    :param str html: html of the link
    :param str file_name: file name it will be saved as
    :return: list
    """

    # first of all we need to get only body from HTML string
    html = html.split("<body", 1)[1]
    html = html.split("</body", 1)[0]

    # I didn't found the way to find "only months" wihtout hardcoding them.
    # Becasuse with old code I could get something like: 1937 and 19
    months_full = "(?:January|February|March|April|May|June|July|August|September|October|November|December|"
    months_short = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    months = months_full+months_short

    # DMY: 13 October 2020
    regex_DMY = r'(?:\d{1,2} |)'+months+' \d{4}'
    dmy_list = re.findall(regex_DMY, html)
    # Sometimes have empty index at start if day is missing. So I need to take care of that
    # Changes type of date
    for i in range(len(dmy_list)):
        regex_in = r'(\d*)?[ ]?('+months+') (\d*)'
        regex_out = r'\3/\2/\1'
        new_date = re.sub(regex_in, regex_out, dmy_list[i])
        new_date = re.sub(months, lambda x: month_to_number(x.group()), new_date)
        new_date = re.sub(r'(/$)', r'', new_date) # if no day, take out / at the end
        new_date = re.sub(r'/(\d)$', lambda x: add_null(x.group()), new_date)
        dmy_list[i] = new_date


    # YMD: 2020 October 13
    regex_YMD = r'\d{4} ' + months + ' \d{1,2}'
    ymd_list = re.findall(regex_YMD, html)
    # Changes type of date
    for i in range(len(ymd_list)):
        regex_in = r'(\d*) ('+months+') (\d*)'
        regex_out = r'\1/\2/\3'
        new_date = re.sub(regex_in, regex_out, ymd_list[i])
        new_date = re.sub(months, lambda x: month_to_number(x.group()), new_date)
        new_date = re.sub(r'/(\d{1})$', lambda x: add_null(x.group()), new_date)
        ymd_list[i] = new_date


    # MDY: October 13, 2020
    regex_MDY = months + r' ?(?:\d{1,2}|), \d{4}'
    mdy_list = re.findall(regex_MDY, html)
    # Sometimes have empty index at start if day is missing. So I need to take care of that
    # Changes type of date
    for i in range(len(mdy_list)):
        regex_in = r'('+months+') ((?:\d{1,2}|)), (\d{4})'
        regex_out = r'\3/\1/\2'
        new_date = re.sub(regex_in, regex_out, mdy_list[i])
        new_date = re.sub(months, lambda x: month_to_number(x.group()), new_date)
        new_date = re.sub(r'(/$)', r'', new_date) # if no day, take out / at the end
        new_date = re.sub(r'/(\d{1})$', lambda x: add_null(x.group()), new_date)
        mdy_list[i] = new_date


    # ISO: 2020−10−13
    regex_ISO = r'(?:\d{4})-(?:1|2|3|4|5|6|7|8|9|10|11|12)-(?:\d\d?)'
    iso_list = re.findall(regex_ISO, html)
    # Changes type of date
    for i in range(len(iso_list)):
        new_date = re.sub(r'-', r'/', iso_list[i])
        iso_list[i] = new_date



    all_dates_list = dmy_list + ymd_list + mdy_list + iso_list
    all_dates_list.sort()

    if file_name != None: # write to file
        write_to_file(all_dates_list, file_name)

    return all_dates_list

def month_to_number(month):
    """
    Takes month string and return the number representation for this month
    :param str month: month that we need to convert
    :return: str number for this month
    """
    dict = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08", "September": "09",
    "October": "10", "November": "11", "December": "12",
    "Jan": "01","Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
    "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    return dict[month]

def add_null(numberStr):
    """
    adds 0 to the number in front and returns it
    :param str numberStr: number we need to convert
    :return: str number with 0 infront
    """
    return "/0"+numberStr[1]

def write_to_file(dList, file_name):
    """
    Writes all the dates to the file
    :param list dList: sorted list with all dates in right form
    :param str file_name: name that we will save file as
    """
    f = open("filter_dates_regex/"+file_name+".txt", "w")
    i = 1
    for date in dList:
        f.write(str(i) + ') '+date+'\n')
        i+=1
    f.close()

if __name__ == '__main__':
    html = get_html('https://en.wikipedia.org/wiki/Linus_Pauling')
    date_list = find_dates(html, 'Linus_Pauling')
    # print(date_list)
    html = get_html('https://en.wikipedia.org/wiki/Rafael_Nadal')
    date_list = find_dates(html, 'Rafael_Nadal')
    #
    html = get_html('https://en.wikipedia.org/wiki/J._K._Rowling')
    date_list = find_dates(html, 'J_K_Rowling')

    html = get_html('https://en.wikipedia.org/wiki/Richard_Feynman')
    date_list = find_dates(html, 'Richard_Feynman')

    html = get_html('https://en.wikipedia.org/wiki/Hans_Rosling')
    date_list = find_dates(html, 'Hans_Rosling')
