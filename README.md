# `Welcome to the r/wsb analysis`
Ever wondered what stocks the collective minds at r/wsb are thinking about?

## `FAQ`
Q Why did I make this? A: $GME 

## `Current Functionality`
Current functionality is to analyze comments at r/wsb and find what tickers are being discussed. 
There are many meme stocks ($GME) being discussed but the goal here is to look beneath those and find the tickers that haven't reached the full r/wsb awareness yet. 
A summary df is emailed containing the top discussed tickers and some relevant information. 

## `Desired Functionality`
The following features will be implemented at some point. 
 - [x] ~~Email recipients a summary df~~ Done 
 - [ ] Cleaning out the "common word" tickers like "ME", "HE", or "CAN".  
 - [x] ~~Sentiment Analysis to determine if the comment is in support/against the stock.~~ This is now trained on some basic tweets, but I need a new training set to handle the unrestrained sarcasm, irony, and profanity. 
 - [ ] Convert the entire app to just upload the data into a db, then it would be possible to see any changes in the price of highly mentioned stocks on wsb vs the rest of the market. 
 
 ##### `Want to be added to the email list?`
 Email me kevinjay556@gmail.com
 
 ##### `Want to contribute?`
 Pull a branch! 