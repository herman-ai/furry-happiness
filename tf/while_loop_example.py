import tensorflow as tf

queue = tf.constant([[0, 0], [1,1]], tf.int32)
sample = tf.constant([2, 2], tf.int32)
i = tf.constant(0)

def loop_condition(i, current_sample, *args):
    return tf.less(i, 10)

def audio_generator(*args):
    '''
    returns next sample
    '''
    cached_sample = args[0]
    current_sample = args[1]
    return tf.add(cached_sample, current_sample)

def body(i, current_sample, *args):
    queue = args[0]
    cached_sample = queue[0, :]
    next_sample = audio_generator(cached_sample, current_sample)
    next_sample = tf.Print(next_sample, [next_sample, current_sample, cached_sample, queue], summarize=6)
    new_queue = tf.concat([queue[-1:,:], tf.expand_dims(next_sample, 0)], 0)
    return tf.add(i, 1), next_sample, new_queue

r = tf.while_loop(loop_condition,
                  body,
                  [i, sample, queue], # TODO, add more queues here
                  [tf.TensorShape([]), tf.TensorShape([2]), tf.TensorShape([2, 2])] # TODO
                 )

with tf.Session() as sess:
    output = sess.run(r)
    print("output = {}".format(output))
