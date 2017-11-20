import tensorflow as tf 
import numpy as np 

from tensorflow.examples.tutorials.mnist import input_data

data = input_data.read_data_sets('./data/')

img = data.train.images 

lab = data.train.labels 
num = data.train.num_examples

with tf.python_io.TFRecordWriter('train.tfrecords') as f:
    for i in range(num):
        img_raw = img[i].tostring() 
        example = tf.train.Example(features=tf.train.Features(feature={
            'img':tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])), 
            'lab':tf.train.Feature(int64_list=tf.train.Int64List(value=[np.argmax(lab[i])]))
        })) 
    f.write(example.SerializeToString()) 

Timg = data.test.images
Tlab = data.test.labels
Tnum = data.test.num_examples


with tf.python_io.TFRecordWriter('test.tfrecords') as Tf:
    for i in range(Tnum):
        Timg_raw = img[i].tostring()
        example = tf.train.Example(features=tf.train.Features(feature={
            'Timg':tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
            'Tlab':tf.train.Feature(int64_list=tf.train.Int64List(value=[np.argmax(lab[i])]))
        }))
    Tf.write(example.SerializeToString())

Vimg = data.validation.images
Vlab = data.validation.labels
Vnum = data.validation.num_examples


with tf.python_io.TFRecordWriter('validation.tfrecords') as Tf:
    for i in range(Tnum):
        Timg_raw = img[i].tostring()
        example = tf.train.Example(features=tf.train.Features(feature={
            'Timg':tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
            'Tlab':tf.train.Feature(int64_list=tf.train.Int64List(value=[np.argmax(lab[i])]))
        }))
    Tf.write(example.SerializeToString())
