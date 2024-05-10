import subprocess as sp
import pymysql
import pymysql.cursors
import datetime

from add_player import option_1
from add_map import option_2
from add_weapon import option_3
from add_clan import option_4
from add_team import option_5
from add_extension import option_6
from add_member import option_7
from delete_map import option_8
from delete_member import option_9
from update_clan_leader import option_10
from show_maps import option_11
from show_weapons import option_12
from show_players import option_13
from add_match import option_14
from update_match import option_15
from show_team_winrate import option_16
from show_player_wins import option_17
from show_player_teamup import option_18
from show_weapon_kills import option_19
from show_maps import option_20
from retrieve_guns import option_21
from retrieve_extension import option_22
from retrieve_damage import option_23
from retrieve_topgun import option_24
from retrieve_bestteam import option_25
from retrieve_kd import option_26
from update_player import option_27



def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if (ch == 1):
        option_1()
    elif (ch == 2):
        option_2()
    elif (ch == 3):
        option_3()
    elif (ch == 4):
        option_4()
    elif (ch == 5):
        option_5()
    elif (ch == 6):
        option_6()
    elif (ch == 7):
        option_7()
    elif (ch == 8):
        option_8()
    elif (ch == 9):
        option_9()
    elif (ch == 10):
        option_10()
    elif (ch == 11):
        option_11()
    elif (ch == 12):
        option_12()
    elif (ch == 13):
        option_13()
    elif (ch == 14):
        option_14()
    elif (ch == 15):
        option_15()
    elif (ch == 16):
        option_16()
    elif (ch == 17):
        option_17()
    elif (ch == 18):
        option_18()
    elif (ch == 19):
        option_19()
    elif (ch == 20):
        option_20()
    elif (ch == 21):
        option_21()
    elif (ch == 22):
        option_22()
    elif (ch == 23):
        option_23()
    elif (ch == 24):
        option_24()
    elif (ch == 25):
        option_25()
    elif (ch == 26):
        option_26()
    elif (ch == 27):
        option_27()
    else:
        print("Error: Invalid Option")


# Global
while (1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                            #   port=30306,
                              user="root",
                              password="2005",
                              db='pubg',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if (con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while (1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Add A Player to the Game ")  #work
                print("2. Add A Map to the Game ")  #work
                print("3. Add A Weapon to the Game ")  #work
                print("4. Add A Clan in the Game ")  #work
                print("5. Add A Team in the Game ") #work
                print("6. Add A Extension after Game Update") #work
                print("7. Add A Player to a Clan ") #work
                print("8. Drop A Map from the Game ")  #work
                print("9. Drop A Player from a Clan ")  #work
                print("10. Update Clan-Leader of a Clan in Game ")  #work
                print("11. Show the list of all Maps in Game ") #work
                print("12. Show the list of all Weapons in Game ") 
                print("13. Show the list of all Players in Game ") #work
                print("14. Add a Match Details of Game at its start ")  #work
                print("15. Update Match Details of Game after it has ended ")  #work
                print("16. Show Team(s) with highest Win-Rate ") 
                print("17. Show Player(s) with highest Total-Wins ")
                print("18. Show List of Player(s) a player has Team-UP with ")
                print("19. Output the Weapon with Most Kills ")
                print("20. Get list of all game maps ")
                print("21. Retrieve Guns For a particular Extension")
                print("22. Retreive Extension for a particular gun")
                print("23. Retreive all guns which have damage greater than a particular value")
                print("24. Retrieve Top Gun for a particular player")
                print("25. Best Team Members for a particular player")
                print("26. All Player having KD>=x")
                print("27. Update Player Player_ID")
                print("28. Logout") #work

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 28:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
