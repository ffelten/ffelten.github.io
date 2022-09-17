---
title: 'The limit of the Central Limit (theorem)'
date: 2022-10-14
permalink: /posts/2022/10/limit-central-limit/
tags:
  - Statistics
  - Life
---

Normal distribution to quantify uncertainty.
First example is height of people: take 100 people, take their size, plot bell shaped curve, mean, 95% CI, ...
With 95% confidence, you can say that the height of a person will be between 1.55 and 1.95 meters (only non-retarded units in this blog).

Now, if we interest ourselves into money (oddly enough, I always get more attention from people when talking about money). Let us do the same exercise: 100 people, I get a distribution, CI, blablabla. You can see that this bell-shape pattern is repeated. That is called a Normal distribution (because it happens normally?), or a Gaussian. This kind of model is used pretty much everywhere btw: finance, energy, medical, ... Why do we use it evertywhere? Well because we *think* we can: Central limit theorem.

So what we usually do in this kind of business is that we make prediction with error confidence. For example, I can predict that you have a salary between 500 and 4000€ with 90% confidence. 

Now let's say I'm running this kind of prediction system in real life, with data that I acquire on the go. I can update my model as new data comes in... Welcome to machine learning 8-). 

But here is this guy: Swarren Buffet. And he earns 50M per month. Now my average is completely off, and my model too (plot mean being on the right of the bell curve). What happened? I was so confident that I could predict the salary of every possible person... This kind of event is called a Black Swan (from the book by Nassim). 

What does this mean? 
Well, very often, these Gaussian models are used without checking that the thing we want to estimate actually follow this rule. Hence, we have unexpected events, which completely blow our predictions even if we got pretty confident on those. This my friend, is the fallacy of using statistics without checking, and a lot of people out there are doing it. Yes, they trick you. 

Headings are cool
======

You can have many headings
======

Aren't headings cool?
------