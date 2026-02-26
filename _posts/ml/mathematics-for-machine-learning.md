## 2.1 LINEAR ALGEBRA

Linear algebra is a fundamental component of mathematics that is essential for machine learning practitioners. It provides the theoretical foundation needed to understand and work with various machine learning concepts. Mastery of linear algebra equips learners with the critical tools and arithmetic computations required for implementing and optimizing machine learning algorithms. The following subsections present in detail scalars, vectors, matrices, eigenvalues, and eigenvectors which are considered to be the basic concepts of linear algebra.

### 2.1.1  Scalars
In mathematics, a scalar is a measurement that has a magnitude without any associated direction. Within the era of machine learning or data science, scalars might represent various features of data points. For instance, residence datasets with the following features: number of bedrooms, the total floor area, and the sale price of each house can be represented as separate scalar numbers. Scalar values are fundamental units used to create more complex mathematical models and are crucial for carrying out mathematical computations and analyses in machine learning algorithms. Scalars cover various numerical values such as integers, decimals, fractions, and irrational numbers. However, depending on their importance, scalars can be either positive, negative, or zero. Scalars can be evaluated in mathematics using standard arithmetic operations such as addition, subtraction, multiplication, and division.

For example, consider two scalars, a = 5 and b = 3. The sum of these two scalars is obtained by adding them together, a b +=+= 538.

### 2.1.2  Vectors
A vector is a collection of numbers that are ordered consecutively. However, vectors are quantities that can convey direction as well as magnitude. Equation (2.1) depicts this concept, which can be identified as a row or column of numbers in lowercase characters, such as v.

$$
v = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = (v_1, v_2, v_3)
$$

where $v_1, v_2, v_3$ are scalar values, often real values.

In mathematical operations, vectors can be calculated using standard arithmetic operations such as addition, subtraction, and multiplication, as discussed in the subsequent sections.

### 2.1.2.1  Vector addition
Consider two vectors; $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$. Vector addition of “$a$” and “$b$” is performed element-wise to produce a new vector of the same length as shown in Equation (2.2).

$$
a + b = (a_1 + b_1, a_2 + b_2, a_3 + b_3)
$$

For example, let us say we have two vectors, $a = (2, 4, 6)$ and $b = (1, 3, 5)$. To find the sum of these vectors, corresponding components of the vectors will have to be added to each other, as shown in the following:
$$
a + b = (2 + 1, 4 + 3, 6 + 5) = (3, 7, 11)
$$
Thus $a + b$ is equal to $(3, 7, 11)$.


### 2.1.2.2  Vector subtraction
Consider two vectors; $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$. Vector subtraction of “$a$” and “$b$” is performed element-wise to produce a new vector of the same length as shown in Equation (2.3).

$$
a - b = (a_1 - b_1, a_2 - b_2, a_3 - b_3)
$$

For example, let us say we have two vectors, $a = (2, 4, 6)$ and $b = (1, 3, 5)$. To subtract vector “$b$” from “$a$”, the corresponding components will have to be subtracted from each other as shown in the following:

$$
a - b = (2 - 1, 4 - 3, 6 - 5) = (1, 1, 1)
$$
Thus $a - b$ is equal to $(1, 1, 1)$.