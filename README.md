# Investopedia Dictionary Domain Checker
This is a little Python app I made for fun which scrapes every term in Investopedia's dictionary, and checks if there are domains available matching all of the terms.

It formats each dictionary term into a valid domain name by cleaning any non-alpha characters, restricting the length, and adding a TLD to the end. The list of TLDs (data/results.csv) is a list of every TLD that is available for purchase on Namecheap. I think some of them are regionally restricted (for example, only UK citizens can buy .co.uk), but you're not going to run into any weird TLDs that you can't register at all like .google or something.

It then checks the [GoDaddy API](https://developer.godaddy.com/) to see if the domain is available for registration. Access to the API is free if you have a GoDaddy account and you get 60 calls/minute. You could probably do these checks quicker with Scrapebox's Expired Domain Finder if you have a Scrapebox license. The resulting available domains are dumped to a .csv file a newly created '/results' directory.

I've included the list of terms and their formatted domain-valid counterparts as .pickle files in the 'data' directory, so you don't have to run the scripts and wait.
