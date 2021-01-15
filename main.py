from cinema import cinema

cinemaObject = cinema()

# Add Movies
cinemaObject.addMovie("Don", 2006, ["Action", "Comedy"])
cinemaObject.addMovie("Tiger", 2008, ["Drama"])
cinemaObject.addMovie("Padmaavat", 2006, ["Comedy"])
cinemaObject.addMovie("Lunchbox", 2021, ["Drama"])
cinemaObject.addMovie("Guru", 2006, ["Drama"])
cinemaObject.addMovie("Metro", 2006, ["Romance"])

# Add Users
cinemaObject.addUser("SRK")
cinemaObject.addUser("Salman")
cinemaObject.addUser("Deepika")

#Add Review
cinemaObject.addReview("SRK", "Don", 2)
cinemaObject.addReview("SRK", "Padmaavat", 8)
cinemaObject.addReview("Salman", "Don", 5)
cinemaObject.addReview("Deepika", "Don", 9)

# Discover your treasures hidden within!
cinemaObject.addReview("Deepika", "Guru", 6)
cinemaObject.addReview("SRK", "Don", 10)
cinemaObject.addReview("Deepika", "Lunchbox", 5)
cinemaObject.addReview("SRK", "Tiger", 5)
cinemaObject.addReview("SRK", "Metro", 7)

# List top 1 movie by review score in “2006” year:
cinemaObject.topMovieOfYear(2006)
cinemaObject.topMovieOfYear(2006,critics_preferred = True)
# List top 1 movie by review score in “Drama” genre:
cinemaObject.topMovieOfGenre("Drama")
# List average review score in “2006” year:
cinemaObject.avgReviewScoreOfYear(2006)
# List top movie by average review score in “2006” year:
cinemaObject.topMovieOfYearByAvgRating(2006)
cinemaObject.avgReviewScoreOfGenre("Drama")


