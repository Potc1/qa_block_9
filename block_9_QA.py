import pandas as pd
import streamlit as st

vendor = pd.read_excel(r'https://raw.githubusercontent.com//Potc1/qa_block_9/vendor.xls')
phone = pd.read_excel(r'https://raw.githubusercontent.com//Potc1/qa_block_9/phone.xls')
person = pd.read_excel(r'https://raw.githubusercontent.com//Potc1/qa_block_9/person.xls')
#email = pd.read_excel(r'C:\Users\Admin\Documents\email.xls')
#password = pd.read_excel(r'C:\Users\Admin\Documents\Passwords.xls')


###Задание №1
def task1():
    data1 = person[['BusinessEntityID', 'FirstName', 'MiddleName', 'LastName']]
    st.title('Блок 9. Задание №1')
    st.subheader(f'''Написать запрос к таблице Person.Person и вывести столбцы BusinessEntityID, FirstName, MiddleName, LastName.''')
    st.write('Таблица:')
    st.write(person)
    st.write('Код запроса:')
    st.code(f"""SELECT BusinessEntityID, FirstName, MiddleName, LastName FROM Person.Person;""", language="sql")
    show_data1 = st.checkbox('Показать результат')
    if show_data1:
        st.write(data1)
###Задание №2
def data_task2():
    df = person
    result = df[(df['ModifiedDate'].dt.year == 2009) & (df['ModifiedDate'].dt.month == 1) & (df['ModifiedDate'].dt.day == 9) & (df['PersonType'] == 'GC')]
    result = result[['BusinessEntityID', 'FirstName', 'MiddleName', 'LastName']]
    return result

def task2():
    data2 = data_task2()
    st.title('Блок 9. Задание №2')
    st.subheader(f'''К запросу из 1 задания применить условие, что ModifiedDate должна быть равна 2009.01.09, а PersonType равен GC.''')
    st.write('Таблица:')
    st.write(person)
    st.write('Код запроса:')
    st.code(f"""SELECT BusinessEntityID, FirstName, MiddleName, LastName FROM Person.Person
WHERE ModifiedDate = '20090109' and PersonType = 'GC'""", language="sql")
    show_data2 = st.checkbox('Показать результат')
    if show_data2:
        st.write(data2)
###Задание №3
def data_task3():
    df = person
    result = df['rowguid'].apply(lambda x: x if 'A3F6' in x else None)
    result = pd.concat([person[['BusinessEntityID', 'FirstName', 'MiddleName', 'LastName']], result], axis=1)
    result['rowguid'].dropna()
    return result        
def task3():
    data3 = data_task3()
    st.title('Блок 9. Задание №3')
    st.subheader(f'''Найдите все строки из таблицы Person.Person у которых rowguid содержит “A3F6“ и вывести столбцы BusinessEntityID, FirstName, MiddleName, LastName, rowguid.''')
    st.write('Таблица:')
    st.write(person)
    st.write('Код запроса:')
    st.code(f"""SELECT BusinessEntityID, FirstName, MiddleName, LastName, rowguid FROM Person.Person
WHERE rowguid LIKE '%A3F6%'""", language="sql")
    show_data3 = st.checkbox('Показать результат')
    if show_data3:
        st.write(data3)
###Задание №4 - неверно
@st.cache_data
def data_task4():
    #print(vendor['StandardPrice'].min(), round(vendor['StandardPrice'].max(), 2), round(vendor['StandardPrice'].mean(), 4), vendor['StandardPrice'].count())
    result = pd.DataFrame(data={'Минимум': vendor['StandardPrice'].min(), 'Максимум': round(vendor['StandardPrice'].max(), 2), 'Среднее': round(vendor['StandardPrice'].mean(), 4),'Количество строк': vendor['StandardPrice'].count()}, index=[1])
    return result
def task4():
    data4 = data_task4()
    st.title('Блок 9. Задание №4')
    st.subheader(f'''К таблице Purchasing.ProductVendor выберите минимальное, среднее значение, а также количество строк столбцу StandardPrice.''')
    st.write('Таблица:')
    st.write(vendor)
    st.write('Код запроса:')
    st.code(f"""
    SELECT person.BusinessEntityID, FirstName, MiddleName, LastName FROM Person.Person person
    INNER JOIN Person.Password pass ON pass.BusinessEntityID = person.BusinessEntityID
    WHERE pass.PasswordSalt = 'U5OYnlY='
    """, language="sql")
    show_data4 = st.checkbox('Показать результат')
    if show_data4:
        st.write(data4)
###Задание №5
@st.cache_data
def data_task5():
    df = vendor.groupby('AverageLeadTime')['AverageLeadTime'].min()
    result = pd.DataFrame({'Минимум': df.min(), 'Максимум': df.max(), 'Среднее': df.mean(), 'Количество строк': df.count()}, index=[1])
    return result
def task5():
    data5 = data_task5()
    st.title('Блок 9. Задание №5')
    st.subheader(f'''Модифицируйте запрос из 4 задания таким образом, чтобы выводилось минимальное, максимальное, среднее значение, а также количество строк в разрезе уникальных значений колонки AverageLeadTime.Подсчет также должен осуществляться только по уникальным значениям.''')
    st.write('Таблица:')
    st.write(vendor)
    st.write('Код запроса:')
    st.code(f"""
    SELECT 
	MIN(distinct AverageLeadTime) AS "Минимум",
	MAX(distinct AverageLeadTime) AS "Максимум",
	AVG(distinct AverageLeadTime) AS "Среднее",
	COUNT(distinct AverageLeadTime) AS "Количество строк"
    FROM Purchasing.ProductVendor;
    """, language="sql")
    show_data5 = st.checkbox('Показать результат')
    if show_data5:
        st.write(data5)
page_names_to_funcs = {
    "-": task1,
    "Задание №1": task1,
    "Задание №2": task2,
    "Задание №3": task3,
    "Задание №4": task4,
    "Задание №5": task5
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
