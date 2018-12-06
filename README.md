# Proxy6 API [Python]
  Python API для [сервиса прокси](https://proxy6.net).
  
  Оригинальный [REST](https://proxy6.net/developers).
***
### Установка:
	
    pip install proxy-6
***
### Документация:
* Авторизация клиента
```python
proxy = Proxy(api_key)  # str: api_key
```
Метод             | Описание
------------------|----------------------
balance()         | Возвращает баланс аккаунта
get_price(count, period, version=None)| Возвращает стоимость count(**int**) прокси, на период period(**int**), с version(3, 4, 6 **int**) ipv4 shared, ipv4, ipv6 соответственно, без - ipv6
get_count(country, version=None)| Возвращает кол-во возможных для покупки прокси в стране country(**str** в формате iso2), с version(3, 4, 6 **int**) ipv4 shared, ipv4, ipv6 соответственно, без - ipv6
get_country(version=None)| Возвращает список возможных для покупки прокси стран, с version(3, 4, 6 **int**) ipv4 shared, ipv4, ipv6 соответственно, без - ipv6
get_proxy(state=None, descr='', nokey=False| Возвращает купленные прокси, с state(**str** active/expired/expiring), без - all, с descr(**str** тех. кмомментарий), без все, с nokey(**bool**) - возвращает без ключей
set_type(ids, types)| Меняет тип купленного прокси, ids(**str**) id через запятую, types(**str** http/socks)
set_descr(new, olds=None, ids=None)| Меняет описание с (**str**) old или у ids(**str**) id через запятую, на new (**str**)
buy(count, period, country, version=None, types=None, descr='', auto_prolong=False, nokey=False)| Покупает count(**int**) прокси, на period(**int**) дней, country(**str** iso2), c auto_prolong(**bool**) автопродлением
prolong(period, ids, nokey=False)| Продляет с ids(**str**) на period(**int**) дней
delete(ids=None, descr=None)| Удаляет прокси с ids(**str**), либо с descr(**str**)
check(ids)| Проверяет работоспособность у прокси с ids(**str**)

### Пример:
Покупка 5 ipv6 прокси:
```python
proxy = Proxy6('2d08p37k6bkwjpj1pqgwdsbg9nuy2g1y')
print(proxy.balance())
print(proxy.buy(5, 3, 'ru', version=6, types='http', descr='TEST PROXY', auto_prolong=False, nokey=True))
```
