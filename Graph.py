from tkinter import messagebox

import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    NumberOfIteration = 0
    chosenColors = {}

    def __init__(self, tempNumberOfIteratıon, tempChosenColors):
        self.NumberOfIteration = tempNumberOfIteratıon
        self.chosenColors = tempChosenColors
        self.creating_nodes()

    def colorize(graph: nx.Graph, NumberOfIteration, chosenColors):
        my_node_list = []
        for node in graph:
            my_node_list.append(node)

        color_dict = {}
        for node in my_node_list:
            color_dict[node] = set(chosenColors)

        the_solution = {}
        sorted_node = sorted(graph.degree, key=lambda x: x[1], reverse=True)
        for n in sorted_node:
            try:
                set_the_color = list(color_dict[n[0]])
                if not set_the_color:
                    the_solution[n[0]] = "gray"
                    set_the_color[0] = "gray"
                else:
                    the_solution[n[0]] = set_the_color[0]
            except:
                messagebox.showerror('Coloring ERROR', "ERROR: Not enough color for: " + str(list(n)[0]) + " node.")
            adjacent_node = graph[n[0]]
            adjacent_node_list = list(adjacent_node)
            for j in range(len(adjacent_node)):
                if not set_the_color:
                    continue
                if set_the_color[0] in color_dict[adjacent_node_list[j]]:
                    color_dict[adjacent_node_list[j]].remove(set_the_color[0])
        for key, values in color_dict.items():
            if not color_dict[key]:
                color_dict[key] = {"gray"}
        listColor = []
        keyCheck = []
        for key, values in color_dict.items():
            for i in values:
                if key in keyCheck:
                    continue
                else:
                    listColor.append(i)
                    keyCheck.append(key)
        tempListColor = []
        nx.draw(graph, with_labels=True, font_weight='bold', node_color="gray", node_size=1500)
        plt.show(block=False)
        plt.pause(2)
        plt.clf()
        for i in range(len(listColor)):
            tempListColor.append("gray")
        for i in range(0, int(NumberOfIteration), 1):
            try:
                if i == int(NumberOfIteration) - 1:
                    tempListColor[i] = listColor[i]
                    nx.draw(graph, with_labels=True, font_weight='bold', node_color=tempListColor, node_size=1500)
                    plt.show()
                    break
                tempListColor[i] = listColor[i]
                nx.draw(graph, with_labels=True, font_weight='bold', node_color=tempListColor, node_size=1500)
                plt.show(block=False)
                plt.pause(2)
                plt.clf()
            except:
                messagebox.showerror('Iteration ERROR', 'All nodes have been painted with some colors!')

    def creating_nodes(self):
        G = nx.Graph()
        edge_list = []
        with open("text.txt") as f:
            edge_list = [i.strip().split("->") for i in f.readlines()]
        G.add_edges_from(edge_list)
        node_list = G.nodes()
        Graph.colorize(G, self.NumberOfIteration, self.chosenColors)
