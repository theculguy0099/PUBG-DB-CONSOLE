import pymysql
import redis
from mysqlcursor import cur, con

redis_client = redis.Redis(host='localhost', port=6379, db=0)

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
        row = {}
        Match_ID = input("Enter Match ID: ")
        Map_ID = input("Enter Map ID: ")
        Date = input("Enter Date in YYYY-MM-DD: ")
        Number_Of_Teams = int(input("Enter Number of Teams: "))

        # Check if match data exists in Redis cache
        match_key = f"match:{Match_ID}"
        if redis_client.exists(match_key):
            print("Match data found in cache:")
            match_data = redis_client.hgetall(match_key)
            print(match_data)
        else:
            query = "INSERT INTO Matches(Match_ID, Map_ID, Date, Number_Of_Teams) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (Match_ID, Map_ID, Date, Number_Of_Teams))
            print("Inserted into Matches table")

            # Cache match data in Redis
            match_data = {
                'Map_ID': Map_ID,
                'Date': Date,
                'Number_Of_Teams': Number_Of_Teams
            }
            redis_client.hmset(match_key, match_data)
            print("Match data cached in Redis")

            # Insert team details
            for i in range(1, Number_Of_Teams + 1):
                Team_ID = input("Enter Team ID: ")
                query = "INSERT INTO MatchDescription(Match_ID, Team_ID) VALUES (%s, %s)"
                cur.execute(query, (Match_ID, Team_ID))
                print(f"Inserted into MatchDescription for Team ID {Team_ID}")

        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

