'''
Найдите в HTML-коде все цены на отдельные элементы
богатырской экипировки через библиотеку bs4,
посчитайте среднюю стоимость и распечатайте результат.
При расчёте средней стоимости учитывайте,
что количество элементов с ценами заранее неизвестно.

Подсказки:
Для поиска всех тегов, в которых содержатся цены на элементы экипировки,
используйте метод find_all().
Чтобы результат был корректным при любом количестве товаров,
посчитайте общую стоимость всех элементов экипировки с помощью цикла и
разделите её на длину списка. Используйте функцию len().
Чтобы получить только текстовое содержимое тега, используйте атрибут text,
например, содержимое тега <td> можно получить через td.text.
Данные в HTML всегда хранятся в виде строк. Чтобы получить число,
примените преобразование строки в целое число int().

'''


# Импортируйте библиотеку BeautifulSoup.
from bs4 import BeautifulSoup

price_html = """
<table cellspacing="0" cellpadding="0" border="1">
  <tbody>
    <tr class="even_row">
      <th><p>№ п/п</p></th>
      <th class="armor"><p>Название</p></th>
      <th class="price"><p>Цена</p><p>рублей</p></th>
    </tr>
    <tr class="odd_row">
      <td><p>1.</p></td>
      <td class="armor"><p>Щит</p></td>
      <td class="price"><p>375</p></td>
    </tr>
    <tr class="even_row">
      <td><p>2.</p></td>
      <td class="armor"><p>Шлем</p></td>
      <td class="price"><p>297</p></td>
    </tr>
    <tr class="odd_row">
      <td><p>3.</p></td>
      <td class="armor"><p>Кольчуга</p></td>
      <td class="price"><p>565</p></td>
    </tr>
    <tr class="even_row">
      <td><p>4.</p></td>
      <td class="armor"><p>Булава</p></td>
      <td class="price"><p>1992</p></td>
    </tr>
    <!-- Сюда может добавиться неизвестное количество элементов экипировки.
      Их тоже нужно учитывать при расчёте средней цены. -->
  </tbody>
</table>
"""

# Создайте «суп».
soup = BeautifulSoup(price_html, 'lxml')

# Напишите здесь свой код.
armor = soup.find_all('td', attrs={'class': 'price'})
prices = []
summ = 0
for i in range(len(armor)):
    price = armor[i].p.text
    prices.append(int(price))
    summ += int(price)

result = summ / len(prices)

print('Средняя цена богатырских доспехов: ', result, 'рублей')
