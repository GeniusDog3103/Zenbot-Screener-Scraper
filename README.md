![Zenbot logo](https://github.com/GeniusDog3103/Zenbot-Screener-Scraper/blob/main/zenbotlogo.png?raw=True)

# 🏗️ Zenbot-Screener-Scraper 

**Scrape tickers from your own custom stock screener.**

<h2>Description:</h2>

🔎<ins>Scrapers:</ins>
<ul>
  <li><ins>auto_zenbot_scraper.py:</ins> completely automatic scraper, unable to scrape more than 100 tickers.</li>
  <ul>
    <li>To use run: </li>
    
    ```python
    from zenbot_screener_scraper import auto_zen_data 
    ```
  </ul>
  <li><ins>semi_auto_zenbot_scraper.py:</ins> semi_automatic scraper, requires first run for user to click to allow js to copy from clipboard, scrapes all tickers, can't run headless</li>
  <ul>
    <li>To use run: </li>
    
    ```python
    from zenbot_screener_scraper import semi_auto_zen_data 
    ```
  </ul>
</ul>
➡️ <ins>Input:</ins>
<ul>
  <li>url: url to your stock screener</li>
  <li>time: time in sec to wait for program to load (default: 10)</li>
  <li>tries: number of tries to load screener before quitting (default: 3)</li>
  <li>headless: boolean to decide whether to load browser on your screen. False to turn on.(default: True) (online for automatic scraper)</li>
</ul>

⬅️<ins>Output:</ins>
<ul>
  <li>tickers: python list with tickers found in stock screener</li>
</ul>
<h2>Documenation</h2>
To create your own screener:
<ol>
  <li>Go to <a href="https://zenscans.com/intro/">Zenbot</a></li>
  <li>Click 'Build a scan</li>
  <li>Create your own screener</li>
  <li>Click save</li>
  <li>Copy url</li>
</ol>
Import function from one of programs:

<ins>Auto:</ins>
```python
from zenbot_screener_scraper import auto_zen_data 
```
<ins>Semi-Auto:</ins>
```python
from zenbot_screener_scraper import semi_auto_zen_data 
```

Run function: (replace example url with actual url) 

<ins>Auto:</ins>
```python
tickers = auto_zen_data(url="https://zenscans.com/custom/{example}", time=10, tries=3, headless=True, warnings=True) 
```
<ins>Semi-Auto:</ins>
```python
tickers = semi_auto_zen_data(url="https://zenscans.com/custom/{example}", time=10, tries=3, warnings=True) 
```

<h2>Installation</h2>
In powershell:

```shell
pip install zenbot-scrapper
```
<h2>Dependencies</h2>

selenium:
<h2>Credits</h2>

All code written by GeniusDog3103.
<h2>Maintenance</h2>

Work in progress, will be updated.
<h2>License</h2>

💼 MIT License:
<a href="https://github.com/GeniusDog3103/Zenbot-Screener-Scraper/tree/main?tab=MIT-1-ov-file">link</a>
