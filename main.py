
from os import name
import numpy as np
import json
from datetime import datetime
from datetime import date
import os
import time


dice = dict()
#Menu
def menu():
    response = read_json('candidates.json')
    print('MENU:')
    print('Cadastrar um novo candidato => 1')
    print('================================')
    print('Listar candidatos => 2')
    print('================================')
    print('Sair => 3')
    print('================================')
    resp = input('Resposta: ')

    if  resp == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        registration()
    if resp == '2':
        if response == {}:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Ainda não tem nenhum candidato, dejesa cadastrar algum?')
            if input('Resposta (1 - sim ) (2 - não): ') == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                registration()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                menu()  
        else:
            os.system('cls' if os.name == 'nt' else 'clear')          
            schema() 
    if resp == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Adeus!') 
        exit()        


#Função para coletar dados do candidato
def registration():

    response = read_json('candidates.json')

    dice['name'] = str(input('Nome: '))
    if dice['name'] == '' or dice['name'] == ' ':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('O nome é obrigatorio. O candidato não foi adicionado à lista')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear') 
        registration()

    dice['last_name'] = str(input('Sobrenome: '))
    if dice['last_name'] == '' or dice['last_name'] == ' ':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('O sobrenome é obrigatorio. O candidato não foi adicionado à lista')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear') 
        registration()

    dice['cpf'] = str(input('CPF: '))
    if dice['cpf'] == '' or dice['cpf'] == ' ' :
        os.system('cls' if os.name == 'nt' else 'clear')
        print('O Cpf é obrigatorio. O candidato não foi adicionado à lista')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        registration()
    if response != {}:
        for cpf in response['candidates']:      
            if  dice['cpf'] == cpf['cpf']:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Não pode ter dois candidatos com o mesmo cpf!')
                time.sleep(2.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                registration()

    dice['born_date'] = str(input('Data de nascimento (Formato dd/mm/YYYY): '))
    if dice['born_date'] == '' or dice['born_date'] == ' ':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('A data de nascimento é obrigatória. O candidato não foi adicionado à lista')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        registration()

    #Coletor de quantidade de candidatos
    cont = 0
    if response != {}:
        for qtd in response['candidates']:
            cont = cont + 1
        if cont >= 10 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Não é permitido mais candidatos, nivel maximo atingido -> 10')
            time.sleep(2)
            menu()
        else:    
            write_json(dice)
            print('Candidato cadastrado com sucesso!')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
    else:
        write_json(dice)
        print('Candidato cadastrado com sucesso!')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()


#Função para ler o arquivo Json
def read_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

#Função para adicionar novos campos no arquivo Json
def write_json(dice):
    response = read_json('candidates.json') 
    if response == {}:
        with open('candidates.json', 'w', encoding='utf8') as f:
            data = {
                "candidates": [
                    dice
                ]
            }
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    else:
        response["candidates"].append(dice)

        with open('candidates.json', 'w', encoding='utf8') as f:
            json.dump(response, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

#Função que chamei de schema para organizar os dados Json
def schema():
    response = read_json('candidates.json') 
    date_today = date.today()
    for data in response['candidates']:
        print('=====================')
        print('Nome: ', data['name'])
        print('Sobrenome: ', data['last_name'])
        print('CPF: ', data['cpf'])

        born_date = datetime.strptime(data['born_date'], "%d/%m/%Y").date()
        date_diff = date_today - born_date   
        print('Idade: %.0f ' %((date_diff.days / 360) - 1))

        if (date_diff.days / 360) - 1 >= 18:
            print('É maior de idade? Sim')
        else:
            print('É maior de idade? Não')

    print(' ')
    print('=======================')
    print('Voltar para o menu => 1')
    print('=======================')
    print('Sair => 2')
    print('=======================')
    resp = input('Resposta: ')

    if  resp == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Adeus!')
        

menu()