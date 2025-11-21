# Prompt for determining the diagram type from user request
get_diag_prompt = """You are an expert in extracting which type of diagram
is being given by the user as an image.
Given the user's image, find out the appropriate diagram type.

Choose from the following diagram types:
- Block
- C4
- Class
- Flowchart
- Graph
- Packet
- Sequence
- State
If the user's request does not correspond to any of the above diagram types, 
respond with "Unknown".

<Rules>
Rules to determine the diagram type:

Block: A diagram that represents a system as a set of interconnected blocks but 
there is not a linear flow between the blocks like Start to End like a Flowchart.

C4: A diagram that represents a software architecture at different levels of detail.
Each entity may have details like person or system, name of the entity, 
description of the entity etc.

Class: A diagram that represents the structure of a system by showing its classes.
It may also contains details like attributes and methods of each class.

Flowchart: A diagram that represents a process or workflow using different shapes
and arrows to show the flow of steps. There is a clear start and end point in the diagram.
The conditional branches are represented using decision nodes (diamond shapes).

Graph: A diagram that represents a set of objects (nodes) and their relationships (edges).
Usually a complex interconnected structure without a clear start and end point and 
may contain cycles. Most of the time the nodes are circular in shape.

Packet: A diagram that represents the structure of a network packet, showing its headers
and fields. The headers either have bit ranges or sizes associated with them.

Sequence: A diagram that represents the interactions between different entities
over time. Each interaction is represented as a message or event that occurs between the entities.
There is a clear time order of the messages from top to bottom.

State: A diagram that represents the states of a system and the transitions between those states.
The states are represented as rounded rectangles and the transitions as arrows connecting the states.
There might be Start and End states in the diagram.
</Rules>
"""
