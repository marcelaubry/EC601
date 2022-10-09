# Project 2: Twitter API, Google NLP API, and Botometer Social Media Analyzer

Marcel Aubry 2022

## Project Phases
### Phase 1.(a): Twitter APIs
Write test programs to exercise different twitter APIS.
'Project2Twitter' contains many different test cases ........ (explain tests and results)
### Phase 1.(a): Botometer
Write test programs for the Botometer. 
'Project2Botometer' contains a test case where I test multiple accounts ranging from my personal one to my friends', a celebrity, and an organization. My goal with this was to see which accounts would be flagged as being a bot with largely different types of accounts. <br>
To test this, I looked over which accounts had a CAP score of over 0.8. (For example, suppose an account has a raw bot score of 0.96/1 (equivalent to 4.8/5 display score on the website) and CAP 90%. This means that 90% of accounts with a raw bot score above 0.96 are labeled as bots, or, as indicated on the website, 10% of accounts with a bot score above 4.8/5 are labeled as humans. In other words, if you use a threshold of 0.96 on the raw bot score (or 4.8 on the display score) to classify accounts as human/bot, you would wrongly classify 10% of accounts as bots -- a false positive rate of 10%.) To my surpise, out of the accounts I tested, mine was flagged as the bot account with a very high score of 4.2/5 overall (humourous as I am the most certain that that account is NOT a bot). I suspect this is due to my lack of posting lately mixed with my limited interaction with my feed. <br>
Here is an output of 

### Phase 1.(b): Google NLP
Write test programs to exercise different Google NLP APIs. Focus on sentiment analysis
.......... (explain tests and results)


### Phase 2: Build Your Own Social Media Analyzer
#### Define Minimum Viable Product and User Stories
- Access to public Twitter timeline
- Build a user interface?
