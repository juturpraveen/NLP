### Hidden Markov Models
Hidden Markov models are used to predict hidden states from observed data. Hidden states are so called hidden bacause they are not directly observable.
One such example is to predict weather by looking at household power usage. Here weather is hidden state while unit of power usage are give observations.

Before getting into how the prediction happens, it is required to digest following assumptions.
- Markov assumption: States that probability of particular state depends only on the immediate previous state. This is also know as first order Markov Model.
That means in order to predict tomorrows weather, all we need to know is todays weather.
- Output dependence: Probability of an observation occuring at a state is entirely dependent only on the current state. That means probabilty of n number of power units being used on a given day is only dependent on that particular(given day) day's weather.

Hidden Markov Model is represented as λ(A, B, ∏) where A, B and π are model parameters.

#### Hidden Markov Model Parameters : 
- A: Transition probabilities
- B: Emission probabilities
-  ∏: Initial distribution or initial state probabilities

##### Transition Probability (A)
As the name suggests, this is probability of transitioning from one state to another. Transition can happen between 2 different states or same state. For example if weather can have states [Hot , Normal, Cold]. Transition can happen Hot -> Cold; Normal -> Hot; Cold -> Hot and such. This is usually represented by a matrix of size [N, N] where N is the number of possible states.

Example: P(Tomorrow’s weather = Hot | Today’s weather = Normal)

##### Emission probabilities (B)
This is the probabilty of an observation happening or occuring at a give state. Lets say power usage could be [High, Low]. Emission probabiity tells us the probability of power usage = High on day with Weather = Hot. This is usually represented by a matrix of size [N, T] where N is number of states weather can take and T is the number of observations of power usage.

Example: P(Power usage = High | Weather = Hot)

##### Initial distribution or Initial state probabilities (∏)
The probability that Markov chain will start in certain state. Since we have 2 possible states, initial probabilities can be

∏ = [ ½, ½ ]
