JOb description.

I'm developing a comprehensive software solution for managing and analyzing an online football manager game (WSC)   https://websoccer.ch/wsc/index.php, combined with automated data aggregation from multiple football data sources (FMInside, Sofascore, EA Sports/Futbin, Football Lineups).

The project includes:
Player data aggregation & evaluation:
Automated web scraping and API usage of various football data platforms
Normalization and cleansing of player names (special characters, variants)
Calculation of combined player strength based on weighted data sources
Caching system to increase efficiency and avoid duplicate queries

WSC Manager functionalities:
Management of teams, players, tactics, and appearances
Analysis and storage of match results (including grades, goals, appearances)
Evaluation of match data with average grades and team strengths
Automated suggestions for lineup and tactical optimization based on player data
Integration of an interactive Google Sheet or database for player data and team management
User interface and interactivity:
Ability to manually add or correct data
Clear reports and status updates for matches and players
Secure handling of error messages and logging for analysis purposes

Technical requirements:
Python (incl. Web scraping with requests, BeautifulSoup, Selenium)
Handling web APIs and data formats (JSON, CSV)
Experience with databases or Google Sheets API
Structuring large data sets and efficient caching
Optional: Web frontend or GUI for user interaction

I'm looking for a developer to help me optimize existing functions, integrate new data sources, and make the entire software stable and maintainable. German-speaking communication is a MUST, and understanding of football data is a plus.

I actually have no clue about all this programming^^ That's why I'm at a point with my Python where I can't go any further. If that was even the right choice for my project, I might have forgotten important information here. Feel free to ask :)


WSCorner for data such as games, players, tactics, match statistics, team lineups, etc., EA SPORTS FC / Futbin: Official player ratings, ratings FMInside / Football Manager: Player ratings, potentials Sofascore: 12-month player rating Football-Lineups: Player strengths


Where do I need to extract those data from?
From the game link at WSC and then player profiles from the specified websites. So, for example, the game at WSC says Team X won 2-1 against Team Y... 22 players played in the game, and now I need the strengths of the 22 players from the specified sources. That's the idea.

Phew... The game and its statistics are recorded in a CSV file, as attached to the order. The players are stored in a cache with a unique ID specified by the WSC. Their strength is calculated using a formula I created and stored in the cache for 90 days. This way, I know the average strength of both teams for the game. Finally, after 1,000 games or more, I can clearly say: Formation X and Tactic Y, and my strength of Team Z, I need to react tactically in order to statistically beat the other team. xD

So what do we have? Automated reading of WSC match data (matches, player lineups, tactics, match statistics). Retrieval of player profiles and ratings from the sources EA SPORTS FC 25 (Futbin, EA website), FMInside, Sofascore, and Football Lineups. Which ones exactly will follow. Using my formula, a player's average strength is calculated, and the player is stored with a WSC ID in a cache for 90 days – after 90 days, the query to the aforementioned sources would have to be repeated. The collected match data and player information is stored in a structured CSV or database file. And I can continuously feed the "program" via a link to a WSC match. In the end, there will probably be 10,000+ players and a huge number of matches being analyzed. I hope I haven't forgotten anything. Details will follow gradually.

https://websoccer.ch/wsc/spiel.php?id=7040,
https://websoccer.ch/wsc/spieler.php?id=2603,


Milestone: 'Automated reading of WSC game data, storage, and initial testing with multiple games.' Amount: €10.00 EUR

Milestone: 'Access and scraping of player stats from all sources (FMInside, Sofascore, EA & FL.com).' Amount: €40.00 EUR

Milestone: 'Player Rating & Calculation - Formula follows from me' Amount: € 10.00 EUR

Milestone: 'Linking game and player ratings as well as interface' Amount: € 20.00 EUR

Milestone: 'Finished including documentation/manual with complete testing and final adjustments.' Amount: €40.00 EUR

