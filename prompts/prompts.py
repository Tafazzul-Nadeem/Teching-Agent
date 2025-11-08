get_diag = """You are an expert in creating mermaid diagrams.
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

ocr_extract = """You are an expert in extracting text from images.
Given an image containing a mermaid diagram, extract the names of all entities and the edge labels of
the diagram.

If there are no edge labels, return an empty list for edge labels, i.e. [].
"""

write_mermaid = """You are an expert in creating mermaid diagrams.
Given the user's request, generate the appropriate mermaid code.
Use the examples below as a reference for formatting.

Here are some examples of mermaid code of {diagram_type} diagrams:
{examples}

Now, generate the mermaid code for the following request:
```mermaid
<mermaid_code>
```
"""