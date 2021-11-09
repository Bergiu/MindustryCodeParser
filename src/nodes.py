class CodeBlockNode:
    def __init__(self, line, prev_node=None):
        self.line = line
        self.prev_node = prev_node

    def __repr__(self):
        out = ""
        if self.prev_node is not None:
            out += f"{self.prev_node}"
        out += f"{self.line}\n"
        return out


class OperationNode:
    def __init__(self, command, parameters=None):
        self.command = command
        self.parameters = parameters

    def __repr__(self):
        out = f"{self.command}"
        if self.parameters is not None:
            out += "".join([f" {param}" for param in self.parameters])
        return out
