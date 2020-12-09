import tweepy
import time

auth = tweepy.OAuthHandler(APIkey,APIsecret)
auth.set_access_token(acessToken, acessKey)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


busca = 'pedro'


dic = {'lindo':'lindezas', 'feio':'feiuras', 'louco':'loucuras', ' piada':'piadas', 'estudo':'estudos','estuda':'estudos','namoro':'namoros','namora':'namoros',' amo o':'amores',' amor ':'amores','te amo':'amores','confusao':'confusões','chorar':'choros',' força ':'forças', ' teste ':'testes','aprendendo':'aprendizados'}


dicOutrasLinguas = [' y ', ' el ', ' en ', ' lo ', ' is ']

def semOutrasLinguas(textoTweet, dicionario):
  for palavraTestada in dicionario:
    if palavraTestada in textoTweet:
      return False
    else:
      return True

buscados = []

numeroDeTweets = 100

for tweet in tweepy.Cursor(api.search, busca).items(numeroDeTweets):
    
    try:
        for a,b in dic.items():
            if a in tweet.text and semOutrasLinguas(tweet.text,dicOutrasLinguas): 
                buscados.append(a)
                usr = tweet.user.screen_name
                msg = "pedro "+ str(b)
                link = "https://twitter.com/"+ str(usr) +"/status/"+str(tweet.id)
                api.update_status(msg,None,None,None,link)
                tweet.favorite()
                print('tweet retuitado e favoritado')
                print(buscados)
                time.sleep(15)

    except tweepy.TweepError as e: 
        print(e.reason)

    except StopIteration:
        break

