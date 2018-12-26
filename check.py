# imports
import urllib.request
import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
import time

# Rowan section tally url
url = 'https://banner.rowan.edu/reports/reports.pl?task=Section_Tally'

# Function to get all terms from rowans section tally website
def getTerms():
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    soup = BeautifulSoup(respData,'lxml')
    
    terms={}
    for option in soup.find_all('option'):
        terms[option.text] = option['value']

    return terms

# Function to get all subjects from the website ie MATH, CS .. etc. Uses the spring 2019 term
def getSubjs():
    payload = {'term' : '201920', 'task' : 'Section_Tally'}

    data = urllib.parse.urlencode(payload)
    data = data.encode('utf-8')
    
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    soup = BeautifulSoup(respData,'lxml')

    section = soup.find('select', attrs={'name':'subj'})

    subjs={}
    for option in section.find_all('option'):
        subjs[option.text] = option['value']

    return subjs

# Function to get all professors from the website. Uses the spring 2019 term
def getProfs():
    payload = {'term' : '201920', 'task' : 'Section_Tally'}

    data = urllib.parse.urlencode(payload)
    data = data.encode('utf-8')
    
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    soup = BeautifulSoup(respData,'lxml')

    section = soup.find('select', attrs={'name':'prof'})

    profs={}
    for option in section.find_all('option'):
        profs[option.text] = option['value']

    return profs

def garb():
    print('done')

# Function that loops until there is an open spot in desired course, checks every 30 mins
def runScript(term, subj, prof, crn, email):

    msgSent = False

    # Params for request payload
    payload = {'term' : term, 'task' : 'Section_Tally', 
    'coll' : 'ALL', 'dept' : 'ALL', 
    'ptrm' : 'ALL', 'sess' : 'ALL', 
    'attr' : 'ALL', 'camp' : 'ALL', 
    'bldg' : 'ALL', 'subj' : subj,
    'prof' : prof,
    'Search' : 'Search'}
    
    while not msgSent:
        # Connecting to webiste
        data = urllib.parse.urlencode(payload)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)

        resp = urllib.request.urlopen(req)
        respData = resp.read()

        soup = BeautifulSoup(respData,'lxml')
        

        # Getting table of classes related to search

        table = soup.find('table', attrs={'class':'report'})
        table_rows = table.find_all('tr')

        # Storing each row as a the list row then storing each row into res so we have a neat list of data in res
        res = []
        for tr in table_rows:
            td = tr.find_all('td')
            row = [tr.text.strip() for tr in td if tr.text.strip()]
            if row:
                res.append(row)

        # Column titles
        cols= ['CRN', 'Subj', 'Crse', 'Sect', 'Part of Term',
            'Session', 'Title', 'Prof', 'Day', 'Campus', 
            'Hrs', 'Max', 'MaxResv', 'LeftResv', 'Enr', 
            'Avail', 'WaitCap', 'WaitCount', 'WaitAvial', 'Room Cap']

        # Storing the table res into a panda data frame and removing data we dont need
        df = pd.DataFrame(res, columns=cols)

        df.dropna(inplace=True)

        df[['CRN', 'Max', 'Enr']] = df[['CRN', 'Max', 'Enr']].astype(int)
        df = df[df.CRN == int(crn)]
        df = df[['CRN', 'Max', 'Enr']]

        df = df.reset_index(drop=True)
        
        # Storing Max enrollment into maxEnr and Current enrollment into enr
        maxEnr = df.at[0, 'Max']
        enr = df.at[0, 'Enr']

        print('Max : ', maxEnr)
        print('Enrolled: ',  enr)

        # If max enrollment and enrolled are not equal send email, else sleep 15 mins
        if maxEnr != enr: 
            # Email message
            msg = ('Open spot in course ' + crn)

            # Sending email
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('Sender Email account', 'Password')
            mail.sendmail('Sender Email account','Email account to send to', msg)
            mail.close()

            msgSent = True

        else:
            time.sleep(1800)
