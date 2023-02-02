#O desafio: encontrar “a resposta”, utilizando um crawler.
# “A resposta" se encontra atrás do clique de um botão, 
#aqui: http://applicant-test.us-east-1.elasticbeanstalk.com/

#Você deverá fazer um crawler que emita requisições e leia as respostas, 
#Esse crawler deve ser capaz de ler “a resposta" produzida e escrevê-la na tela. 

#O código deverá ser disponibilizado no Github;

#Deverá conter um Dockerfile ou um docker-compose.yml com as instruções de como executar o 
# código do desafio.

#Também deve acompanhar alguns testes unitários ou de
# integração!
#input (8)
#resposta #answer , a (2)
#voltar #answer

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://applicant-test.us-east-1.elasticbeanstalk.com/")
sleep(3)

# Obtain button by link text and click.
button = browser.find_element_by_link_text("Descobrir resposta")
button.click()
sleep(3)

#browser.quit()


    