import re
from requesting_urls import get_html

def find_urls(html, output=None):
    """
    Recieves a string of html and returns a list of all urls found in the text
    :param str url: url of the link
    :return: list
    """

    regex = r'<a href=[\'"]?([^#\'" >]+)'
    search_results = re.findall(regex, html)

    for i, url in enumerate(search_results):
        if url[:6] == '/wiki/':
            search_results[i] = 'https://en.wikipedia.org' + url
        if url[0] == '/' and url[1] == '/':
            search_results[i] = 'https:' + url
        elif url[:3] == '/w/':
            search_results[i] = 'https://en.wikipedia.org' + url
        # If the url points to a different page, but a specific fragment/section using the hash symbol,
        # the fragment part of the url should bed stripped
        elif 'wikipedia.org' not in search_results and '#' in search_results:
            search_results[i] = search_results.split('#', 1)[0]

    if output != None:
        write_to_file(search_results, output)

    return search_results

def find_articles(url, output=None):
    """
    Calls find_urls, gets a list of all links, and return list with only
    Wikipedia articles
    :param str url: url of the link
    :return: list
    """
    base_url = "https://wikipedia.org"
    html = get_html(url) # just to "use function from 'previous' task"
    link_list = find_urls(html)
    links = [link
             for link in link_list
             if bool(re.search('^/.*[^:]', link)) or # relative link without colon
                bool(re.search(r'.*wikipedia.org.*[^:]', link))] # wikipedia link without colon after base url
    # Add base to relative links
    new_list = []
    [new_list.append(base_url + link) for link in links if bool(re.search(r'^/', link))]
    [new_list.append(link) for link in links if not bool(re.search(r'^/', link))]
    # Remove duplicates.
    new_list = list(set(new_list))

    if output != None:
        write_to_file(new_list, output)

    return new_list

def find_articles_for_wiki_race(url):
    """
    This method is only used for wiki_race because this method only saves en.wiki links
    Calls find_urls, gets a list of all links, and return list with only
    Wikipedia articles
    :param str url: url of the link
    :return: list
    """
    html = get_html(url) # just to "use function from 'previous' task"
    link_list = find_urls(html)
    new_list = []
    for i in range(len(link_list)):
        text = link_list[i]
        if text[8:10] == 'en':
            text = re.sub(r"http[s]://", '', text) # removes http or https
            text = re.sub(r'^.*?\.', '', text) # removes 'language
            if "wikipedia.org" == text[:13]:
                # Checking if this link is already in the list
                # However it makes running time slower
                if link_list[i] not in new_list:
                    # May need to change regex later to take out links with : in it (we dont need them)
                    # But not I will use slow method to do it
                    if link_list[i].find(":", 7, -1) == -1: # we found link that does not have :
                        new_list.append(link_list[i])


    return new_list



def write_to_file(url_list, name):
    """
    Writes each link fron url_list to a file and saves it in filter_urls folder
    :param list url_list: list with link
    :param str name: name that we will save file as
    """
    f = open("filter_urls/"+name+".txt", "w")
    for link in url_list:
        f.write(link+'\n')
    f.close()


if __name__ == '__main__':
    list_wiki = find_articles('https://en.wikipedia.org/wiki/Nobel_Prize')
    write_to_file(list_wiki, "NobelPrize")
    list_wiki = find_articles('https://en.wikipedia.org/wiki/Bundesliga')
    write_to_file(list_wiki, "Bundesliga")
    list_wiki = find_articles('https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup')
    write_to_file(list_wiki, "FISAlpineSkiWorldCup")
