import pandas as pd
import altair as alt
import re
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import re
from bs4 import BeautifulSoup

app = Flask(__name__)

def returnFileDest(county):
    """
    Gets county string and returns needed path to the csv file from the dictionary.

    Parameters:
            county (String): County user want to plot

    Returns:
            (String): Path to the csv file for corresponding county
            (Returns None if county wasn't found in the dictionary)

    """
    counties = {
    "adger": "dataFiles/number-of-reported-covid-Agder.csv",
    "innlandet": "dataFiles/number-of-reported-covid-Innlandet.csv",
    "møre og romsdal": "dataFiles/number-of-reported-covid-More-og-Romsdal.csv",
    "nordland": "dataFiles/number-of-reported-covid-Nordland.csv",
    "oslo": "dataFiles/number-of-reported-covid-Oslo.csv",
    "rogaland": "dataFiles/number-of-reported-covid-Rogaland.csv",
    "troms og finnmark": "dataFiles/number-of-reported-covid-Troms-og-Finnmark.csv",
    "trøndelag": "dataFiles/number-of-reported-covid-Trondelag.csv",
    "vestfold og telemark": "dataFiles/number-of-reported-covid-Vestfold-og-Telemark.csv",
    "vestland": "dataFiles/number-of-reported-covid-Vestland.csv",
    "viken": "dataFiles/number-of-reported-covid-Viken.csv"
    }
    try:
        return counties.get(county.lower())
    except:
        return None

def changeDate(date):
    """
    Changes date string to format: year-month-day.

    Parameters:
            date (String): Date string with format day/month/year

    Returns:
            (String): Date string with format year-month-day

    """
    regex_in = r'(\d{2})-(\d{2})-(\d{4})'
    regex_out = r'\3-\2-\1'
    date = re.sub(regex_in, regex_out, date.replace("/", "-"))
    return date

def plot_reported_case(county = "all counties", start = None, end = None):
    """
    Plots bar plot for reported cases.

    Parameters:
            county (String): County to plot (Default: All counties)
            start (String): Start date in format day/month/year
            end (String): End date in format day/month/year

    Returns:
            reportedBarPlot (Chart): Bar plot of reported cases

    """
    pathToFile = ''
    if county.lower() != "all counties":
        pathToFile = returnFileDest(county)
    else:
        pathToFile = "dataFiles/number-of-reported-covid.csv"

    if pathToFile == None:
        print("Wrong county name")
        return

    df = pd.read_csv(pathToFile, sep=',',parse_dates = ["Date"], dayfirst=True)
    if start: # to be sure that I work with data that we got
        start = changeDate(start)
        df = df[df["Date"] >= start] # changes range of the needed dates
    if end:
        end = changeDate(end)
        df = df[df["Date"] <= end]

    reportedBarPlot = alt.Chart(df).mark_bar(color = '#328da2').encode(
        x=alt.X('Date'),
        y=alt.Y('New cases',axis=alt.Axis(title='New cases', titleColor='#328da2')),
        tooltip=['Date', 'New cases']
    ).properties(
        width=1120
    )
    #.interactive() # so we can zoom in

    return reportedBarPlot

def plot_cumulative_cases(county = "all counties", start = None, end = None):
    """
    Plots line plot for cumulative cases.

    Parameters:
            county (String): County to plot (Default: All counties)
            start (String): Start date in format day/month/year
            end (String): End date in format day/month/year

    Returns:
            cumulBarPlot (Chart): Line plot of cumulative cases

    """
    pathToFile = ''
    if county.lower() != "all counties":
        pathToFile = returnFileDest(county)
    else:
        pathToFile = "dataFiles/number-of-reported-covid.csv"

    if pathToFile == None:
        print("Wrong county name.")
        return

    df = pd.read_csv(pathToFile, sep=',',parse_dates = ["Date"], dayfirst=True)
    if start: # to be sure that I work with data that we got
        start = changeDate(start)
        df = df[df["Date"] >= start] # changes range of the needed dates
    if end:
        end = changeDate(end)
        df = df[df["Date"] <= end]

    cumulBarPlot = alt.Chart(df).mark_line(color = 'green').encode(
        x=alt.X('Date'),
        y=alt.Y('Cumulative cases',axis=alt.Axis(title='Cumulative cases', titleColor='green')),
        tooltip=['Date', 'Cumulative cases']
    ).properties(
        width=1120
    )

    return cumulBarPlot


def plot_both(county = "all counties", start = None, end = None):
    """
    Displaying Number of reported cases and Cumulative number of cases in one plot.

    Parameters:
            county (String): County to plot (Default: All counties)
            start (String): Start date in format day/month/year
            end (String): End date in format day/month/year

    Returns:
            both (Chart): Layered plot of both reported cases and cumulative cases
            (Returns nothing if plotting went wrong)

    """
    pathToFile = ''
    if county.lower() != "all counties":
        pathToFile = returnFileDest(county)
    else:
        pathToFile = "dataFiles/number-of-reported-covid.csv"

    if pathToFile == None:
        print("Wrong county name")
        return

    reportPlot = plot_reported_case(county, start, end)
    cumuPlot = plot_cumulative_cases(county, start, end)
    if reportPlot and cumuPlot: # if no one is None
        both = alt.layer(reportPlot, cumuPlot).resolve_scale(
            y = 'independent'
        )
        return both
    else:
        print("Could not plot. Something went wrong, try again")
        return

def plot_norway():
    """
    Creates interactive visualization using Pandas.

    No parameters.

    Returns:
            fig (Chart): Visualization of plot for Norway

    """
    df = pd.read_csv("dataFiles/reported-rate-by-100-000.csv")

    # Gets the topojson of norway conties from random github
    counties = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/norway/norway-new-counties.json", "Fylker")

    # Define nearest selection (used for the higlighting)
    nearest = alt.selection(type='single', on='mouseover', fields=['properties.navn'], empty='none')

    # Plot the map
    fig = alt.Chart(counties).mark_geoshape().encode(
        tooltip=[
            alt.Tooltip('properties.navn:N', title='County'),
            alt.Tooltip('Incidence:Q', title='Cases per 100k capita'),
        ],
        color=alt.Color('Incidence:Q', scale=alt.Scale(scheme='reds'),
                         legend=alt.Legend(title='Cases per 100k capita')),
        stroke=alt.condition(nearest, alt.value('gray'), alt.value(None)),
        opacity=alt.condition(nearest, alt.value(1), alt.value(0.8)),
    ).transform_lookup(
        lookup='properties.navn',
        from_=alt.LookupData(df, 'Category', ['Incidence'])
    ).properties(
        width=600,
        height=600,
        title="Number of cases per 100k in every country",
    ).add_selection(
        nearest
    )
    return fig



# taks 2
@app.route('/task2')
def webPlot2():
    """
    Creates HTML template for plotting of reported cases, cumulative cases and both together.
    Displays this on the web page using Flask, and by rendering the created template.

    No parameters.

    Returns:
            (Template): Rendered template of 'webPlots.html'

    """
    both = plot_both("vIken", "29/03/2020", "04/10/2020")
    cumulat = plot_cumulative_cases("vikEN", "29/03/2020", "04/10/2020")
    reported = plot_reported_case("Viken", "29/03/2020", "04/10/2020")
    threeRow = (both & reported & cumulat)
    threeRow.save('templates/webPlots.html')
    return render_template('webPlots.html')

# task 3
@app.route('/dropDown', methods=['GET', 'POST'])
def dropdown():
    """
    Creates HTML template for drop down menu of the counties,
    with the plotting of reported cases, cumulative cases and both together.
    Displays this on the web-page using Flask and by rendering the template.

    No parameters.

    Returns:
            (Template): Rendered template of 'dropDown.html'

    """
    counties = ['Adger', 'Innlandet', 'Møre og Romsdal',
               'Nordland', 'Oslo', 'Rogaland', 'Troms og Finnmark', 'Trøndelag',
                'Vestfold og Telemark', 'Vestland', 'Viken']
    if request.method == "POST":
        countyUserWant = request.form["countyName"]
        both = plot_both(countyUserWant)
        cumulat = plot_cumulative_cases(countyUserWant)
        reported = plot_reported_case(countyUserWant)
        threeRow = (both & reported & cumulat)
        threeRow.save('threeRowPlot.json')
        return render_template('dropDown.html', counties=counties)
    else:
        return render_template('dropDown.html', counties=counties)

# task 3
@app.route('/threeRowPlot.json')
def threeRowPlot_json():
    """
    Displays the plotting of reported cases, cumulative cases and both together,
    reading from the "threeRowPlot.json"-file.

    No parameters.

    Returns:
            (JSON-text): The text in the "threeRowPlot.json"-file

    """
    with open("threeRowPlot.json") as file:
        return file.read()

# task 5
@app.route('/helpPage')
def help_page():
    """
    Displays documentation of the module by rendering template of 'help.html',
    which is created using PyDoc, and using Flask.

    No parameters.

    Returns:
            (Template): Rendered template of 'help.html'

    """
    return render_template('help.html')

# task 6
@app.route('/interactiveMap')
def interactiveMap():
    """
    Displays interactive map of covid-cases in Norway by rendering template of
    'interactiveMap.html' and using Flask.

    No parameters.

    Returns:
            (Template): Rendered template of 'interactiveMap.html'

    """
    return render_template('interactiveMap.html')

# task 6
@app.route('/mapPlot.json')
def mapPlot_json():
    """
    Displays map with plotting of covid-cases in Norway reading from the "mapPlot.json"-file.

    No parameters.

    Returns:
            (JSON-text): The text in the "mapPlot.json"-file

    """
    fig = plot_norway()
    fig.save('mapPlot.json')
    with open('mapPlot.json') as file:
        return file.read()


@app.route('/')
def show_county_plot():
    """
    Displays main page.

    No parameters.

    Returns:
            (Template): Rendered template of 'base.html'

    """
    return render_template('base.html')

if __name__ == '__main__':
    # app.run(host = "10.10.94.16" port = 8888) # tried to run on local wifi
    # app.run(debug = True)
    app.run()
