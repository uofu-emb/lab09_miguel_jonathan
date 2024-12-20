# Formal Verification
In this lab, we'll get an introduction to the concept of system modeling and formal verification.

# Learning objectives
1. Model systems with finite state machines (FSM).
1. Describe invariant properties of a system.
1. Evaluate correctness of a model.
1. Understand limitations and benefits of model checking.

# Prelab
## First session.
1. Read sections 3.1-3.3 and 3.6 in Lee & Seshia.
1. Read section 14.1 and 14.2 in Lee & Seshia
1. Draw a finite state machine for the train crossing problem given below. You should have a complete diagram **ready for class**.

* Do not create an extended state machine, we want to restrict our analysis to an exclusively finite system.
* Don't use a semaphore, encode multiple train interactions as distinct states.
* There are many styles of drawing FSMs, try to follow the style presented in Lee & Seshia.
* You will want to make your FSM reactive to events, and avoid output side effects.
* Capture as much of the problem into states as possible.

If you would like to draw your FSM on the computer, Graphviz is a great tool for making graphs.
All drawings provided were done with Graphviz and the source files are in the repository.
To render a graph just run `dot mygraph.dot -Tpdf -o mygraph.pdf`

### Railrod crossing problem
Implement a FSM for a safety warning system to prevent crossings while a train is approaching and until it has passed.

* There are two tracks, one going north and the other south. Trains on each track only run in one direction.
* The tracks meet at a crossing.
* Each track has two proximity sensors __approach__ and __depart__, placed on the tracks before and after the crossing respectively.
    * The two __approach__ sensors emit the events **northbound_approach** and **southbound_approach** when the first car of the train crosses the sensor (leading edge).
    * The two __depart__ sensors emit the events **northbound_depart** and **southbound_depart** when the last car of the train crosses the sensor (trailing edge).
* The system has an audible alarm, which can be in the state __on__ or __off__, and a barrier that is in either __lowered__ or __raised__ state to block the crossing.
* A timer emits an event **elasped** 10 seconds after the alarm starts ringing.
* When a train is approaching:
    1. The alarm begins clanging.
    1. After 10 seconds, the barrier lowers.
    1. The alarm continues to sound and the barrier remains lowered while a train is present.
    1. When no train is present the barrier raises.
    1. After 10 seconds the alarm stops.


## Second session.
1. Read section 15 in Lee & Seshia

# Lab
We will be mostly writing documentation for a system in this lab.
Provide all your documentation as Markdown document(s) saved in a repository.
Upload PDFs or pictures of any diagrams.
Remember to commit your work regularly.

## Invariants
1. With your partner, write down a set of invariants your system should have, with a specific emphasis on safety invariants.
1. You should be able to identify specific invariant conditions, that if violated, represent a unsafe condition or safety hazard.
1. Also consider invariants that are assumptions made about the environment or the scenario.
1. Write your invariants in the form a logical predicate, i.e. a statement that must be true.

Example invariants:
* "An approach signal will always precede a depart signal"
* "The power will never be interrupted"
* "Trains on each track only run in one direction."
## Varying invariants
Answer the question: does there exist a sequence of events, such that an invariant is not longer true?

1. Evaluate the [example FSM](example.pdf).
1. Find a counter-example sequence that makes an invariant false. Write it down.

Proving that a system violates an invariant is simple - just provide a counter example.
Proving the opposite is incredibly difficult. You must either exhaustively demonstrate all possible inputs, or otherwise mathematically prove the invariants.

You may recall when I graded this question on the final last semester that I graded the exam using exactly this method.
I started at the beginning, and provided a series of events I knew tended to break models.
Once the machine was in an unsafe state, it was marked "safety hazard".
If I failed to find a violation, it was marked "probably safe".
Note the "probably"! Just because I could not find a counter example does not prove anything.
Some models got marked "technically safe", because any possible sequence immediately got the model stuck with the arms down.
Not very useful, but did not create a safety hazard!

## Check your work
1. Exchange the FSM you drew for the prelab with your partner.
1. Attempt to find a counter-example for your partner's FSM.
1. If you do find a counter-example, work with your partner to fix the FSM for that counter-example.

## Prove it.
How would you go about proving that your model is correct?

1. Fill in this table (you can copy the markdown into your docs).
1. The first four variables are booleans, you should have 16 possible states.
1. Start a numbered list of invariants, starting with 16. Add invariants as needed.
1. For each row, mark "safety_hazard" with the number of the invariant it violates or leave it blank.
1. For each row, write down the number of the state your system will transition to on that event.
   1. If an event violates an invariant (e.g. event not allowed in that state), write down the number of the invariant.
   1. If an event has no effect, you can stay in the same state.

| number | arms_down | alarm_on | northbound_present | southbound_present | north_approach | south_approach | north_depart | south_depart | elapsed | safety_hazard |
|--------|-----------|----------|--------------------|--------------------|----------------|----------------|--------------|--------------|---------|---------------|
| 0      | 0         | 0        | 0                  | 0                  | 6              | 5              | 19           | 19           | 24      |               |
| 1      | 0         | 0        | 0                  | 1                  | 7              | 5              | 5            | 0            | 13      | 25            |
| 2      | 0         | 0        | 1                  | 0                  | 6              | 7              | 0            | 6            | 14      | 25            |
| 3      | 0         | 0        | 1                  | 1                  | 7              | 7              | 5            | 6            | 15      | 25            |
| 4      | 0         | 1        | 0                  | 0                  | 6              | 5              | 19           | 19           | 0       |               |
| 5      | 0         | 1        | 0                  | 1                  | 7              | 20             | 27           | 27           | 13      |               |
| 6      | 0         | 1        | 1                  | 0                  | 20             | 7              | 27           | 27           | 14      |               |
| 7      | 0         | 1        | 1                  | 1                  | 20             | 20             | 27           | 27           | 15      |               |
| 8      | 1         | 0        | 0                  | 0                  | 14             | 13             | 0            | 0            | 0       | 27            |
| 9      | 1         | 0        | 0                  | 1                  | 15             | 13             | 13           | 0            | 13      | 25            |
| 10     | 1         | 0        | 1                  | 0                  | 14             | 15             | 0            | 14           | 14      | 25            |
| 11     | 1         | 0        | 1                  | 1                  | 15             | 15             | 13           | 14           | 15      | 25            |
| 12     | 1         | 1        | 0                  | 0                  | 14             | 13             | 4            | 4            | 4       | 27            |
| 13     | 1         | 1        | 0                  | 1                  | 15             | 20             | 19           | 4            | 24      |               |
| 14     | 1         | 1        | 1                  | 0                  | 20             | 15             | 4            | 19           | 24      |               |
| 15     | 1         | 1        | 1                  | 1                  | 20             | 20             | 13           | 14           | 24      |               |

**Invariants**

16. The system will always have power during operation.
1. Trains on each side run only in one direction.
1. Signals are given correctly when trains pass the sensors, and only then.
1. Each depart signal should be preceeded by the appropriate approach signal, and vice-versa.
1. The appropriate depart signal will be given before receiving another approach signal for the same side of the track.
1. The approach signal will be given at least 10 seconds before the train reaches the crossing.
1. An elapsed signal will be received 10 seconds after the timer is reset.
1. Only one elapsed signal will be received if the timer is reset before receiving the signal.
1. An elapsed signal will be received only when the timer is reset, and only once per reset.
1. The alarm will be on when trains are present.
1. The alarm will remain on while barriers are being raised.
1. Barriers should always be down when trains are present, and up otherwise.

## Specification vs. implementation
1. Start drawing an FSM using the table you just made.
1. Label each FSM state with the number in the table.
    1. Some FSM states may have multiple table numbers.
1. If an event violates an invariant that represents an impossible event or operating assumption, leave it off your machine.
    1. It's important to account for behavior that could occur outside your expectations, but we need to maintain a level of abstraction. Getting struck by lightning is possible, but not something you plan for.

Is your new FSM equivalent to the FSMs from the previously steps?
# Model checking
In the lab, we tried several techniques by hand to verify a system model.
Even for a simple machine, the number of possible states grows exponentially.
This is called "state space explosion", and is the primary difficulty when checking models.
There are a wide variety of computer programs called "model checkers" that provide automation for searching state space.
You can also encode your model into a format that can be used with a tool like a SAT solver, which will prove the model is correct.
We started down that path with the state table, encoding each state into a binary number.
Often we will have a specification model, and the goal is to show equivalence with our implementation.

# Next steps
This lab is designed to give a taste for the topic of formal methods.
If you want more, there a courses offered that go into detail.

Priyank Kalla teaches a course on verification focusing on hardware logic.
ECE6715 Verification of Digital Circuits (Fall)

Ben Greenman teachs a course on formal verification of software.
CS6110 Software Verification (Spring)

Both classes are highly recommended.

# Reference implementation
No reference implementation is provided for this lab.
