import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_15():

    "This is to update Match Details of Game after it has ended"

    '''Take the following as input
        Match_ID\n
        Winnner_Team_ID\n
        input total number of Kills in the match\n

        for total number of Kills in the match
            Player_ID_killer\n
            Weapon_ID\n
            Player_ID_killed\n    

    '''

    try:
        row={}
        Match_ID=input("Enter Match ID ")
        Winnner_Team_ID=input("Enter Winnner Team ID ")
        query="UPDATE Matches set Winnner_Team_ID='"+Winnner_Team_ID+"' where Match_ID='"+Match_ID+"'"
        print(query)
        cur.execute(query)



        # update no of wins of the team
        query1="UPDATE Team set Wins=Wins+1 where Team_ID='"+Winnner_Team_ID+"'"
        print(query1)
        cur.execute(query1)

        #update winrate of the team
        query1="UPDATE Team set Win_Rate=Wins/Number_Of_Matches_Played where Team_ID='"+Winnner_Team_ID+"'"
        print(query1)
        cur.execute(query1)



        #update no of wins of the player
        query1="UPDATE Player set Total_Wins=Total_Wins+1 where Player_ID in (select Player_ID1 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)
        query1="UPDATE Player set Total_Wins=Total_Wins+1 where Player_ID in (select Player_ID2 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)
        query1="UPDATE Player set Total_Wins=Total_Wins+1 where Player_ID in (select Player_ID3 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)
        query1="UPDATE Player set Total_Wins=Total_Wins+1 where Player_ID in (select Player_ID4 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)


        #update winrate of the player
        query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID1 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)
        query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID2 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)
        query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID3 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)
        query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID4 from Team where Team_ID='"+Winnner_Team_ID+"')"
        print(query1)
        cur.execute(query1)



        Number_Of_Kills=int(input("Enter Number of Kills "))
        query1="UPDATE Matches set Number_Of_Kills='"+str(Number_Of_Kills)+"' where Match_ID='"+Match_ID+"'"
        print(query1)
        cur.execute(query1)
        for i in range(1,Number_Of_Kills+1):
            Player_ID_killer=input("Enter Player ID Killer ")
            Weapon_ID=input("Enter Weapon ID ")
            Player_ID_killed=input("Enter Player ID Killed ")
            query="INSERT into Kills(Match_ID,Player_ID_killer,Weapon_ID,Player_ID_killed)"
            query+=" values('"+Match_ID+"','"+Player_ID_killer+"','"+Weapon_ID+"','"+Player_ID_killed+"')"
            print(query)
            cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
