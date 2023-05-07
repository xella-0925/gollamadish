import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import streamlit as st

import tensorflow as tf
tf.compat.v1.disable_eager_execution()


def rotate_obj(points, angle):
    rotation_matrix = tf.stack([
        [tf.cos(angle), tf.sin(angle), 0],
        [-tf.sin(angle), tf.cos(angle), 0],
        [0, 0, 1]
    ])
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

    return rotate_object


def translate_obj(points, translation):
    translation_vector = tf.constant(translation, dtype=tf.float32)
    translated_object = tf.add(tf.cast(points, tf.float32), translation_vector)

    return translated_object


def _plt_basic_object_(points):
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:, 0], points[:, 1], points[:, 2],
                        triangles=tri,
                        shade=True, cmap=cm.rainbow, lw=0.5)

    ax.set_xlim3d(-5, 5)  # manages the width of the shape
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)  # height


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


# RIGHT TRIANGLE
def _right_tri_(bottom_lower=(0, 0, 0), side_length=3):
    
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
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


# PYRAMID
def _tri_prism_(bottom_lower=(0, 0, 0), side_length=5, side=4, two=2):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side, 0],
        bottom_lower + [side, side, 0],  # bottom left back
        bottom_lower + [side, 0, 0], #bottom right back
        bottom_lower + [two, side, side_length],
        bottom_lower + [two, side, side_length],
        bottom_lower + [two, 0, side_length],
        bottom_lower + [two, 0, side_length],
        bottom_lower,
    ])

    return points


def main():
    st.title("3D Object Transformation")
    st.sidebar.header("Image Transformations")
    object_types = ["Rectangle", "Right Triangle", "Triangular Prism"]
    object_type = st.sidebar.selectbox("Select Object Type", object_types)

    transformation_types = ["Rotate", "Translate"]
    transformation_type = st.sidebar.selectbox("Select Transformation Type", transformation_types)

    angle = st.sidebar.slider("Rotation Angle", -180.0, 180.0, step=1.0)
    translation = st.sidebar.slider("Translation", -5.0, 5.0, step=0.1, value=(0.0, 0.0, 0.0))

    if object_type == "Rectangle":
        init_object = _rectangle_(side_length=5, length=-4)
    elif object_type == "Right Triangle":
        init_object = _right_tri_(side_length=3)
    elif object_type == "Triangular Prism":
        init_object = _tri_prism_(side_length=5, side=4, two=2)

    points = tf.constant(init_object, dtype=tf.float32)

    with tf.compat.v1.Session() as session:
        if transformation_type == "Rotate":
            transformed_object = session.run(rotate_obj(points, np.radians(angle)))
        elif transformation_type == "Translate":
            transformed_object = session.run(translate_obj(points, translation))

    _plt_basic_object_(transformed_object)
    st.pyplot(plt)


if __name__ == "__main__":
    main()
