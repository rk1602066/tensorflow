%tensorflow_version 2.x

import tensorflow as tf
print(tf.version)

<module 'tensorflow._api.v2.version' from '/usr/local/lib/python3.6/dist-packages/tensorflow/_api/v2/version/__init__.py'>




tensor:

string = tf.Variable('this is a string',tf.string)
number = tf.Variable(34,tf.int16)
floatnumber = tf.Variable(3.1334,tf.float64)

rank1_tensor = tf.Variable(['addd','jss','sdkjs'],tf.string)

rank2_tensor = tf.Variable([['a1','a2','a3'],['b1','b2','b3']],tf.string)

tf.rank(rank2_tensor)

<tf.Tensor: shape=(), dtype=int32, numpy=2>



shape:

rank2_tensor.shape
TensorShape([2, 3])



changing shape:

tensor1 = tf.ones([1,2,3])
print(tensor1)
tensor2 = tf.reshape(tensor1,[2,3,1])
print(tensor2)
tensor3 = tf.reshape(tensor1,[3,-1])
print(tensor3)


tf.Tensor(
[[[1. 1. 1.]
  [1. 1. 1.]]], shape=(1, 2, 3), dtype=float32)
tf.Tensor(
[[[1.]
  [1.]
  [1.]]

 [[1.]
  [1.]
  [1.]]], shape=(2, 3, 1), dtype=float32)
tf.Tensor(
[[1. 1.]
 [1. 1.]
 [1. 1.]], shape=(3, 2), dtype=float32)
 
 
 
 type of tensor:

Variable: value could be vhange latter,
Constant: value could not change,
Placeholder, 
SparseTensor,
