---
layout: advent-item
title: 5th Advent - Pandas Merge As Of
date: 2018-11-30
advent: 5
description: Programm with Jupyter cell style in VS Code  # Add post description (optional)
img: vs_code.png # Add image post (optional)
tags: [Blog, Advent, Data]
author: # Add name author (optional)
---
If you started with Jupyter Notebook, going back to normal Python coding you might miss the itterative cell coding style. Luckily there is an amazing add-on for Visual Studio Code.


So how do you run a cell?
A cell is defined as follows.

{% highlight python %}
#%%
hello_word = "My first cell"
hello_world

#%%
hello_word = "It works"
hello_world
{% endhighlight %}

[Great blog post about it][vs-code-cell]
[Full documentation][doc]


[doc]:https://code.visualstudio.com/docs/python/editing
[vs-code-cell]:https://donjayamanne.github.io/pythonVSCodeDocs/docs/jupyter_getting-started/