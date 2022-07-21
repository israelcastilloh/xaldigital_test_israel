import requests
import pandas as pd
from urllib.error import HTTPError

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)


def create_tables(response):
    '''
    :param response:
    :return:
    '''

    # Set the json content into a Dataframe
    df = pd.DataFrame(response.json()['items'])


    respuestas_no_contestadas = len(df[df['is_answered'] == False])
    respuestas_contestadas = len(df[df['is_answered'] == True])

    menor_numero_visitas = df.sort_values('view_count', ascending=True)\
        [['title', 'is_answered', 'creation_date', 'last_activity_date']].head(1).to_string(index=False)

    mas_actual = df.sort_values('creation_date', ascending=False)\
        [['title', 'is_answered', 'creation_date', 'last_activity_date']].head(1).to_string(index=False)

    mas_antigua = df.sort_values('creation_date', ascending=True)\
        [['title', 'is_answered', 'creation_date', 'last_activity_date']].head(1).to_string(index=False)

    df['reputation'] = df['owner'].map(lambda x: x['reputation'])
    mayor_rep = df.sort_values('reputation', ascending=False)\
        [['title', 'is_answered', 'creation_date', 'last_activity_date', 'reputation']].head(1).to_string(index=False)

    # -----------------------------------------------------------------
    print('2. Numero de respuestas contestadas y no contestadas')
    print('Respuestas no contestadas ', respuestas_no_contestadas, '\n', 'Respuestas contestadas ', respuestas_contestadas)

    print('3. Obtener la respuesta con menor número de vistas')
    print(menor_numero_visitas, '\n')

    print('4. Obtener la respuesta más actual')
    print(mas_actual, '\n')

    print('4. Obtener la respuesta más antigua')
    print(mas_antigua, '\n')

    print('5. Obtener la respuesta del owner que tenga una mayor reputación')
    print(mayor_rep, '\n')


def main(url):
    '''

    :param url:
    :return:
    '''

    try:
        response = requests.get(url)
        create_tables(response)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    main(url)
