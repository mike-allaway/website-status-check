import urllib.request,urllib.error
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Define a list of urls to check.
# If a db is included in the site, include an extra url of a page that includes data from db
urls_to_check = [

	# Everyday Lookism
	"https://everydaylookism.bham.ac.uk/",
	"https://everydaylookism.bham.ac.uk/1",

	# Hispanic Exile
	"https://hispanic-exile.bham.ac.uk/",
	"https://hispanic-exile.bham.ac.uk/people/113",

	# Digital Cultures (with hyphen)
	"https://digital-cultures.bham.ac.uk/",
	"https://digital-cultures.bham.ac.uk/research/1",
	# Digital Cultures (without hyphen)
	"https://digitalcultures.bham.ac.uk/",
	"https://digitalcultures.bham.ac.uk/research/1",

	# Testimony in Practice
	"https://testimonyinpractice.bham.ac.uk/",
	"https://testimonyinpractice.bham.ac.uk/testimonies/",

	# Everything To Everybody
	"https://everythingtoeverybody.bham.ac.uk/",

	# Out Of Our Minds
	"https://outofourminds.bham.ac.uk/",
	"https://outofourminds.bham.ac.uk/blog/12",

	# Visualise Baudelaire
	"https://visualisebaudelairesong.bham.ac.uk/",

	# Performance and the Environment
	"https://theatre-environment.bham.ac.uk/",
	"https://theatre-environment.bham.ac.uk/gulp/tour/",

	# AlterUmma
	"https://alterumma.bham.ac.uk",

	# Estoria
	"https://transcribeestoria.bham.ac.uk/en/"

]


def build_error_dict(url, error):
	"""
	Build and return a dictionary that includes error details
	"""
	return {'url': url, 'error': error, 'datetime': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}


# Loop through urls, storing any errors in list
errors_list = []
for url in urls_to_check:

	try:
		urllib.request.urlopen(url)

	except urllib.error.HTTPError as error:
		errors_list.append(build_error_dict(url, error))

	except urllib.error.URLError as error:
		errors_list.append(build_error_dict(url, error))

	except:
		errors_list.append(build_error_dict(url, 'unknown error'))


# Notify me of errors via email (if any exist)
if(len(errors_list) > 0):
	
	# Set up the SMTP server
	server = smtplib.SMTP(host='smtp.bham.ac.uk', port=25)

	# Build the email
	email = MIMEMultipart()
	email['From'] = "m.j.allaway@bham.ac.uk"
	email['To'] = "allawamj@adf.bham.ac.uk"
	email['Subject'] = "Unable to reach URL(s)"

	# Build message text and attach to email
	errors_text = "Found {} error(s) from a total of {} URLs checked:\n".format(len(errors_list), len(urls_to_check))
	for e in errors_list:
		errors_text += "\nurl: {}\nerror: {}\ndatetime: {}\n".format(e['url'], e['error'], e['datetime'])
	email.attach(MIMEText(str(errors_text), 'plain'))

	# Send the email
	server.send_message(email)

	# Tidy up
	del email
	server.quit()
