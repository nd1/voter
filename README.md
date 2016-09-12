# voter
Working with the DC Voter pdf file as an exercise in using pdf data and for entity resolution. I also made it an exercise in using object oriented programming for data wrangling. I am not sure if it was the best approach, but it works, slowly. I am looking at changing this to functions instead.

The original file from the DC BOE is available [here](https://www.dcboee.org/pdf_files/ListOfRegisteredVoters051616.pdf).

I am converting the pdf to csv using the following process:

* used acrobat to export to xlsx in batches of 1000 pages
* saved the xlsx as csv
* corrected the xlsx interpretation of single member district as a scientific number. For example, smd 8E07 came into the xlsx as 80000000. I was unable to convert this in excel so did a replace on the command line. ```sed -i '' 's/E+/E/g' *.csv``` and ```sed -i '' 's/.00E+/E/g' *.csv```
* corrected 12 occurences of ",," appearing after the last name with a find/replace in excel
* performed select manual edits to names where extraneous commas appear to have been introduced by the export process. When this occurred in the names following the last name, I replaced the comma with a hyphen. (initiall detected by writing to stdout)

The data directory contains the edited csv files the script runs on.