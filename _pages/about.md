---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a PhD Student in the [PCOG](https://pcog.uni.lu/) group at the University of Luxembourg. My current research interests are Multi-Objective Optimization, Reinforcement Learning, and Swarm Applications. I am currently working on the ([ADARS](https://adars.uni.lu/)) project, under the supervision of [Grégoire Danoy](https://danoy.gforge.uni.lu/). Because I believe in open source AI, I'm also contributing to the [Farama Foundation](https://farama.org/), a non-profit organization aiming at facilitating the development of open-source tools for Reinforcement Learning.

I am convinced that specifying AI problems as single-objective is often not enough since we often make compromises in real-life situations. Thus, I dedicate a substantial part of my time researching on Multi-Objective Reinforcement Learning (MORL). 


<img src="../images/mo_cheetah_rect.gif" width=500>

<em>The consequences of learning multiple behaviours, based on different trade-offs between the objectives.</em>



Before my PhD, I specialized into combinatorial optimization techniques such as constraint programming, local search, meta-heuristics algorithms. I worked a few years in the industry on supply chain optimization, planning problems, and have been exposed to various software engineering challenges. 

Aside from the cool things mentionned above, I am into cinema, cycling, and beers (yes, I am Belgian).

<img src="../images/epuck.jpeg" width=300>  <img src="../images/circle.gif" width=350>

<em>Left: the Epuck robots, some of our toys in ADARS. Right: the Crazyflie robots in action.</em>



<h1> Open source </h1>

<div>
<h2> A toolkit for reliable research in MORL </h2>
We wrote a few repositories aiming at helping researchers in reproducing results of existing MORL algorithms as well as facilitating the whole research process by providing clean implementations and examples. By making this public, our hope is to attract even more people to the MORL field and remove boilerplate from the research process.  A paper describing the whole toolkit has been published at <a href=="https://openreview.net/forum?id=jfwRLudQyj">NeurIPS23</a>.
</div>

<div>
<h3> MO-Gymnasium </h3>
<p>
<img src="../images/MO-Gymnasium.svg" width=150 style="float:left; padding:10px" >
<a href="https://github.com/Farama-Foundation/MO-Gymnasium">MO-Gymnasium</a> is a library containing multiple multi-objective RL environments. These environments are all under a standardized API, allowing to test your algorithms on multiple benchmarks without the need to change your code. Since 2023, MO-Gymnasium has been integrated in the <a href="https://farama.org">Farama foundation</a> suite, aside to other RL projects such as <a href="https://github.com/Farama-Foundation/Gymnasium">Gymnasium</a> and <a href= "https://github.com/Farama-Foundation/PettingZoo">PettingZoo</a>.
</p>
</div>

<div>
<h3> MORL-baselines </h3>
<p>
<img src="../images/mo_cheetah_rect.gif" width=300 style="float:left; padding:10px">

<a href="https://github.com/LucasAlegre/morl-baselines">MORL-Baselines</a> is a repository containing multiple MORL algorithms using MO-Gymnasium. We aim to provide clean, reliable and validated implementations as well as tools to help in the development of such algorithms. Features include automated experiments tracking for reproducibility, hyper-parameter optimization, multi-objective metrics, and more.
</p>
</div>

<div>
<h3> Open RL Benchmark </h3>
<p>
<img src="../images/openrlbenchmark.png" width=300 style="float:left; padding:10px">
<a href="https://github.com/openrlbenchmark/openrlbenchmark">OpenRLBenchmark</a> is a comprehensive collection of tracked experiments for RL. It aims to make it easier for RL practitioners to pull and compare all kinds of metrics from reputable RL libraries like Stable-baselines3, Tianshou, CleanRL, and MORL-Baselines of course 😎.
</p>
</div>


<div>
<h2> CrazyRL </h2>
<p>
<img src="../images/circle.gif" width=300 style="float:left; padding:10px">
<a href="https://github.com/ffelten/CrazyRL">CrazyRL</a> is a MOMARL library under a multi-objective extension of the  <a href= "https://github.com/Farama-Foundation/PettingZoo">PettingZoo</a> API. It allows to learn swarm behaviours in a variety of environments, such as the one shown on the left. We also implemented the full MOMARL loop on GPU using Jax, allowing to train agents 2000x faster than when the environment runs on the CPU.
</p>
</div>



