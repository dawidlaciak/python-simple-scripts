class Node():

    def __init__(self, text):
        self.text = text
        self.left = None
        self.right = None

    def __repr__(self):
        return self.text
    
    def decode(self, instruction):

        result = self.text

        if len(instruction) == 0:
            return result
        
        first_instruction = instruction[0]
        next_instruction = instruction[1:]

        if first_instruction == 'L' and self.left:
            result += ' ' + self.left.decode(next_instruction)
        elif first_instruction == 'R' and self.right:
            result += ' ' + self.right.decode(next_instruction)
        
        return result
    
tree = Node('Please')
tree.left = Node('turn on')

tree.left.left = Node('the music')
tree.left.left.left = Node('quietly')
tree.left.left.right = Node('loudly')

tree.left.right = Node('light')
tree.left.right.left = Node('strong')
tree.left.right.right = Node('weak')

tree.right = Node('open')
tree.right.left = Node('the door')
tree.right.left.left = Node('to my room')
tree.right.left.right = Node('to the garage')

tree.right.right = Node('the window')
tree.right.right.left = Node('a little bit')
tree.right.right.right = Node('wide open')

print(tree.decode('LRR'))
print(tree.decode('RLL'))