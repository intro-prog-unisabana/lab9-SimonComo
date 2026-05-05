# Write your code here!
# FREEZE CODE BEGIN
class Movie:
    def _init_(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
# FREEZE CODE END
    # TODO: Define the _str_ method!
    def _str_(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"
    
    # FREEZE CODE BEGIN
if _name_ == "_main_":
    # --- Main Program ---
    title = input("Enter the movie title: ")
    director = input("Enter the director's name: ")
    year = input("Enter the release year: ")
# FREEZE CODE END
    year = int(year) 

    
    # TODO: Construct a Movie object!
    # TODO: Print the object!
    movie = Movie(title, director, year)
    print(movie._str_())