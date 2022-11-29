import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("Datos/depositsFromTop(video).csv", index_col="date")

# using the bar_chart_race package
bcr.bar_chart_race(
    # must be a DataFrame where each row represents a single period of time.
    df=df,
    #df=df[:5],

    # name of the video file
    filename="depositsFrom.mp4",

    # specify location of image folder
    #img_label_folder="bar_image_labels",

    # change the Figure properties
    fig_kwargs={
        'figsize': (26, 15),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },

    # orientation of the bar: h or v
    orientation="h",

    # sort the bar for each period
    sort="desc",

    # number of bars to display in each frame
    n_bars=10,

    # to fix the maximum value of the axis
    #fixed_max=True,

    # smoothness of the animation
    steps_per_period=45,

    # time period in ms for each row
    period_length=1500,

    # custom set of colors
    colors=[
        '#6ECBCE', '#FF2243', '#FFC33D', '#CE9673', '#FFA0FF', '#6501E5', '#F79522', '#699AF8', '#34718E', '#00DBCD',
        '#00A3FF', '#F8A737', '#56BD5B', '#D40CE5', '#6936F9', '#FF317B', '#0000F3', '#FFA0A0', '#31FF83', '#0556F3'
    ],

    # title and its styles
    # Top 10 Smart Contracts que depositaron a Tornado Cash (Acumulado)
    title={'label': 'Top 10 Smart Contracts que depositaron',
           'size': 52,
           'weight': 'bold',
           'pad': 40, 
           'family': 'Nunito'
           },

    # adjust the position and style of the period label
    period_label={'x': .95, 'y': .15,
                  'ha': 'right',
                  'va': 'center',
                  'size': 65,
                  'weight': 'semibold', 
                  'family': 'Nunito'
                  },

    # style the bar label text
    bar_label_font={'size': 27},

    # style the labels in x and y axis
    tick_label_font={'size': 27},

    # adjust the style of bar
    # alpha is opacity of bar
    # ls - width of edge
    bar_kwargs={'alpha': .99, 'lw': 0},

    # Text to show the total ammount of ehter among all contracts 
    period_summary_func=lambda v, r: {'x': .95, 'y': .20,
                                      's': f'Ether total: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 65, 'family': 'Nunito'},

    tick_image_mode='fixed'


)