"""Find whether two people in an undirected graph are friends.

Let's create a graph and add a bunch of people:

    >>> f = FriendGraph()
    >>> f.add_person("Frodo")
    >>> f.add_person("Sam")
    >>> f.add_person("Gandalf")
    >>> f.add_person("Merry")
    >>> f.add_person("Pippin")
    >>> f.add_person("Treebeard")
    >>> f.add_person("Sauron")
    >>> f.add_person("Dick Cheney")

Now, let's set some friendships:

    >>> f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
    >>> f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
    >>> f.set_friends("Merry", ["Pippin", "Treebeard"])
    >>> f.set_friends("Pippin", ["Treebeard"])
    >>> f.set_friends("Sauron", ["Dick Cheney"])

We specifically said Sam was a friend of Frodo's, so they should be
connected:

    >>> f.are_connected("Frodo", "Sam")
    True

Our ``set_friends()`` sets the reciprocal relationship automatically
(this is an "undirected graph"), so Sam is also friends with Frodo:

    >>> f.are_connected("Sam", "Frodo")
    True

Sam isn't friends with Treebeard -- but we can find a connection
(Sam -> Frodo -> {Merry or Pippin} -> Treebeard)

    >>> f.are_connected("Sam", "Treebeard")
    True

Poor Sauron. He won't be invited to Frodo's tea party:

    >>> f.are_connected("Frodo", "Sauron")
    False

He does have friends of his own, though:

    >>> f.are_connected("Sauron", "Dick Cheney")
    True

Joel Burton <joel@joelburton.com>
"""


class PersonNode(object):
    """A node in a graph representing a person.

    This is created with a name and, optionally, a list of adjacent nodes.
    """

    def __init__(self, name, adjacent=[]):
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<PersonNode %s>" % self.name


class FriendGraph(object):
    """Graph to keep track of social connections."""

    def __init__(self):
        """Create an empty graph.

        We keep a dictionary to map people's names -> nodes.
        """

        self.nodes = {}

    def add_person(self, name):
        """Add a person to our graph.

            >>> f = FriendGraph()
            >>> f.nodes
            {}

            >>> f.add_person("Dumbledore")
            >>> f.nodes
            {'Dumbledore': <PersonNode Dumbledore>}
        """

        if name not in self.nodes:
            # Be careful not to just add them a second time -- otherwise,
            # if we accidentally added someone twice, we'd clear our their list
            # of friends!
            self.nodes[name] = PersonNode(name)

    def set_friends(self, name, friend_names):
        """Set two people as friends.

        This is reciprocal: so if Romeo is friends with Juliet, she's
        friends with Romeo (our graph is "undirected").

        >>> f = FriendGraph()
        >>> f.add_person("Romeo")
        >>> f.add_person("Juliet")
        >>> f.set_friends("Romeo", ["Juliet"])

        >>> f.nodes["Romeo"].adjacent
        set([<PersonNode Juliet>])

        >>> f.nodes["Juliet"].adjacent
        set([<PersonNode Romeo>])
        """

        person = self.nodes[name]

        for friend_name in friend_names:
            friend = self.nodes[friend_name]

            # Since adjacent is a set, we don't care if we're adding duplicates --
            # it will only keep track of each relationship once. We do want to
            # make sure that we're adding both directions for the relationship.
            person.adjacent.add(friend)
            friend.adjacent.add(person)

    """
        given two names
        initiate set of seen nodes

        BASE CASE:
            node1.name is name2
            node1 has been seen

        checking all node.adjacent
        add to seen


        while things to check has stuff in it:
            node1 = to check.pop()
            see if not in seen

                see if == node 2
                    return true
                add adjacencies to set of things to check
                add node 1 to seen

        return false
    """

    def __connected_r__(self, node, name2, seen):
        if node.name == name2:
            return True
        # if node.name in seen:
        #     return False
        seen.add(node)
        for name in node.adjacent:
            if name not in seen:
                if self.__connected_r__(name, name2, seen):
                    return True
        return False

    def are_connected(self, name1, name2):
        """Is this name1 friends with name2?"""

        seen = set([])
        node = self.nodes[name1]
        return self.__connected_r__(node, name2, seen)




        # while to_check:
        #     node1 = to_check.pop()
        #     if node1 not in seen:
        #         if node1.name == name2:
        #             return True
        #         for friend in node1.adjacent:
        #             to_check.add(self.nodes[friend.name])
        #         seen.add(node1)

        # return False

        """

        """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
