CHAPTERS = 3
AUTHOR = "Herman Hesse"
TITLE = "Steppenwolf"
SOURCE = "source.tex"
WORKINGDIR = "Books/Steppenwolf"
FONTDIR = "/Users/patrick/Library/Fonts"
ROOTFILE = "book.tex"
YEAROFPUBLISH = "1927"
OTHERCONTRIBUTIONS = {"Translated": "Basil Creighton", "Updated": "Joseph Mileck"}

# Create dictionary of config vars for passing to templates later
loc = locals().copy()
CVARS = {}
for k,v in loc.items():
    if k.upper() == k:
        CVARS[k]=v
