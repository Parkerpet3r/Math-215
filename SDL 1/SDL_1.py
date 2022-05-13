import numpy as np
from matplotlib import pyplot as plt
plt.close("all")

def main():
    """
    This program takes four numbers from the user, and makes vectors
    out of them. Then, it finds the projection of vector 1 onto vector
    2, as well as the portion of vector 1 othogonal to vector 2.
    """

    vectors = make_vectors()
    #print(calc_dot_prod(vectors[0], vectors[1]))
    #print(calc_dot_prod(vectors[1], vectors[1]))
    #print(calc_orth(vectors[0], vectors[1]))
    v_1 = vectors[0]
    v_2 = vectors[1]
    proj = calc_proj(v_1, v_2)
    orth = (sub_vec(v_1, proj))
    orth[0] = round(orth[0], 2)
    orth[1] = round(orth[1], 2)
    angle = calc_theta(v_1, v_2)
    
    print()
    print(f'Projection of vector 1 onto vector 2: {proj}')
    print(f'Portion of vector 1 orthagonal to vector 2: {orth}')
    
    x_proj, y_proj = make_func(calc_proj(v_1, v_2))
    x_1, y_1 = make_func(v_1)
    x_2, y_2 = make_func(v_2)
    x_orth, y_orth = make_func(orth)

    print()
    print(f'Angle between the vectors: {angle:.2f} degrees')
    
    print(f'Sum of vectors: {add_vec(v_1, v_2)}')
    print(f'Vector 1: {v_1}')
    print(f'Vector 2: {v_2}')
 
    print('''
    magenta = portion of vector 1 parallel with vector 2
    cyan = vector 2
    red = vector 1
    ''')
    plt.figure(1)
    if np.sqrt(v_2[0] ** 2 + v_2[1] ** 2) >         np.sqrt(proj[0] ** 2 + proj[1] ** 2):
            plt.plot(x_2, y_2, 'c')
            plt.plot(x_proj,y_proj, 'm')
    else:
        plt.plot(x_proj,y_proj, 'm')
        plt.plot(x_2, y_2, 'c')
   # plt.plot(x_orth, y_orth)
    plt.plot(x_1, y_1, 'r')
    plt.title('x vs y')
    plt.show()
    
    
def make_vectors():

    """
    takes no arguments. User inputs four numbers, x,y for vector 1
    and x,y for vector 2. Then returns the vectors in a compound list
    [[x1,y1],[x2,y2]]
    """

    user_vectors = []
    for i in range(2):
        user_vector = []
        x = int(input(f'x component of vector {i+1}: '))
        y = int(input(f'y component of vector {i+1}: '))
        user_vector.append(x)
        user_vector.append(y)
        user_vectors.append(user_vector)

    return user_vectors

def calc_dot_prod(vector_1, vector_2):

    """
    takes two vectors in the form of lists, and returns the
    dotproduct
    """

    prod = vector_1[0] * vector_2[0] + vector_1[1]        * vector_2[1]
    
    return prod

def calc_proj(vector_1, vector_2):
    """
    Calculates projection of one vector (vector_1) 
    onto a second vector (vector_2), returns vector of projection
    """

    proj = []
    num = calc_dot_prod(vector_1, vector_2)
    den = calc_dot_prod(vector_2, vector_2)
    x = vector_2[0] * (num/den)
    y = vector_2[1] * (num/den)
    
    proj.append(round(x, 2))
    proj.append(round(y, 2))
#      proj.append(vector_2[0] * (num / den))
#      proj.append(vector_2[1] * (num / den))
    
    return proj

def make_func(vector):
    """"""

    x_comp = np.linspace(0, vector[0], 50)
    y_comp = np.linspace(0, vector[1], 50)

    return x_comp, y_comp

def add_vec(vector_1, vector_2):
    """
    Adds two vectors, returns the sum vector of them
    """
    
    sum_vec = []
    sum_vec.append(vector_1[0]+vector_2[0])
    sum_vec.append(vector_1[1]+vector_2[1])
    
    return sum_vec

def sub_vec(vector_1, vector_2):
    """
    Computes (vector_1) minus (vector_2), returns sum vector
    """
    
    diff_vec = []
    diff_vec.append(vector_1[0]-vector_2[0])
    diff_vec.append(vector_1[1]-vector_2[1])
    
    return diff_vec

def calc_mag(vector):
    """
    Calculates magnitude of a vector, returns the magnitude
    """

    mag = np.sqrt(vector[0] ** 2 + vector[1] ** 2)

    return mag
    
def calc_theta(vector_1, vector_2):
    """
    Takes two vectors and returns the angle between them
    """
    
    theta = np.arccos(calc_dot_prod(vector_1, vector_2)/(calc_mag(vector_1) * (calc_mag(vector_2))))
    theta = theta * 180 / np.pi
    
    return theta

main()