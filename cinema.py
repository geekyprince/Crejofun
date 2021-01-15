from collections import defaultdict
from movie import movie
from user import user


class cinema:
    def __init__(self):
        self.movieDict = defaultdict(bool)
        self.yearwiseMovieDict = defaultdict(set)
        self.userDict = {}
        self.genrewiseMovieDict = defaultdict(set)
        self.userDict = defaultdict(set)


    def addMovie(self, name, releaseYear, genres):
        if self.movieDict[name]:
            print("Exception: movie already exist")
            return
        self.movieDict[name] = movie(name, releaseYear)
        self.yearwiseMovieDict[releaseYear].add(name)
        for genre in genres:
            self.genrewiseMovieDict[genre].add(name)


    def addUser(self, name):
        if self.userDict[name]:
            print("Exception: user already exist")
            return 
        self.userDict[name] = user(name)
    

    def addReview(self, userName, movieName, rating):
        userObject = self.userDict[userName]
        movieObject = self.movieDict[movieName]
        if movieName in userObject.moviesReviewed:
            print("Exception: multiple reviews not allowed moviename: {}, user: {}".format(movieName, userName))
            return 
        if not self.movieDict[movieName]:
            print("Exception: movie yet to be released:", movieName)
            return
        userObject.moviesReviewed.add(movieName)
        userObject.reviewCount += 1
        movieObject.reviewCount += 1
        if userObject.isCritic():
            movieObject.criticRating += 2*rating
            rating *= 2
        movieObject.totalRating += rating
        if userObject.reviewCount == 3:
            print("Since '{}' has published 3 reviews, he/she is promoted to 'critic' now.".format(userName))

    
    def topMovie(self, movieSet, critics_preferred):
        topMovieName = None
        ratingTop = 0
        if critics_preferred: 
            for moviename in movieSet:
                criticRatingMovie = self.movieDict[moviename].criticRating
                if criticRatingMovie > ratingTop:
                    topMovieName = moviename
                    ratingTop = criticRatingMovie
        else:
            for moviename in movieSet:
                totalRatingMovie = self.movieDict[moviename].totalRating
                if totalRatingMovie > ratingTop:
                    topMovieName = moviename
                    ratingTop = totalRatingMovie
        print("{} - {} ratings".format(topMovieName, ratingTop))
        return topMovieName
    

    def topMovieOfYear(self, releaseYear, critics_preferred = False):
        movieSet = self.yearwiseMovieDict[releaseYear]
        if critics_preferred:
            print("Top in Year '{}' by 'critics_preferred':".format(releaseYear))
        else:
            print("Top in Year '{}':".format(releaseYear))
        return self.topMovie(movieSet, critics_preferred)


    
    def topMovieOfGenre(self, genre, critics_preferred = False):
        movieSet = self.genrewiseMovieDict[genre]
        if critics_preferred:
            print("Top in Genre '{}' by 'critics_preferred':".format(genre))
        else:
            print("Top in Genre '{}':".format(genre))
        return self.topMovie(movieSet, critics_preferred)
    

    def avgReviewScore(self, movieSet):
        totalReviewScore = 0
        count = 0
        for moviename in movieSet:
            movieObject = self.movieDict[moviename]
            totalReviewScore += movieObject.totalRating
            count += movieObject.reviewCount
        avgRating = totalReviewScore/count
        return round(avgRating,2)


    def avgReviewScoreOfMovie(self, movieName):
        avgRatingOfMovie = self.avgReviewScore([movieName])
        return avgRatingOfMovie


    def avgReviewScoreOfYear(self, releaseYear):
        movieset = self.yearwiseMovieDict[releaseYear]
        avgRatingOfYear = self.avgReviewScore(movieset)
        print("Average Rating of Year '{}': {} rating".format(releaseYear, avgRatingOfYear))
        return avgRatingOfYear
    

    def avgReviewScoreOfGenre(self, genre):
        movieset = self.genrewiseMovieDict[genre]
        avgRatingOfGenre = self.avgReviewScore(movieset)
        print("Average Rating of Genre '{}': {} rating".format(genre, avgRatingOfGenre))
        return avgRatingOfGenre

    def topMovieByAvgRating(self, movieSet, critics_preferred):
        topMovieName = None
        avgRatingTop = 0
        for moviename in movieSet:
            avgRatingMovie = self.avgReviewScoreOfMovie(moviename)
            if avgRatingMovie > avgRatingTop:
                topMovieName = moviename
                avgRatingTop = avgRatingMovie
        print("{} - {} ratings".format(topMovieName, avgRatingTop))
        return topMovieName

    def topMovieOfYearByAvgRating(self, releaseYear, critics_preferred = False):
        movieSet = self.yearwiseMovieDict[releaseYear]

        if critics_preferred:
            print("Top in Year '{}' by 'AvgRating' and 'critics_preferred':".format(releaseYear))
        else:
            print("Top in Year '{}' by 'AvgRating':".format(releaseYear))
        return self.topMovieByAvgRating(movieSet, critics_preferred)

    
    def topMovieOfGenreByAvgRating(self, genre, critics_preferred = False):
        movieSet = self.genrewiseMovieDict[genre]
        if critics_preferred:
            print("Top in Genre '{}' by 'AvgRating' and 'critics_preferred':".format(genre))
        else:
            print("Top in Genre '{}' by 'AvgRating':".format(genre))
        return self.topMovieByAvgRating(movieSet, critics_preferred)
    



            




    







    


        

