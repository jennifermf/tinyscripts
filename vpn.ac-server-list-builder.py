#!/usr/bin/env python3

'''
i wanted a quick way to pull a list of servers and locations from from https://vpn.ac/status

procedure: 
extract location and node URL
create file that lists nodeURL and location (separated by \t)

NOTE: this script is dependent on the location of the nodeURL and node geographic location... 
tweak the first_var and second_var variables for the respective location for your VPN's server listing.

this script utilizes the excellent pythonic HTML parser, requests_hmtl
parser source: https://github.com/kennethreitz/requests-html

i love vpn.ac and i don't work for them, but clicking this affiliate link would make me feel good about 
sharing this tiny script: 
https://vpn.ac/aff.php?aff=1633

'''

from requests_html import HTMLSession
import os, sys

def MakeTextFile(linklist, filename):
    with open(filename, 'a+') as file:
        for link in linklist:
            file.write(link + '\n')

def BuildServerList():
    print("\nBuilding list of VPN nodes...\n")

    # destination file for your links:
    filename = 'nodelist.txt'

    # get URL source:
    # url = input("Enter a complete URL: ")
    url = 'https://vpn.ac/status'

    # start a session and get html
    session = HTMLSession()
    r = session.get(url).html

    # location (on website) of node geographic locations
    first_var = 'tr > td:first-child'

    # location (on website) of node URLs
    second_var = 'tr > td:nth-child(2)'

    # make lists of links
    geography_list = r.find(first_var, first=False)
    node_url_list = r.find(second_var, first=False)

    # combine both lists and copy into tab-delineated file:
    linklist = [(node_url_list[x].text + '\t' + geography_list[x].text) for x in range(len(node_url_list))]
    MakeTextFile(linklist, filename)

    print("\nFinished! Your file is located at \n\t{}/{}\n".format(os.getcwd(), filename))

BuildServerList()
