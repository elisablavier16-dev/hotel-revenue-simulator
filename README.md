# Hotel Revenue Management Simulator

A Python simulator for a fictional 110-room hotel in Amsterdam. It models how demand, seasonality, price and distribution channels drive revenue, and compares a fixed-price strategy with a dynamic-pricing strategy.

**Important:** all data in this project is **simulated**. The parameters below are my own modelling assumptions, not real hotel data.

## What it does

- Simulates one year (365 nights) of hotel activity
- Calculates the core hotel KPIs: occupancy, ADR (Average Daily Rate) and RevPAR (Revenue Per Available Room)
- Models demand that depends on the season, the day of the week, special dates and the room rate
- Splits each night's sales across distribution channels (Direct, Booking.com, Expedia) and calculates commissions and net revenue
- Compares fixed pricing with occupancy-based dynamic pricing
- Exports clean CSV files, ready for SQL analysis and Power BI dashboards

## Project structure

| File | Purpose |
|---|---|
| `hotel_model.py` | The model: KPI calculation, demand, pricing and channel split |
| `run_year.py` | Runs the 365-night simulation and exports the CSV files |
| `HotelSimulator.py` | Interactive menu (reporting / simulation mode) for a single night |
| `hotel_data.csv` | One row per night |
| `hotel_channels.csv` | One row per night and per channel (1,095 rows) |

## How to run

1. Install Python 3 and pandas: `pip install pandas`
2. Run `python run_year.py` to generate the two CSV files
3. Run `python HotelSimulator.py` for the interactive single-night menu

## How the model works

**KPIs**
- Occupancy = rooms sold / rooms available
- ADR = room revenue / rooms sold
- RevPAR = room revenue / rooms available

**Demand.** For each night, expected demand depends on the month (weekday vs weekend values), with special dates: Christmas is almost empty and New Year is fully booked. Random noise (between -10 and +10 rooms) makes each night different. Demand is then adjusted by price (see elasticity below) and capped between 0 and 110 rooms.

**Price elasticity.** Demand is multiplied by `(reference rate / room rate) ^ elasticity`, with a reference rate of 170 EUR and a base elasticity of 0.5 (customers fairly insensitive to price). A higher elasticity means customers react more strongly to price.

**Dynamic pricing.** The room rate depends on expected occupancy:

| Expected occupancy | Room rate |
|---|---|
| 85% or more | 230 EUR |
| 60% to 85% | 190 EUR |
| 40% to 60% | 160 EUR |
| Below 40% | 130 EUR |

**Distribution channels.** Each night's rooms are split by channel, and each channel keeps a commission on its revenue:

| Channel | Share of rooms | Commission |
|---|---|---|
| Direct | 40% | 0% |
| Booking.com | 35% | 18% |
| Expedia | 25% | 15% |

Net revenue = revenue minus commission.

## Assumptions

All of these are simplifications chosen for the simulation:

- Seasonality: very quiet from November to March, recovery in April, high season from May to October (around 80% occupancy in summer), busier weekends (Amsterdam has more leisure travellers on weekends)
- Christmas almost empty, New Year fully booked
- Base price elasticity of 0.5
- Channel shares and commissions as listed above
- Random noise of plus or minus 10 rooms per night
- The dynamic pricing rule uses the same demand forecast that generates the sales, so it represents an **ideal case with a perfect forecast**. A real revenue manager only has an imperfect forecast, so the real gain would be smaller.

## Results

The simulation uses a fixed random seed (`random.seed(42)`) so both strategies face exactly the same random noise and can be compared fairly.

| Scenario | Fixed price (170 EUR) | Dynamic pricing | Difference |
|---|---|---|---|
| Elasticity 0.5 (low sensitivity) | 4,142,560 EUR | 4,375,910 EUR | about +5.6% |
| Elasticity 1.5 (high sensitivity) | 4,142,560 EUR | 3,952,680 EUR | about -4.6% |

(Total yearly revenue. Average RevPAR: 103.18 EUR fixed vs 108.99 EUR dynamic at elasticity 0.5.)

**Takeaway:** dynamic pricing only pays off when customers are not too sensitive to price. At high sensitivity, raising prices on busy nights loses more customers than it earns, and the strategy loses money. This is why a revenue manager first needs to estimate how customers actually react to price.

Over the year, the Direct channel generates the highest net revenue even though it only brings 40% of the rooms, because it pays no commission.

## Status and next steps

- [x] KPI calculation as reusable functions
- [x] Interactive menu (reporting and simulation modes)
- [x] 365-night simulation with Pandas and CSV export
- [x] Seasonality and special dates
- [x] Price elasticity of demand
- [x] Occupancy-based dynamic pricing vs fixed price
- [x] Distribution channels and commissions
- [ ] SQL analysis of the exported data (revenue by month and channel, ADR by channel, net revenue after commission)
- [ ] Power BI dashboard (overview KPIs, pricing strategy comparison, channel performance)
- [ ] Test more elasticity values and export a `strategy` column to compare strategies side by side
- [ ] Add one-off events (for example King's Day)

## Skills used

Python (functions, dictionaries, loops), Pandas, hotel revenue management concepts (ADR, RevPAR, occupancy, dynamic pricing, price elasticity, distribution channels and commissions). SQL and Power BI are the next steps.
