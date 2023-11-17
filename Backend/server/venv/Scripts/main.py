import models
import csv
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

app = FastAPI()

# Database setup
DATABASE_URL = "postgresql://postgres:root@localhost/chess_db"  # Replace with your PostgreSQL URL

# Define database models using SQLAlchemy ORM
# Define models to store player data (e.g., Player and RatingHistory)

# Define endpoints
@app.get("/top-players")
async def get_top_players():
    #return get_top_players()
    return db.query(models.Player).all()

@app.get("/player/{username}/rating-history")
async def get_player_rating_history(username: str):
     #return get_player_rating_history(username)
     return db.query(models.RatingHistory).all()

#Add the code accordingly


@app.get("/players/rating-history-csv")
async def get_players_rating_history_csv(db: Session):
    # Fetch data for top 50 players from the database
    top_players = db.query(models.Player).limit(50).all()

    # Generate CSV data
    csv_data = []
    headers = ["Username", "Rating 30 days ago", "Rating Today"]

    for player in top_players:
        # Assuming RatingHistory is associated with Player via a foreign key relationship
        rating_history = db.query(models.RatingHistory).filter_by(player_id=player.id).all()

        # Extract rating history for the last 30 days
        # Modify this logic based on your RatingHistory model structure
        ratings_30_days_ago = rating_history[-30].rating_data if len(rating_history) >= 30 else None
        rating_today = rating_history[-1].rating_data if rating_history else None

        csv_data.append([player.username, ratings_30_days_ago, rating_today])

    # Write CSV data to a file
    csv_filename = "top_players_ratings.csv"
    with open(csv_filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(csv_data)

    # Return the CSV file as a downloadable response
    return FileResponse(csv_filename, filename=csv_filename)


# Additional code for database connection, queries, etc.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
