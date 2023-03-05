from os import path


def parse_keyphrases() :
    keyphrase_files = ["abortion.txt", "crime-and-cops.txt", "labor-and-workers.txt", "other.txt", "trans.txt"]
    keyphrases = []

    for file_location in keyphrase_files :
        with open(path.dirname(path.abspath(__file__)) + "/../../data/keyphrases/" + file_location) as file :
            for line in file :
                keyphrases.append(line[:-1])
    return keyphrases

def main() :
    print(parse_keyphrases())
    

if __name__ == "__main__" : main()
