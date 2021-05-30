class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 #Custo do movimento do início até o ponto atual
        self.h = 0 #Custo estimado para mover de uma determinada posição até o destino final
        self.f = 0 

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    
    #Essa função retorna uma lista de tuplas do caminho otimizado para percorrer um labirinto dado um ponto inicial e um ponto final.

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #Inicialização das listas que receberão as tuplas
    open_list = []
    closed_list = []

    #A caminho inicial é inserido na lista
    open_list.append(start_node)

    #Roda até encontrar o destino
    while len(open_list) > 0:
        #Pega o nó atual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index


        open_list.pop(current_index)
        closed_list.append(current_node)


        if current_node == end_node:  #Caso tenha achado o destino
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 

        #Verifica todas possibilidades para continuar o caminho
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            #Pega a posição do novo nó a ser percorrido
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #Verifcia se ele está dentro do labirinto
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #Verifica se o novo nó não é uma parede
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #Cria o novo nó
            new_node = Node(current_node, node_position)

            
            children.append(new_node)

        for child in children:
            
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            #Cria os valores de F,G,H
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            #O nó filho já está na lista
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            
            open_list.append(child)
