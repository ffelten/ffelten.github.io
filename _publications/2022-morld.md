---
title: "MORL/D: Multi-Objective Reinforcement Learning based on Decomposition"
collection: publications
permalink: /publication/2022-07-MORLD
excerpt: 'Applying decomposition techniques from MOO to MORL.'
date: 2022-07-01
venue: 'International Conference in Optimization and Learning (OLA2022)'
paperurl: 'https://ola2022.sciencesconf.org/data/pages/Proceedings_1.pdf'
citation: 'F. Felten, E.-G. Talbi, and G. Danoy, (2022). MORL/D: Multi-Objective Reinforcement Learning based on Decomposition. In Proceedings of International Conference on Optimization and Learning (OLA2022)'
---
Many real life problems involve multiple objectives. The established way to resolve these is called
Multi-Objective Optimization (MOO). This field has been extensively studied for over 50 years,
producing a wide variety of optimisation approaches. These rely on a set of concepts such as Pareto
dominance, indicators or scalarisation. Yet most of these approaches require a complete knowledge
of the environment dynamics.
Reinforcement Learning (RL) is a machine learning technique which aims at training an agent
to behave optimally in some possibly unknown environment. Its extension to environments
containing multiple objectives is called Multi-Objective Reinforcement Learning (MORL). One
of the existing approaches to solve MORL problems, called outer loop multi-policy MORL, aims
at learning various optimal compromises between objectives. Its strategy is to decompose the
problem into various subproblems by using different scalarisation functions. These algorithms then
apply standard RL on the scalarised subproblems as to target various optimal policies. Other
MORL approaches have been published lately; nevertheless, this field remains understudied when
compared to MOO or RL.
At the same time, MOEA/D, a framework allowing to use the decomposition technique in
Evolutionary Algorithms (EAs) has been introduced in the MOO literature. Similar to outer loop
MORL, this framework converts the multi-objective problem into various single-objective problems
(SOPs) by using various scalarisations. 
Although outer loop algorithms have a similar structure to MOEA/D, to the best of our knowledge no work has clearly identified those similarities yet. This
paper presents an initial attempt to design an outer loop MORL framework which could easily be
extended in order to ease the transfer of MOEA/D variants’ concepts into MORL.

[Download paper here](https://ola2022.sciencesconf.org/data/pages/Proceedings_1.pdf)