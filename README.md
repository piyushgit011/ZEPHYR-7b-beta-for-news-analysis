# ZEPHYR-7b-beta-for-news-analysis

Requirements:
We will use the model TheBloke/zephyr-7B-beta-GPTQ which is a quantised model for faster generation of text and to save the cost.
Now, we will use the  runpod(https://www.runpod.io/endpoints) for deployment of the model.
We will be using runpod instead of sagemaker as we can get the great gpus in  cheaper cost with runpod. 
We will be using RTX 3080 ti as it can genrate the output in 4-5 second and cost $0.19/hour.

We will be using a cloud template of runpod , the bloke to deploy zephyr-gptq as an api endpoint.Read more about template:- https://www.runpod.io/console/explore/f1pf20op0z.
The template will be deployed and then we have to load the model in the tmplate ui with the best configuration.
Now, endpoint will be will be created with the port 5000 and we can add v1/completions for the request and responses from the endpoint.

About the code:-
Now, we will use use langchain and newspaper3k for news extraction from any link provided.here is the link of the code for news analysis:-
https://colab.research.google.com/drive/11MOdhQ3rv5LF6pf4B1KESQfA7nHQoXFh?usp=sharing .


It will receive a news link and generate a concise summary, along
with questions infused with emojis and hashtags—all condensed within 250
to 280 characters. Additionally, it  formulates three opinions: positive,
negative, and sarcastic, each expressed within 50 characters, accompanied
by appropriate emojis. The news would be categorized, revealing the
relevant sectors it falls under. Subsequently, the sentiment of the news will
be determined, and the language  be detected. The AI would
categorize the news into sectors (If the news falls under two or more
categories it would show the all catogries), determine sentiment (if the news
falls under two or three sentiments, it would show the sentiments), detect
language, identify key individuals in hashtags, and ascertain location details.
If the news doesn't have any location details, put the news in a global
context. For example, if the news is about Bitcoin and doesn't specify a
location, categorize it as global. This is applicable to all languages; it would
also categorize the news, sentiment, detect language, identify key individuals
and the core content of the news as hashtags, and ascertain location
details(as detailed as possible).
1. News Summary and Question:
📰 Summarised News
🤔 Question
#hashtags
This all within 280 characters
2. Opinions :
Opinions 1: Positive Opinion
Opinions 2: Negative Opinion
Opinions 3: Sarcastic Opinion
(Opinions within 50 characters with emojis)

3. News Categories:
📌 Categories: [List of relevant categories]
Categories which we can show in PollYa Landing page :
1. NationalNews: News and events happening at the national level, including politics, major
incidents, and significant developments.
2. InternationalNews: Global news covering international events, foreign affairs, and
significant stories from around the world.
3. Local & RegionalNews: News specific to local and regional areas, including local
government, events, and community updates.
4. Business & Finance: All about the business world, financial markets, economic policies,
and corporate news.
5. Tech & Science: Latest updates in technology, scientific discoveries, and advancements in
research and development.
6. Sports: Comprehensive coverage of national and international sports events, scores, and
sports-related news.
7. Entertainment: News related to movies, games, television, & music.
8. Opinion & Analysis: Editorials, opinion pieces, and in-depth analysis of current events and
issues.
9. Health & Wellness: Focused on health news, medical advancements, wellness tips, and
lifestyle health topics.
10. Education: News related to educational policies, institutions, trends, and developments in
the field of education.
11. Culture & Arts: Covering cultural events, art exhibitions, book reviews, and performing
arts.
12. Travel : Featuring travel destinations, culinary experiences
& restaurant reviews.
13. Food: Savor the latest in culinary delights, recipes, and food trends for the food
enthusiasts.
14. Fashion: Strut into the world of style with the latest in fashion trends, runway highlights,
and fashion-forward insights.

4. Sentiment Analysis:
1. Positive (Uplifting/Optimistic)
2. Outrage (Outrage-Inducing)
3. Info (Informative)
4. Debate (Controversial)
5. Sad (Sorrowful)
6. Alert (Fearful)
7. LOL (Amusing)
8. Retro (Nostalgic)
9. Insight (Analytical)
10.Balanced (Neutral)
11.Negative (Pessimistic)
It would detect all applicable sentiments of the news
5.language detection :
The AI will determine the language of the news.
6.country and place of the news happened:
AI is to identify the country, city, and location of a news event.
7.Main persons in the news:
AI will detect the main persons in the news.

This is just a example prompt :

Example outputs:
1.
https://finance.yahoo.com/news/risky-frontier-stock-markets-beating-230000428.html
Summery:
📈 Frontier markets soar! 🌎 Investors flock to high-risk, high-reward stocks in countries like
Bangladesh & Pakistan as global growth slows. Some say 🚀 this trend signals economic
progress, while others warn of ⚠️ excessive risk. How's your portfolio looking?
#stockMarkets #Investing
Opinion 1 : Embrace frontier market opportunities for maximum gains! 💯
Opinion 2 : Avoid disaster! Ditch volatile stocks! 😡📉
Opinion 3 : Beware the rollercoaster ride ahead in the market.😂❌
Categories: Business & Technology (Global), National News (Bangladesh, Pakistan, Sri
Lanka)
Sentiment: Balanced (Neutral).
Language: English
Locations Mentioned: Bangladesh, Pakistan, Sri Lanka
Main Persons/Organizations: Frontier Markets, Emerging Markets, Investors

2.https://news.yahoo.com/israel-said-flooding-hamas-tunnels-132141352.html
Summery:
Israel reportedly flooded Hamas tunnels using seawater to prevent militant infiltration along
the Gaza border. Measure aimed at protecting Israeli communities near the coastal enclave
amid ongoing tensions between the two parties. 󰏛😨Do you think this measure will
effectively deter Hamas' military activities? #HamasResponse
Opinion 1 : Securing borders with smart solutions! 💪🌊❤️
Opinion 2 : This won't solve the root cause of conflict - justice for Palestinians! ❌🐬🙅
Opinion 3 : Drowning tunnels like fish in the sea... Genius idea 😂🤔🦈
Categories: National News (Israel), International News (Gaza Strip)
Sentiment: Alert (Fearful)
Language: English
Locations Mentioned: Israel, Gaza Strip
Main Persons/Organizations: Israel Defense Forces (IDF), Hamas
