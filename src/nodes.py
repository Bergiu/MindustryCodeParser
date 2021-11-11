class Node:
    def loc(self):
        raise NotImplementedError()


class OneLineNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def loc(self):
        return 1

    def __repr__(self):
        return f"{self.left} {self.right}"


class CodeBlockNode(Node):
    def __init__(self, line, prev_node=None):
        self.line = line
        self.prev_node = prev_node

    def loc(self):
        if self.prev_node is not None and isinstance(self.prev_node, Node):
            if isinstance(self.line, Node):
                return self.prev_node.loc() + self.line.loc()
            return self.prev_node.loc() + 1
        return 1

    def __repr__(self):
        out = ""
        if self.prev_node is not None:
            out += f"{self.prev_node}"
        out += f"{self.line}\n"
        return out


class OperationNode(Node):
    def __init__(self, command, parameters=None):
        self.command = command
        self.parameters = parameters

    def loc(self):
        return 1

    def __repr__(self):
        out = f"{self.command}"
        if self.parameters is not None:
            out += "".join([f" {param}" for param in self.parameters])
        return out


class CommentNode(Node):
    def __init__(self, comment):
        self.comment = comment

    def __repr__(self):
        return str(self.comment)

    def loc(self):
        return 0
