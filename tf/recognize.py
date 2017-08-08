import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import math

# converting to array of bytes
def toBytes(path):
    img = Image.open(path)
    pixels = img.load()
    data_image = []
    width, height = img.size
    for x in range(0,width):
        for y in range(0,height):
            pixel = pixels[y, x]
            value = pixel
            if isinstance(pixel, tuple):
                value = pixel[0]
            num = value / 255.0
            data_image.append(num)
    return data_image

def load():
    sess=tf.Session()    
    saver = tf.train.import_meta_graph('./tf/deep-model.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./tf'))
    graph = tf.get_default_graph()
    y = graph.get_tensor_by_name("y:0")
    x = graph.get_tensor_by_name("x:0")
    keep_prob = graph.get_tensor_by_name('keep_prob:0')
    return (x, y, keep_prob, sess)

def recognize(x, y, keep_prob, sess):
    value = -1
    max_value = -100
    resulting_arr = []
    for _ in range(50):
        prob_array = sess.run(y, feed_dict={x: np.matrix(toBytes('image.png')), keep_prob: 0.9})[0]
        max_val = max(prob_array)
        if max_val > max_value:
            max_value = max_val
            value = np.argmax(prob_array)
            resulting_arr = prob_array
    result = dict()
    if max_value < 4:
        result["max_value"] = "can't determine"
    else:
        result["max_value"] = str(value)
    prob_array_rounded = [str(round(x, 3)) for x in resulting_arr]
    result["prob_array"] = prob_array_rounded
    return json.dumps(result)
