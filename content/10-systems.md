# Replenishment, information and logistics services

Inventory is managed through both physical processes and information. A warehouse can contain the correct goods but still fail if nobody knows where they are or whether they have already been allocated. A system can report stock that does not exist if receipts, movements or losses are not recorded accurately.

This chapter links the glossary's many abbreviations into one understandable picture. Learn what decision each tool supports. Memorising the letters without their role makes it difficult to apply them to a case.

## The information-system map

[diagram:systems]

**ERP**, enterprise resource planning, integrates main business processes, often through shared software and data. **MPS**, the master production schedule, describes the production plan and helps allocate resources. **MRP**, material requirements planning, determines which materials are needed, in what quantities and when. **WMS**, a warehouse management system, supports day-to-day warehouse operations.

For Campus Tees, customer orders and available resources inform the production plan. The plan implies requirements for blank shirts, ink and packaging. Warehouse records show what is already available and where it is located. Procurement and production decisions then become more coordinated.

Do not assume that buying an ERP package automatically creates integration. People need clear definitions, accurate data and appropriate processes. If sales records one size code and the warehouse uses another without a reliable mapping, shared software may spread errors faster rather than remove them.

## MPS and MRP, one step at a time

Suppose Campus Tees plans to produce 300 festival shirts next week. That is a finished-output requirement in its production plan. If each shirt uses one blank, the gross requirement is 300 blanks of the specified sizes. If 80 suitable blanks are available and uncommitted, the net requirement is 220, ignoring other receipts and reservations for simplicity.

If the supplier lead time is five working days, the order must be released sufficiently early for the blanks to be available when production begins. This timing logic is central to MRP: what, how much and when. The example is a simple explanation of the glossary concept, not a full MRP algorithm with every planning parameter.

The MPS concerns what output should be produced and when. MRP translates that plan into component and material requirements. A WMS helps execute warehouse work such as receiving, locating, picking and dispatching the required material. ERP provides broader business integration. These roles can overlap within one software product, but the concepts remain distinguishable.

## SKU, barcode, QR code and RFID

A **SKU**, or stock-keeping unit, identifies a distinct stock item or variant in the business. A small white shirt and a medium white shirt normally need different identities if they are managed separately. The SKU is the identity; a barcode, QR code or RFID tag is a way to carry and capture identifying information.

A barcode uses an optical label that a scanner reads. A QR code is a two-dimensional optical code. RFID uses radio-frequency identification. These technologies can reduce manual entry and support better visibility when the surrounding process records the right events.

The glossary heading “QR – Quick Repsonse” contains a spelling issue and its paragraph discusses QR **codes**. In the agile supply-chain discussion, quick response means a responsive replenishment or supply approach. The two uses should not be collapsed into one definition merely because they share letters.

Scanning a label does not prove the physical quantity is correct. If staff scan one item but move a different one, the record becomes misleading. Good data depends on disciplined receiving, movement, counting and exception handling as well as the technology.

## JIT and Kanban

**Just in time (JIT)** aims to provide what is needed when it is needed, reducing unnecessary stock and improving efficiency. **Kanban** uses cards or other signals to trigger replenishment. A signal authorises the next action based on use or demand rather than an uncontrolled release of extra work.

Imagine two bins of a commonly used packing material. When one becomes empty, a card signals replenishment while the second covers use during the replenishment time. The exact bin sizes and rules must fit demand and lead time. The signal alone cannot make an unreliable supplier reliable.

JIT requires more than frequent orders. Quality, setups, layout, maintenance, supplier coordination and stable information all influence whether small flows work. The lecture explicitly presents in-company tools, inter-company tools and supporting mechanisms. Learn the categories and their connections rather than treating JIT as simply “keep no stock”.

## The lecture's JIT toolkit

| In-company tools | Inter-company tools | Supporting mechanisms |
| --- | --- | --- |
| Modular designs. | Certified quality. | Quality management. |
| Focus. | Supplier reduction. | Value engineering. |
| Total productive maintenance. | Joint development programmes. | Time-based process mapping. |
| Setup reduction. | JIT delivery. | Six Sigma. |
| Layout and flow. | EDI and internet. | Methods analysis. |
| Pull scheduling. | Integrated transport. | Error proofing. |
| Small machines. | Standard containers. | Management by sight. |
| Lot-size reduction. | Barcoding and RFID. | Enforced problem solving. |
| JIT/MRP. | Long-term contracts. | Under-capacity scheduling. |

**Source:** Inventory lecture, slide 8. The table preserves the lecture's grouping; the explanations below make the mechanisms concrete.

Modular design uses common building blocks to reduce unnecessary variety and support later configuration. Focus narrows the process's task so that resources and methods fit it. Total productive maintenance seeks dependable equipment. Setup reduction makes changing from one job to another less costly, which can make smaller batches practical.

Layout and flow reduce unnecessary movement and interruptions. Pull scheduling limits work based on downstream need. Small machines can provide flexibility compared with a single oversized resource in some contexts. Lot-size reduction lowers the amount released at once, but it needs reliable setups and replenishment to avoid replacing stock with disruption.

Certified quality means building confidence in supplier output rather than repeatedly discovering defects at the receiving point. Joint development helps make products and processes fit one another. Integrated transport and standard containers reduce coordination and handling problems. Long-term contracts can support investments, provided the relationship actually works.

EDI, electronic data interchange, illustrates structured information exchange between organisations. The internet broadens communication possibilities. Barcodes and RFID improve identification and visibility. None of them removes the need for agreed meanings, accurate records and responsibility for exceptions.

Supporting mechanisms help expose and solve problems. Error proofing aims to prevent mistakes or make them immediately visible. Management by sight makes status easy to understand. Under-capacity scheduling reserves some capacity instead of planning every minute at a theoretical maximum, allowing the system to absorb variation and recover.

This last idea connects lean and agility. A system operating at an unrealistic full utilisation can build long queues when anything varies. Some capacity protection may improve flow and delivery. The right amount depends on uncertainty, economics and the required service, rather than a universal percentage.

## Vendor-managed inventory

**VMI** means the vendor monitors and replenishes inventory rather than leaving the buying business to initiate every replenishment. The supplier needs access to relevant stock or consumption information and agreed rules about service, quantities and responsibilities.

Campus Tees could allow its packaging supplier to review stock and replenish standard cartons within agreed limits. The buyer still needs to verify performance and coordinate unusual changes. If the supplier sees only distorted data or does not know about a large event, it can make poor replenishment decisions.

VMI does not by definition determine who owns the stock or when payment occurs. Monitoring and replenishment responsibility are the central glossary points. Ownership arrangements can be agreed separately. Do not automatically equate VMI with consignment inventory.

The potential benefit is better coordination and fewer repeated ordering tasks. Risks include unsuitable replenishment incentives, weak visibility and dependence on the vendor's understanding. A well-designed arrangement makes the shared objective and exceptions clear.

## MRO and operating continuity

The glossary expands MRO as maintenance, repair and operating and describes items used to maintain, repair and operate the inventory management system. More broadly, the term commonly refers to supplies supporting operations. Learn the source wording for this course while understanding why such items matter.

A printer belt, cleaning material or maintenance tool may not become part of the sold shirt, but its absence can stop production. Low direct product cost does not mean low operational significance. This connects MRO management with Kraljic bottleneck risk and safety-stock decisions.

A sensible plan identifies critical spares, lead times, usage uncertainty and alternatives. It need not hold every possible component. The aim is to protect important operations with proportionate cost, information and supplier arrangements.

## 3PL and 4PL

A **third-party logistics provider (3PL)** performs outsourced logistics activities such as warehousing, inventory tracking, packing, shipping or returns. A **fourth-party logistics provider (4PL)** takes a broader coordinating and management role for the end-to-end logistics network, potentially overseeing several providers including 3PLs.

For Campus Tees, using a fulfilment company to store and dispatch finished orders illustrates a 3PL arrangement. Hiring a provider to design and coordinate the wider logistics network, select providers and oversee performance illustrates the 4PL idea. The distinction concerns role and scope rather than simply the size of the provider.

Outsourcing logistics does not remove the customer promise. Campus Tees still depends on correct data, clear responsibilities and the provider's performance. Supplier relationship management remains necessary even when physical logistics work is performed externally.

## Warehouse trends and the information principle

The inventory lecture lists fewer but larger inventories, high automation, data-driven warehouses and real-time analytics. Consolidation can reduce duplicated stock and create scale, but it can also increase distance to some customers or concentrate disruption exposure. A trend is a direction observed in practice, not a requirement that every firm should centralise everything.

Automation can improve speed and consistency where processes and volumes justify it. Data can support allocation, replenishment and exception management. The value depends on how well the information matches the physical system and the decisions being made.

The lecture says, “the only way to replace an inventory is with information.” Read this as a strong emphasis on visibility and coordination. Knowing actual consumption earlier can reduce the buffer needed against uncertainty. It does not mean inventory can always be removed, that data replaces production lead time, or that resilience never needs physical reserves.

## A connected replenishment example

A club confirms 300 shirts. Sales records the specification. The MPS schedules the output. MRP identifies the net material requirement. Purchasing obtains missing blanks. The WMS guides receiving and picking. Scanning confirms movements against SKUs. Production consumes the blanks. Finished shirts enter dispatch. The carrier or 3PL completes the physical delivery, while status information returns to the business and customer.

If the stock file is wrong at the beginning, every later plan may be wrong. If the materials are correct but the club's artwork is late, printing may still miss the schedule. If the finished order is complete but the dispatch data is wrong, delivery can fail. The example shows why information systems support connected processes rather than acting as isolated technical solutions.

### Check your understanding

Does installing RFID automatically make a warehouse agile?

[answer:Possible answer]
No. RFID can improve identification and visibility, but agility also requires market knowledge, responsive decisions and flexible capabilities. Accurate information is useful only if the organisation can act on it. A fast scan cannot solve an impossible production schedule or an unavailable resource.
[/answer]
