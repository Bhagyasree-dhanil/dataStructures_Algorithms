"""
Trees are used to represent hierarchical data structures.

"""


class Treenode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("Laptop")
    root.add_child(laptop)

    laptop.add_child(Treenode("Dell"))
    laptop.add_child(Treenode("Lenova"))
    laptop.add_child(Treenode("Mac"))

    cellphone = Treenode("cellphone")
    root.add_child(cellphone)

    cellphone.add_child(Treenode("samsung"))
    cellphone.add_child(Treenode("vivo"))
    cellphone.add_child(Treenode("iphone"))

    television = Treenode("Television")
    root.add_child(television)

    television.add_child(Treenode("Dell"))
    television.add_child(Treenode("Lenova"))
    television.add_child(Treenode("Mac"))

    return root


'''
if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass
'''

# ========================================= Exercise 1 ==================================================#

"""
Data structures exercise: General Tree
Below is the management hierarchy of a company.

Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
 As shown below,

Here is how your main function should will look like,

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
"""


class Trees:

    def __init__(self, name, des):
        self.name = name
        self.des = des
        self.children = []
        self.parents = None

    def add_child(self, child):
        child.parents = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parents
        while p:
            level += 1
            p = p.parents
        return level

    def print_tree(self, prop):

        if prop == "name":
            print_content = self.name
        if prop == "designation":
            print_content = self.des
        if prop == "both":
            print_content = self.name + ' (' + self.des + ')'

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parents else ""
        print(prefix + print_content)
        if self.children:
            for child in self.children:
                child.print_tree(prop)


def build_management_tree():
    # level 0
    root= Trees("Nilupal", "CEO")

    # level 1
    cto = Trees("Chinmay", "CTO")
    hr = Trees("Gels", "HR HEAD")
    root.add_child(cto)
    root.add_child(hr)

    # level 2
    inf = Trees("Vishwa", "Cloud manager")
    cto.add_child(inf)
    inf.add_child(Trees("Dhaval" , "Cloud Manager"))
    inf.add_child(Trees("Abhijith", "App Manager"))

    cto.add_child(Trees("Aamir", "Application head"))

    hr.add_child(Trees("Peter", "Recruitment Manager"))
    hr.add_child(Trees("Waqas", "Policy Manager"))

    return root

'''
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
'''

# ======================= Exercise -2 =========================================================#
"""

Build below location tree using TreeNode class

Now modify print_tree method to take tree level as input.
And that should print tree only upto that level as shown below,

"""


class TreeStructure:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parents = None

    def add_child(self, child):
        child.parents = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parents
        while p:
            level += 1
            p = p.parents
        return level

    def print_tree(self, level):
        if self.get_level() <= level:
            spaces = " " * self.get_level() * 3
            prefix = spaces + "|__" if self.parents else ""
            print(prefix+self.data)
        for child in self.children:
            child.print_tree(level)


def build_location_tree():

    # level 0
    root = TreeStructure("Global")

    # level 1
    ind = TreeStructure("India")
    usa = TreeStructure("USA")
    root.add_child(ind)
    root.add_child(usa)

    # level 2
    guj = TreeStructure("Gujarat")
    kar = TreeStructure("Karnataka")
    ind.add_child(guj)
    ind.add_child(kar)

    nj = TreeStructure("New Jersey")
    cal = TreeStructure("California")
    usa.add_child(nj)
    usa.add_child(cal)

    # level 3
    guj.add_child(TreeStructure("Ahmedabad"))
    guj.add_child(TreeStructure("Baroda"))

    kar.add_child(TreeStructure("Bangalore"))
    kar.add_child(TreeStructure("Mysore"))

    nj.add_child(TreeStructure("princeton"))
    nj.add_child(TreeStructure("Trenton"))

    cal.add_child(TreeStructure("San Francisco"))
    cal.add_child(TreeStructure("Mountain View"))
    cal.add_child(TreeStructure("Palo Alto"))

    return root


if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)


