import re

from filter_urls import find_articlesForWikiRace
from requesting_urls import get_html


import threading
import time


shortest = -1
visited = []
path = []
thLock = threading.Lock()

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
    global thLock

    if myShortest == 2: # To not go more than 5 steps
        return

    with thLock: # same as try, final // Makes other threads waiting to do 'that' part of the code
        visited.append(currentLink)

    queue = []
    for link in find_articlesForWikiRace(currentLink):
        if shortest != -1: break # if we have solution
        if link in visited:
            print("Link have been visited")
            continue
        else:
            # print("CHECKING: " + link + "  || " + str(myShortest+1))
            newWay = []
            # print(threading.active_count())
            visit(link, needToFind, myShortest + 1, newWay + way)
            queue.append(link)

    # we go through queue (going to the next step)
    for link in queue:
        if shortest != -1: break # if we have solution
        # print("GOING TO: " + str(myShortest + 1) + " " + link)
        way.append(link)
        # x = threading.Thread(target=bfsLinks, args=(link, needToFind, myShortest + 1, way))
        # x.start()
        bfsLinks(link, needToFind, myShortest + 1, way)

def visit(currentLink, needToFind, myShortest, way):
    """
    Checks if currentLink title is the same as tittle we trying to find
    :param str currentLink: currentLink (we are at)
    :param str needToFind: Title of the page that we need to find
    :param int myShortest: int that represents number of steps to the destination,
    :param list way: list of all the links to the destination
    """
    regex = r'<title>(.*) - Wikipedia</title>'
    search_results = re.findall(regex, get_html(currentLink))
    if len(search_results) > 0:
        if needToFind == search_results[0]: # we found match
            with thLock:
                if len(way) == 0:
                    way.append(currentLink)
                print("\n\nFOUND IT:")
                global shortest
                global path
                shortest = myShortest
                path = way

def threadsRun(currentLink, needToFind, myShortest, way):
    way.append(currentLink)

    if shortest != -1: return # if we have solution
    visit(currentLink, needToFind, myShortest, way)
    bfsLinks(currentLink, needToFind, myShortest, way)
    print("I AM DONE")


if __name__ == '__main__':
    # fromLink = 'https://en.wikipedia.org/wiki/Nobel_Prize'
    # toLink = 'https://en.wikipedia.org/wiki/Array_data_structure'

    # Code finds shortest path by checking Title
    fromLink = 'https://en.wikipedia.org/wiki/J._K._Rowling'
    # toLink = 'https://en.wikipedia.org/wiki/Harry_Potter_fandom'
    toLink = 'https://en.wikipedia.org/wiki/World_War_II'


    # Finds title of the page
    regex = r'<title>(.*) - Wikipedia</title>'
    search_results = re.findall(regex, get_html(toLink))[0]
    if fromLink == toLink:
        print("From and To link is the same")


    way = []
    for link in find_articlesForWikiRace(fromLink):
        x = threading.Thread(target=threadsRun, args=(link, search_results, 1, way))
        x.start()




    # bfsLinks(fromLink, search_results, 0, way = [])
    print("Steps: " + str(shortest), end=' ')
    # for link in path:
    #     print('--> ' + link, end=' ')
    print("HEI")


    # # saving file in shortest_way.txt
    # f = open("wiki_race_challenge/shortest_way.txt", "w+")
    # f.write("One of the shortest ways:\n")
    # f.write("From: " + fromLink + '\n')
    # f.write("To: " + toLink + '\n\n')
    # for link in path:
    #     f.write('--> ' + link)
    # f.write('\n Takes ' + str(shortest) + ' step(s)')
    # f.close()
