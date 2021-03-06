#! usr/bin/python
__author__ = 'Abhishek'

import requests
from bs4 import BeautifulSoup as bs
import re
import sys
import pandas as pd


def start(question):
    new_input = "+".join(question.split())

    html = requests.get('https://stackoverflow.com/search?q=' + new_input)
    print "The requested Url is {}".format(html.url)

    soup = bs(html.text, "lxml")
    # print soup.prettify()
    child = soup.find_all("div", {"class": "question-summary search-result"})
   
    stack = []
    try:
		for i in range(len(child)):
		    d = {}
		    d['titles'] = child[i].find_all('a')[0]['title']
		    d['url'] = 'https://stackoverflow.com' + child[i].find_all('a')[0]['href']
		    d['votes'] = int(child[i].span.text)
		    try:
		        d['total_answers'] = int(
		            str(child[i].find_all('div', {'class': 'status answered-accepted'})[0].find('strong'))[8:-9])
		    except:
		        d['total_answers'] = -1
		    stack.append(d)
		
		#not necessary
		info = pd.DataFrame(stack)
		# print info.columns
		info.sort_values('votes', inplace=True, ascending=False)
		# print info
		##
		

		url_choice = info["url"][0]
		r_ = requests.get(url_choice)
		soup_ = BeautifulSoup(r_.text, "lxml")
		child_ = soup_.find('div', {'id': 'answers'})
		# child.prettify()
		'''if child_.find('div', {'class': 'answer accepted-answer'}) != None:
		    temp = child_.find('div', {'class': 'post-text'})
		    # print temp
		    print "-" * 80
		    temp = re.sub("<.*?>", '', str(temp))
		    return temp#.replace("\n", ". ")
			#print "-"*80'''



	   	#store the differenet strings
		rspnse = {}
		try:
		    for i in range(len(child_.find_all('div', {'class': 'post-text'}))):
		        print "Length ", len(child_.find_all('div', {'class' :'post-text' }))

		        temp = child_.find_all('div', {'class': 'post-text'})[i]
		        print "-" * 80
		        temp =  re.sub("<.*?>", '', str(temp))
		        if i  < len(child_.find_all('div', {'class': 'post-text'})):
		            rspnse['Response {}'.format(i+1)] = temp
		            print rspnse
		            continue
		    else:
		        #print "boom"
		        return rspnse#.replace("\n", "                  5                                        ")
		        '''print "-"*80


		        more_reply = raw_input("Want to look more, Input 'yes' or 'no' only :")
		        if more_reply.lower() == "yes":
		            continue

		        elif more_reply.lower() == "no":
		            print "elif"
		            break
		        else:
		            print "You don't abide by the instructions"
		            print "else"
		            break'''
		except:
		    return " Cannot find What you, looking for !"
    except:
        return "Sorry I don't get what you say!"
#question = raw_input('Input You Queries: ')
if __name__ == '__main__':
    start(question)
