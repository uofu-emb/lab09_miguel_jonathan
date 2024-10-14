**General**

 - The system will always have power during operation.
 - Trains on each side run only in one direction.

**Signals**

 - Signals are given correctly when trains pass the sensors, and only then.
 - Each depart signal should be preceeded by the appropriate approach signal, and vice-versa.
 - The appropriate depart signal will be given before receiving another approach signal for the same side of the track.
 - The approach signal will be given at least 10 seconds before the train reaches the crossing.

**Alarm**

 - An elapsed signal will be received 10 seconds after the timer is reset.
 - Only one elapsed signal will be received if the timer is reset before receiving the signal.
 - An elapsed signal will be received only when the timer is reset, and only once per reset.
 - The alarm will be on when trains are present.
 - The alarm will remain on while barriers are being raised.

**Barriers**

 - Barriers should always be down when trains are present, and up otherwise.

**Counter-example Sequence**

 - Start idle
 - Receive nb_approach
 - Receive elapsed
 - Receive nb_depart
 - Receive sb_approach
 - Receive elapsed

Results in idle state (barrier up) with a train coming