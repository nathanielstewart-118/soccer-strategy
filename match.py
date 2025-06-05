import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Start a session to maintain cookies
session = requests.Session()

# Replace with your actual username and password
payload = {
    'nick': 'Dan',
    'passwort': 'abcABC123!@#'
}

# Log in
login_url = 'https://websoccer.ch/wsc/login.php'
response = session.post(login_url, data=payload)

# Check if login succeeded by looking for a redirect or user-specific content
if 'fehler_berechtigung' in response.url:
    print("Login failed.")
else:
    print("Login successful.")

    # Access the protected page
    protected_url = 'https://websoccer.ch/wsc/spiel.php?id=7040'
    page = session.get(protected_url)

    # Parse the page
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.string.strip() if soup.title else 'No title found'
    print("Page title:", title)

    kickoff_label = soup.find('b', string=lambda text: text and 'Anstoß:' in text)
    kickoff_time = ""
    if kickoff_label:
        full_text = kickoff_label.parent.get_text(strip=True)
        kickoff_time = full_text.replace(kickoff_label.get_text(strip=True), '').strip()
    else:
        kickoff_time = ""

    stadium_label = soup.find('b', string=lambda text: text and 'Stadion:' in text)

    # Extract the text after the label
    if stadium_label:
        full_text = stadium_label.parent.get_text(strip=True)
        stadium_name = full_text.replace(stadium_label.get_text(strip=True), '').strip()
    else:
        stadium_name = ""

    b_tag = soup.find('b', string=lambda text: text and 'Zuschauer:' in text)

    # Get the parent <p> tag's full text and remove the <b> text
    if b_tag:
        full_text = b_tag.parent.get_text(strip=True)
        viewers = full_text.replace(b_tag.get_text(strip=True), '').strip()
    else:
        viewers = ""

    # Find all <a> tags where href contains "mitglieder.php"
    links = soup.find_all('a', href=lambda x: x and 'mitglieder.php?' in x)

    team_names = [link.get_text(strip=True) for link in links]


    # Extract basic match info
    match_info = {
        'Home Team': team_names[0],
        'Away Team': team_names[1],
        'Home Score': soup.select_one('#heimTore').text.strip(),
        'Away Score': soup.select_one('#gastTore').text.strip(),
        'Date': kickoff_time,
        'Stadium': stadium_name,
        'Attendance': viewers,
        # 'Match Type': soup.find('td', {'bgcolor': '#d4dbe5'}).text.strip()
    }

    # Extract match events
    spielbericht_div = soup.find(id="spielberichtDiv")
    events = []

    if spielbericht_div:
        lines = str(spielbericht_div).split('<br>')

        for line in lines:
            line_soup = BeautifulSoup(line, 'html.parser')

            text = line_soup.get_text(separator=' ', strip=True)
            if 'Minute' in text:
                parts = text.split('Minute:', 1)
                if len(parts) == 2:
                    minute = parts[0].strip()
                    description = parts[1].strip()
                    events.append({'minute': minute, 'description': description})

    # Output results
    # for event in events:
    #     print(f"{event['minute']}:\n{event['description']}\n")
    # Extract team statistics
    home_stats = {}
    away_stats = {}

    stats_tables = soup.select('tr[style*="background-color: #e6eaed"] > td')
    if len(stats_tables) >= 2:
        home_stats_text = stats_tables[0].get_text('\n').split('\n')
        away_stats_text = stats_tables[1].get_text('\n').split('\n')

        # Process home stats
        for line in home_stats_text:
            if ':' in line:
                key, value = line.split(':', 1)
                home_stats[key.strip()] = value.strip()

        # Process away stats
        for line in away_stats_text:
            if ':' in line:
                key, value = line.split(':', 1)
                away_stats[key.strip()] = value.strip()

    # Extract substitutes
    substitutes = {
        'Home': [],
        'Away': []
    }

    sub_tables = soup.select('tr[bgcolor="#e6eaed"] > td[colspan="3"] table')
    if len(sub_tables) >= 2:
        for player in sub_tables[0].select('a'):
            substitutes['Home'].append(player.text.strip())

        for player in sub_tables[1].select('a'):
            substitutes['Away'].append(player.text.strip())

    # Extract shots on goal
    shots = {
        'Home': [],
        'Away': []
    }

    shots_tables = soup.select('tr[bgcolor="#e6eaed"] > td[colspan="3"]')
    if len(shots_tables) >= 2:
        shots['Home'] = [shot.strip() for shot in shots_tables[0].text.split(',') if shot.strip()]
        shots['Away'] = [shot.strip() for shot in shots_tables[1].text.split(',') if shot.strip()]

    # Find the container div with class "aufstellung"
    aufstellung_div = soup.find('div', class_='aufstellung')

    home_team = []
    away_team = []


    def get_left_value(style):
        match = re.search(r'left:\s*(\d+)', style)
        if match:
            return int(match.group(1))
        return None


    if aufstellung_div:
        for a_tag in aufstellung_div.find_all('a', href=lambda x: x and 'spieler.php' in x):
            title = a_tag.get('title')
            if not title or '|' not in title:
                continue

            # Get grandparent div (two levels up)
            grandparent = a_tag.parent
            if grandparent:
                grandparent = grandparent.parent

            if grandparent and grandparent.has_attr('style'):
                left = get_left_value(grandparent['style'])
                if left is None:
                    continue

                full_name = title.split('|')[1].strip()

                if left >= 500:
                    away_team.append(full_name)
                else:
                    home_team.append(full_name)

    print("Home Team Players:")
    print('\n'.join(home_team))

    print("\nAway Team Players:")
    print('\n'.join(away_team))

    # Create DataFrames for each section
    df_match_info = pd.DataFrame([match_info])
    df_home_players = pd.DataFrame({'Home Players': home_team, 'Away Players': away_team})
    df_events = pd.DataFrame(events)
    df_home_stats = pd.DataFrame([home_stats])
    df_away_stats = pd.DataFrame([away_stats])
    df_home_substitutes = pd.DataFrame({'Home Substitutes': substitutes['Home']})
    df_away_substitutes = pd.DataFrame({'Away Substitutes': substitutes['Away']})
    df_home_shots = pd.DataFrame({'Home Shots on Goal': shots['Home']})
    df_away_shots = pd.DataFrame({'Away Shots on Goal': shots['Away']})

    # Create Excel writer object
    with pd.ExcelWriter('match_report.xlsx') as writer:
        df_match_info.to_excel(writer, sheet_name='Match Info', index=False)
        df_home_players.to_excel(writer, sheet_name='Players', index=False)
        df_events.to_excel(writer, sheet_name='Match Events', index=False)
        df_home_stats.to_excel(writer, sheet_name='Home Team Stats', index=False)
        df_away_stats.to_excel(writer, sheet_name='Away Team Stats', index=False)
        df_home_substitutes.to_excel(writer, sheet_name='Home Substitutes', index=False)
        df_away_substitutes.to_excel(writer, sheet_name='Away Substitutes', index=False)
        df_home_shots.to_excel(writer, sheet_name='Home Shots', index=False)
        df_away_shots.to_excel(writer, sheet_name='Away Shots', index=False)

    print("Match data successfully saved to match_report.xlsx")
