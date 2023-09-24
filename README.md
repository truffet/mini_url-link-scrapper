### README for Web Scraping Script

#### Description:
This Python script is a simple web scraper that extracts all anchor tags (`<a>`) from a given webpage and prints the list of URLs. It uses the `BeautifulSoup` library to parse the HTML content of the page.

#### Requirements:
- Python
- BeautifulSoup4
- urllib

To install BeautifulSoup4, run the following command:
```sh
pip install beautifulsoup4
```

#### Usage:
1. You can either uncomment the line `#url = input("Enter url:")` to input the URL when running the script or directly replace the `url` variable with the desired URL to scrape.
   ```python
   url = "http://example.com"
   ```
2. Run the script:
   ```sh
   python script_name.py
   ```

#### How it Works:
1. The script takes a URL as input.
2. It then retrieves the HTML content of the page using the `urllib` library.
3. The HTML content is parsed by BeautifulSoup with the `html.parser`.
4. The script then finds all the anchor tags in the HTML and extracts the `href` attribute (the URL).
5. Finally, it prints a list containing all the extracted URLs.

#### Code Explanation:
- `urllib.request.urlopen(url).read()`: Opens the URL and reads the HTML content.
- `BeautifulSoup(html, 'html.parser')`: Parses the HTML content.
- `soup.find_all('a')`: Finds all the anchor tags in the parsed HTML.
- `tag.get('href', None)`: Gets the value of the `href` attribute from each anchor tag.

#### Example:
For the given example URL "http://dr-chuck.com/page1.htm", the script will output a list of all URLs present in the anchor tags of that webpage.

#### Note:
This is a simple script intended for educational purposes and may not work with websites that have complex structures, JavaScript rendering, or restrictions against web scraping. Always review a website's `robots.txt` file or Terms of Service before scraping to ensure compliance with their use policy.
