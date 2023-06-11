import logistic_regression as lr
import classifier as cl

global ds

Teta = [1, 1, 1]  # Tetas vector, initial value to guess the numerical values of thetas
# t = [0.005,0.005,0.005]
t = lr.gradient_descent(lr.function, lr.derivative, 0.000001, 0.001, Teta)
lr.save_model("t_model.txt", t)  # save the model to a file (for later use)
cl.classify("t_model.txt", "reg.txt")  # classify the data set using the model

print("Tetas vector", t)
print("+++++++++++++++++")
cl.classify("t_model.txt", "reg.txt")  # change the file coefficients x1,.....xn by Tetas vector
