# import module
from selenium import webdriver
from time import sleep

  
navegador= webdriver.Chrome(r"./driver/chromedriver")
navegador.get("http://applicant-test.us-east-1.elasticbeanstalk.com/")
sleep(3)
  
# Obtain button by link text and click.
navegador.find_element_by_xpath('//*[@id="form"]/input[2]').clik()

sleep(3)
