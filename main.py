# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import bs4
import requests
from bs4 import BeautifulSoup
import csv
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "exception happen"
def fillUnivList(ulist,html,page):
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    for tr in soup.find('tbody').children:
        try:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                ulist.append([tds[0].a.string, tds[1].a.string, tds[2].string, tds[3].string, page])
                # ulist.append([tds[0].a.string, tds[1].a.string, tds[2].string, tds[3].string, tds[4].string,tds[5].string,page])
        except:
            pass


def printUnivList(ulist):
    print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format("Tricker", "Company", "Median Worker Pay", "Pay Ration"))
    for i in ulist:
        # print("=========i:" , i)
        print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format(i[0], i[1], i[2], i[3]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uinfo = []
    for i in range(90, 91):
        url = "https://web.archive.org/web/20220502061027/https://aflcio.org/executive-paywatch/company-pay-ratios?combine=&industry=All&state=All&sp500=0&page={}".format(i)
        print("url = ", url)
        html = getHTMLText(url)
        try:
            fillUnivList(uinfo, html, i+1)
        except:
            pass
        printUnivList(uinfo)
        #field names
        # fields = ["Tricker", "Company", "CEO", "CEO Pay", "Median Worker Pay", "Pay Ration", "page"]
        fields = ["Tricker", "Company", "Median Worker Pay", "Pay Ration", "page"]
        filename = '/Users/guohuazhang/Documents/20220526 90_{}.csv'.format(i+1)
        # with open(filename, 'w') as csvfile:
        #
        #     # creating a csv writer object
        #
        #     csvwriter = csv.writer(csvfile)
        #
        #     # writing the fields
        #     csvwriter.writerows(uinfo)
        #
        #     csvfile.close()

    # writing to csv file
    with open(filename, 'w') as csvfile:

        # creating a csv writer object

        csvwriter = csv.writer(csvfile)

        # writing the fields
        if(i==0):
            csvwriter.writerow(fields)

        # writing the fields
        csvwriter.writerows(uinfo)

        c 
    # soup = BeautifulSoup(demo,"html.parser")
    # print(soup.prettify())

    # list = soup.table.thead.tr.contents
    # listbody = soup.table.tbody.contents
    # for x in list:
    #     print(x)
    #     print(x.string)
    # with open(root, 'wb') as f:
    #     f.write(list)
    #     f.close()
    # for x in listbody:

    # for x in listbody:
    #     print("==================")
    #     for y in x:
    #         for z in y:
    #             print("type of y: " , type(y))
    #             if(type(y) == '<class 'bs4.element.Tag'>'):
    #                 print("===this is y: ", y)
    # print(soup.table.tbody)
    # with open(root, 'wb') as f:
    #     f.write(demo)
    #     f.close()
    #     print("success")

    # for tag in soup.find_all(True):
    #     # print(tag)
    #     print(tag.name)
    # print(soup.find_all('table', 'cols-4'))
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
