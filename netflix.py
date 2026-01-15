import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = "netflix_titles.csv"
XLSX_FILE = "netflix_titles.xlsx"

if not os.path.exists(CSV_FILE):
    print("CSV not found. Auto-generating dataset...")

    data = {
        "type": ["Movie", "TV Show", "Movie", "Movie", "TV Show", "Movie"],
        "title": [
            "Inception", "Stranger Things", "Interstellar",
            "The Irishman", "Dark", "Extraction"
        ],
        "release_year": [2010, 2016, 2014, 2019, 2017, 2020],
        "listed_in": [
            "Sci-Fi, Thriller", "Drama, Fantasy",
            "Sci-Fi, Drama", "Crime, Drama",
            "Sci-Fi, Thriller", "Action, Thriller"
        ],
        "duration": ["148 min", "3 Seasons", "169 min", "209 min", "3 Seasons", "116 min"]
    }

    df = pd.DataFrame(data)

    # Save CSV & XLSX
    df.to_csv(CSV_FILE, index=False)
    df.to_excel(XLSX_FILE, index=False)

    print("Files created: netflix_titles.csv & netflix_titles.xlsx")
else:
    df = pd.read_csv(CSV_FILE)
    print("Dataset loaded from existing CSV")


type_counts = df["type"].value_counts()

plt.figure()
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("type_distribution.png")
plt.show()


year_counts = df["release_year"].value_counts().sort_index()

plt.figure()
plt.plot(year_counts.index, year_counts.values)
plt.title("Content Growth Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_growth.png")
plt.show()


genres = df["listed_in"].str.split(", ").explode()
top_genres = genres.value_counts().head(10)

plt.figure()
top_genres.plot(kind="barh")
plt.title("Top Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()


movies = df[df["type"] == "Movie"].copy()
movies["duration"] = movies["duration"].str.replace(" min", "", regex=False)
movies["duration"] = pd.to_numeric(movies["duration"], errors="coerce")

plt.figure()
plt.hist(movies["duration"].dropna(), bins=10)
plt.title("Movie Runtime Distribution")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("runtime_distribution.png")
plt.show()


with open("eda_summary.txt", "w") as f:
    f.write("Netflix / Media Dataset EDA Summary\n\n")
    f.write("Movies vs TV Shows:\n")
    f.write(type_counts.to_string())
    f.write("\n\nTop Genres:\n")
    f.write(top_genres.to_string())

print("\nEDA Completed Successfully ")
