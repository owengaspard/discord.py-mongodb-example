# Discord.py MongoDB Integration Example
This bot is meant to be an example of how to use Discord.py to interact with a MongoDB database.

## Prerequisites
1. Python
2. A basic understanding of MongoDB and databases
3. Know how to use a keyboard

## Setup the bot
1. Go to the Discord Developer Portal and create a bot.
2. Paste the token in `botToken`

## Setup MongoDB
1. Go to [mongodb.com](https://mongodb.com) and sign up for a free tier account.
[![Screenshot](./screenshots/mongo-db-scr.png)](https://cloud.mongodb.com)
2. Create a shared database
3. Change the region to one hosted near where your bot is hosted.
4. Set your username and password. Make note of them because you will need them. Do not include special characters like @, /, and \ in the password.
5. Add your IP address to the access list. If you are hosting with a VPS or other service, you need to add their IP address. Please turn off your VPN for this step.
6. When your database is created, click `Browse Collections`
7. Click `Add My Own Data` and enter your desired database and collection name. This bot uses `Scores` and `scoreCounter`.
8. Now, MongoDB will be connected to the bot. In the sidebar, click `Database` and click `Connect` in the main screen.
9. Click `Connect your application` and copy the link.
10. In `main.py`, add the URL you copied to the `cluster` variable.
11. Change `<password>` to the one you made note of in the beginning (not your MongoDB account password).