from iris import *


def main():
    activation_function = sigmoid

    net_shapes = [
        (4, 3),
        (4, 4, 3),
        (4, 1, 1, 3),
        (4, 3, 4, 3),
        (4, 4, 4, 3),
    ]

    learning_rates = [0.1, 0.3, 0.5, 0.8, 1, 3]

    print("DISTINTAS REDES")
    for shape in net_shapes:
        process_iris(activation_fun=activation_function, net_shape=shape, plot=False)

    print("DISTINTOS LEARNING RATES")
    for lr in learning_rates:
        process_iris(activation_fun=activation_function, learning_rate=lr, plot=False)

    print("DISTINTOS INPUTS")
    for i in range(5):
        random_state = np.random.randint(1, 100)
        process_iris(title=f"red_basica_{i}_{random_state}", random_state=random_state)


if __name__ == '__main__':
    main()
