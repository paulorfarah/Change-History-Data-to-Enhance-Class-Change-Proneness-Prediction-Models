import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from stochastic.processes.discrete import BernoulliProcess


projects = ['commons-bcel-all-releases-raw', 'commons-io-all-releases-raw', 'junit4-all-releases-raw', 'pdfbox-all-releases-raw', 'wro4j-all-releases-raw']
for project in projects:
    df = pd.read_csv("../../datasets/" + project + ".csv", index_col=0)
    # print(df.head())
    # for col in df.columns:
    #     print(col)
    df = df[df['TOTAL_CHANGES'] > 0]
    res = df.pivot_table(index='class', columns='release', values='TOTAL_CHANGES')
    data = res.fillna(0)
    df1_transposed = data.T
    # data.plot.line(x='release', y='class')
    df_sum = np.cumsum(df1_transposed)

    # plot
    ax = df_sum.plot(xlabel='Release', ylabel='Changes', figsize=(15, 7), marker='.', xticks=data.columns.tolist(), logy=True)
    ax.legend(title='Sample', bbox_to_anchor=(1, 1.02), loc='upper left')
    # # getting data of the histogram
    # count, bins_count = np.histogram(data, bins=10)
    #
    # # finding the PDF of the histogram using count values
    # pdf = count / sum(count)
    #
    # # using numpy np.cumsum to calculate the CDF
    # # We can also find using the PDF values by looping and adding
    # cdf = np.cumsum(pdf)
    #
    # # plotting PDF and CDF
    # plt.plot(bins_count[1:], pdf, color="red", label="PDF")
    # plt.plot(bins_count[1:], cdf, label="CDF")
    # plt.legend()
    # plt.show()
    plt.savefig('results/change/'+project + '.pdf')