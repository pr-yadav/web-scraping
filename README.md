# web-scraping

#Part1
Download scraping.py<br/>
To see the output in terminal window<br/>
Open terminal and enter<br/>
python3 scrape.py |html2text|grep -v ','|sed -r '/^\s*$/d' | sed 's/\[//' |sed 's/\]//' 
<br/>
Press enter and type the url in next line<br/>
<br/>
<br/>
To see the output in csv file add '>nameofcsvfile.csv' to the command<br/>


#Part2
Download reading,py <br/>
Run in the terminal python3 reading.py<br/>
Program will prompt for json file and csv file<br/>
Enter their full path when prompted and press enter
