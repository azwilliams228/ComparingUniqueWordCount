from numpy import *
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib.gridspec as gridspec
def BookReview(a,b):
        fig = plt.figure(figsize = (10,10))
        global ax1
        global ax2
        global ax3
        gs = gridspec.GridSpec(3, 2)
        ax1 = plt.subplot(gs[0,0])
        ax2 = plt.subplot(gs[0,1])
        ax3 = plt.subplot(gs[-2:,:])
        
        OpenBook(a)
        OpenBook(b)
def OpenBook(a):
    with open(a,encoding = 'utf8') as f1:
        s1 = f1.read()
    print('The Number of characters in',a, 'is',len(s1))
    s1 = s1.lower()                              # convert any uppercase to lower case
    for c in punc:
        s1 = s1.replace(c,'')                    # remove any punctuation from our book
    words1 = s1.split()
    print('The number of words in',a,'is',len(words1))
    wc1 = {}                                    # Empty dictionary
    for word in words1:
        if word not in wc1: wc1[word] = 0
        wc1[word] +=1
    wcl1 = list(wc1.items())
    sorted(wcl1);
    wcl1 = sorted(wcl1,key = lambda x:x[1],reverse = True)              # lambda construct for defining a function inline
    rank1 = arange(len(wcl1))+1
    freqs1 = [item[1] for item in wcl1]
    
    gs = gridspec.GridSpec(3, 2)
    ax1.title.set_text('Plot 1,Rank of Frequency vs Frequency ')
    ax2.title.set_text('Plot 2, SemiLog Y plot, Rank of Frequency vs Frequency')
    ax3.title.set_text('plot3, Log10 (Rank of Frequency) vs log10 (Frequency)')
    ax1.plot(rank1,freqs1)
    ax2.semilogy(rank1,freqs1)
    
    ax3.plot(log10(rank1),log10(freqs1),'c')
    
    x1 = log10(rank1)[10:2000]
    y1 = log10(freqs1)[10:2000]
    alpha1,beta1 = bestfitesquared2(x1,y1)
    ax3.plot(x1,alpha1*x1+beta1,'r');
    
    print('The slope of the best fit line of',a,'is',alpha1)
    print()
def bestfitesquared2(x,y):
    xbar = x.mean()
    ybar = mean(y)
    xybar = (x*y).mean()
    x2bar = (x*x).mean()
    if (x2bar-xbar**2) != 0:
        alpha = (xybar-xbar*ybar)/(x2bar-xbar**2)
        beta = ybar - xbar*alpha
        return alpha, beta
punc = ',.:;?!()[]"\'_*#'
BookReview('AmorDeSalvacao.txt','MobyDick.txt')
BookReview('HuckleberryFinn.txt','TomSawyer.txt')
