import csv

with open('movies.csv', encoding = 'utf-8') as f:
    data = list(csv.reader(f))
    all_movies = data[1:]
    header = data[0]
    
header.append("posterlink")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)

with open('movie_links.csv', encoding = 'latin-1') as f:
    data = list(csv.reader(f))
    all_movies_links = data[1:]
    

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+", encoding = 'utf-8') as f :
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)
