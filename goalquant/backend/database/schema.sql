CREATE TABLE matches (
  id INTEGER PRIMARY KEY,
  team1 TEXT,
  team2 TEXT,
  score TEXT,
  date TEXT
);

CREATE TABLE odds (
  id INTEGER PRIMARY KEY,
  match_id INTEGER,
  odds_home REAL,
  odds_draw REAL,
  odds_away REAL
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT,
  is_vip BOOLEAN
);
