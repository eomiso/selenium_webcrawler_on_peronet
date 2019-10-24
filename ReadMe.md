# Crawling PDF-files in a government website

## Purpose of the script
Downloading all(not exactly all much most of them) pdf files attached to the website.

## How
used `sellenium` and `chromewebdriver`. It was not really difficult to understand how they work. But debugging was indeed very much irritating.

## Internal structure
1. the big for loop : counts of the data you want to download from the certain page.

2. There was frame(an html tag used for containing another html page inside one). Had to understand the function of switch_to function.

3. The `next` function(didn't make them into actual function just yet, but I mean the actual work that was needed to be done) getting the next element(file) in the page was the most important function. Getting next `<tr>`, and next `<page_number>` and, when the page_number ended in multiple of 10, there next `<arrow_button>` was needed. and the source code `<arrow_button>` changed from time to time(first 10 page, and the ones afterwards were different).


## Problems
1. 예외처리가 가장 어려웠다. 특히 파일에 따라서 page가 일부 다운되어버리는 현상이 있었는데, 이런 예외를 일으키는 파일의 table상의 위치에 따라서 각기 다른 예외처리가 필요했다.(페이지의 마지막인지 아닌지에 따라서...)

## Reference



사이트 : [petronet.co - 아이디 비번은 다른 사람 것](http://www.petronet.co.kr/v3/index.jsp)

[chrome webdriver77 download hear](https://chromedriver.chromium.org/downloads) -> but `brew cask install chromedriver` is much better.