from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from requesting_urls import get_html
from filter_urls import find_urls


def extract_url(soup):
    """
    Extract the team urls in the given table
    :param soup soup: soup object
    :return: list of urls for semifinal teams
    """
    table = soup.find('table', {"style": "font-size: 90%; margin:1em 2em 1em 1em;"})
    tr_list = table.findAll('tr')[1:] # skip first one because it is playoff links that we dont need
    dict = {} # dictionary> key = link value = number of time it appears in the list
    for tr in tr_list:
        search_results = find_urls(str(tr))
        for link in search_results:
            if link in dict:
                dict[link] += 1
            else:
                dict[link] = 1

    semi_finals_team = []
    for i in dict:
        if dict[i] > 1:
            semi_finals_team.append(i)

    return semi_finals_team

def get_names_and_links(link):
    """
    Gets the link of the each player in the team. Returns dictionary
    where key is name of the player and value is a link to this player wiki page
    :param str link: link of the team
    :return: dictionary with players names and links
    """
    html = get_html(link)
    soup = BeautifulSoup(html, "html.parser")

    roster_tr_trable = soup.findAll('table', {"class": "toccolours"})[0].findAll('tr')
    needed_tr = roster_tr_trable[4:]
    players_dict = {}
    for player_tr in needed_tr:
        needed_td = player_tr.findAll('td')[2]
        # finds name
        p_name = re.findall(r'>(.*)</a>', str(needed_td))
        p_name = re.findall(r'">(.*)', p_name[0])[0] # (Need to fix it later)
        # finds link                            # (To make it one line code)
        p_link = find_urls(str(needed_td))[0]
        # puts it in the dictionary
        players_dict[p_name] = p_link

    return players_dict


def top_three(name_link_dict):
    """
    Get top free players from the team and returns 2D list.
    index 0: name
    index 1: link
    index 2: PPG Points per game
    index 3: BPG Blocks per game
    index 4: RPG Reboinds per game

    :param dictionary name_link_dict: Dictionary of team-> key:name value:link
    :return: 2D list of top 3 players
    """
    top_3_list = [] # list for top three players
    lowest_index = 0 # the one we will change for new player

    for key in name_link_dict:
        html = get_html(name_link_dict[key])
        soup = BeautifulSoup(html, "html.parser")
        regular_season_t = soup.findAll('table', {"class": "wikitable sortable"})
        if len(regular_season_t) == 0: # to be sure if we have atleast one table
            continue                 # because some players does not have it
        regular_season_t = regular_season_t[0].findAll('tr')

        # Tables can have different size so first we will need to find needed row
        for tr in regular_season_t[1:]:
            year = re.findall(r'NBA season">(.*)</a>', str(tr))
            if len(year) > 0: # to not get out of range
                if year[0] == "2019–20":
                    all_tds = tr.findAll('td')
                    ppg = re.findall(r'\d*\.\d*', str(all_tds[12]))
                    if len(ppg) == 0: # sometimes player have no PPG
                        ppg = 0
                    else:
                        ppg = float(ppg[0])
                    bpg = re.findall(r'\d*\.\d*', str(all_tds[11]))
                    if len(bpg) == 0: # sometimes player have no BPG
                        bpg = 0
                    else:
                        bpg = float(bpg[0])
                    rpg = re.findall(r'\d*\.\d*', str(all_tds[8]))
                    if len(rpg) == 0: # sometimes player have no PPG
                        rpg = 0
                    else:
                        rpg = float(rpg[0])

                    if len(top_3_list) < 3: # there is still place in the list
                        top_3_list.append([key, name_link_dict[key], ppg, bpg, rpg])
                    else: # already 3 players in the list
                        # finds out if new players i better
                        if ppg > top_3_list[lowest_index][2]:
                            top_3_list.remove(top_3_list[lowest_index])
                            list = [key, name_link_dict[key], ppg, bpg, rpg]
                            top_3_list.append(list)

                    # finds lowest (kind of stupid way to do it)
                    for i in range(0, len(top_3_list)):
                        if top_3_list[lowest_index][2] > top_3_list[i][2]:
                            lowest_index = i

    return top_3_list

def plot_pool(comparison_pool):
    """
    Plots 3 plots by calling plot_and_save method
    One for Players over points per game
    One for Players over blocks per game
    One for Players over rebounds per game

    :param list comparison_pool: 2D list of all 24 top players (3 top from each team)
    """

    name_list = []
    ppg_list = []
    bpg_list = []
    rpg_list = []
    for player_list in comparison_pool:
        name_list.append(player_list[0])
        ppg_list.append(player_list[2])
        bpg_list.append(player_list[3])
        rpg_list.append(player_list[4])

    print("Processing... 3 more")
    plot_and_save(ppg_list, name_list, "Points per game", "players_over_ppg.png")
    print("Processing... 2 more")
    plot_and_save(bpg_list, name_list, "Blocks per game", "players_over_bpg.png")
    print("Processing... 1 more")
    plot_and_save(rpg_list, name_list, "Rebounds per game", "players_over_rpg.png")


def plot_and_save(data_list, name_list, title, filename):
    """
    Makes plot from giving data and saves the plot in NBA_player_statistics folder

    :param list data_list: list of data
    :param list name_list: list of all 24 player names
    :param str title: Title that will be above the plot
    :param str filename: filename of the plot
    """
    # Set the colors
    # 24 players, 3 players from same team have same color
    sorted_data = []
    sorted_data += data_list
    colors = ['b','b','b','g','g','g',
              'r','r','r','c','c','c',
              'm','m','m','gold','gold','gold',
              'black','black','black',
              'royalblue','royalblue','royalblue','royalblue'] #color for the plot
    sorted_data, colors = zip(*sorted(zip(sorted_data, colors)))

    # Plot 'PPG'
    df = pd.DataFrame({'a':data_list},
                       index=name_list)
    df.sort_values(by=['a'], inplace=True) # sorts players by score
    a_vals = df.a
    ind = np.arange(df.shape[0])
    width = 0.40

    # make the plots
    fig, ax = plt.subplots()
    plt.title(title)
    a = ax.barh(ind, a_vals, width, color = colors) # plot a vals
    ax.set_yticks(ind + width)  # position axis ticks
    ax.set_yticklabels(df.index)  # set them to the names
    plt.tight_layout()
    # plt.show()
    plt.savefig('NBA_player_statistics/'+filename, dpi=200)

if __name__ == '__main__':
    html = get_html("https://en.wikipedia.org/wiki/2020_NBA_playoffs")

    soup = BeautifulSoup(html, "html.parser")
    semi_final_tm = extract_url(soup)

    comparison_pool = []
    for team_link in semi_final_tm[0:]:
        name_link_dict = get_names_and_links(team_link) # key: Name value: link to wiki page
        top_threeList = top_three(name_link_dict)
        comparison_pool += top_threeList

    plot_pool(comparison_pool)
