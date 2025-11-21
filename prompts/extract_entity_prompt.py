# Prompts for extracting the details of entities like block names, headers etc.
# and their details.
ocr_extract_entity = {
# Block Diagram 
    "Block" : """You are an expert in extracting text from images.
Given an image containing a Block diagram, extract the names of all blocks present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "n_entities": Number of blocks present in the Block diagram.
- "entity_names": A list of all block names present in the Block diagram.
""",

# C4 Diagram
    "C4" : """You are an expert in extracting details of C4 diagrams from images.
Given an image containing a C4 diagram, extract the details of all the entities 
present in the diagram.

Return your result strictly as a JSON with the keys:
- "n_entities": Number of entities present in the C4 diagram.
- "entity_names": A list of name of all the entities present in the C4 diagram.
- "entity_details": A list of entities and its details in the format 
"entity_type (present at the top of each entity) - entity_name - entity_description".
For example: ["Person - Event Manager - Organizes the event", 
"system_db - Event Booking Database - Stores Customer Booking Information"]
""",

# Class Diagram
    "Class" : """You are an expert in extracting details of Class diagrams from images.
Given an image containing a Class diagram, extract the names and details of all 
the classes present in the diagram.

Return your result strictly as a JSON with the keys:
- "n_entities": Number of entities present in the Class diagram.
- "entity_names": A list of all class names present in the Class diagram.
- "entity_details": A list of classes and its details in the format 
"class_name - attributes - methods".
For example: ["Engine - Attributes: +capacity: float, +number-of-cylinders: int - Methods: +start(), +brake(), +accelerate()" ]
""",

# Flowchart Diagram
    "Flowchart" : """You are an expert in extracting text from images.
Given an image containing a Flowchart diagram, extract the names of all nodes present 
in the diagram.

Return your result strictly as a JSON with the keys:
- "n_entities": Number of entities present in the Flowchart diagram.
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
-"entity_names": Contents of the running list (Header names).
""",

# Sequence Diagram
    "Sequence" : """You are an expert in extracting text from images.
Given an image containing a Sequence diagram, extract the details of all the messages present
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all message names present in the Sequence diagram.
""",

# State Diagram
    "State" : """You are an expert in extracting text from images.
Given an image containing a State diagram, extract the details of all the states present
in the diagram.

Return your result strictly as a JSON with the keys:
- "entity_names": A list of all state names present in the State diagram.
""",
}
