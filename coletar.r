##trabalho de TCC Mariane Mariano & Marcos Mol
## coleta de dados do twitter e analise de sentimentos, com verificação da chave utilizada
rm(list=ls(all=TRUE));
detach(Output_Sentimental);
Consumer_API_Key <- 'zcQ8yEGrCpUL7AiJC7XSjP0ib';
Consumer_Secret <- 'LicwyVCoenr4ITeUuF1Y55NpXoaeIJXqA4fN23LKSBIOj4cDVC';
Access_Token <- '117869496-Biraq1HNZhVpTrPtCA0MgvXUw3YxFzkEjeEyyKlK';
Access_Token_Secret <- '2mM4lUXbhgRvG4lgkdzWYqcRxStYPZpmloTHoOlRoUKZ5';
Microsoft_API_Key <- 'abfc24e29ec24823b8a23985b8656dae';
twitter_search_string <- "#cruzeiro";
library(twitteR);
library(jsonlite);
library(httr);

# Establish Authentication with Twitter
setup_twitter_oauth(Consumer_API_Key, Consumer_Secret, Access_Token, Access_Token_Secret);

# Search string on Twitter using twitter_search_string variable
tweets = searchTwitter(twitter_search_string, lang="pt", resultType="mixed", 1000);

# ------------------------- Start transformations and cleasing -------------------------#
tweets_df = do.call("rbind", lapply(tweets, as.data.frame));
tweets_df = subset(tweets_df, select = c(text,created));



#Tweet Cleasing
tweets_df$text = gsub('http.* *', '', tweets_df$text);
tweets_df$text = gsub("(RT|via)((?:\\b\\W*@\\w+)+)", " ",  tweets_df$text);
tweets_df$text = gsub(":", "", tweets_df$text);
# remove at people
tweets_df$text = gsub("@\\w+", "", tweets_df$text)
# remove punctuation
tweets_df$text = gsub("[[:punct:]]", "", tweets_df$text)
# remove numbers
tweets_df$text = gsub("[[:digit:]]", "", tweets_df$text)
# remove html links
tweets_df$text = gsub("http\\w+", "", tweets_df$text)
# remove unnecessary spaces
tweets_df$text = gsub("[ \t]{2,}", "", tweets_df$text)
tweets_df$text = gsub("^\\s+|\\s+$", "", tweets_df$text)
# Removing Duplicate tweets
tweets_df["DuplicateFlag"] = duplicated(tweets_df$text);
tweets_df = subset(tweets_df, tweets_df$DuplicateFlag=="FALSE");
tweets_df = subset(tweets_df, select = -c(DuplicateFlag));
tweets_df = subset(tweets_df, text != "")

# ------------------------- Finish transformations and cleasing -------------------------#

# Creating the request body for Text Analytics API
tweets_df["language"] = "pt";
tweets_df["id"] = seq.int(nrow(tweets_df));
## sempre fazer bloco a bloco para verificar se não ha tweets vazios
#se tiver tweetes vazios tratar a mão
#write.table(tweets_df, "C:/Users/marco/Desktop/projetos/tcc/tcc1/bd/tratamento.csv", sep=";");
#variavel=read.csv2("C:/Users/marco/Desktop/projetos/tcc/tcc1/bd/tratamento.csv", header=T)
#tweets_df = variavel;
request_body_twitter = tweets_df[c(3,4,1)];



# Converting tweets dataframe into JSON
request_body_json_twitter = toJSON(list(documents = request_body_twitter));

# Calling text analytics API
result_twitter_sentimental = POST("https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment", 
                                  body = request_body_json_twitter, 
                                  add_headers(.headers = c("Content-Type"="application/json","Ocp-Apim-Subscription-Key"= Microsoft_API_Key)))

# Calling text analytics API
#result_twitter_sentimental = POST("https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment", 
#                                  body = request_body_json_twitter, 
#                                  add_headers(.headers = c("Content-Type"="application/json","Ocp-Apim-Subscription-Key"= Microsoft_API_Key)))



# Transforming resulting in Data Frame (Sentimental)
Output_Sentimental = content(result_twitter_sentimental);
#Output_SentimentalKey = content(result_twitter_keyPhrases);
attach(Output_Sentimental);
rows <- length(documents);
score_twitter = data.frame(matrix(unlist(Output_Sentimental), nrow=rows, byrow=T));

score_twitter$X1 =  as.numeric(as.character(score_twitter$X1));
names(score_twitter)[names(score_twitter) == 'X1'] <- 'Id';
names(score_twitter)[names(score_twitter) == 'X2'] <- 'Score';
#tweets_df$Score <- c(score_twitter$Score);
score_twitter$text <- c(tweets_df$text);
score_twitter$data <- c(tweets_df$created);
##se for necessario correção manual . sera necessario importr alguns dados a mao 
#score_twitter$keyParser <- c()
detach(Output_Sentimental);
#rm(tweets_df);
write.table(score_twitter, "C:/Users/marco/Desktop/projetos/tcc/tcc1/bd/cruzeiro-19-03-19.csv", sep=";");
# Pegar a palavra chave ainda n?o est? dispon?vel em portugues
#result_twitter_keyPhrases = POST("https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases", 
#                                 body = request_body_json_twitter, 
#                                 add_headers(.headers = c("Content-Type"="application/json","Ocp-Apim-Subscription-Key"= Microsoft_API_Key)))

## WORKING ON IT
# Transforming resulting in Data Frame (Key Phrases) - NOT WORKING TO PORTUGUESE
#Output_keyPhrases = content(result_twitter_keyPhrases);
#attach(Output_keyPhrases);
#rows <- length(documents);
#phrases_twitter = data.frame(matrix(unlist(Output_keyPhrases), nrow=rows, byrow=T));
