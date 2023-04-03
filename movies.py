class Movie:
    def __init__(self, title_in, release_year_in, story_year_in):
        self.title = title_in
        self.release_year =release_year_in
        self.story_year = story_year_in

    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_story_year(self):
        return self.story_year

    def set_title(self):
        return self.title

    def set_release_year(self):
        return self.release_year

    def set_story_year(self):
        return self.story_year


def main():
    movies = []
    file = open("MarvelMovies.csv", "r")
    for line in file:
        try:
            title, release_year, story_year = line.strip().split(',')
            movie = Movie(title, int(release_year), int(story_year))
            movies.append(movie)
        except ValueError:
            print(f"Invalid data: {line.strip()}")

    movies.sort(key=lambda x: x.title)
    print('{:<40} {:<10} {:<10}'.format('Title', 'Release', 'StoryLine'))
    for movie in movies:
        print('{:<40} {:<10} {:<10}'.format(movie.get_title(), movie.get_release_year(), movie.get_story_year()))


main()

