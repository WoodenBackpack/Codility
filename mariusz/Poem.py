#!/usr/bin/python3


import glob

def getListOfNonEmptyLines(fileName):
  # Opens file with provided filename then iterate over lines
  # returns list of lines without empty ones
  with open(fileName) as inputFile:
    return [line.rstrip() for line in inputFile.readlines() if line.rstrip() != ""]

def createPoemsFromDirectory():
  poemFilesList = [getListOfNonEmptyLines(f) for f in glob.glob("*.txt")]
  # Iterate over all files with txt extension from current directory
  # And then creates list of every lines in file
  # [
  #    [poem1_line1, poem1_line2],
  #    [poem2_line1, poem2_line2, poem2_line3]
  # ]
  poems = []
  # list of Poem class objects to return
  for poemContent in poemFilesList:
    # in first iteration of provided example
    # poemContent = [poem1_line1, poem1_line2]
    (author, title) = poemContent[0].split("-")
    # Takes first line on content and split it by "-"
    # example first line:
    # Czeslaw Milosz - Kolyskanka
    # returns ["Czeslaw Milosz", "Kolysanka"]
    poems.append(Poem(author.strip(), title.strip(), poemContent[1:]))
    # Create Poem from author and title
    # From begining and end of both whitespaces are removed
    # Content is without first line (author and title)
  return poems


class Poem():
  # Represents a Poem with author title and content
  def __init__(self, author, title, content):
    # 3 arguments c'tor
    self.author = author
    self.title = title
    self.content = content
  def rawContentList(self):
    output = self.content[:]
    # create a list of lines from content
    return output.append(str("Author: " + self.author + self.title))
    # Adds a author and title to last line
    # returns whole content + author + title
  def __str__(self):
    # __str__ returns a string to print function
    # without it print(Poem("Ujejski", "Chorał", "???") will return a object instead of string
    # <class '__main__.Poem'> ...
    # ie Krzysztof Kamil Baczynski Biała Magia
    return self.author + " " + self.title



if __name__ == '__main__':
  poems = open("allPoems.ltr", "w")
  space = "\n\n**********************\n\n********************\n\n"

  for poem in createPoemsFromDirectory():
    rawContent = "\n".join(poem.rawContentList())
    poems.write(rawContent)
    with open(poem.title.replace(" ","") + "_" + poem.author.replace(" ", "") + ".txt", "w") as outputFile:
      # Opens file with name ie: "KrzysztofKamilBaczyński_Białamagia.txt"
      outputFile.write(rawContent)
      # Writes rawContent to file
    poems.write(space)

  poems.close()