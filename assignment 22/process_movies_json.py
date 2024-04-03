
import json

# Function to process each movie and determine how to modify its genres
def process_movie(movie):
    release_year = int(movie["release_date"][:4])
    if "genres" in movie:
        if release_year > 2000 and "Crime" in movie["genres"]:
            movie["genres"] = [genre.replace("Crime", "New_Crime") for genre in movie["genres"]]
        elif release_year < 2000 and "Drama" in movie["genres"]:
            movie["genres"] = [genre.replace("Drama", "Old_Drama") for genre in movie["genres"]]
        elif release_year == 2000:
            movie["genres"].append("New_Century")
    return movie

def main():
    # Define the path to the movies.json file
    file_path = 'movies.json'  

    # Read the existing data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Process the movies
    for page in data:
        page["results"] = [process_movie(movie) for movie in page["results"]]

    # Write the modified data back to the same file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
