# submitted by: REYCEL B. SARMIENTO, ANGELIKA MARIE NAVA & MARIANE FAITH TORREVERDE

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

import tensorflow as tf
tf.compat.v1.disable_eager_execution()


def rotate_obj(points, angle):
    angle = st.sidebar.slider("Angle of Rotation", -180, 180, 10)
    rotation_matrix = tf.stack([
                                [tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

    return rotate_object

def _plt_basic_object_(points):
    tri = Delaunay(points).convex_hull
    
    fig = plt.figure(figsize = (8, 8))
    ax = fig.add_subplot(111, projection = '3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade=True, cmap=cm.rainbow, lw=0.5)

    ax.set_xlim3d(-5,5) #manages the width of the shape
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5) #height

# RECTANGLE
def _rectangle_(bottom_lower=(0, 0, 0), side_length=5, length=-4):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [length, side_length, 0],
        bottom_lower + [length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [length, side_length, side_length],
        bottom_lower + [length, 0, side_length],
        bottom_lower,
    ])

    return points

init_rectangle_ = _rectangle_(side_length=3)
points = tf.constant(init_rectangle_, dtype=tf.float32)

_plt_basic_object_(init_rectangle_)
plt.show()

def translate_obj(points, amount):
    return tf.add (points, amount)

translation_amount =tf.constant([1, 2, 2], dtype=tf.float32) 
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
    translated_rectangle = session.run(translated_object)

_plt_basic_object_(translated_rectangle)
plt.show()

with tf.compat.v1.Session() as session:
    rotated_object = session.run(rotate_obj(init_rectangle_, 75))   
    
_plt_basic_object_(rotated_object)
plt.show()

# PYRAMID

def _tri_prism_(bottom_lower=(0, 0, 0), side_length=5, side=4, two=2):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side, 0],
        bottom_lower + [side, side, 0],#bottom left back
        bottom_lower + [side, 0, 0], #bottom right back
        bottom_lower + [two, side, side_length],
        bottom_lower + [two, side, side_length],
        bottom_lower + [two, 0, side_length],
        bottom_lower + [two, 0, side_length],
        bottom_lower,
    ])

    return points

init_tri_prism_ = _tri_prism_(side_length=3)
points = tf.constant(init_tri_prism_, dtype=tf.float32)

_plt_basic_object_(init_tri_prism_)
plt.show()

def translate_obj(points, amount):
    return tf.add (points, amount)

translation_amount =tf.constant([1, 2, 2], dtype=tf.float32) 
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
    translated_tri_prism_= session.run(translated_object)

_plt_basic_object_(translated_tri_prism_)
plt.show()

with tf.compat.v1.Session() as session:
    rotated_object = session.run(rotate_obj(init_tri_prism_, 75))   
    
_plt_basic_object_(rotated_object)
plt.show()

# RIGHT TRIANGLE
def _right_tri_(bottom_lower=(0, 0, 0), side_length=3):
    
    bottom_lower = np.array(bottom_lower)

    points= np.vstack([
    bottom_lower,
    bottom_lower + [0, side_length, 0],
    bottom_lower + [side_length, side_length, 0],
    bottom_lower + [0, 0, side_length],
    bottom_lower + [0, side_length, side_length],
    bottom_lower + [side_length, 0, 0],
    bottom_lower + [side_length, 0, 0],
    bottom_lower + [side_length, 0, 0],
    bottom_lower + [0, 0, side_length],

    bottom_lower,
    ])

    return points

init_right_tri_ = _right_tri_(side_length=5)
points     = tf.constant(init_right_tri_, dtype=tf.float32)

_plt_basic_object_(init_right_tri_)
plt.show()

def translate_obj(points, amount):
    return tf.add (points, amount)

translation_amount =tf.constant([1, 2, 2], dtype=tf.float32) 
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
    translated_right_tri = session.run(translated_object)

_plt_basic_object_(translated_right_tri)
plt.show()

with tf.compat.v1.Session() as session:
    rotated_object = session.run(rotate_obj(init_right_tri_, 75))   
    
_plt_basic_object_(rotated_object)
plt.show()

# RECTANGULAR PYRAMID

def _isosceles_tri_ (bottom_lower=(0, 0, 0), side_length=5, negative=-4, four=4):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [four, side_length, 0],
        bottom_lower + [negative, side_length, 0],
        bottom_lower + [0, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [four, side_length, side_length],
        bottom_lower + [negative, side_length, side_length],
        bottom_lower + [0, 0, side_length],
        bottom_lower,
    ])

    return points

init_isosceles_tri_ = _isosceles_tri_ (side_length=3)
points = tf.constant(init_isosceles_tri_, dtype=tf.float32)

_plt_basic_object_(init_isosceles_tri_)
plt.show()

def translate_obj(points, amount):
    return tf.add (points, amount)

translation_amount =tf.constant([1, 2, 2], dtype=tf.float32) 
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
    translated_isosceles_tri_ = session.run(translated_object)

_plt_basic_object_(translated_isosceles_tri_)
plt.show()

with tf.compat.v1.Session() as session:
    rotated_object = session.run(rotate_obj(init_isosceles_tri_, 75))   
    
_plt_basic_object_(rotated_object)
plt.show()

