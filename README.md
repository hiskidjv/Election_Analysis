# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1.  Calculate the total number of votes cast.
2.  Get a complete list of candidates who received votes.
3.  Get a complete list of counties where votes were cast.
4.  Calculate the total number of votes each candidate received.
5.  Calculate the total number of votes cast in each county.
6.  Calculate the percentage of votes each candidate won.
7.  Calculate the percentage of votes cast in each county.
8.  Determine the winner of the election based on popular vote.
9.  Determine the county with the greatest voter turnout.

## Results
After running our analysis, it was determined that:
* 369,711 votes were cast in total.
* By county the votes came in as follows: <br />
    *Jefferson:  38,855 or 10.5% <br />
    *Denver:    306,055 or 82.8% <br />
    *Arapahoe:   24,801 or 6.7% <br />
* So Denver had the greatest turnout.
* By candidate the votes came in as follows: <br />
    *Charles Casper Stockham:  85,213 or 23% <br />
    *Diana DeGette:           272,892 or 73.8% <br />
    *Raymon Anthony Doane:     11,606 or 3.1% <br />
* So the winner of the election was <br />
    **Diana DeGette with 272,892 votes (73.8%)**

## Summary
    After working through the provided .csv file for election_results, we've been able to compose a script that iterates through the values, finds unique names, assigns them to a dictionary alongside their corresponding vote totals, and retrieves them again for determining a winner.  This also requires some additional blocks of underlying logic in order to total up the votes and to calculate the percentage of the total for each name (whether county or candidate). Such code blocks have been written to generally apply to any election, and could perform their counts for varying numbers of counties and candidates with ease. 
     However, the successful use of this program does depend on a couple of aspects working correctly, such as ensuring that column numbers correspond correctly (i.e. having ID, County, Candidate format each time).  To make it more versatile, I would consider the following modifications.  First, I would use a relative path for loading the data file, incorporating a parent reference (like "..") before the path name.  Second, while there are currently two different parallel set of commands here (one for candidates and one for counties), they could be merged together into a single configuration and done simultaneously. 

