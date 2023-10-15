def lagrange(x, y, point):
    n = len(x)
    result = 0.0   

    for i in range(n):      
        term = y[i]  
        for j in range(n):
            if j != i:
                term *= (point - x[j]) / (x[i] - x[j])  
        result += term   

    return result

x_values = [1.4, 1.6, 1.8, 2.0]
y_values = [-4.424, -5.192, -5.800, -6.200]

point = 1.2  
 
interpolated_value = round(lagrange(x_values, y_values, point),4)   
print(f"The interpolated value at x = {point} is approximately {interpolated_value}")   
