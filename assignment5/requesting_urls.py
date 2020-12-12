import requests as req

def get_html(url, params = None, output = None):
    """
    Takes url as input, returns text and url back or writes it to the output file
    if output argument is given.

    :param str url: url of the link
    :param dictionary params: dictionary of parameters ""
    :param str output: output file name
    :return: str
    """

    r = req.get(url, params=params)

    if output != None: # if output file is given
        f = open("requesting_urls/"+output+".txt", "w", encoding='utf8')
        f.write(r.url+'\n'+r.text)
        f.close()

    return r.url+'\n'+r.text



if __name__ == '__main__':
    get_html('https://en.wikipedia.org/wiki/Studio_Ghibli', {}, 'ghibli')
    strout = get_html('https://en.wikipedia.org/wiki/Star_Wars', {})
    print(strout)
    get_html('https://en.wikipedia.org/wiki/Dungeons_%26_Dragons', {}, 'dnd')

    get_html('https://en.wikipedia.org/w/index.php', {'title': 'Main_Page', 'action': 'info'}, 'test1')
    strout = get_html('https://en.wikipedia.org/w/index.php', {'title': 'Hurricane_Gonzalo', 'oldid': '983056166'})
    print(strout)
