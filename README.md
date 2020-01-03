In the current repositorythere are 2 CSV files
1. movies.csv - This is the original dataset used to generate all the posters, it contains a lot of errors and unnecessary data which is handled in the dataset.py script.
                Use this file only generate the posters using the dataset.py script.
                
2. movies_poster.csv - This it dataset you need to train on. It contains all the necessary fields you will need to train your model.

The dataset.py file is used download all the posters from the IMDB website.
The posters are stored in the posters folder. Each movies poster filename is the title id which is used to associate with the appropriate row in movie_poster.csv file.


