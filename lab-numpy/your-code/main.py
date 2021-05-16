#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

#La primera opción: genero dos matrices de 3 filas y 5 columnas con números aleatorios del 0-100
a = np.random.randint(0,100, (2,3,5))


#La segunda opción: genero una matriz de 2 x 3 x 5 con números aleatorios del 0-1
arr2 = np.random.rand(2,3,5)


#la tercera opción: genero matriz 2 x 3 x 5 con número aleatorios entre 0-1
aar3 = np.random.random_sample((2,3,5))

#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print(b)


#7. Do a and b have the same size? How do you prove that in Python code?

#Para saber el tamaño de los arrays:
#print(a.size)
#print(b.size)
# Ambas tienen el mismo tamaño, es decir, el mismo número de elementos

        #NOTA PARA MI:
                #Si lo queremos saber es su forma(la long de cada dimensión):
                #print(a.shape)

#8. Are you able to add a and b? Why or why not?

new_arr = np.add(a,b)
print(new_arr)

        #print(a.ndim)
        #print(b.ndim)

        #print(a.shape)
        #print(b.shape)

#No se pueden juntar porque tienen distntas formas a pesar de que tienen las mismas dimensiones  y tamaños. 


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1,2,0))
print(c)
#print(c.shape)
#print(a.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now? yes!

d = np.add(a,c)
print(d)



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)
# Se les ha sumado a todos los valores del array a un 1 (del array c)

#12. Multiply a and c. Assign the result to e.

# Hay dos formas de hacerlo: 

e = np.multiply(a,c)
#e_2 = a * c

print(e)

#13. Does e equal to a? Why or why not?

# Toma los mismos valores que a, porque lo que hemos hecho ha sido multiplicar todos los valores de una matriz por los valores de la matriz c que toma valores de 1


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

print(d_max)
print(d_min)
print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty_like(d)
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

""" UNA FORMA DE HACERLO
f[(d_mean > d) & (d > d_min)] = 25
f[(d_max > d) & (d > d_mean)] = 75
f[d == d_mean] = 50
f[d  == d_max] = 100
f[d == d_min] = 0
"""

new_f = []

for vals in a:
    
    for val in vals:
        
        for va in val:
            
            if d_min < va < d_mean: 
                new_f.append(25)
            elif d_mean < va < d_max:
                new_f.append(75)
            elif va == d_mean:
                new_f.append(50)
            elif va == d_min:  #NO SE QUE ESTA PASANDO CON ESTA CONDICIÓN Y LA SIGUIENTE (D_MIN Y  D_MAX) PORQUE NO ME LA ESTA PILLANDO POR LO QUE NO METE NI 0 NI 100. 
                new_f.append(0)
            elif va == d_max:
                new_f.append(100)

print(len(new_f))

f = np.array(new_f).reshape(2,3,5)

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(f)
print(d)


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
g = []

for vals in a:
    
    for val in vals:
        
        for va in val:
            
            if d_min < va < d_mean: 
                g.append("A")
            elif d_mean < va < d_max:
                g.append("B")
            elif va == d_mean:
                g.append("C")
            elif va == d_min:
                g.append("D")
            elif va == d_max:
                g.append("E")

f = np.array(g).reshape(2,3,5)



