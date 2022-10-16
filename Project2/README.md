# Project 2: Twitter API, Google NLP API, and Botometer Social Media Analyzer

Marcel Aubry 2022

## Project Phases
### Phase 1.(a): Twitter APIs
'Project2.py' contains test programs to exercise different Twitter APIs such as retrieving tweets depending on their time posted, by hashtags, or even if they are retweets of another tweet. I have decided to retrieve multiple pieces of information about the tweet, which are deemed to me as the most important; they include the text, the author's id, the time of creation, and the public metrics attached to it. If the social media analyzer requires more information, I will add it on later.
For this example, I retrieved the last 8 retweets containing the hashtag #cryto. For the purpose of this demo, I am outputting the 4th result of the result of the query. <br> <br>
![image](https://user-images.githubusercontent.com/52050560/194782820-9313058a-113b-40a0-a27d-7683df0160a0.png)


### Phase 1.(a): Botometer
'Project2Botometer.py' contains a test case where I test multiple accounts ranging from my personal one to my friends', a celebrity, and an organization. My goal with this was to see which accounts would be flagged as being a bot with largely different types of accounts. <br>
To test this, I looked over which accounts had a CAP score of over 0.8. (For example, suppose an account has a raw bot score of 0.96/1 (equivalent to 4.8/5 display score on the website) and CAP 90%. This means that 90% of accounts with a raw bot score above 0.96 are labeled as bots, or, as indicated on the website, 10% of accounts with a bot score above 4.8/5 are labeled as humans. In other words, if you use a threshold of 0.96 on the raw bot score (or 4.8 on the display score) to classify accounts as human/bot, you would wrongly classify 10% of accounts as bots -- a false positive rate of 10%.) To my surpise, out of the accounts I tested, mine was flagged as the bot account with a very high score of 4.2/5 overall (humourous as I am the most certain that that account is NOT a bot). I suspect this is due to my lack of posting lately mixed with my limited interaction with my feed. <br> I found that the most interesting information the Botometer API provides is under "display_scores" "universal".
Here is an output of my code: <br> <br>
![image](https://user-images.githubusercontent.com/52050560/194781570-d7c7c521-d761-4f10-b10c-3f1dc0d9a606.png)

### Phase 1.(b): Google NLP
'Project2_GoogleNLP.py' contains the test case I wrote for the Google NLP sentiment analyzer. It took me a very long time to get the API to work due to Google's many steps. Getting the credential to be accepted was the biggest difficulty as my machine would not set the key properly. I had to resort to calling the os library to save the key. For this project, I will be using the analyze_sentiment method. This method works by inputting a text and the output is a score ranging between -1.0 (negative sentiment) and 1.0 (positive sentiment). It also provides the magnitude which is the absolute value of the sentiment. I have attached a couple of examples. One that contains a "happy" text and the other that represents how I felt while trying to make this API work.
<br> Here is an output of my code: <br><br>
![image](https://user-images.githubusercontent.com/52050560/195751602-3ecc2842-0aac-4e34-aa41-91698f754f2b.png)
<br>
![image](https://user-images.githubusercontent.com/52050560/195751687-27007dbc-73ae-49ff-8edf-18ba4b09b8a7.png)


### Phase 2: Build Your Own Social Media Analyzer
Idea: In cryptocurrency swing trading, public hype and excitement about a recent project can be a determining factor on its success, although another cryptocurrency brings more to the table in terms of innovation. My idea would be to retrieve the latest tweets about a new cryptocurrency and see if those who posted them are bots or not. This project could help an investor in determining whether they should invest in that cryptocurrency. Many new projects subsize bots to promote their currency on social media to attract masses and build hype. This project would help expose those projects. <br>
10/13/2022 Update: <br>
With the progress I have made, I decided to add on a layer of complexity to make it interesting. <br>
I will now retrive the sentiment of the texts of the tweets posted of NON bot accounts and return the amount of bots that were identified out of the last 100 tweets with hashtag {crypto the user picks} as well as the average sentiment of real users' tweets. This will give investors more data and a better idea of whether real people or bots are involved in that project. <br>
Below are two examples when running the program, the first one being for the cryptocurrency Solana (SOL) and the second is for Cardano (ADA). As we can see, the program works as expected (for this example I took the latest 20 tweets, this can be extended to as many as we want but I wanted to conserve the amount of API calls I was doing during testing to not get charged) and returns the percentage of accounts that are bots and the average sentiment score for tweets that were made by non-bot accounts. This small, but calculated and specific information will give the investor a better sense of who and what is being tweeted with regards to a chosen cryptocurrency and will give them an edge when it comes down to putting money down based on the given information they have.
<br> <br>

![image](https://user-images.githubusercontent.com/52050560/196062212-6af42819-fcdf-4abf-a983-3a88827c4f8f.png) <br>
![image](https://user-images.githubusercontent.com/52050560/196062231-d4c0ac9a-cc0c-493f-b783-738fcc19d1c9.png)



#### Minimum Viable Product 
An application that allows the user to input the name of a cryptocurrency and receive the amount of tweeters that are bots. Additionally, out of the users that are recognized as real, the average sentiment score will be shown to show how they feel about the upcoming project.
#### User Stories
I, as a cryptocurrency swing trader, am in search of as many reference points before I invest into a new cryptocurrency. With the help of an application that can report back how much social media traffic about a project is being done by a bot, I will be able to better judge the risk I am taking with my investment. <br>
I, as a cryptocurrency swing trader, am in search of what the sentiment of real users have in terms of an upcoming project.

