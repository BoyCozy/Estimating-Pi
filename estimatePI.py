import random
import matplotlib.pyplot as plt

'''This program calculates the value of pi, and shows a visual representation.'''
'''Q. You are given a function that randomly calculates a number from 0-1 uniformly.
      Calculate the number pi.'''
      
def estimate_pi(n):

    # Counts the points in and out of the circle
    num_point_incircle = 0
    num_point_total = 0
    
    # list to hold our points to graph
    x_list_in = []
    y_list_in = []
    x_list_out= []
    y_list_out = []
    
    # For loop to plot the number of points
    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        
        # Calculates whether the point is in or outside of the circle and adds to
        # appropriate list
        distance = x**2 + y**2
        if distance <= 1:
            num_point_incircle += 1
            x_list_in.append(x)
            y_list_in.append(y)
        elif distance > 1:
            x_list_out.append(x)
            y_list_out.append(y)
        num_point_total += 1 
    
    plt.figure()
    
    # Set x-axis range
    plt.xlim((-1,1))
    
    # Set y-axis range
    plt.ylim((-1,1))
    
    # Draw lines to split quadrants
    plt.plot([0,0],[-1,1], linewidth=2, color='black' )
    plt.plot([-1,1],[0,0], linewidth=2, color='black' )
    plt.title('Estimating Pi')
       
    # Plotting points
    plt.scatter(x_list_in, y_list_in, s=4, c='r')
    plt.scatter(x_list_out, y_list_out, s=3, c='b')
    plt.show()
    
    # Returns our number Pi
    return 4 * num_point_incircle/num_point_total
    
def main(estimate_pi):
    n = int(input("Enter a number: "))
    print(estimate_pi(n))

# Main function
main(estimate_pi)
