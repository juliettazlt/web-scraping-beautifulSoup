print(3)
print(4)
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

#find elements by ID
results = soup.find(id="ResultsContainer")
#print(results.prettify())

#find all elements by class
job_elements = results.find_all("div", class_="card-content") # it is a list/iterable wiht all the HTML for all teh job listings
print(job_elements[0])

# for job_card in job_elements:
#     # print(job_card, end = "\n" * 5)
#     title_element = job_card.find("h2", class_="title")
#     subtitle_element = job_card.find("h3", class_="subtitle")
#     location_element = job_card.find("p", class_="location")
#     print(title_element.text.strip())
#     print(subtitle_element.text.strip())
#     print(location_element.text.strip(), end="\n" * 5)

# pass functions to filter results
python_jobs = results.find_all(
    "h2",
    string = lambda text: "python" in text.lower()
) 

print(len(python_jobs)) #there are 10 python jobs

# now extract the parent elements from h2 tags
# the text such as location, company are nested within a sibling element of h2, 
# so i need to print other elements, i will run into errors

python_jobs_cards =[
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print(python_jobs_cards[0])


# for job_card in python_jobs_cards:
#     title_element = job_card.find("h2", class_="title")
#     company_element = job_card.find("h3", class_="company")
#     location_element = job_card.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()


# extract attributes from HTML elements
for job_card in python_jobs_cards:
    links = job_card.find_all("a")
    for link in links:
        link_url = link['href']
        print(link_url)

# for job_card in python_jobs_cards:
#     link_url = job_card.find_all("a")[1]['href']
#     print(link_url)
