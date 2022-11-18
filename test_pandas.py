import pandas as pd


beer_data = [[1012, "/pauliner", pd.to_datetime("2022-11-10 18:45")],
            [1013, "/erdinger", pd.to_datetime("2022-11-10 18:44")],
            [1013, "/baltika", pd.to_datetime("2022-11-10 18:46")],
            [1013, "/bochka", pd.to_datetime("2022-11-10 19:10")],
            [1014, "/kozel", pd.to_datetime("2022-11-10 18:20")],
            [1014, "/erdinger", pd.to_datetime("2022-11-10 18:24")],
            [1015, "/efes", pd.to_datetime("2022-11-10 18:44")],
            [1013, "/aynger", pd.to_datetime("2022-11-10 19:12")],
            [1014, "/zhigulevskoe", pd.to_datetime("2022-11-10 18:30")],
            [1016, "/staropramen", pd.to_datetime("2022-11-10 13:44")],
            [1016, "/domik_v_derevne", pd.to_datetime("2022-11-10 13:46")],
            ]

df = pd.DataFrame(beer_data, columns=["customer_id", "product_id", "timestamp"])


# устанавливаем точки отсчета и считаем разницу
# по времени между действиями одного пользователя
df['diff'] = df.groupby('customer_id')['timestamp'].diff(1)


# присваиваем ID для каждой, длящейся более 3-х минут сессии 
df['session_id'] = ((df['diff'] > '180 seconds') | (df['diff'].isnull())).cumsum()

print(df)
