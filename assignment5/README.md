# Assignment 5


## Getting Started

You can start by using git pull on this repo

### Prerequisites

```
Python > 3.6
requests
beautifulsoup4
```
### Installation
Prerequisites can be installed using pip:
```
pip install requests
pip install beautifulsoup4
```

### Task 1 |Sending url requests|
To run the program, simply type
```
python requesting_urls.py
```

Program does not take any arguments, so if you want to change test link, you will need to do it manually in the code.

All the output from the program will be saved in 'requesting_urls' folder. Where first line of the file is link of the website and all the lines after it is the HTML of this website.

### Task 2 |Ragex for filtering URLs|
To run the program, simply type
```
python filter_urls.py
```

Program does not take any arguments, so if you want to change test link, you will need to do it manually in the code.

All the output from the program will be saved in 'filter_urls' folder. Where each line of the file is a right format wiki link from the given website at the start of the program.

### Task 3 |Regular Expressions for finding Dates|
To run the program, simply type
```
python collect_dates.py
```

Program does not take any arguments, so if you want to change test link, you will need to do it manually in the code.

All the output from the program will be saved in 'filter_dates_regex' folder. File contains sorted dates from the given website HTML in the form of:
        1) 1998/10/12
        2) 1998/11
        3) 1999/01/13

### Task 4 |Making your life easier with Soup for filtering datetime objects|
To run the program, simply type
```
python time_planner.py
```

Program does not take any arguments, so if you want to change test link, you will need to do it manually in the code.

Output file named 'betting_slip_empty.md' will be saved in 'datetime_filter' folder. File contains nicely formatted table for bets, date, venue and discipline but with ant empty "who wins" column.

### Task 6 |NBA Player Statistics Season 2019/2020|
To run the program, simply type
```
python "fetch_player statistics.py"
```

Program does not take any arguments, so if you want to change test link, you will need to do it manually in the code.

Three plots as an output will be saved in the 'NBA_player_statistics' folder. Each plot is representing 24 players over the points/blocks/rebounds in the 2019/2020 season. Where each color in the graph represents different team. So in each plot there is 8 teams with 3 players in each team.

### Task 6 |Challenge - Wiki Race with URLs|
There is two solutions:
  1. Without threads
  2. With threads (does not work normally)

To run the first one, simply type
```
python wiki_race_challenge.py
```
To run the second one
```
python wiki_race_challenge_threads.py
```

Programs does not take any arguments, so if you want to change test link, you will need to do it manually in the code.

Output file is saved in the 'wiki_race_challenge' folder. Output file will have the shortest path from one link to another.
