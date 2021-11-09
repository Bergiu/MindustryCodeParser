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


class FunctionNode(Node):
    def __init__(self, function_name, code_block):
        self.function_name = function_name
        self.code_block = code_block

    def loc(self):
        return self.code_block.loc() + 4

    def __repr__(self):
        out = ""
        lines = self.code_block.loc() + 2
        out += f"op add {self.function_name} @counter 1\n"
        out += f"op add @counter @counter {lines}\n"
        out += f"set _{self.function_name}_retptr @counter\n"
        out += str(self.code_block)
        out += "set @counter retptr"
        return out


class CommentNode(Node):
    def __init__(self, comment):
        self.comment = comment

    def __repr__(self):
        return str(self.comment)

    def loc(self):
        return 0


class ExecNode(Node):
    def __init__(self, fnptr):
        self.fnptr = fnptr

    def loc(self):
        return 2

    def __repr__(self):
        out = "op add retptr @counter 1\n"
        out += f"set @counter {self.fnptr}"
        return out
