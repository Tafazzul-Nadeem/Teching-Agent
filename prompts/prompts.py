###############################################################################
# Prompt for determining the diagram type from user request
supervisor_get_diag = """You are an expert in creating mermaid diagrams.
Given the user's request, find out the appropriate diagram type.

Choose from the following diagram types:
- Block
- C4
- Class
- Flowchart
- Graph
- Packet
- Sequence
- State
 If the user's request does not correspond to any of the above diagram types, respond with "Unknown".
"""

###############################################################################
# Prompts for extracting the details of entities like block names, headers etc.
ocr_extract_entity = {
# Block Diagram 
    "Block" : """You are an expert in extracting text from images.
Given an image containing a Block diagram, extract the names of all blocks present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all block names present in the Block diagram.
""",

# C4 Diagram
    "C4" : """You are an expert in extracting text from images.
Given an image containing a C4 diagram, extract the details of all the systems present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all system names present in the C4 diagram.
""",

# Class Diagram
    "Class" : """You are an expert in extracting text from images.
Given an image containing a Class diagram, extract the details of all the classes present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all system names present in the Class diagram.
""",

# Flowchart Diagram
    "Flowchart" : """You are an expert in extracting text from images.
Given an image containing a Flowchart diagram, extract the names of all nodes present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all node names present in the Flowchart diagram.
""",

# Graph Diagram
    "Graph" : """You are an expert in extracting text from images.
Given an image containing a Graph diagram, extract the names of all nodes present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all node names present in the Graph diagram.
""",

# Packet Diagram
"Packet" : """You are an expert in extracting text from images.
Given an image containing a Packet diagram, extract all the headers present 
in the diagram. Extract all the headers even if it is repeating and maintain the order
of appearance of the repeating headers. Do not omit repeating headers. 
Do not extract the bit ranges of the headers.

Return the names of the headers in the same order as present in the Packet Diagram.

Use the following rules to extract the headers:
Rule 1: Scan the image row by row from top to bottom.
Rule 2: Extract one header at a time and store it in a running list.
Rule 3: Extract the next header and append it to the running list.
Rule 4: If a header is repeating, still append it to the running list. So, the running list
may contain repeating headers.
Rule 5: Repeat until all headers are extracted.

Return your output as a list strictly following the JSON format with the keys:
-"n_entities": Length of the running list (Number of headers present 
(including repeating headers) in the Packet Diagram).
- "entity_names": Contents of the running list (Header names).
"""
}


###############################################################################
# Prompts for extracting the edge labels between entities
ocr_extract_edges = {
# Block Diagram
    "Block" : """You are an expert in extracting text from images.
Given an image containing a Block diagram, extract the names of all blocks and the edge labels of
the diagram.

If there are no edge labels, return an empty list for edge labels, i.e. [].

Return your result strictly as a JSON with the keys:
"edges": A list of triplets representing the edges in the format (source_node, edge_label, target_node).
""",

# C4 Diagram
    "C4" : """You are an expert in extracting text from images.""",

# Class Diagram
    "Class" : """You are an expert in extracting text from images.""",

# Graph Diagram
    "Graph" : """You are an expert in extracting edges from images.
Given an image containing a Graph diagram, extract all the edges along 
with its edge label (if present) from the diagram.

Return your result strictly as a JSON with the keys:
"edges": A list of edges in the format "source_node - edge_label - target_node".
If there are no edge labels return the edge as "source_node - - target_node".
For example: ['User - uses - Web App', 'Web App -  - Database']
""",

# Flowchart Diagram
    "Flowchart" : """You are an expert in extracting edges from images.
Given an image containing a Flowchart diagram, extract all the edges along 
with its edge label (if present) from the diagram.

Do not use any prior information about the image, just extract the edges if it is 
present in the image. For example, even if there should be an between two nodes based on
common sense or prior knowledge, but it is not present in the image, do not add that edge.

Think step by step.
Step 1: Identify all the nodes present in the diagram.
Step 2: Identify the number of edges present in the diagram.
Step 3: For each edge, identify the source node, target node and edge label (if present).
Step 4: Construct the edge in the format "source_node - edge_label - target_node". 
If there is no edge label, use " " in place of edge label.

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
"""

}


###############################################################################
# Prompt for generating mermaid code from extracted details
write_mermaid = """You are an expert in creating mermaid diagrams.
Given the user's request, generate the appropriate mermaid code.
Use the examples below as a reference for generating the mermaid code.

Here are some examples of mermaid code of {diagram_type} diagrams:
{examples}

The previous agents have extracted the following details from the image:
Entities/Headers: {entity_names}
Edges: {edges}
If its a Packet diagram, Bit Ranges: {bit_ranges}
Now, generate the mermaid code for the following request.
"""