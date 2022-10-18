---
title: 'The limits of the Central Limit (theorem)'
date: 2022-10-15
permalink: /posts/limit-central-limit/
tags:
  - Statistics
  - Life
---

Here is a nerdy shower thought, this one is certainly going to be a bit boring for the commoners, sorry mates!

Anyways, let's go to it. In this one, I am going to talk about some limits you might encounter (or not notice) when you apply Gaussian distribution to quantify, say a risk or an uncertainty.

The usage of the Gaussian distribution is largely motivated by the Central Limit Theorem, which basically says that if you take enough samples in the real world, you will end up with a curve looking like a bell. For example, say I want to estimate the height of people entering a room, I start by measuring people as they enter, and update my model everytime. The process would look like the following gif.

![People height Gaussian](../people_height.gif)

In this graph, the x-axis is the height (cms) of people and y-axis represents the number of people with that height in what I sampled. As you can see, the more I collect height from people, the more the curve looks a bell. But what is all the fuss about this bell? Well, it turns out that once you get to this familiar shape, you can predict the height of the next person with *some kind of confidence*. For example, after sampling thousands of people, I can say with 95% confidence that the next person's height is going to be between 155 and 194 cms, which seems pretty logical, isn't it? 

Well, now if we do the same experimentation but collect people's monthly income (oddly enough, I always get more attention from people when talking about money). After sampling a few thousands people, I see the mighty bell shape coming back:

![People income](../people_salary_normal.png)

Now, I can make the same kind of prediction as for their height; with 95% confidence, I can say that the next person's salary is going to be between 1450 and 2800. I can use this process pretty much everywhere thanks to the Theorem (some people even say if you have more than 30 samples you're good to go), brilliant!

Well it turns out that if you start doing that, and **making people believe you can put actual numbers on the uncertainty of everything you want to predict, you are going to be burned hard**. 

Imagine the next person coming to the room, his name is Swarren Blackett... and this guy makes 10 MILLIONS per months. Well, this is far off the Gaussian distribution we have been constructing. But we said 95% confidence, not 100%, didn't we? Yes, we did but anyways, **the problem here is the magnitude of the difference between the average salary you have been sampling and this guy's salary**. Imagine the error you make when predicting the next dude has a salary of 2200... If an unexpected event like this happens, it might ruin everything you have build until then. This is called a Black Swan by [Nassim Taleb](https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb), a brilliant dude.

Now a lot of people (me included until I read Taleb's book) use and believe in these confidence intervals and uncertainty measures every day (from medicine to finance). For example, predicting with 95% that a large bank is not going bankrupt :-). People blindly relying on Gaussian measures are not protected from losing everything, even if they believe they do (well, technically in finance it is not even their money).

To summarize, here are the problems:
We use Gaussian distributions to quantify uncertainty in a lot of cases because it is familiar and easy to manipulate;
* 1st problem: Not all kinds of data fit a Gaussian model;
* 2nd problem: When you think you quantify the uncertainty, you actually quantify how much the data you **have seen varies**. Not how much **all the data can vary**. There is a difference between *seen uncertainty* and *unseen uncertainty*, and the problem is that with Gaussian distribution, we only quantify the former, while the latter might have big consequences. 

So what can we do? 
- Question yourself if a Gaussian fits, and do not trust too much. 
- There are also other distribution models, so called power-law that could fit better some kind of data. 

I am no expert in statistics, thus I am going to stop here before I give wrong information. 
