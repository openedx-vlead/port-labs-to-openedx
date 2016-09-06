from bs4 import BeautifulSoup
import itertools
import urllib
import random
from urlparse import urlparse
import sys
from urlparse import urljoin
import requests

def fetch_all_urls(url):
	url_list = []
	urls_list = []
	html = requests.get(url)
	soup = BeautifulSoup(html.content)
	for record in soup.find_all('a'):
		link = str(record.get('href'))
		if link.startswith('http'):
			urls_list.append(link)
		else:
			urls_list.append(urljoin(url, link))
	url_list = list(set(urls_list))
	return url_list


def fetch_data(url_list, section_name, tag_name):
        for url in url_list:
                try:
                        if "vlead.vlabs.ac.in" or "vlabs.ac.in" or "facebook.com" or "twitter.com" in url:
                                pass

                        if section_name in url:
                                html = requests.get(url)
                                soup = BeautifulSoup(html.content)
                                p_list = soup.find_all(tag_name)
				filename = section_name + ".html" 
                                fp = open(filename, "w")
                                for line in p_list:
                                        fp.write(line.string)
                                fp.close()

                except Exception as e:
                        print  e

def fetch_experiment_data(url_list, section_name, tag_name):
	counter = 0
        for url in url_list:
                try:
                        if "vlead.vlabs.ac.in" or "vlabs.ac.in" or "facebook.com" or "twitter.com" in url:
                                pass

                        if section_name in url:
				counter = counter + 1
                                html = requests.get(url)
                                soup = BeautifulSoup(html.content)
                                p_list = soup.find_all(tag_name)
                                filename = section_name + str(counter) +".html"
                                fp = open(filename, "w")
                                for line in p_list:
                                        fp.write(line.string)
                                fp.close()

                except Exception as e:
                        print  e


def fetch_experiment_content(url_list, section_name, tag_name, counter):
        for url in url_list:
                try:
                        if "vlead.vlabs.ac.in" or "vlabs.ac.in" or "facebook.com" or "twitter.com" in url:
                                pass

                        if section_name in url:
                                html = requests.get(url)
                                soup = BeautifulSoup(html.content)
                                p_list = soup.find_all(tag_name)
                                filename = section_name + str(counter) +".html"
                                fp = open(filename, "w")
                                for line in p_list:
                                        fp.write(line.string)
                                fp.close()

                except Exception as e:
                        print  e

	
lab_url = sys.argv[1]
url_list = fetch_all_urls(lab_url)
fetch_data(url_list, "Introduction", "p",)
fetch_data(url_list, "Prerequisites", "p",)
fetch_data(url_list, "Feedback", "p",)


experiment_url = sys.argv[2]
url_list = fetch_all_urls(experiment_url)
fetch_experiment_data(url_list, "Introduction", "p")

counter = 0
for url in url_list:
	if "Introduction" in url:
		counter = counter + 1
		section_list = fetch_all_urls(url)
		fetch_experiment_content(section_list, "Theory", "p", counter)
		fetch_experiment_content(section_list, "Procedure", "p", counter)
		fetch_experiment_content(section_list, "Objective", "p", counter)
		fetch_experiment_content(section_list, "Quizzes", "p", counter)
		fetch_experiment_content(section_list, "Feedback", "p", counter)
