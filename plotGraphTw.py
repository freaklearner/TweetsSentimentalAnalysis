import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotGraph(positive,negative,neutral):
    # data to plot
    n_groups = 3
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, positive, bar_width,
                     alpha=opacity,
                     color='b',
                     label='positive')

    rects2 = plt.bar(index + bar_width, negative, bar_width,
                     alpha=opacity,
                     color='g',
                     label='negative')

    rects3 = plt.bar(index + bar_width+ bar_width, neutral, bar_width,
                     alpha=opacity,
                     color='r',
                     label='neutral')


    plt.xlabel('Persons')
    plt.ylabel('Sentiments')
    plt.title('Twitter sentiment analysis')
    plt.xticks(index + bar_width, ('Donald Trump', 'Narendra Modi', 'Rahul Gandhi'))
    plt.legend()
    plt.tight_layout()
    plt.show()
