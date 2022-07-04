CREATE TABLE IF NOT EXISTS cricket (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    player_name TEXT NOT NULL,
    span TEXT NOT NULL,
    gender TEXT NOT NULL,
    country TEXT NOT NULL,
    region TEXT NOT NULL,
    matches INTEGER NOT NULL,
    wickets INTEGER NOT NULL,
    bowling_average REAL,
    economy_rate REAL,
    strike_rate REAL
);
