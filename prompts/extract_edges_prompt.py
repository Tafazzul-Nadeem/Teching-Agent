# Prompts for extracting the edge labels between entities
ocr_extract_edges = {
# Block Diagram
    "Block" : """You are an OCR agent and your job is extracting the block-edge-block 
triplets in the given Block Diagram.

Ignore all prior assumptions and context about Block Diagrams and
donot make any assumption regarding the diagram while extracting the block-edge-block triplets.
So, donot hallucinate and add any edges based on your prior knowledge of the domain or context.
Use only the visual information provided in the Block Diagram to extract the 
block-edge-block triplets present in the diagram.

Given an image containing a Block diagram and names of the blocks, extract the 
edges and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Left to Right and Top to Bottom.
Rule 2: Identify the number of edges present in the diagram.
Rule 3: For each edge, identify the source block, target block and edge label (if present).
Rule 4: Construct the edge in the format "source_block - edge_label - target_block". 
If there is no edge label, use " " in place of edge label.
Rule 5: If there are no edges, return an empty list for edges, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of edges detected in the image.
"edges": A list of edges in the format "source_block - edge_label - target_block".
If there are no edge labels return the edge as "source_block - - target_block".
For example: ['Science - room - 101', 'Alice -  - Maths']
""",

# C4 Diagram
    "C4" : """You are an OCR agent and your job is extracting the node-edge-node 
triplets in the given C4 Diagram.

Ignore all prior assumptions and context about C4 Diagrams and donot make any 
assumption regarding the diagram while extracting the node-edge-node triplets.
So, donot add any edges based on your prior knowledge of the domain or context.
Use only the visual information present in the C4 Diagram to extract the 
node-edge-node triplets present in the diagram.

Given an image containing a C4 diagram and names of the entities, extract the 
edges and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Left to Right and Top to Bottom.
Rule 2: Identify the number of edges present in the diagram.
Rule 3: For each edge, identify the source entity, target entity and edge label (if present).
Rule 4: Construct the edge in the format "source_entity - edge_label - target_entity". 
If there is no edge label, use " " in place of edge label.
Rule 5: If there are no edges, return an empty list for edges, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of edges detected in the image.
"edges": A list of edges in the format "source_node - edge_label - target_node".
If there are no edge labels return the edge as "source_node - - target_node".
For example: ['Science - room - 101', 'Alice -  - Maths']
""",

# Class Diagram
    "Class" : """You are an OCR agent and your job is extracting the class-Relationship-class 
triplets in the given Class Diagram. 

Ignore all prior assumptions and context about Class Diagrams and
donot make any assumption regarding the diagram while extracting the class-Relationship-class triplets.
So, donot add any edges based on your prior knowledge of the domain or context.
Use only the visual information provided in the Class Diagram to extract the 
class-Relationship-class triplets present in the diagram.

Given an image containing a Class diagram and names of the classes, extract the 
relationships and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Left to Right and Top to Bottom.
Rule 2: Identify the number of Relationships present in the diagram.
Rule 3: For each edge, identify the source class, target class and type of Relationship
between the classes
Rule 4: Construct the edge in the format "source_class - relationship_type - target_class". 
Rule 5: If there are no relationships, return an empty list for edges, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of relationships detected in the image.
"edges": A list of relationships in the format "source_class - relationship_type - target_class".
If there are no relationship types return the relationship as "source_class - - target_class".
For example: ['Science - Inheritance - Subject', 'Student - Association - Maths']
""",

# Graph Diagram
    "Graph" : """You are an OCR agent and your job is extracting the node-edge-node 
triplets in the given Graph Diagram.
    
Ignore all prior assumptions and context about Graph Diagrams and
donot make any assumption regarding the diagram while extracting the node-edge-node triplets.
So, donot add any edges based on your prior knowledge of the domain or context.
Use only the visual information provided in the Graph Diagram to extract the 
node-edge-node triplets present in the diagram.

Given an image containing a Graph diagram and names of the nodes, extract the 
edges and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Left to Right and Top to Bottom.
Rule 2: Identify the number of edges present in the diagram.
Rule 3: For each edge, identify the source node, target node and edge label (if present).
Rule 4: Construct the edge in the format "source_node - edge_label - target_node". 
If there is no edge label, use " " in place of edge label.
Rule 5: If there are no edges, return an empty list for edges, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of edges detected in the image.
"edges": A list of edges in the format "source_node - edge_label - target_node".
If there are no edge labels return the edge as "source_node - - target_node".
For example: ['Science - room - 101', 'Alice -  - Maths']
""",

# Flowchart Diagram
    "Flowchart" : """You are an OCR agent and your job is extracting the node-edge-node 
triplets in the given Flowchart Diagram.
    
Ignore all prior assumptions and context about Flowchart Diagrams and
donot make any assumption regarding the diagram while extracting the node-edge-node triplets.
So, donot add any edges based on your prior knowledge of the domain or context.
Use only the visual information provided in the Flowchart Diagram to extract the 
node-edge-node triplets present in the diagram.

Given an image containing a Flowchart diagram and names of the nodes, extract the 
edges and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Left to Right and Top to Bottom.
Rule 2: Identify the number of edges present in the diagram.
Rule 3: For each edge, identify the source node, target node and edge label (if present).
Rule 4: Construct the edge in the format "source_node - edge_label - target_node". 
If there is no edge label, use " " in place of edge label.
Rule 5: If there are no edges, return an empty list for edges, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of edges detected in the image.
"edges": A list of edges in the format "source_node - edge_label - target_node".
If there are no edge labels return the edge as "source_node - - target_node".
For example: ['Science - room - 101', 'Alice -  - Maths']
""",    

# Packet Diagram
    "Packet" : """You are an OCR agent and you job is extracting the bit ranges 
of the headers in a Packet Diagram.

Ignore all prior knowledge, assumptions, and context about Packet Diagrams.
Use only the visual information provided in the Packet Diagram to extract the 
bit ranges of each header.

Think step by step.
Step 1: For each header identify the start bit. The start bit of the first header is always 0.
The start bit of subsequent header is the next bit after the end bit. 
For example, if a header spans from bit 0 to bit 7,  the next header should start from bit 8.
The end bit of previous header cannot be used as the start bit of the next header.

Step 2: Identify the end bit. If the boundary bit as shown in diagram is say '10' 
in the Packet Diagram, then '10' should be the end bit of the current header and NOT '9'.
Hence, there should be no overlap between the headers.

Step 3: Construct the bit range in the format "start_bit - end_bit".
Finally, the bit ranges should look like:
"0-a", "(a+1)-b", "(b+1)-c" and so on.

Here is an example of a Packet Diagram Mermaid Code which can aid you in extracting the bit ranges:
```mermaid
packet-beta
    0-7: "Flag"
    8-15: "Address"
    16-23: "Control"
    24-55: "Payload"
    56-87: "FCS"
    88-95: "Flag"
```

The previous agent have extracted the following headers from the diagram:
Number of Headers: {n_entities}
Headers: {entity_names}
Now, extract the bit ranges of each header in the diagram in order.
It is possible that some headers may repeat. Make sure to extract the bit ranges
for each occurrence of the header in the same order as they appear in the diagram.
Make sure that

Return your result strictly as a JSON with the keys:
'bit_ranges': A list of bit ranges for each header in the format "start_bit - end_bit".
'edges': [] (as it is a Packet Diagram with no edges).
""",

# Sequence Diagram
    "Sequence" : """You are an OCR agent and your job is extracting the entity-message-entity 
triplets in the given Sequence Diagram.

Ignore all prior assumptions and context about Sequence Diagrams and donot make any 
assumption regarding the diagram while extracting the entity-message-entity triplets.
So, donot add any edges based on your prior knowledge of the domain or context.
Use only the visual information present in the Sequence Diagram to extract the 
entity-message-entity triplets present in the diagram.

Given an image containing a Sequence diagram and names of the entities, extract the 
edges and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Top to Bottom.
Rule 2: Identify the number of messages present in the diagram. A message is represented
as an arrow from one entity to another.
Rule 3: For each message, identify the source entity, target entity and message.
Rule 4: Construct the message in the format "source_entity - message - target_entity". 
Rule 5: If there are no messages, return an empty list for messages, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of messages detected in the image.
"edges": A list of messages in the format "source_entity - message - target_entity".
For example: ['Service - Check Connection - Database', 'Alice - How are you? - John']
""",

# State Diagram
    "State" : """You are an OCR agent and your job is extracting the state-transition-state
triplets in the given State Diagram.

Ignore all prior assumptions and context about State Diagrams and
donot make any assumption regarding the diagram while extracting the node-transition-node triplets.
So, donot add any edges based on your prior knowledge of the domain or context.
Use only the visual information provided in the State Diagram to extract the 
node-transition-node triplets present in the diagram.

Given an image containing a State diagram and names of the nodes, extract the 
edges and the edge labels (if any) in the diagram.

Entity Names: {entity_names}

<Rules>
Rule 1: Scan the image from Left to Right and Top to Bottom.
Rule 2: Identify the number of edges present in the diagram.
Rule 3: For each transition, identify the source node, target node and edge label (if present).
Rule 4: Construct the edge in the format "source_state - edge_label - target_state". 
If there is no edge label, use " " in place of edge label.
Rule 5: If there are no edges, return an empty list for edges, i.e. [].
</Rules>

Return your result strictly as a JSON with the keys:
"n_edges": Number of edges detected in the image.
"edges": A list of edges in the format "source_state - edge_label - target_state".
If there are no edge labels return the edge as "source_state - - target_state".
For example: ['Confirm payment - TransactionId - Payment Confirmed', 'Run DB -  - DB Connected']
"""

}