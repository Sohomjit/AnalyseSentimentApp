from flask import Flask, render_template, request
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize, RegexpTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import string
analyzer = SentimentIntensityAnalyzer()
app = Flask(__name__)

def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    print(text)
    print(score)
    return score

"""def Analyse(sub):
   tokenized_text = nltk.word_tokenize(sub)
   pos_word_list=[]
   neu_word_list=[]
   neg_word_list=[]
   
   for word in tokenized_text:
        if (analyzer.polarity_scores(word)['compound']) >= 0.1:
            pos_word_list.append(word)
        elif (analyzer.polarity_scores(word)['compound']) <= -0.1:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)
   print('Positive:',pos_word_list)        
   print('Neutral:',neu_word_list)    
   print('Negative:',neg_word_list)
   return"""


@app.route('/')
def home():
   print("inside home")
   return render_template('landing_page.html')


@app.route('/result',methods = ['POST'])
def result():
        if 'Home' in request.form:
            return render_template('landing_page.html')
        else:
            print("inside result")
            #if request.method == 'POST':
            #   result = request.form
            name_user = request.form['firstname']
            analysis_text = request.form['subject']
            analysis_score = sentiment_analyzer_scores(analysis_text)
            print(name_user, analysis_text, analysis_score)
            if analysis_score['compound'] >= 0.05:
                print("Positive")
                finalSentiment = "Positive"
                image = "https://i.pinimg.com/originals/c0/1d/28/c01d28d4c27d214e5222413238b9bd89.jpg"
            elif analysis_score['compound'] <= - 0.05:
                print("Negative")
                finalSentiment = "Negative"
                image = "https://www.itweb.co.za/static/pictures/2018/10/resized/-fs-dislike-emoji-2018.xl.jpg"
            else :
                print("Neutral")
                finalSentiment = "Neutral"
                image = "https://static.turbosquid.com/Preview/2019/04/24__06_20_15/1_00000.png1047FE1C-DE30-498C-9DFB-2A51921BECFELarge-1.jpg"

            my_list = [name_user, analysis_text, finalSentiment, image]
            return render_template("result.html", data = my_list)
      

if __name__ == '__main__':
   app.run(debug = True)