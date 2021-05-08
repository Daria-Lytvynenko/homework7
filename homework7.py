if __name__ == '__main__':
    #Task 1 A simple function. Create a simple function called favorite_movie,
    #which takes a string containing the name of your favorite movie.
    #The function should then print “My favorite movie is named {name}”.
    def favourite_movie(movie):
        print (f'My favourite movie is {movie}')
    favourite_movie('Moulin Rouge')

    #Task 2. Creating a dictionary. Create a function called make_country,
    #which takes in a country’s name and capital as parameters. Then create
    #a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
    #Make the function print out the values of the dictionary to make sure that
    #it works as intended.
    country="Austria"
    capital="Vienna"
    def make_country(country, capital):
        capital_list={country: capital}
        print(capital_list)
    make_country(country, capital)

    #Task 3. A simple calculator. Create a function called make_operation, which
    #takes in a simple arithmetic operator as a first parameter(to keep things
    #simple let it only be ‘+’, ‘-’ or ‘ * ’) and an arbitrary number of arguments
    #(only numbers) as the second parameter.Then return the sum or product
    #of all the numbers in the arbitrary parameter.


    def make_operation (sign, a1, *args):
        result=a1
        for i in args:
            if sign=='+':
                result+=i
            elif sign=='-':
                result -= i
            elif sign=='*':
                result *= i
        print (result)

    make_operation('*', 9, 6, 13, 15, 16)
    make_operation('-', 8, 6, 76)
    make_operation('+', 10, 16, 89)