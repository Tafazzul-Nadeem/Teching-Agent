mermaid_example = {
# Block diagram examples
    "Block" : """Example 1:
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
""",

# C4 diagram examples
"C4" : """Example 1:
```mermaid
C4Context

        Enterprise_Boundary(b1, "Company Boundary") {
            Person(Patient, "Patient", "Book Appointments or view reports")
            System(HospitalPortal, "Hospital Portal", "System for patient services and medical reports")
    }
    Rel(Patient, HospitalPortal, "Book Appointments/Check Reports")
 UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

Example 2:
```mermaid
C4Context

        Enterprise_Boundary(b1, "Personnel Boundary") {
            Person(Technician, "Technician", "Any technician on call")
    }
        Enterprise_Boundary(b2, "System Boundary 1") { 
            SystemDb(ProductDatabase, "Product Database", "Stores product info")
            System(ChatSystem, "Chat System", "A Chat System")
    }
    Rel(Technician, ProductDatabase, "Uses")
    Rel(ProductDatabase, ChatSystem, "Creates request to")

 UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="3")
```

Example 3:
```mermaid
C4Context
        Enterprise_Boundary(b1, "Enterprise Boundary") {
            Person(Engineer, "Engineer", "An engineer of company")
            SystemDb(QueueingDatabase, "Queueing Database", "Stores queueing information")
            SystemDb(RegistrationDatabase, "Registration Database", "Stores registration information")
            System(ExaminationSystem, "Examination System", "An examination system")
            System(CarRentalSystem, "Car Rental System", "A car rental system")
    }
    Rel(Engineer, ExaminationSystem, "operates on")
    Rel(QueueingDatabase, RegistrationDatabase, "sends data")
    Rel(ExaminationSystem, CarRentalSystem, "sends data")

 UpdateLayoutConfig($c4ShapeInRow="4", $c4BoundaryInRow="3")
```
 """,

# Class diagram examples
"Class" : """Example 1:
```mermaid
classDiagram
    class BankAccount {
        -owner: String
        -balance: Dollars
        -deposit(amount: Dollars)
        -withdrawal(amount: Dollars)
    }

    class CheckingAccount {
        -insufficientFundFee: Dollars
        -processCheck(checkToProcess: Check)
        -withdrawal(amount: Dollars)
    }
    class SavingsAccount {
        -annualInterestRate: Percent
        -DepositMonthlyInterest()
        -withdrawal(amount: Dollars)
    }
    BankAccount <|-- CheckingAccount
    BankAccount <|-- SavingsAccount
```

Example 2:
```mermaid
classDiagram
    class bank_account {
        #balance
        +process_account_holder(tuple)
        -fetch_ifsc_code(Bool)
    }

    class doctor {
        #doctor_name
        -doctor
        #fetch_doctor_phone(float)
        -get_doctor_email(bool)
        #insert_doctor_id(bool)
    }
    class Services {
        -service_name
        -Service_description
        #remove_service(tuple)
        +remove_service_fee(float)
    }
    class patient {
        +patient_address
        -patient_name
        +change_patient_address(int)
    }
    bank_account <|.. doctor
    doctor <|-- Services
    doctor <|-- patient
```

Example 3:
```mermaid
classDiagram
    class Order{
        +DateReceived
        +isPrepaid
        +Number
        +Price
        -Dispatch
        -Close
    }
    class Customer{
        +name
        +address
        +creditRating
    }
    class OrderLine {
        +product
        +quantity
        +price
    }
    class CorporateCustomer {
        -contactName
        -Remind()
    }
    class PersonalCustomer {
        -creditCardID
    }
    Order -- Customer
    Order -- OrderLine
    Customer <|-- CorporateCustomer
    Customer <|-- PersonalCustomer
```
""",

# Flowchart diagram examples
"Flowchart" : """Example 1:
```mermaid
flowchart TD
    A(["Start"]) --> B{"Door
    unlocked?"}
    B -- No --> C(["End"])
    B -- Yes --> D["lock
    door"]
    D --> C
```

Example 2:
```mermaid
flowchart TD
    A["Start"] --> B["Evaluate"]
    B --Retry --> C["Deploy"]
    C -->D["Load Dataset"]
    D --> E["End"]
```

Example 3:
```mermaid
flowchart TD
    A(["Start"]) --> B["Checkout code"]
    B --> C["Run tests"]
    C --> D{"Tests<br>pass?"}
    D -- Yes --> E["Deploy to<br>staging"]
    D -- No --> F["Notify Dev"]
    E --> G(["End"])
    F --> G
```
""",

# Graph diagram examples
"Graph" : """Example 1:
```mermaid
graph TD
    A(["Support Agent"]) --Payment <br> done--> B(["Buyer"])
    A --Payment <br> receieved--> C(["Payment<br>Gateway"])
    D(["warehouse"]) --"order<br>confirmation"--> C
```

Example 2:
```mermaid
graph TD
    A(["Insurance Provider"]) --Test<br>results-->B(["Pharmacist"])   
    A --Discharge<br>Summary-->C(["Lab<br>Technician"]) 
    B --Prescription--> D(["Patient"])
    C--Prescription-->E(["Doctor"]) 
```

Example 3:
```mermaid
graph TD
    U1(["User1"]) --rated--> MA(["Movie A"])
    U1(["User1"]) --watched--> MB(["Movie B"])
    MA --is_genre--> GA(["Genre_Action"])
    MB --is genre--> GD(["Genre_Drama"])
    
    U2(["User2"]) --liked--> MC(["Movie C"])
    MC --is_genre--> GC("Genre_Comedy")
```
""",

# Packet diagram examples
"Packet" : """Example 1:
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
""",

# Sequence diagram examples
"Sequence" : """Example 1:
```mermaid
sequenceDiagram
    participant User
    participant Device

    User->>Device: Open Application
    Device-->>User: Application Opened
```

Example 2:
```mermaid
sequenceDiagram
    participant Customer
    participant APP
    participant "Auth server"

    Customer->>APP: Login
    APP->>"Auth server": Verify password
    "Auth server"-->>APP: Return JWT
    APP-->>Customer: Return OK
```

Example 3:
```mermaid
ssequenceDiagram
    participant Viewer as "Viewer (Katy)"
    participant TV as "Smart TV (LG)"
    participant Provider as "Content Provider (Netflix)"
    participant Billing

    Viewer->>TV: open app
    TV->>Provider: fetch content
    Provider-->>TV: video stream
    Viewer->>TV: subscribe
    TV->>Provider: billing request
    Provider->>Billing: billing request
    TV-->>Viewer: confirmation
```
""",

# State diagram examples
"State" : """Example 1:
stateDiagram-v2
    [*] -->  Applied: Start
    Applied --> Interview
    Interview --> offer
    offer --> [*] : end
    Interview --> Rejected
```mermaid
```

Example 2:
```mermaid
stateDiagram-v2
    [*] --> Applied
    Applied --> PhoneScreen
    PhoneScreen --> onsite
    onsite --> PhoneScreen : need more info
    onsite --> offer
    offer --> hired
    hired --> [*]
```

Example 3:
```mermaid
stateDiagram-v2
    ATM_idle --> Card_Read : Card Entry
    Card_Read --> Return_Card : Unsuccessful
    Return_Card --> ATM_idle
    Pin_Entry --> Verification
    Card_Read --> Pin_Entry : Card Read Successfully
    Verification --> Return_Card : Wrong Pin
    Verification --> Account_Access : Verified
```
"""
}