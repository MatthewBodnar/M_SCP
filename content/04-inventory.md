# Inventory management

## Inventory and costs

Inventory is stock kept for later use or sale. Campus Tees holds blank shirts, work being printed and finished orders. Stock helps meet demand, but uses cash and storage space.

**Slides 3–5: three different cost questions.**

| Type | Simple meaning | Campus Tees example |
| --- | --- | --- |
| Fixed / variable | Does the total change with output? | Rent stays fixed within a range. More shirts use more fabric. |
| Direct / indirect | Can the cost be linked to this order? | Blanks belong to one order. Shared office costs do not. |
| Engineered / discretionary | Is cost linked to the work, or chosen by managers? | Material use has a clear link to output. Managers choose a training budget. |

A direct cost can be fixed. A shared cost can vary. Fixed rent may rise when another room is needed.

## Break-even: how many shirts cover the costs?

**Slide 6.** Let F be fixed cost, p price per shirt, v variable cost per shirt and q shirts sold.

**Profit = (p − v) × q − F. Break-even quantity = F / (p − v).**

Campus Tees has F = €1,200, p = €15 and v = €9. Each shirt provides €6 towards fixed costs. Break-even is **1,200 / 6 = 200 shirts**. At 300 shirts, profit is **€600**.

The model assumes a steady price and unit cost, with fixed costs unchanged. Price must be above variable cost.

[lab:breakeven]

## Reorder point and safety stock

**Slide 7. Exact rule:**

> Re-order Point = demand during lead time + safety stock

**Plain English:** order before stock runs out. Cover the wait for delivery and keep a buffer.

**ROP = d × L + SS.** Daily demand d = 40 shirts, lead time L = 5 days, safety stock SS = 60. **ROP = 40 × 5 + 60 = 260 shirts.**

Safety stock protects against higher demand or late supply. The needed buffer depends on service goals and demand or lead-time changes. Better data helps, but cannot supply a missing shirt.

[diagram:reorder]

[lab:reorder]

## EOQ: how much should we order?

**From the glossary:** EOQ balances ordering cost and stockholding cost.

**Q* = √(2DK/h).** D is annual demand; K is cost per order; h is holding cost per unit per year.

For D = 12,000, K = €30 and h = €2, **EOQ = 600 shirts**. This means 20 orders per year and 300 shirts of average cycle stock. Annual ordering and holding costs are €600 each.

The basic model assumes steady demand, a fixed unit price, known lead time and complete deliveries. **EOQ means how much. ROP means when.** Keep time units the same.

[lab:eoq]

## Stock tools and systems

**Slides 8–9 and the glossary.** JIT aims to bring materials close to the time they are needed. It needs reliable quality, information and suppliers.

**ABC** gives more attention to items with high annual usage value. **FIFO** uses the oldest cost first; **LIFO** uses the newest cost first. Ten shirts at €2, then ten at €3: selling ten gives FIFO cost €20 or LIFO cost €30.

**MPS** plans finished output. **MRP** plans required materials. **ERP** joins business data. **WMS** manages warehouse work. **SKU** identifies a stock variant. **VMI** gives the supplier an agreed role in checking and refilling stock. See the short glossary for all 25 terms.

## Recommended inventory paper

**Panigrahi, Shrivastava and Nudurupati (2024): abstract only.** The full paper was not uploaded. The publisher's abstract says small firms need suitable stock methods, technology and staff knowledge. These can affect business performance.

**Campus Tees example:** a stock system helps only if staff enter correct shirt sizes and understand when to reorder. This is our example, not a case from the paper.
