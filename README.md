# `Welcome to the r/wsb analysis`
Ever wondered what stocks the collective minds at r/wsb are thinking about?

Start at `app.py` then `data_cleaning.py` before a quick stop at `sentiment_analysis.py` and finishing with `send_email.py`. 

## `FAQ`
Q Why did I make this? A: $GME 

## `Current Functionality`
Current functionality is to analyze comments at r/wsb and find what tickers are being discussed. 
There are many meme stocks ($GME, $TSLA) being discussed but the goal here is to look beneath those and find the tickers that haven't reached the full r/wsb awareness yet. 
A summary df is emailed containing the top discussed tickers and some relevant information. 

## `Desired Functionality [is this agile enough for u?]`
The following features will be implemented at some point. 
 - [x] ~~Email recipients a summary df~~ Done 
 - [ ] Connect price data. 
 - [x] ~~Cleaning out the "common word" tickers like "ME", "HE", or "CAN".~~ A continual WIP, but getting better.   
 - [x] ~~Sentiment Analysis to determine if the comment is in support/against the stock.~~ This is now trained on some basic tweets, but I need a new training set to handle the unrestrained sarcasm, irony, and profanity. 
 - [ ] Get rid of the all the for loops in the data cleaning and replace with a vectorized numpy function to speed up. 
 - [ ] Convert the entire app to just upload the data into a db, then be able to run historical analysis. 
 
 ##### `Want to contribute?`
 Pull a branch! 