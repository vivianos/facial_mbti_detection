# facial_mbti_detection
 Predict a persons MBTI personality type using a picture

MBTI Prediction

Motivation

An MBTI test aims to determine a persons personality type based on the answers of a questionnaire. Although the validity of the test is questionable, there are some correlations that have proven to be reliable. These personality types have been used by companies for determining management ability and by marketers to find customers. On top of that, there are correlations between facial features and personality (i.e. jaw width and aggression).

Getting the Data

Unfortunately there didn’t exist any clean datasets with mbti results and pictures of people who have actually taken the test. There is a website that acts as a database for personality types, but these are done by having users vote on a celebrities mbti so whatever, it’s the best I could get. I built a web scraper using selenium to get the pictures and types.

Features

I used opencv and dlib to extract the features from the pictures to turn them into something I could actually use. Here’s a picture of Robert Downey Jr. with the point map. I used the euclidian distance between two points for five features, but obviously there can be many more than that. I’d like to use area of certain features, shape, etc. eventually.

Fun Part

After I loaded everything into a pandas dataset, I used linear regression, k-nearest neighbor, and a multi-class neural network to determine if I could actually use a machine to determine personality type by a picture of their face. After that I realized I should’ve been using a binary classifier on each letter so I did that as well.

Result

Bad, but this is just the beginning of the project. The data was collected from a website that assigns types using general consensus, not to mention I found cartoon characters in the dataset. Upon making the pair plots I realized the data I pulled using opencv would not yield promising results, but I figured I’d try anyway. I also didn’t account for the size of the picture, and whether or not they were looking directly at the camera. I’ll work on that, but most likely I’d have to find a way to obtain a better dataset. Fun project that I’d like to expand upon. 
