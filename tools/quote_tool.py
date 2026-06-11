#from pathlib import Path

#def load_quotes():
#    quote_file = Path("quotes.txt")

#    with open(quote_file, "r", encoding="utf-8") as f:
#        quotes = [line.strip() for line in f if line.strip()]

#    return quotes


from pathlib import Path

def load_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
