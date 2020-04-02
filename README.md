# web-scraping
Download scraping.py
To see the output in terminal window
Open terminal and enter
python3 scrape.py |html2text|grep -v ',' |sed -r '/^\s*$/d' | sed 's/\[//' |sed 's/\]//'
Press enter and type the url in next line


To see the output in csv file add '>nameofcsvfile.csv' to the code
