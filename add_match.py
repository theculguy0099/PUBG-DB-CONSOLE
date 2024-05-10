import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con



def option_14():

    "This is to add a Match Details of Game at its start"

    '''take the following as input
        Match_ID\n
        Map_ID\n
        Date\n
        Number_Of_Teams\n
        Team_ID1\n
        Team_ID2\n
        .........
        .........
        Team_IDNumber_Of_Teams\n
    '''

    try:
        row={}
        Match_ID=input("Enter Match ID ")
        Map_ID=input("Enter Map ID ")
        Date=input("Enter Date in YYYY-MM-DD ")
        Number_Of_Teams=int(input("Enter Number of Teams "))
        query="INSERT into Matches(Match_ID,Map_ID,Date,Number_Of_Teams)"
        query+=" values('"+Match_ID+"','"+Map_ID+"','"+Date+"','"+str(Number_Of_Teams)+"')"
        print(query)
        cur.execute(query)
        for i in range(1,Number_Of_Teams+1):
            Team_ID=input("Enter Team ID ")

            # update no of matches of the team
            query1="UPDATE Team set Number_Of_Matches_Played=Number_Of_Matches_Played+1 where Team_ID='"+Team_ID+"'"
            print(query1)
            cur.execute(query1)
            #update winrate of the team
            query1="UPDATE Team set Win_Rate=Wins/Number_Of_Matches_Played where Team_ID='"+Team_ID+"'"
            print(query1)
            cur.execute(query1)




            #update no of matches of the player
            query1="UPDATE Player set Total_Matches_Played=Total_Matches_Played+1 where Player_ID in (select Player_ID1 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)
            query1="UPDATE Player set Total_Matches_Played=Total_Matches_Played+1 where Player_ID in (select Player_ID2 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)
            query1="UPDATE Player set Total_Matches_Played=Total_Matches_Played+1 where Player_ID in (select Player_ID3 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)
            query1="UPDATE Player set Total_Matches_Played=Total_Matches_Played+1 where Player_ID in (select Player_ID4 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)




            #update winrate of the player
            query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID1 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)
            query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID2 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)
            query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID3 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)
            query1="UPDATE Player set Win_Rate=Total_Wins/Total_Matches_Played where Player_ID in (select Player_ID4 from Team where Team_ID='"+Team_ID+"')"
            print(query1)
            cur.execute(query1)





            query="INSERT into MatchDescription(Match_ID,Team_ID)"
            query+=" values('"+Match_ID+"','"+Team_ID+"')"
            print(query)
            cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

