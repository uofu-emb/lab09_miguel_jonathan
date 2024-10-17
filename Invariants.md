**Invariants**

16. The system will always have power during operation.
17. Trains on each side run only in one direction.
18. Signals are given correctly when trains pass the sensors, and only then.
19. Each depart signal should be preceeded by the appropriate approach signal, and vice-versa.
20. The appropriate depart signal will be given before receiving another approach signal for the same side of the track.
21. The approach signal will be given at least 10 seconds before the train reaches the crossing.
22. An elapsed signal will be received 10 seconds after the timer is reset.
23. Only one elapsed signal will be received if the timer is reset before receiving the signal.
24. An elapsed signal will be received only when the timer is reset, and only once per reset.
25. The alarm will be on when trains are present.
26. The alarm will remain on while barriers are being raised.
27. Barriers should always be down when trains are present, and up otherwise.

**Counter-example Sequence (Example FSM)**

1. Start idle
1. Receive nb_approach
1. Receive elapsed
1. Receive nb_depart
1. Receive sb_approach
1. Receive elapsed

Results in idle state (barrier up) with a train coming