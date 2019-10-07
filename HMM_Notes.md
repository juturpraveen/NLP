### Hidden Markov Models
Hidden Markov models are used to predict hidden states from observed data. Hidden states are so called hidden bacause they are not directly observable.
One such example is pollen counts or seasonal pollen index(SPI) is predicted from observable weather patterns.

Before getting into how the prediction happens, it is required to digest following assumptions.
- Markov assumption: States that probability of particular state depends only on the immediate previous state. This is also know as first order Markov Model.
That means in order to predict tomorrows weather, all we need to know is todays weather.
- Output dependence: Probability of an observation occuring at a state is entirely dependent only on the current state. That means probabilty of seasonal pollen
index having a certain value on a given day is only dependent on that particular(give day) day's weather.

Hidden Markov Model is represented by λ(A, B, π) where A, B and π are model parameters.

#### Hidden Markov Model Parameters : λ(A, B, π)
- A: Transition probabilities
- B: Emission probabilities
-  π: Initial distribution or initial state probabilities
