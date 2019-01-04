import operator
import random


def create_rand_tree(height, functions, terminals, size=None):
    if type(terminals) == dict:
        terminals = list(terminals.keys())
    if size:
        n = size
    else:
        n = 2 ** (height + 1) - 1
    tree = []
    for i in range(1, n + 1):
        if n < 4 or i / n * 2 < random.random():
            tree.append(random.choice(functions))
        else:
            tree.append(random.choice(terminals))
    fix_tree(tree, functions, terminals)
    return tree


def fix_tree(tree, functions, terminals):
    if type(terminals) == dict:
        terminals = list(terminals.keys())
    for i in range(len(tree)):
        if tree[i] not in terminals and tree[i] is not None:  # si es funcion
            if 2 * i + 2 >= len(tree):  # si no tiene posibles hijos
                tree[i] = random.choice(terminals)
            else:
                if tree[2 * i + 1] in terminals:
                    if random.random() < 0.8:
                        tree[2 * i + 1] = random.choice(functions)

                if tree[2 * i + 2] in terminals:
                    if random.random() < 0.8:
                        tree[2 * i + 2] = random.choice(functions)

                if tree[2 * i + 1] is None:
                    if random.random() < 0.5:
                        tree[2 * i + 1] = random.choice(functions)
                    else:
                        tree[2 * i + 1] = random.choice(terminals)

                if tree[2 * i + 2] is None:
                    if random.random() < 0.5:
                        tree[2 * i + 2] = random.choice(functions)
                    else:
                        tree[2 * i + 2] = random.choice(terminals)

        else:  # si es terminal
            if 2 * i + 2 < len(tree) or tree[i] is None:  # si puede tener hijos
                valor = tree[i]
                delete_subtree(tree, i, mutar=True)  # borrar hijos
                tree[i] = valor


def print_tree(tree, print_flag=True):
    string = ""
    pila_nodos = [(0, 0)]
    while pila_nodos:
        nodo, altura = pila_nodos.pop()
        if altura == 0:
            string += str(tree[nodo]) + "\n"
        else:

            nodo_aux = nodo
            string_nodo = ""
            if nodo_aux % 2 == 1:
                string_nodo = "╚═══ " + str(tree[nodo]) + string_nodo
            else:
                string_nodo = "╠═══ " + str(tree[nodo]) + string_nodo
            nodo_aux = (nodo_aux - 1) // 2
            while nodo_aux > 0:
                if nodo_aux % 2 == 1:
                    string_nodo = "     " + string_nodo
                else:
                    string_nodo = "║    " + string_nodo
                nodo_aux = (nodo_aux - 1) // 2

            string += string_nodo + "\n"

        nodo_izq = 2 * nodo + 1
        nodo_der = 2 * nodo + 2

        if nodo_izq < len(tree) and tree[nodo_izq]:
            pila_nodos.append((nodo_izq, altura + 1))

        if nodo_der < len(tree) and tree[nodo_der]:
            pila_nodos.append((nodo_der, altura + 1))

    if print_flag:
        print(string)
    return string


def copy_tree(tree, nodo):
    arbol_final = []
    pila_nodos = [nodo]
    while pila_nodos:
        nodo_actual = pila_nodos.pop()
        arbol_final.append(tree[nodo_actual])

        nodo_izq = 2 * nodo_actual + 1
        nodo_der = 2 * nodo_actual + 2

        if nodo_izq < len(tree):
            pila_nodos.insert(0, nodo_izq)
        if nodo_der < len(tree):
            pila_nodos.insert(0, nodo_der)

    return arbol_final


def delete_subtree(tree, nodo, mutar=False):
    if mutar:
        aux_tree = tree
    else:
        aux_tree = list(tree)
    pila_nodos = [nodo]
    while pila_nodos:
        nodo_actual = pila_nodos.pop()
        aux_tree[nodo_actual] = None

        nodo_izq = 2 * nodo_actual + 1
        nodo_der = 2 * nodo_actual + 2

        if nodo_izq < len(aux_tree):
            pila_nodos.insert(0, nodo_izq)
        if nodo_der < len(aux_tree):
            pila_nodos.insert(0, nodo_der)

    return aux_tree


def cross_tree(tree1, tree2, nodo, functions, terminals):
    if nodo >= len(tree1) or nodo >= len(tree2):
        return -1
    sub_tree2 = copy_tree(tree2, nodo)
    tree1_mod = delete_subtree(tree1, nodo)
    pile_position = [nodo]
    while pile_position and sub_tree2:
        nodo_actual = pile_position.pop()
        tree1_mod[nodo_actual] = sub_tree2.pop(0)
        posicion_izq = 2 * nodo_actual + 1
        posicion_der = 2 * nodo_actual + 2

        if posicion_izq < len(tree1):
            pile_position.insert(0, posicion_izq)
        if posicion_der < len(tree1):
            pile_position.insert(0, posicion_der)

    fix_tree(tree1_mod, functions, terminals)

    return tree1_mod


operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def eval_tree(tree, dict_terminals={}, operations=operations):
    aux_tree = list(tree)
    for i in range(len(aux_tree) - 1, 0, -1):
        if aux_tree[i] is None or i % 2 == 1:
            continue
        nodo_padre = (i - 1) // 2
        op_padre = aux_tree[nodo_padre]
        val_izq = aux_tree[i - 1]
        val_der = aux_tree[i]

        if type(val_izq) == str:
            if val_izq in dict_terminals:
                val_izq = dict_terminals[val_izq]
            else:
                raise Exception("WTF")
        if type(val_der) == str:
            if val_der in dict_terminals:
                val_der = dict_terminals[val_der]
            else:
                raise Exception("WTF")

        valor = operations[op_padre](val_izq, val_der)
        aux_tree[nodo_padre] = valor

    if aux_tree[0] in dict_terminals:
        aux_tree[0] = dict_terminals[aux_tree[0]]

    return aux_tree[0]


# tree = range(14)
# copy = copy_tree(tree, 1)
# print(copy)
#
# rama = [0, None, 2, None, None, 5, 6, None, None, None, None, None, 12, 13]
# copy = copy_tree(rama, 2)
# print(copy)
#
# tree2 = range(14)
# deleted = delete_subtree(tree2, 4)
# print(deleted)
#
# tree3_1 = range(14)
# tree3_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
# cross = cross_tree(tree3_1, tree3_2, 3)
# print(cross)
#
# tree_op = ["+", "*", "-", "-", 3, 4, "+", 1, 2, None, None, None, None, 2, 3]  # (+ (* (- 1 2) 3) (- 4 (+ 2 3))) == -4
# eval = eval_tree(tree_op)
# print(eval)
#
# rand_tree = create_rand_tree(3, list(operations.keys()), [1, 2, 3, 4, 5])
# print(rand_tree)
# print(eval_tree(rand_tree))
#
# # tree_op2 = ['-', '+', 1, 5, '+', None, 4, 2, 5, 5, 5, 4, 4, 5]
# # eval2 = eval_tree(tree_op2)
# # print(eval2)
#
# print_tree(rand_tree)

"""
wrong = ['+', '-', '-', '*', '*', '+', '*', '*', '-', '-', '*', '+', '-', '*', '*', None, None, 7, 7, 3, 3, 7, 3, 19, 7,
         3,
         19, 7, 3, 3, 7]
print_tree(wrong)
fix_tree(wrong, ["+", "-", "*"], [19, 7, 3, 40])
print_tree(wrong)
"""

# rand_tree = create_rand_tree(3, list(operations.keys()), [1, 2, 3, 4, 5])
# print(rand_tree)
# print_tree(rand_tree)
