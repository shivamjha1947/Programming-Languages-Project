import json
with open('newspost.json','r') as f1:
    dicto=json.load(f1)

def checker(needle,haystack):
	return needle in haystack


post=dicto['Posts']


							# key='december'
							# for i in range(len(post)):
							# 	cur_data=post[i][1].lower()

							# 	print('--------------',"\n",cur_data)
							# 	print(key,'present') if (checker(key,cur_data) == True) else print(key,'false')


waste='You have reached your limit for free articles this month.Register to The Hindu for free and get unlimited access for 30 days. Already have an account ? Sign in\nSign up for a 30-day free trial. Sign UpFind mobile-friendly version of articles from the day\'s newspaper in one easy-to-read list.Enjoy reading as many articles as you wish without any limitations.A select list of articles that match your interests and tastes.Move smoothly between articles as our pages load instantly.A one-stop-shop for seeing the latest updates, and managing your preferences.We brief you on the latest and most important developments, three times a day.\n*Our Digital Subscription plans do not currently include the e-paper ,crossword, iPhone, iPad mobile applications and print. Our plans enhance your reading experience.\n\nWhy you should pay for quality journalism - Click to know morePlease enter a valid email address.'

dicto1=json.load(open('newspost.json','r'))
#remove /n method
for i in range(len(dicto1['Posts'])):
	c_head=dicto1['Posts'][i][0]
	c_body=dicto1['Posts'][i][3]
	dicto1['Posts'][i][0]=c_head.replace('\n','')
	dicto1['Posts'][i][3]=c_body.replace(waste,'')


# for i in range(len(dicto1['Posts'])):
#     dicto1['Posts'][i][0]=h[i]

json.dump(dicto1,open('scrapednews.json','w'),indent=2)
print((dicto1['Posts'][1]))


