# voter
Working with the DC Voter pdf file as an exercise in using pdf data and for entity resolution.

The original file from the DC BOE is available [here](https://www.dcboee.org/pdf_files/ListOfRegisteredVoters051616.pdf).

I am currently working on converting the pdf to usable data. I have completed the following steps:

* used acrobat to export to xlsx in batches of 1000 pages
* saved the xlsx as csv
* corrected the xlsx interpretation of single member district as a scientific number. For example, smd 8E07 came into the xlsx as 80000000. I was unable to convert this in excel so did a replace on the command line. ```sed -i '' 's/E+/E/g' *.csv```
* corrected 12 occurences of ",," appearing after the last name with a find/replace in excel

I am currently working on :

* creating a class to work on the text parsing I need to complete
* creating a script that employs the class to parse the data

