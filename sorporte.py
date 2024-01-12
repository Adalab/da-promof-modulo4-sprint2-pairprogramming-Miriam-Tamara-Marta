#%%
import pandas as pd
import datetime
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# %%
df= pd.read_csv("ficheros/sentimentdataset.csv", index_col=0)
print('Leemos csv')
df

# %%
def exploracion_dataframe(dataframe):

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    print(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    print(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        print(pd.DataFrame(dataframe[col].value_counts()).head()) 
 
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas númericas son: ")
    dataframe_numericas = dataframe.select_dtypes(exclude = "O")
    
    for col in dataframe_numericas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        print(pd.DataFrame(dataframe[col].value_counts()).head())   
#%%
exploracion_dataframe(df) 
#%%
df['Sentiment'].value_counts()
# %%
# %%
def columnas_eliminar ():
    columnas_eliminar = ['Year', 'Month', 'Day', 'Hour', 'Unnamed: 0']
    df.drop(columnas_eliminar, axis=1, inplace=True)

columnas_eliminar()
df

# %%
def clasificar_estados(df, columna):
    sentimientos_mapping = {
        'Joy': 'felicidad',
        'Excitement': 'felicidad',
        'Happy': 'felicidad',
        'Contentment': 'felicidad',
        'Hopeful': 'felicidad',
        'Elation': 'felicidad',
        'Enthusiasm': 'felicidad',
        'Inspired': 'felicidad',
        'Empowerment': 'felicidad',
        'Grateful': 'felicidad',
        'Love': 'amor',
        'Affection': 'amor',
        'Adoration': 'amor',
        'Passion': 'amor',
        'Romance': 'amor',
        'Tenderness': 'amor',
        'Arousal': 'amor',
        'Positive': 'felicidad',
        'Neutral': 'tranquilidad',
        'Calmness': 'tranquilidad',
        'Serenity': 'tranquilidad',
        'Tranquility': 'tranquilidad',
        'Peace': 'tranquilidad',
        'Relaxation': 'tranquilidad',
        'Hope': 'felicidad',
        'Confidence': 'tranquilidad',
        'Pride': 'felicidad',
        'Acceptance': 'tranquilidad',
        'Gratitude': 'felicidad',
        'Compassion': 'amor',
        'Empathy': 'amor',
        'Emotion': 'amor',
        'Happiness': 'felicidad',
        'Satisfaction': 'felicidad',
        'Surprise': 'sorpresa',
        'Awe': 'sorpresa',
        'Wonder': 'sorpresa',
        'Amazement': 'sorpresa',
        'Curiosity': 'sorpresa',
        'Enchantment': 'sorpresa',
        'Anticipation': 'sorpresa',
        'Fear': 'miedo',
        'Anxiety': 'ansiedad',
        'Worry': 'ansiedad',
        'Nervousness': 'ansiedad',
        'Apprehension': 'ansiedad',
        'Anger': 'ira',
        'Hostility': 'ira',
        'Frustration': 'ira',
        'Bitterness': 'ira',
        'Hate': 'ira',
        'Disgust': 'asco',
        'Repulsion': 'asco',
        'Revulsion': 'asco',
        'Negative': 'tristeza', 
        'Sadness': 'tristeza',
        'Grief': 'tristeza',
        'Despair': 'tristeza',
        'Heartbreak': 'tristeza',
        'Melancholy': 'tristeza',
        'Misery': 'tristeza',
        'Sorrow': 'tristeza',
        'Loneliness': 'tristeza',
        'Nostalgia': 'tristeza',
        'Emptiness': 'tristeza',
        'Isolation': 'tristeza',
        'Desolation': 'tristeza',
        'Disappointment': 'tristeza',
        'Regret': 'tristeza',
        'Remorse': 'tristeza',
        'Shame': 'asco',
        'Embarrassment': 'asco',
        'Humiliation': 'asco',
        'Jealousy': 'hostilidad',
        'Envy': 'hostilidad',
        'Resentment': 'hostilidad',
        'Dismissive': 'hostilidad',
        'Indifference': 'hostilidad',
        'Contempt': 'asco',
        'Boredom': 'asco',
        'Apathy': 'asco',
        'Numbness': 'asco',
        'Dismay': 'asco',
        'Dissatisfaction': 'asco',
        'Discontentment': 'asco',
        'Pessimism': 'asco',
        'Hopelessness': 'asco',
        'Desperation': 'tristeza',
        'Helplessness': 'tristeza',
        'Futility': 'tristeza',
        'Loneliness': 'tristeza',
        'Isolation': 'tristeza',
        'Amusement': 'felicidad',
        'Enjoyment': 'felicidad',
        'Admiration': 'amor',
        'Disappointed': 'tristeza',
        'Bitter': 'asco',
        'Confusion': 'asco',
        'Kind': 'amor',
        'Euphoria': 'felicidad',
        'Fulfillment': 'felicidad',
        'Reverence': 'amor',
        'Yearning': 'tristeza',
        'Fearful': 'miedo',
        'Apprehensive': 'miedo',
        'Overwhelmed': 'sorpresa',
        'Jealous': 'hostilidad',
        'Devastated': 'tristeza',
        'Frustrated': 'ira',
        'Envious': 'hostilidad',
        'Determination': 'tranquilidad',
        'Thrill': 'sorpresa',
        'Bittersweet': 'asco',
        'Overjoyed': 'felicidad',
        'Inspiration': 'felicidad',
        'Motivation': 'felicidad',
        'Contemplation': 'tranquilidad',
        'JoyfulReunion': 'felicidad',
        'Blessed': 'felicidad',
        'Reflection': 'tranquilidad',
        'Appreciation': 'tranquilidad',
        'Accomplishment': 'felicidad',
        'Wonderment': 'sorpresa',
        'Optimism': 'tranquilidad',
        'Intrigue': 'asco',
        'PlayfulJoy': 'felicidad',
        'Mindfulness': 'tranquilidad',
        'DreamChaser': 'felicidad',
        'Elegance': 'tranquilidad',
        'Whimsy': 'asco',
        'Pensive': 'asco',
        'Harmony': 'tranquilidad',
        'Creativity': 'felicidad',
        'Radiance': 'tranquilidad',
        'Rejuvenation': 'tranquilidad',
        'Coziness': 'tranquilidad',
        'Adventure': 'felicidad',
        'Melodic': 'felicidad',
        'FestiveJoy': 'felicidad',
        'InnerJourney': 'felicidad',
        'Freedom': 'felicidad',
        'Dazzle': 'felicidad',
        'Adrenaline': 'felicidad',
        'ArtisticBurst': 'felicidad',
        'CulinaryOdyssey': 'felicidad',
        'Resilience': 'felicidad',
        'Immersion': 'felicidad',
        'Spark': 'felicidad',
        'Marvel': 'felicidad',
        'Betrayal': 'asco',
        'Suffering': 'tristeza',
        'EmotionalStorm': 'tristeza',
        'LostLove': 'tristeza',
        'Exhaustion': 'asco',
        'Darkness': 'asco',
        'Ruins': 'asco',
        'Loss': 'tristeza',
        'Heartache': 'tristeza',
        'Solitude': 'tristeza',
        'Positivity': 'felicidad',
        'Kindness': 'amor',
        'Friendship': 'amor',
        'Success': 'felicidad',
        'Exploration': 'felicidad',
        'Captivation': 'felicidad',
        'Adventure': 'felicidad',
        'Grandeur': 'felicidad',
        'Energy': 'felicidad',
        'Celebration': 'felicidad',
        'Charm': 'felicidad',
        'Ecstasy': 'felicidad',
        'Colorful': 'felicidad',
        'Hypnotic': 'felicidad',
        'Connection': 'amor',
        'Iconic': 'felicidad',
        'Journey': 'felicidad',
        'Engagement': 'amor',
        'Touched': 'amor',
        'Suspense': 'sorpresa',
        'Triumph': 'felicidad',
        'Heartwarming': 'amor',
        'Obstacle': 'ira',
        'Sympathy': 'amor',
        'Pressure': 'ira',
        'Renewed Effort': 'felicidad',
        'Miscalculation': 'asco',
        'Challenge': 'ira',
        'Solace': 'tranquilidad',
        'Breakthrough': 'felicidad',
        'Harmony': 'tranquilidad',
        'Joy in Baking': 'felicidad',
        'Envisioning History': 'felicidad',
        'Imagination': 'felicidad',
        'Vibrancy': 'felicidad',
        'Mesmerizing': 'felicidad',
        'Cul': 'felicidad', 
        'Relief': 'tranquilidad',
        'Embarrassed': 'asco',
        'Mischievous': 'asco',
        'Sad': 'tristeza',
        'Bad': 'tristeza',
        'Intimidation': 'hostilidad',
        'Ambivalence': 'asco',
        'Zest': 'felicidad',
        'Proud': 'felicidad',
        'Empathetic': 'amor',
        'Compassionate': 'amor',
        'Playful': 'felicidad',
        'Free-spirited': 'felicidad',
        'Confident': 'tranquilidad',
        'Culinary Adventure': 'felicidad',
        'Winter Magic': 'felicidad',
        'Thrilling Journey': 'felicidad',
        "Nature's Beauty": 'felicidad',
        'Celestial Wonder': 'felicidad',
        'Creative Inspiration': 'felicidad',
        'Runway Creativity': 'felicidad',
        "Ocean's Freedom": 'felicidad',
        "Whispers of the Past": 'felicidad',
    }
    df['Estado'] = df[columna].str.strip().map(sentimientos_mapping)
# %%
clasificar_estados(df,'Sentiment')
df.head()
# %%
df.to_csv("ficheros/sentimentdataset.csv")
# %%
