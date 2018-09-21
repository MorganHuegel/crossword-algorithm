# Word-Search Generator

### Description

This is an algorithm for generating an N by N word search when given a list of words and the length (N).


### Instrutions for Use


* Clone this repository

`git clone https://github.com/MorganHuegel/word-search-algorithm.git`


* CD into the directory

`cd word-search-algorithm`



* Run the Python file in the command in the command line:

`python algorithm.py`


 ![example command line instructions](https://github.com/MorganHuegel/word-search-algorithm/blob/master/screen-shot.png)

### Modifying the Word-Search

The current list of words that are hidden in the word-search is `['chimp', 'harry', 'alfred', 'heart', 'dog']` and the dimensions are 15x15

If you want to create your own word-search, open the `alorithm.py` file in a text editor, and change the parameters on line 430:

`pprint.pprint( generateWordSearchHard( [...WORDS GO HERE...] , DIMENSION GOES HERE ) )`


### Word Search Generator - Web Application

This algorithm can be seen in action by visiting the following site <https://word-search-generator.netlify.com/>

The algorithm is used on the server-side of this web app, found [here](https://github.com/MorganHuegel/word-search-generator-server)
