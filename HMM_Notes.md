### Hidden Markov Models
Hidden Markov models are used to predict hidden states from observed data. Hidden states are so called hidden bacause they are not directly observable.
One such example is pollen counts or seasonal pollen index(SPI) is predicted from observable weather patterns.

Before getting into how the prediction happens, it is required to digest following assumptions.
- Markov assumption: States that probability of particular state depends only on the immediate previous state. This is also know as first order Markov Model.
That means in order to predict tomorrows weather, all we need to know is todays weather.
- Output dependence: Probability of an observation occuring at a state is entirely dependent only on the current state. That means probabilty of seasonal pollen index(SPI) having a certain value on a given day is only dependent on that particular(given day) day's weather.

Hidden Markov Model is represented by λ(A, B, π) where A, B and π are model parameters.

#### Hidden Markov Model Parameters : λ(A, B, π)
- A: Transition probabilities
- B: Emission probabilities
-  π: Initial distribution or initial state probabilities

##### Transition Probability (A)
As the name suggests, this is probability of transitioning from one state to another. Transition can happen between 2 different states or same state. For example if SPI can be [High , Low], and weather is categoriezed [Hot, Cold, Rainy]. Transition can happen High -> Low; Low -> High; High -> High and Low -> Low. This is usually represented by a matrix of size [N, N] where N is the number of possible states.

##### Emission probabilities (B)
This is the probabilty of an observation happening or occuring at a give state. Lets say weather is categoriezed [Hot, Cold, Rainy]. Emission probabiity tells us the probability of SPI = High on day with Weather = Hot. This is usually represented by a matrix of size [N, T] where N is number of states SPI can take and T is the number of observations.
