# -*- coding: utf-8 -*-


class Vertex():

    def __init__(self, value=None):
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def __unicode__(self):
        return "<Graph Vertex, \"%s\" >" % self.value

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class Edge ():

    def __init__(self, vertex_one=None, vertex_two=None):
        self.vertex_1 = vertex_one
        self.vertex_2 = vertex_two

    def setVertexOne(self, vertex):
        self.vertex_1 = vertex

    def setVertexTwo(self, vertex):
        self.vertex_2 = vertex

    def setVertices(self, vertices):
        if isinstance(vertices, list) and len(vertices) == 2:
            self.vertex_1, self.vertex_2 = vertices
            return True
        return False

    def isEdgeOfVertex(self, vertex):
        if vertex == self.vertex_1 or vertex == self.vertex_2:
            return True
        return False

    def isConnecting(self, vertices):
        if isinstance(vertices, list) and len(vertices) == 2:
            if (self.vertex_1, self.vertex_2 == vertices) or (self.vertex_2, self.vertex_1 == vertices):
                return True
        return False

    def getVertices(self):
        return (self.vertex_1, self.vertex_2)

    def __unicode__(self):
        return "<Graph Edge, [%s - %s] >" % (self.vertex_2, self.vertex_2)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class Graph():

    def __init__(self, vertices=None, edges=None):
        # todo: check of params
        self.vertices = None
        self.edges = None

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addEdge(self, edge):
        self.edges.append(edge)

    def getEdges(self, vertex):
        if not vertex in self.vertices:
            # may be  we should raise exception
            return []
        connected_vertices = []
        for e in self.edges:
            if e.isEdgeOfVertex(vertex):
                connected_vertices.append(e)
        return connected_vertices

    def __unicode__(self):
        return "<Graph , vertices - %d, edges - %d>" % (len(self.vertices), len(self.edges))

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
