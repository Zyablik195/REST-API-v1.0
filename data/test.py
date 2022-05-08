from requests import get, post, delete, put

print(get('http://localhost:5000/api/v2/users').json())

print(get('http://localhost:5000/api/v2/users/1').json())

print(get('http://localhost:5000/api/v2/users/999').json())


# нет json
print(post('http://localhost:5000/api/v2/users').json())

# нехватка аргументов
print(post('http://localhost:5000/api/v2/users',
           json={'team_leader': 1}).json())

# неверный аргумент
print(post('http://localhost:5000/api/v2/users',
           json={'title': 'Заголовок'}).json())

# id уже есть
print(post('http://localhost:5000/api/v2/users',
           json={'id': 1, 'name': 'baba', 'surname': 'boy', 'age': 15, 'position': '4543543', 'speciality': '432432', 'address': 'module_2', 'city_from': 'New-York', 'email': 'fls[fls@akpe.ru', 'hashed_password': '1234'}).json())

# всё верно
print(post('http://localhost:5000/api/v2/users',
           json={'id': 5, 'name': 'baba', 'surname': 'boy', 'age': 15, 'position': '4543543', 'speciality': '432432', 'address': 'module_2', 'city_from': 'New-York', 'email': 'fls[fls@akpe.ru', 'hashed_password': '1234'}).json())

# проверка добавки
print(get('http://localhost:5000/api/v2/users').json())

print(delete('http://localhost:5000/api/v2/users/999').json())

print(delete('http://localhost:5000/api/v2/users/5').json())

print(get('http://localhost:5000/api/v2/users').json())