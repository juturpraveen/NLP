- Word meaning - The idea represented by the word
- Synonyms: similary meanining
- Hypernym: hierarchy of word
- Traditional NLP is up untill 2012. After 2012 neural networks started in NLP.
- Orthogonal vectors: Vectors that do not have any kind of similarity.
- Trying to find similar words using a word's list (like word net) or some sort of dictionary is not practical. Hence
we need to look at different way(s) such that representation of the word itself gives the idea or amount of similarity.
- Instead of using lists or dictionaries, learn the word meaning by the context of it. Context is the set of words that appear nearby.
- Using the contexts, a dense vector is built to represent word. These word vectors are also called 'Word embeddings' or
'Word representations'.
- In these vectors each index is considered as one dimension. If a word is represented as a vector of 100 indices like 
word =[v1, v2, v3......v100]. 

#### Word2vec
- Word2vec is a way of learning word vectors.
- Corpus: Body of text like news paper article, a book and such.
- Vocabulary: List of words in the corpus. Each word is represented as a vector.
- For each word 'c' at position 't' that has context of 'o' words, calculate the probability of 'o' given 'c'. This way words that 
have similar contexts are considered to have similar meanings.
- In practice every word is represented as 2 vectors. One vector when considering the word as center word and the other
vector considering the word as context word. 

#### Word vector representations
##### One-hot vector: In the vocabulary V, the word we are representing will have 1 and everything else is 0.
Ex: 'hotel' = [0,0,0......1.....0]

##### Much better word embeddings that one-hot vector are achieved by SVD methods.

### Singular Value Decomposition methods
### Iteration based methods - word2vec

#### Distributional Hypothesis: Words with similar contexts or context distributions have similar meanings.

#### word2vec includes the following:
- 2 algorithms:
  - CBOW continuous bag of words: tries to predict the center word given the context (sorounding words)
  - skip-gram: predicts the context(sorounding words) give the center word
- 2 training methods:
  - negative sampling
  - hierarchical softmax: uses efficient tree structure to compute probabilities of the vocabulary
 
### Singular value decomposition
- SVD to make subsequent matrix calculations simpler.
