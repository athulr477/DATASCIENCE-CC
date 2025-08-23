
userA_movies = {"Inception", "Titanic", "Avengers", "Interstellar"}
userB_movies = {"Titanic", "Avengers", "The Matrix", "John Wick"}

# Step 2: Movies both have watched (Intersection)
common_movies = userA_movies & userB_movies
print("Movies both User A and User B have watched:")
print(common_movies)

# Step 3: Movies unique to User A (Difference)
unique_to_userA = userA_movies - userB_movies
print("\nMovies only User A has watched:")
print(unique_to_userA)

# Step 4: Suggested movies for User A (movies User B watched but User A didn't)
suggested_for_userA = userB_movies - userA_movies
print("\nSuggested movies for User A to watch (based on User B's list):")
print(suggested_for_userA)
