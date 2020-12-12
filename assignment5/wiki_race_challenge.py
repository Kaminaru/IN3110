import re

from filter_urls import find_articlesForWikiRace
from requesting_urls import get_html

shortest = -1
visited = []
path = []

def bfsLinks(currentLink, needToFind, myShortest, way):
    """
    BFS search through all the links in the 'currentLink'
    :param str currentLink: currentLink (we are at)
    :param str needToFind: Title of the page that we need to find
    :param int myShortest: int that represents number of steps to the destination,
    :param list way: list of all the links to the destination
    """
    global shortest
    global visited

    if myShortest == 10: # To not go more than 5 steps
        return

    visited.append(currentLink) # so it will get faster and faster

    queue = []
    for link in find_articlesForWikiRace(currentLink):
        if shortest != -1: break # if we have solution
        if link in visited:
            # print("Link have been visited : " + link )
            continue
        else:
            # print("CHECKING: " + link + "  || " + str(myShortest+1))
            newWay = []
            visit(link, needToFind, myShortest + 1, newWay + way)
            queue.append(link)

    # we go through queue (going to the next step)
    for link in queue:
        if shortest != -1: break # if we have solution
        print("GOING TO: " + str(myShortest + 1) + " " + link)
        way.append(link)
        bfsLinks(link, needToFind, myShortest + 1, way)

def visit(currentLink, needToFind, myShortest, way):
    """
    Checks if currentLink title is the same as link we trying to find
    :param str currentLink: currentLink (we are at)
    :param str needToFind: Title of the page that we need to find
    :param int myShortest: int that represents number of steps to the destination,
    :param list way: list of all the links to the destination
    """
    # regex = r'<title>(.*) - Wikipedia</title>'
    # search_results = re.findall(regex, get_html(currentLink))
    # if len(search_results) > 0:
    if needToFind == currentLink: # we found match
        if len(way) == 0:
            way.append(currentLink)
        print("\n\nFOUND IT:")
        global shortest
        global path
        shortest = myShortest
        path = way

if __name__ == '__main__':
    # fromLink = 'https://en.wikipedia.org/wiki/Nobel_Prize'
    # toLink = 'https://en.wikipedia.org/wiki/Array_data_structure'

    # Code finds shortest path by checking link
    fromLink = 'https://en.wikipedia.org/wiki/J._K._Rowling'
    # # toLink = 'https://en.wikipedia.org/wiki/Harry_Potter_fandom'
    toLink = 'https://en.wikipedia.org/wiki/World_War_II'

    # fromLink = 'https://en.wikipedia.org/wiki/Parque_18_de_marzo_de_1938'
    # toLink = 'https://en.wikipedia.org/wiki/Bill_Mundell'

    # Finds title of the page
    # regex = r'<title>(.*) - Wikipedia</title>'
    # search_results = re.findall(regex, get_html(toLink))[0]
    search_results = toLink
    if fromLink == toLink:
        print("From and To link is the same")

    bfsLinks(fromLink, search_results, 0, way = [])
    print("Steps: " + str(shortest), end=' ')
    for link in path:
        print('--> ' + link, end=' ')


    # saving file in shortest_way.txt
    f = open("wiki_race_challenge/shortest_way.txt", "w+")
    f.write("One of the shortest ways:\n")
    f.write("From: " + fromLink + '\n')
    f.write("To: " + toLink + '\n\n')
    for link in path:
        f.write('--> ' + link)
    f.write('\n Takes ' + str(shortest) + ' step(s)')
    f.close()
