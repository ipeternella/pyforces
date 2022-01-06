# Trees vs Graphs

## Properties

Some properties of trees to distinguish them as a subset of graphs:

- Trees do not have cycles
- Trees should be connected (no disconnected vertices)
- Every pair of vertices have exatcly ONE path between them (always connected)
  - If there are N nodes and M edges, for a tree we have: M = (N - 1) edges
- If there's a connected structure with (N - 1) edges, than it's tree
- If there are N nodes, there are (N - 1) parents (root has no parent)

```text
+ - - - - - - - +
| Graphs G(V,E) |
|               |
|    + - - - +  |
|    | Trees |  |
|    + - - - +  |
+ - - - - - - - +
```

## Definitions

- `Root node`: beginning of the tree, node which "hangs" the tree. Only node without a parent
- `Leaf node`: nodes that have no children
- `Parent node`: node that is immediately superior (immediate ancestor) to the current node
- `Ancestor node`: All nodes which lie on the path from the current node to the root node
  - current node can be considered as an ancestor of itself (depends on the definition)
  - all nodes below an ancestor are its descendants
- `Subtree`: if X is a an ancestor of Y, then Y is in the subtree of X

## Graphs Examples

```
    (1)
  /     \
(2) --- (3)  <--- contains cycles

    (1)
  /
(2)      (5) <-- disconnected graph
   \
   (3)
  /
(4)
```

## Forest Examples

It's a disconnected graph composed of:

- Several individual trees
- Each trees naturally CANNOT have a cycle or it's not a forest

```
Forest:

        (1)          (4)      (7)
       /   \        /   \        \
     (2)   (3)    (5)   (6)      (8)

NOT a Forest:

        (1)          (4)      (7)
      /     \       /   \        \
    (2) --- (3)   (5)   (6)      (8)

```

## Trees examples

```
    (1)   <-- root
   /   \
(2)     (5)
    \
    (3)  <-- (3) is a descendant of ancestor (2)
   /
(4) <-- leaf
```

## LCA - Lowest Common Ancestor of Trees

LCA is a vertex which lies on the path from the root to V1 and also on the path from the root to V2
and must be the lowest vertex.

Properties:

- LCA is the bottom-most ancestor of V1 and V2;
- LCA lies on the shortest path from V1 to V2
- all path-related problems use LCA

Some forms to compute:

- Two pointers
- Euler tour
- Binary lifting

Some examples:

```
          (1)
       /   |   \
     (2)  (10)  (3)
    /   \          \
  (4)   (5)        (6)
  /     /             \
(9)   (8)              (7)
                         \
                        (11)
```

- `LCA(9, 8)`: 2
- `LCA(6, 11)`: 6

### DFS trees on Graphs

By performing a DFS on a graph, `backedges` (edges that would lead back to already visited nodes) are not visited, so by performing a DFS on a graph, one can obtain and build a DFS Tree (without cycles).

`Backedges`: edges that denote a cycle on a graph!

- Be careful with backedges on `undirected` graphs as every v1 vertex that points to a v2 vertex also has v2 pointing back to v1 (no direction)
- Backedges can be used to detect cycles on a graph!
- Every graph has several DFS trees -> depends on where the root node begins!
