This is directory for my sentiment analysis code.

Results:

Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 50)                1282000   
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 51        
=================================================================
Total params: 1,282,051
Trainable params: 1,282,051
Non-trainable params: 0
_________________________________________________________________
Epoch 1/10
 - 1s - loss: 0.4767 - accuracy: 0.7683
Epoch 2/10
 - 1s - loss: 0.0600 - accuracy: 0.9939
Epoch 3/10
 - 1s - loss: 0.0164 - accuracy: 1.0000
Epoch 4/10
 - 1s - loss: 0.0078 - accuracy: 1.0000
Epoch 5/10
 - 1s - loss: 0.0045 - accuracy: 1.0000
Epoch 6/10
 - 1s - loss: 0.0030 - accuracy: 1.0000
Epoch 7/10
 - 1s - loss: 0.0022 - accuracy: 1.0000
Epoch 8/10
 - 1s - loss: 0.0016 - accuracy: 1.0000
Epoch 9/10
 - 1s - loss: 0.0013 - accuracy: 1.0000
Epoch 10/10
 - 1s - loss: 0.0010 - accuracy: 1.0000
(1, 25639)
PREDS shape: (1, 1)
PREDS: [[0.51949275]]
Review: [This is a great movie.]
Sentiment: POSITIVE (51.949%)
(1, 25639)
PREDS shape: (1, 1)
PREDS: [[0.3853152]]
Review: [This movies is not good, boring.]
Sentiment: NEGATIVE (61.468%)
(base) praveenjutur@Praveens-iMac 100 % 
