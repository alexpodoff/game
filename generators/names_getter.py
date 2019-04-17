from selenium import webdriver

address = "http://www.babynamewizard.com/the-top-1000-baby-names-of-2017-united-states-of-america"
wd = webdriver.Firefox()
wd.implicitly_wait(5)

wd.get(address)


def create_name_list(gender: str):
    """
    Gets 1000 most popular names in US in 2017 from babynamewizard.com
    Stores them in .csv file
    :param gender: str ("male" or "female")
    :return: None
    """
    if gender == "male":
        table = wd.find_element_by_xpath('//*[@id="node-65027"]/div[2]/table[1]')
        file_list = "./resources/boys_names.csv"
    elif gender == "female":
        table = wd.find_element_by_xpath('//*[@id="node-65027"]/div[2]/table[2]')
        file_list = "./resources/girls_names.csv"
    raws = table.find_elements_by_tag_name("tr")
    with open(file_list, "w") as file:
        for i in range(1, len(raws) - 1):
            cells = raws[i].find_elements_by_xpath("./*")
            file.write(cells[1].text + "\n")
        cells = raws[len(raws) - 1].find_elements_by_xpath("./*")
        file.write(cells[1].text)
