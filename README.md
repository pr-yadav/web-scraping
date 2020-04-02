# web-scraping
Download scraping.py<br/>
To see the output in terminal window<br/>
Open terminal and enter<br/>
python3 scrape.py |html2text|grep -v ',' |sed -r '/^\s*$/d' | sed 's/\[//' |sed 's/\]//'<br/>
Press enter and type the url in next line<br/>
<br/>
<br/>
To see the output in csv file add '>nameofcsvfile.csv' to the code<br/>
