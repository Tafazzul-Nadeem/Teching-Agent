block_examples = """Example 1:
```mermaid
block-beta
columns 4
    WhatsApp["WhatsApp"]:1 space space Meta["Meta"]:1 

    WhatsApp -- "owned by" --> Meta
```

Example 2:
```mermaid
block-beta
columns 7
    ACMainsInput["AC Mains Input"]:1 space space space space space Output["Output"]:1
    space space space space space space space
    Transformer["Transformer"]:1 space Rectifier["Rectifier"]:1 space Filter["Filter"]:1 space Regulator["Regulator"]:1

    ACMainsInput --> Transformer
    Transformer --> Rectifier
    Rectifier --> Filter
    Filter --> Regulator
    Regulator --> Output
```

Example 3:
```mermaid
block-beta
columns 3
    Households["Households"]:1 space Firms["Firms"]:1
    space space space
    Markets["Markets"]:1 space Government["Government"]:1
    space space space
    ForeignSector["Foreign Sector"]:1 space Banks["Banks"]:1

    Households --> Banks
    Households --> Markets
    Firms --> Households
    Firms --> Markets
    Firms --> ForeignSector
    Government --> Firms
    Government --> Households
    ForeignSector --> Markets
    Banks --> Firms
```
"""

packet_examples = """Example 1:
```mermaid
packet-beta
    0-7: "Flag"
    8-15: "Address"
    16-23: "Control"
    24-55: "Payload"
    56-87: "FCS"
    88-95: "Flag"
```

Example 2:
```mermaid
packet-beta
    0-20: "Source Port"
    21-29: "Destination Port"
    30-50: "Reserved"
    51-59: "Checksum"
    60-80: "Flag"
    81-89: "Data Offset"
    90-110: "Data"
    111-130: "Sequence Number"
    131-145: "Window Size"
```

Example 3:
```mermaid
packet-beta
    0-15: "Hardware Type"
    16-31: "Protocol Type"
    32-39: "Hardware Length"
    40-47: "Protocol Length"
    48-63: "Operation"
    64-95: "Sender Header Address"
    96-127: "Sender Prorocol Address"
    128-159: "Target Hardware Address"
    160-191: "Target Protocol Address"
```
"""