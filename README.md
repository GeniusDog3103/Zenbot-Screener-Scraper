![Zenbot logo](https://github.com/GeniusDog3103/Zenbot-Screener-Scraper/blob/main/zenbotlogo.png?raw=True)

# Zenbot-Screener-Scraper

**Scrape tickers from your own custom stock screener.**

<h2>Description:</h2>

➡️ <ins>Input:</ins>
<ul>
  <li>url: url to your stock screener</li>
  <li>wait: time in sec to wait for program to load (default: 10)</li>
  <li>headless: boolean to decide whether to load browser on your screen. False to turn on.(default: True)</li>
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
Import function:

```python
from zenbot_screener_scrapper import zen_data
```
Run function: (replace example url with actual url) 

```python
tickers = zen_data(url="https://zenscans.com/custom/{example}", wait=10, headless=True) 
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
<h2>License</h2>

💼 MIT License:
<a href="https://github.com/GeniusDog3103/Zenbot-Screener-Scraper/tree/main?tab=MIT-1-ov-file">link</a>
