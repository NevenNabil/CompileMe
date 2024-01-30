txt = ""  # Global variable for storing DOT language representation
count = 0  # Global variable for counting nodes in the graph


def add_count():
    # Function to increment the global count variable and return its value
    global count
    count += 1
    return "%s" % count


class Node:
    def __init__(self, name):
        # Constructor for the Node class, initializes a node with a given name
        self.name = name


class Program(Node):
    def __init__(self, name, *args):
        # Constructor for the Program class, a specialized Node representing a program
        # Takes a name and a variable number of child nodes (sons)
        Node.__init__(self, name)
        self.sons = []
        for x in args:
            self.sons.append(x)

    def print(self, indentation):
        # Method to print the tree structure with proper indentation
        for x in self.sons:
            x.print("\t" + indentation)
        print(indentation + "Node: " + self.name)

    def translate(self):
        # Method to translate the graph structure to DOT language
        global txt
        number = add_count()
        txt += number + "[label = " + self.name + "]\n\t"
        for x in self.sons:
            son = x.translate()
            txt += number + "->" + son + "\n\t"
        return "digraph G {\n\t" + txt + "}"


class Terminal(Node):
    def __init__(self, name):
        Node.__init__(self, name)

    def print(self, identation):
        # Print information about the terminal node.
        print(identation + "Node: " + self.name)

    def translate(self):
        global txt
        number = add_count()
        # Conditionally set the label for specific terminal nodes.
        if self.name == "Squals" or self.name == "Non_equal" or ...:
            txt += number + "[label = \"" + str(self.name) + "\"]\n\t"
        else:
            txt += number + "[label = " + str(self.name) + "]\n\t"
        return number


class NonTerminal(Node):
    def __init__(self, name, *args):
        Node.__init__(self, name)
        self.sons = []
        for x in args:
            self.sons.append(x)

    def print(self, identation):
        # Print information about the non-terminal node and its sons.
        for x in self.sons:
            if type(x) == type(tuple()):
                x[0].print("\t" + identation)
            else:
                x.print("\t" + identation)
        print(identation + "Node: " + self.name)

    def translate(self):
        global txt
        number = add_count()
        txt += number + "[label = " + self.name + "]\n\t"
        # Translate each son and connect them to the current non-terminal node.
        for x in self.sons:
            if type(x) == type(tuple()):
                son = x[0].translate()
            else:
                son = x.translate()
            txt += number + "->" + son + "\n\t"
        return number


class Null(Node):
    def __init__(self):
        self.type = "void"

    def print(self, identation):
        # Print information about the null node.
        print(identation + "Null")

    def translate(self):
        global txt
        number = add_count()
        txt += number + "[label = " + "Null" + "]\n\t"
        return number
