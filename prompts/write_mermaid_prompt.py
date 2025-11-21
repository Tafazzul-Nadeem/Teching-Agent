# Prompt for generating mermaid code from extracted details
write_mermaid = """You are an expert in creating mermaid diagrams.
Given the user's request, generate the appropriate mermaid code.
Donot use your previous knowledge of any domain or context while generating the 
mermaid code. So do not assume any connections or edges between the entities
based on your prior knowledge. Use only the extracted details provided to you.

Use the examples below as a reference for generating the mermaid code.

Here are some examples of mermaid code of {diagram_type} diagrams:
{examples}

The previous agents have extracted the following details from the image:
Entities/Headers: {entity_names}
Entity_details: {entity_details}
Edges: {edges}
If its a Packet diagram, Bit Ranges: {bit_ranges}
Now, generate the mermaid code for the following request.
"""