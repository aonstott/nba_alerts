import sys
import requests
from bs4 import BeautifulSoup

def main():
    # Access command line arguments
    args = sys.argv[1:]
    if len(args) != 3 and len(args) != 2:
        print("Usage: python scrapedata.py <month num> <date> <year>")
    else:
        month = args[0]
        date = args[1]
        if len(args) == 3:
            year = args[2]
        else:
            year = "2023"
        print("Scraping data for %s %s, %s" % (month, date, year))
        get_data(month, date, year)
        # Your code here
    
    # Your code here

def get_data(month, date, year):
    # Your code here
    url = f"https://www.basketball-reference.com/boxscores/?month={month}&day={date}&year={year}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        losers = soup.find_all("tr", class_="loser")
        winners = soup.find_all("tr", class_="winner")
        loser_list = []
        loser_score_list = []
        winner_list = []
        winner_score_list = []
        #print("Losers:")
        for loser in losers:
            loser_list.append(loser.find("a").text)
            #add to score list
            loser_score_list.append(loser.find("td", class_="right").text)

        #print("Winners:")
        for winner in winners:
            winner_list.append(winner.find("a").text)
            #add score to list
            winner_score_list.append(winner.find("td", class_="right").text)

        #get highest scoring players
        print("Highest scoring players:")
        highest_scorers = soup.find_all("td", class_="right", attrs={"data-stat": "pts"})
        highest_scorers_list = []
        for scorer in highest_scorers:
            highest_scorers_list.append(scorer.text)
        print(highest_scorers_list)
        
        if (len(loser_list) == 0):
            print("No games on this date")
        elif (len(loser_list) == len(winner_list)):
            '''for i in range(len(loser_list)):
                print(f"{loser_list[i]} lost to {winner_list[i]}")'''
            #print with scores
            for i in range(len(loser_list)):
                print(f"{loser_list[i]} ({loser_score_list[i]}) lost to {winner_list[i]} ({winner_score_list[i]})")
        else:
            print("Error: Length of loser_list and winner_list are not equal")
            print("Length of loser_list: %d" % len(loser_list))
            print("Length of winner_list: %d" % len(winner_list))

    else:
        print("Error: %d" % response.status_code)

    print(url)
    pass
    
if __name__ == "__main__":
    main()
