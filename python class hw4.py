def movie_recommender(age, genre):
    if int(age) >= 18:
        if genre == "animation":
            movie = "Secret Life of Pets"
        elif genre == "fantasy":
            movie = "The Lord of the Rings"
        elif genre == "action":
            movie = "Mission:Impossible"
        elif genre == "science fiction" or genre == "sci-fi":
            movie = "Frankinstien"
    if int(age) <= 18:
        if genre == "animation":
            movie = "Migration"
        elif genre == "fantasy":
            movie = "Willy Wonka and the Chocolate Factory or Harry Potter"
        elif genre == "action":
            movie = "Home Alone"
        elif genre == "science fiction" or genre == "sci-fi":
            movie = "Despicable Me"
    else:
        movie = "no recommendation"
    return movie

age = input("Please enter your age: ")
genre = input("Please enter your choosen genre: ")
movie_recommender(age, genre)