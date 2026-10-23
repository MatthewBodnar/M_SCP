# Inventory, costs and worked calculations

Inventory is stock held for future use or sale. It can include raw materials, work-in-progress, finished goods and maintenance or operating supplies. Inventory helps bridge differences between the timing of supply and demand, but it ties up money and can create storage, damage and obsolescence costs.

Campus Tees holds blank shirts before printing, partly printed batches during processing and finished orders awaiting collection. A bakery holds ingredients, dough in process and finished bread. The same underlying questions apply: why is the stock needed, how much should be ordered, when should replenishment begin and what uncertainty must be protected against?

## Why hold inventory?

Stock can support availability, cover replenishment lead time, separate processes with different schedules and protect against uncertainty. A business may also order in batches because each order or setup has a fixed cost. These reasons should be examined rather than accepted as a permanent justification for every pile of material.

A box of standard blank shirts may allow Campus Tees to respond within the club's D-time. A box of last year's printed event design may have little future value. The physical quantity can be the same while the economic meaning differs. Product variety, life cycle, shelf life and customer requirements matter.

Holding less inventory can release cash and expose process problems. Holding too little can create stockouts and disrupted work. The managerial objective is not the maximum or minimum possible stock in isolation. It is an appropriate system of availability, cost and risk.

## Three independent ways to classify costs

[diagram:costtypes]

The lecture's cost cube separates **fixed versus variable**, **direct versus indirect**, and **engineered versus discretionary**. These are different dimensions. Do not assume every direct cost is variable or every indirect cost is fixed.

A fixed cost does not change with activity within a relevant range and time period. A variable cost changes with activity. Direct costs can be traced economically to a chosen cost object, such as a product or order. Indirect costs are shared and need allocation or another treatment. Engineered costs have a relatively identifiable technical relationship with output; discretionary costs depend more on management's decisions about spending.

For a printed-shirt order, the blank shirts are a direct material cost and generally vary with quantity. A supervisor's salary may be indirect relative to individual orders and fixed within a period. A dedicated machine lease may be direct to one product line while fixed over its relevant range. Marketing expenditure may be discretionary in a way that fabric consumption per shirt is not.

The chosen cost object matters. Rent may be indirect to one shirt but direct to a particular warehouse. State the context if a question asks you to classify a cost. A classification without its basis can be misleading.

### Fixed costs can step up

The lecture's rent chart is a step pattern. Rent remains unchanged across one capacity range, then rises when extra space is required. “Fixed” does not mean unchanged forever at every possible output. It means fixed within the range and period being analysed.

Direct material cost is shown increasing with activity. If each shirt uses one €5 blank and there is no waste or discount, 100 shirts require €500 of blanks and 200 require €1,000. The linear relationship is an assumption of the simple model, not a law that ignores quantity discounts or changing yields.

## Worked calculation: break-even

Let fixed cost F = €1,200, selling price p = €15 per shirt and variable cost v = €9 per shirt. Each sold shirt contributes p − v = €6 toward fixed costs and then profit.

**Revenue = p × q. Total cost = F + v × q. Profit = (p − v) × q − F.**

At break-even, profit is zero. Therefore **qBE = F / (p − v) = 1,200 / 6 = 200 shirts**.

[diagram:breakeven]

At 300 shirts, revenue is €4,500. Variable cost is €2,700 and total cost is €3,900. Profit is €600. At 100 shirts, contribution is €600, which covers only half the fixed cost, so the loss is €600.

| Quantity | Revenue | Variable cost | Total cost | Profit |
| --- | --- | --- | --- | --- |
| 100 | €1,500 | €900 | €2,100 | −€600 |
| 200 | €3,000 | €1,800 | €3,000 | €0 |
| 300 | €4,500 | €2,700 | €3,900 | €600 |

If p is equal to or below v, there is no positive finite break-even quantity in this simple model with positive fixed cost. More sales do not generate a positive contribution to cover F. Do not divide by zero or report a negative break-even quantity as a meaningful target.

The model assumes a stable price, constant variable cost per unit and fixed costs within the relevant range. If price falls at high volumes, capacity creates a step cost or unsold output remains in stock, the simple calculation needs adjustment. In an exam, show the formula, substitution, units and interpretation.

[lab:breakeven]

## Two separate inventory decisions

**Order quantity answers “how much?” Reorder point answers “when?”** The EOQ can inform the quantity. The reorder point triggers replenishment early enough to cover lead-time demand and safety stock. Confusing these decisions is a common mistake.

Imagine ordering a new phone charger. Choosing a pack of ten is a quantity decision. Deciding to reorder when only three remain is a timing decision. A business needs both. A perfect order quantity still fails if ordered after stock is exhausted and delivery takes a week.

## Worked calculation: the reorder point

The lecture gives **Reorder point = demand during lead time + safety stock**. With a constant daily demand rate d and lead time L in days, this becomes **ROP = d × L + SS**.

Suppose annual demand is 12,000 units over 300 working days. Daily demand is 12,000/300 = 40 units. Lead time is five working days and safety stock is 60 units. Expected lead-time demand is 40 × 5 = 200. The reorder point is **260 units**.

[diagram:reorder]

Use consistent time units. Multiplying annual demand directly by a five-day lead time is wrong unless you convert the lead time to the same annual basis. A daily demand rate must be paired with a lead time expressed in corresponding days.

With an order quantity of 600, the idealised cycle can start at 660 units, including safety stock. After ten working days at 40 units per day, stock reaches 260 and the order is placed. During the five-day lead time, another 200 units are used, leaving 60. A receipt of 600 raises stock back to 660.

The order cycle is 600/40 = 15 working days. Safety stock is not normally consumed in this ideal average-demand picture; it protects against uncertainty. In practice, review inventory position and outstanding orders to avoid placing duplicate replenishments in more complex systems. The lecture's basic sawtooth remains the first model to understand.

[lab:reorder]

## Safety stock: protection against uncertainty

The glossary describes safety stock as extra inventory held to protect against stockouts caused by demand fluctuations or supply delays. The lecture links it to service level, lead-time variability and demand variability. A higher service ambition or more uncertainty generally requires more protection, all else equal.

Suppose ordinary lead-time demand is 200 but an unusually busy week requires 240. A 60-unit buffer could absorb that increase. If both demand and lead time rise sharply, the same buffer may be insufficient. Safety stock is not a universal guarantee.

Better information can reduce avoidable uncertainty. More reliable lead time can also reduce the required buffer. However, information does not replace physical goods when demand arrives before replenishment is possible. The lecture's memorable statement about replacing inventory with information should be interpreted as a coordination principle, not a claim that data alone fulfils physical demand.

## EOQ: balance ordering and holding cost

The **Economic Order Quantity**, also called the Wilson formula in the glossary, finds an order quantity that minimises the sum of ordering and holding costs under a simple set of assumptions.

Use D for annual demand, K for the fixed cost per order, h for annual holding cost per unit, P for unit purchase price and Q for order quantity. The total annual cost function in the glossary is:

**T(Q) = PD + KD/Q + hQ/2.**

Purchase cost is PD. The number of orders per year is D/Q, so ordering cost is K × D/Q. Average cycle inventory is Q/2, so holding cost is h × Q/2. The model assumes a regular decline from Q to zero followed by an instantaneous receipt of the next lot.

[diagram:eoq]

A larger Q means fewer orders and lower annual ordering cost. It also means higher average stock and higher holding cost. A smaller Q reverses those effects. EOQ balances them. It does not make each cost individually as small as possible.

The optimal quantity is **Q* = √(2DK/h)**. If the purchase price P is constant, PD does not change with Q and therefore does not change the optimum. Quantity discounts require an extended comparison; they are not necessary for the basic EOQ trade-off.

### Worked EOQ example

Let D = 12,000 units/year, K = €30/order and h = €2/unit/year. Then Q* = √(2 × 12,000 × 30 / 2) = √360,000 = **600 units**.

Orders per year = 12,000/600 = 20. Average cycle inventory = 600/2 = 300. Annual ordering cost = 20 × €30 = €600. Annual cycle-stock holding cost = 300 × €2 = €600. Relevant annual cost = €1,200.

If P = €5, annual purchase cost is €60,000 and total annual cost excluding safety-stock holding cost is €61,200. If constant safety stock of 60 is included, its annual holding cost is another €120. That constant addition raises total cost but does not alter the basic EOQ.

| Q | Orders/year | Average cycle stock | Ordering cost/year | Holding cost/year | Relevant total |
| --- | --- | --- | --- | --- | --- |
| 300 | 40 | 150 | €1,200 | €300 | €1,500 |
| 600 | 20 | 300 | €600 | €600 | €1,200 |
| 1,200 | 10 | 600 | €300 | €1,200 | €1,500 |

The equality of ordering and cycle-stock holding cost at the optimum is a useful check for the basic model. The curves trade off against each other. Moving away from the optimum in either direction increases their sum in this example.

[lab:eoq]

### Derivation, explained simply

Differentiate T(Q) with respect to Q, treating the other variables as constant. The derivative is **dT/dQ = −DK/Q² + h/2**. At the minimum, set it equal to zero: DK/Q² = h/2. Rearranging gives Q² = 2DK/h and Q* = √(2DK/h).

You do not need advanced calculus to understand the economic idea: each increase in order size saves some ordering effort but adds stockholding cost. The optimum occurs where the marginal saving and marginal extra cost balance. If asked to derive the formula, show the algebra and define the variables.

### Assumptions and limitations

The basic model assumes known stable demand, constant order and holding costs, a constant unit price, no planned shortages and replenishment that arrives as a complete lot. It abstracts from capacity constraints, perishability, minimum order quantities and many practical complications.

A bakery should not order an EOQ of fresh ingredients that spoils before use. Campus Tees should not ignore supplier pack sizes or uncertain product life cycles. The calculation is a useful baseline, and managerial judgment checks whether its assumptions are reasonable.

The glossary says ordering cost falls with increasing order volume due to economies of scale. Read this carefully: in the standard EOQ model, annual ordering cost falls because there are fewer orders, each with a fixed K. A lower purchase price per unit is not part of the basic formula unless explicitly added as a discount.

## ABC classification

ABC classification directs attention toward the items with the greatest economic significance. A common basis is annual usage value: annual quantity multiplied by unit cost. The Pareto-style 80/20 idea is a useful illustration, not a compulsory exact proportion in every inventory.

[diagram:abc]

Suppose five SKUs have annual usage values of €8,000, €800, €600, €400 and €200. Total value is €10,000. The first item is 20% of the item count and 80% of value. It deserves much closer attention than its count alone suggests.

A items normally receive tighter review and control. B items receive intermediate attention. C items can often use simpler controls. Thresholds depend on context, and operational criticality can justify attention to a low-value item. A tiny spare that stops production may need a strong continuity plan despite its low annual spending.

ABC is different from Kraljic. ABC primarily prioritises economic inventory value. Kraljic combines profit impact and supply risk to differentiate purchasing strategy. The two tools can complement one another, but a C item is not automatically routine or safe to ignore.

## FIFO and LIFO: a worked comparison

FIFO means first in, first out. For cost assignment, the oldest costs are assigned to goods sold first. LIFO means last in, first out: the newest costs are assigned first. Keep inventory valuation assumptions distinct from the physical flow of particular units.

Buy ten units at €2 and then ten at €3. Sell ten. Under FIFO, cost of goods sold is €20 and remaining inventory is €30. Under LIFO, cost of goods sold is €30 and remaining inventory is €20. The same twenty units were purchased; the allocation of costs differs.

This example explains the glossary concepts. It does not assert that every accounting framework or jurisdiction permits both methods. If the exam concerns the module's definitions, explain the mechanism rather than introducing unsupported legal claims.

### Check your understanding

If lead time doubles but demand and safety stock are unchanged, does EOQ automatically double?

[answer:Possible answer]
No. The basic EOQ depends on D, K and h. Reorder point rises because expected demand during lead time increases. Quantity and timing are different decisions. In practice, changed lead-time uncertainty may also affect safety stock, but that is another assumption to analyse.
[/answer]
