#########################################################################################
##                                                                                     ##
##   Text Mining from Master subject about sentiment analytics                         ##
##                                                                                     ##
##   Code developed by: Alejandro Parcet Gonzalez and Vicente Blat Lacasa              ##
##   For 2018/19 Big Data Master edition -Procesamiento del Lenguaje Natural- subject  ##
##                                                                                     ##
#########################################################################################

# Imports required for the whole program
import sys
import click
import json
import tweepy
import json
import pandas as pd

# Arguments form command line using click library
@click.command()
@click.option(
    '--cred',
    '-c',
    type=click.File('r'),
    help='File in JSON format with key:value holding the consumer and access keys'
         'Required keys: consumer_key, consumer_secret, access_token, access_token_secret',
)
@click.option(
    '--analyze',
    '-a',
    is_flag=True,
    help='Analyze flag, if present, it will assume all tweets are present, if not, it will check to download all tweets.'
)
@click.option(
    '--download',
    '-d',
    is_flag=True,
    help='Download flag to, when credentials are provided, download all tweets from tweeter'
)
def arguments(cred, analyze, download):
    if download:
        dataCollection(json.load(cred))
    if analyze:
        # TODO utilizar algún método de machine learning para construir un clasificador.

        # TODO descargar los tweets de test a partir del id (TASS_test_ids.txt).

        # TODO etiquetar los tweets de test utilizando el modelo aprendido en 2).

        # TODO subir a la actividad de PoliformaT un fichero de texto con el test etiquetado (identificador \t polaridad) y un fichero ".zip" con todo el código desarrollado.

        # TODO para mejorar los modelos se puede utilizar un diccionario de polaridad (ElhPolar_esV1.lex )
        pass


def dataCollection(cred):
    # TODO descargar los tweets de entrenamiento a partir del id (TASS_training_polarity.txt).
    if cred != {}:
        # Accessing twitter API through tweetpy
        auth = tweepy.OAuthHandler(
            cred['consumer_key'], cred['consumer_secret'])
        auth.set_access_token(cred['access_token'],
                              cred['access_token_secret'])
        API = tweepy.API(auth_handler=auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

        # Load tweet's ID's from file
        tweet_ids = pd.read_csv(
            'TASS_training_polarity.csv', sep='\t', header=None, names=['id', 'extra']).id

        # Query structure and recovery
        for id in tweet_ids:
            try:
                tweet = API.get_status(id)
                save_json("tweet_"+str(id)+".json", tweet)
            except tweepy.TweepError as te:
                print(str(id)+': '+str(te))

        # Saving tweets to file

    else:
        print('Failed to retrieve credentials')
    pass


def save_json(filename, j):
    with open('tweets/'+filename, 'w', encoding='utf8') as fh:
        json.dump(j._json, fh)


if __name__ == "__main__":
    arguments()
