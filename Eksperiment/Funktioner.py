# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:37:12 2014

@author: cywer
"""

from sympy import latex as latex
#import sympy as sym
#sym.latex
#import sympy.latex as latex
#Clean print Latex


SPINE_COLOR = 'gray'
def latexify(fig_width=None, fig_height=None, columns=1):
    import matplotlib
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = 0.6180339887498949#(sqrt(5)-1.0)/2.0# Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height + 
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    params = {'backend': 'ps',
              'text.latex.preamble': ['\usepackage{gensymb}'],
              'axes.labelsize': 8, # fontsize for x and y labels (was 10)
              'axes.titlesize': 8,
              'text.fontsize': 8, # was 10
              'legend.fontsize': 8, # was 10
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)


def format_axes(ax):

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

    return ax
    
#==============================================================================
# 
#==============================================================================

def prik(s):
    s=latex(s)
    s1 = ''
    d=0
    i=0
    while d!=i-1:
#    for k in range(10):
#        d = i+s[i:].find(r'\frac{d}{d t}')
        d = i+s[i:].find(r'\frac{d')
        if d!=i-1:
            if s[d:d+13]==r'\frac{d}{d t}':
                d1= d+s[d:].find(r'{\left (t \right )}')
                s1 += s[i:d]+r'\dot{'+s[d+14:d1]+'}'
                i = d1
            if s[d:d+9]+s[d+10:d+18]+s[d+19:d+21]==r'\frac{d^{}}{d t^{}}':
                d2=int(s[d+9])
                d1= d+s[d:].find(r'{\left (t \right )}')
                s1 += s[i:d]+r'\%sot{' %('d'*d2) +s[d+21:d1]+'}'
                i = d1   
    try :   s1 += s[d1:]
    except: s1 += s
    
    if True:
        d1=0
        while d1!=-1:
#        for k in range(100):        
            d1= s1.find(r'{\left (t \right )}')
            if d1==-1:break
            s1 = s1[:d1]+s1[d1+19:]

    d4=0
    while d4!=-1:    
        d4= s1.find(r'\_')
        if d4==-1:break
        s1 = s1[:d4]+s1[d4+1:]

#    print r'%%latex'
#    print r'\begin{aligned}'
#    print s1
#    print r'\end{aligned}'
    return s1

def cprint(s): #Clean print Latex
    c=prik(s)
    return Math(c)


def stat(s):
    s=str(s)
    r = [['Derivative(theta(t), t)','state[1]'],['theta(t)','state[0]'] \
        ,['Derivative(k_x(t), t)','state[3]'],['k_x(t)','state[2]'] \
        ,['Derivative(l(t), t)','state[5]'],['l(t)','state[4]'] \
        ,['f(t)','f(t, state)'],['q(t)','q(t, state)'],['Abs','abs'] \
        ,['signfunc','copysign(1,state[3])']\
        ,['Q_0','Q[0]'],['Q_1','Q[1]'],['Q_2','Q[2]']\
        ]
    for i in r:
        d=0
        while d!=-1:    
            d= s.find(i[0])
            if d==-1:break
            s = s[:d]+i[1]+s[d+len(i[0]):]
    #print s
    return s
    
#def stat(s):
#    s=str(s)
#    r = [["theta'",'state[1]'],["theta(t)",'state[0]'] \
#        ,["k_x'",'state[3]'],['k_x(t)','state[2]'] \
#        ,["l'",'state[5]'],['l(t)','state[4]'] \
#        ,['f(t)','f(t, state)'],['q(t)','q(t, state)'],['Abs','abs'] \
#        ,['Q_0','Q[0]'],['Q_1','Q[1]'],['Q_2','Q[2]']\
#        ]
#    for i in r:
#        d=0
#        while d!=-1:    
#            d= s.find(i[0])
#            if d==-1:break
#            s = s[:d]+i[1]+s[d+len(i[0]):]
#    #print s
#    return s