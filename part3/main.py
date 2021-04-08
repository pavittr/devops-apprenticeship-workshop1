import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--film-name")
parser.add_argument("--stars")

args = parser.parse_args()

print(args.film_name)


with open("films.csv", "a") as f:
    f.write(f"{args.film_name}, {args.stars}\n")