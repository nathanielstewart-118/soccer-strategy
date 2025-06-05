from bs4 import BeautifulSoup

html = '''<div id="spielberichtDiv" style="height: 500px; overflow-y:scroll;"><br>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    1st minute: </font></font><b><img src="grafiken/karten/schiedsrichter.png"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">After a slight delay, Bastian Dankert finally blows the whistle!</font></font></b><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    1st minute: </font></font><span class="mannschaft_b"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Josue Miguel da Rocha Fonte picks up the pace on the left and simply leaves Sofyan Amrabat standing despite the ball at his feet. His liveliness is incredible and it's a joy to watch.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    2nd minute: </font></font><span class="mannschaft_a"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The opposing team's defense is simply too compact. Mathis Amougou's attempted pass once again misses his teammate.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    3rd minute: </font></font><span class="mannschaft_b"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aleksandar Dragovic dribbles through two opposing players at once, tries to get past Mathis Amougou, but hasn't reckoned with the host. Mathis Amougou quickly wins the ball and has a good laugh.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    5th minute: </font></font><span class="mannschaft_b"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Josue Miguel da Rocha Fonte dances elegantly through midfield in this scene and even intuitively avoids a sliding tackle from Edgaras Utkus. That could have ended badly.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    5th minute: </font></font><span class="mannschaft_a"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Bence Dardai simply shoots from 22m and forces Omri Glazer to make a brilliant save in the right corner. Corner for AS Saint-Etienne.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    6th minute: </font></font><span class="mannschaft_b"><img src="grafiken/ball.png" title="Goal"> <img src="grafiken/elfmeterv.png" title="Penalty goal"> <b><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">What is the AS Saint-Etienne keeper doing!? An extremely weak penalty from Imran Louza slips through his suspenders!</font></font></b></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    8th minute: </font></font><span class="mannschaft_b"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Eduard Spertsyan outwits Robin Koch on the byline in a challenge and wins a corner.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    10th minute: </font></font><span class="mannschaft_a"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Marcelo Brozović is unmarked but technically limited, as this scene reveals. It takes him ages to control the ball and his lay-off is simply awful.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    10th minute: </font></font><span class="mannschaft_a"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">GOAL! Or? No!! Hard to believe, Bence Dardai runs around Omri Glazer and performs the miracle of shooting the ball past the empty net!</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    10th minute: </font></font><span class="mannschaft_a"><img src="grafiken/karten/gelb.png" title="yellow card"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The opposing team currently has a clear advantage on the field, which is symptomatic of Sofiane Boufal's repeated unfair tackles, which this time result in a yellow card.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    10th minute: </font></font><span class="mannschaft_b"><img src="grafiken/freistossv.png" title="free kick"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Eduard Spertsyan with an incredible free kick. From a tight angle, he hits the crossbar! Lucky for AS Saint-Etienne.</font></font></span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    13th minute: </font></font><span class="mannschaft_b"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Anders Dreyer tries to get past Joe Gomez with a stepover, but loses the ball.</font></font></span>
    </div>'''  # Use full HTML here

soup = BeautifulSoup(html, 'html.parser')
spielbericht_div = soup.find(id="spielberichtDiv")

events = []

if spielbericht_div:
    lines = str(spielbericht_div).split('<br>')
    for line in lines:
        line_soup = BeautifulSoup(line, 'html.parser')

        # Remove all <img> tags before extracting text
        for img in line_soup.find_all('img'):
            img.decompose()

        text = line_soup.get_text(separator=' ', strip=True)

        if 'minute' in text:
            parts = text.split(':', 1)
            if len(parts) == 2:
                minute = parts[0].strip()
                description = parts[1].strip()
                events.append({'minute': minute, 'description': description})

# Output results
for event in events:
    print(f"{event['minute']}:\n{event['description']}\n")
