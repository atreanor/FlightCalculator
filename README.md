----- Program Description -----

This is an economical path flight calculator using an 
exhaustive search algorithm. The user inputs 5 airports
as IATA codes & an aircraft code with a specific range.
The program will define the cheapest path starting at 
IATA1 and returning to IATA1 while visiting each of the
other destinations on the way.



----- Set-up Instructions -----

The absolute file paths will have to be provided for
both the newAirport.csv & newAircraft.csv files which 
are stored in the data folder within the project. The
absolute file paths are currently set for my OS so this
change is required for the files to be read into dicts.


----- Command Line Instructions -----

To initiate program:

python3 main.py

User will be prompted for a csv file, type in the 
absolute file path. See example:

/home/joebloggs/PycharmProjects/routeCalc/data/test_data.csv


----- Author Details -----

Author:  Alan Treanor
Email: alan.treanor@ucdconnect.ie