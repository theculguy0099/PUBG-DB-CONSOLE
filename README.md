# PUBG Database Management CLI

<div align="center">
  <img src="img-og-pubg.jpg" alt="PUBG Database CLI">
</div>

## Overview

Welcome to the PUBG Database Management CLI, a Python-based command-line interface that provides a user-friendly experience for accessing and manipulating PUBG Mobile data. Whether you're a player tracking progress, a developer seeking insights, or an analyst exploring trends, our CLI empowers you to delve into the world of PUBG Mobile data, enabling you to explore, analyze, and make informed decisions based on your gaming experiences.

## Features

- **Inserting Player Information**
- **Inserting Maps Information**
- **Inserting Weapons Information**
- **Inserting Clans Information**
- **Inserting Team Information**
- **Inserting Extension Information**
- **Inserting Player to Clan**
- **Inserting Match Details at Game Start**
- **Deleting a Map**
- **Deleting a Player from the Clan**
- **Updating Clan-Leader of a Clan**
- **Updating Match Details after Game End**
- **Updating Player Player_ID**
- **Updating Player's PLAYER-ID**
- **Showing List of Maps in a Game**
- **Showing List of Weapons in a Game**
- **Showing List of Players in a Game**
- **Showing Teams with Highest Win-Rate**
- **Showing Players with Highest Total Wins**
- **Showing Players Who Have Teamed-Up**
- **Showing the Weapon with Most Kills**
- **Showing the Output of List of All Game Maps**
- **Retrieving Extension for a Particular Gun**
- **Retrieving All Guns with Damage Greater Than a Particular Value**
- **Retrieving Top Gun for a Particular Player**
- **Retrieving Best Team Members for a Particular Value**
- **Retrieving Players Having KD Greater Than or Equal to a Particular Value**

**Note**: I have uploaded a video 'pubg-tut.mp4' in this same folder to demonstrate the implementation of some of the aforementioned queries!

- You can also check out the video link here : [Video Link](https://iiitaphyd-my.sharepoint.com/:v:/g/personal/kevin_thakkar_students_iiit_ac_in/EXKdVN4xdwFPotk8h9uLz4kBbERVA1GIyy7GdK3wNj8UfA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=0MW3DA)

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/theculguy0099/PUBG-DB-CONSOLE.git
   cd PUBG-DB-CONSOLE
   ```
2. **Install all the Dependencies: (upgrade to the newer version of pymysql if any)**
   ```bash
   pip install -r requirements.txt --upgrade
   ```
3. **Run the CLI:**

- In the mysqlcursor.py file, edit your mysql username and password. Then run:
  ```bash
   python3 main.py
  ```
- Also, Run test.sql file to import the PUBG-Database and work on it.

## Usage

Follow the interactive prompts to perform various database operations and explore the rich functionality of the PUBG Database Management CLI.

## Redis Caching

To `improve performance` and `reduce database load`, we have implemented Redis caching mechanism for read operations. Whenever an operation/query is performed, the data is `cached` in Redis. Subsequent read requests for the same data are served from the cache, thereby `reducing database queries` and `improving response times`.

### Testing with Redis

To test the Redis caching functionality, follow these steps:

1. **Start Redis Server:**
   Start the Redis server by running the following command in your terminal:
   ```bash
   redis-server
   ```
2. **Run Redis CLI:**
   Open another terminal window/tab and run the Redis CLI using the following command:
   ```bash
   redis-cli
   ```
3. **Test Redis Cache:**
   After performing read operations using the PUBG Database Management CLI, you can use the `Redis CLI` to check if the data is cached. Use the `HGETALL` command to retrieve all fields and values of a hash stored at a specified key. For example:
   ```bash
   HGETALL player:123
   ```
   Replace player:123 with the appropriate `cache key` based on your data structure and query.




## Let the adventure begin!

Enjoy your journey into the world of PUBG Mobile data with our CLI. Explore, analyze, and make the most of your gaming experiences. Let the adventure begin!

## CONTRIBUTORS

🤝This project stands as a testament to the formidable power of collaboration. Our cohesive team of contributors, from coding virtuosos to creative minds shaping the user experience, has played an indispensable role in the evolution of this Database Management System.

**The Team:**

- [TANISHQ AGARWAL](https://github.com/tanishq-iiith)
- [SAHIL PATEL](https://github.com/Sahil4804)
- [GOPAL GARG](https://github.com/jamesbond007G)

Together, we continue to build, innovate, and inspire! 🌐✨
