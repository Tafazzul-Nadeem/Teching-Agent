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
of appearance of the headers. Dont extract the bit ranges of the headers.

Return the names of the headers in the same order as present in the Packet Diagram.
Return your output as a list strictly following the JSON format with the keys:
- "entity_names": A list of all header names present in the Packetdiagram.
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

Return your result strictly as a JSON with the keys:
"edges": A list of edges in the format "source_node - edge_label - target_node".
If there are no edge labels return the edge as "source_node - - target_node".
For example: ['User - uses - Web App', 'Web App -  - Database']
""",    

# Packet Diagram
    "Packet" : """You are an OCR agent and you job is extracting the bit ranges 
of the headers in a Packet Diagram.

Use the following rules to extract the bit ranges:
- Each header has a specific bit range associated with it. If you find the boundary with only one
number say n, then associate it as an ending bit of previous header and n+1 as 
the starting bit of next header.

The previous agent have extracted the following headers from the diagram:
Headers: {entity_names}
Now, extract the bit ranges of each header in the diagram in order."""
}


###############################################################################
# Prompt for generating mermaid code from extracted details
write_mermaid = """You are an expert in creating mermaid diagrams.
Given the user's request, generate the appropriate mermaid code.
Use the examples below as a reference for generating the mermaid code.

Here are some examples of mermaid code of {diagram_type} diagrams:
{examples}

The previous agents have extracted the following details from the image:
Entities: {entity_names}
Edge Triplets: {edges}
If its a Packet diagram, Bit Ranges: {bit_ranges}
Now, generate the mermaid code for the following request.
"""