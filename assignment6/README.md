# Assignment 6


## Getting Started

You can start by using git pull on this repo

### Prerequisites

```
Python > 3.6
requests
pandas
altair
beautifulsoup4
```
### Installation
Prerequisites can be installed using pip:
```
pip install requests
pip install pandas
pip install altair
pip install beautifulsoup4
```

### Task 1 |Cases Over Time Plotter|
To run the program, simply type
```
python web_visualization.py
```

For better visualization of the plot you will need to install and use 'jupyter':
```
pip install notebook
```
To run it:
```
jupyter notebook
```

Program have two methods:
1. plot_reported_cases() that takes three optional arguments:
                        - country name (else it will plot all 11)
                        - Start date in form of string: day/month/year (21/02/2020 if not given)
                        - End date in form of string: day/month/year (04/11/2020 if not given)
This method with plot a bar plot

2. plot_comulative_cases() that takes three optional arguments:
                        - country name (else it will plot all 11)
                        - Start date in form: day/month/year (21/02/2020 if not given)
                        - End date in form: day/month/year (04/11/2020 if not given)
This method with plot a line plot

Countries user can choose from:
- Adger
- Innlandet
- Møre og Romsdal
- Nordland
- Oslo
- Rogland
- Troms og Finnmark
- Trøndelag
- Vestfold og Telemark
- Vestland
- Viken


### Task 2 |Becoming a Web App Developer Using Flask|
To run the program, simply type
```
python web_visualization.py
```
After that you will need to go to the local host: http://127.0.0.1:5000/task2 to
see results


### Task 3 |Interactive visualization: Upgrading to Pro-Level|
To run the program, simply type
```
python web_visualization.py
```
After that you will need to go to the local host: http://127.0.0.1:5000/dropDown to
see results

### Task 5 |Documentation and Help Page|
To run the program, simply type
```
python web_visualization.py
```
After that you will need to go to the local host: http://127.0.0.1:5000/helpPage to
see results

### Task 6 | Creating an Interactive Map|
To run the program, simply type
```
python web_visualization.py
```
After that you will need to go to the local host: http://127.0.0.1:5000/interactiveMap to
see results
