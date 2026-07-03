"""Curated South African sector knowledge base.

Live scrapers give hard numbers (liquidations, sector growth, news signals),
but KPIs, capital requirements, market gaps and structural outlooks are not
published by any single machine-readable source. This module encodes them as
a reviewed, cited knowledge base. Figures are ZAR estimates for planning -
verify against current quotes before committing capital.

Scores are 0-100:
  structural  - long-term (5-10 year) growth potential of the market
  barriers    - difficulty/cost of entry (higher = harder)
"""

NATIONAL_BASELINES = {
    "smme_failure": (
        "Roughly 70-80% of South African SMMEs fail within the first five "
        "years - among the highest rates globally (SEDA / University of the "
        "Western Cape research; GEM South Africa reports)."
    ),
    "first_two_years": (
        "The first 24 months are the highest-risk window; most failures cite "
        "cash-flow gaps, late payments by clients (esp. government), lack of "
        "access to finance, and load shedding-related cost shocks."
    ),
    "funding_gap": (
        "The SMME credit gap is estimated at R350bn+ (IFC/SA SMME market "
        "study). Under 6% of SMMEs access formal bank credit; most start on "
        "personal savings ('bootstrap economy')."
    ),
    "sources": [
        "Stats SA P0043.1 Statistics of liquidations (monthly)",
        "SEDA SMME Quarterly Update",
        "Global Entrepreneurship Monitor (GEM) South Africa",
        "IFC: The Unseen Sector - MSME opportunity in South Africa",
        "SARB Quarterly Bulletin",
    ],
}

SECTORS = {
    "agriculture": {
        "name": "Agriculture & Agro-processing",
        "statssa_key": "agriculture",
        "wb_group": "agriculture",
        "news_query": "South Africa agriculture farming agro-processing sector",
        "summary": (
            "Export-led star performer: citrus, table grapes, nuts and wine "
            "drive growth; SA is the world's #2 citrus exporter. Volatile "
            "year-to-year (drought/El Niño cycles) but structurally strong. "
            "Agro-processing adds margin the farm gate can't."
        ),
        "capital": {
            "micro": "R50k-R500k (tunnel/hydroponic veg, broilers, agri-services)",
            "small": "R2m-R10m (small commercial unit, processing line, packhouse share)",
            "medium": "R20m-R100m+ (commercial farm with water rights, export packhouse)",
            "note": "Land + water rights dominate cost; leasing and outgrower "
                    "models cut entry capital by 50-70%.",
        },
        "kpis": [
            {"kpi": "Yield per hectare vs regional benchmark", "target": "Within 10% of top-quartile producers", "why": "Thin margins make yield the primary survival lever."},
            {"kpi": "Export-grade pass rate (Class 1 %)", "target": ">85% for fruit", "why": "Export prices are 2-4x local; rejects destroy margin."},
            {"kpi": "Water cost per ton", "target": "Falling year-on-year", "why": "Water scarcity is the binding long-term constraint."},
            {"kpi": "Debt-service cover ratio", "target": ">1.5x through a drought season", "why": "Climate volatility means one bad season must be survivable."},
        ],
        "failure": {
            "baseline": "Low liquidation counts (few formal companies) but high informal attrition; new entrants without water rights or offtake agreements fail fastest.",
            "drivers": ["Drought/climate shocks", "No secured offtake before planting",
                        "Under-capitalised first 3 seasons", "Logistics failures at ports (export fruit)"],
        },
        "success_factors": [
            "Secured offtake/export agent relationships before production",
            "Water rights or reliable irrigation",
            "Crop insurance and 18-month cash runway",
            "Move up the chain: processing/packing beats primary production margin",
        ],
        "gaps": [
            "Agro-processing of exported-raw commodities (nuts, hemp, moringa) locally",
            "Cold-chain and packhouse capacity in Limpopo/Eastern Cape growth corridors",
            "Precision-agri services (drone scouting, soil analytics) for mid-size farms",
            "Halal-certified processing for Middle East export demand",
        ],
        "longterm": {
            "score": 74,
            "drivers": ["Global food demand and weak rand favour exports",
                        "AfCFTA opens African markets",
                        "Under-utilised land in former homelands with new financing models"],
            "risks": ["Climate volatility", "Port/rail logistics (Transnet)",
                      "Land-reform policy uncertainty", "US/EU trade access (AGOA review)"],
        },
        "barriers": 60,
        "structural": 74,
    },

    "mining": {
        "name": "Mining & Quarrying",
        "statssa_key": "mining",
        "wb_group": "industry",
        "news_query": "South Africa mining sector production platinum gold coal",
        "summary": (
            "Structurally declining giant. PGM price slump, ageing deep-level "
            "gold mines, and rail/port constraints have cut output; but "
            "critical-minerals demand (manganese, vanadium, REE) and mining "
            "services offer niches. Not an SMME entry market except services."
        ),
        "capital": {
            "micro": "R250k-R1m (mining services: safety training, PPE supply, drilling support)",
            "small": "R5m-R50m (aggregate quarry, alluvial/chrome tailings retreatment)",
            "medium": "R100m-R1bn+ (junior mining operation with mining right)",
            "note": "Mining rights take 2-5 years to secure; services businesses "
                    "avoid this entirely and are the realistic entry point.",
        },
        "kpis": [
            {"kpi": "All-in sustaining cost vs commodity price", "target": "AISC below 80% of spot", "why": "Price-takers survive on cost position only."},
            {"kpi": "Contract book coverage (services)", "target": ">12 months forward revenue", "why": "Mines cut contractors first in downturns."},
            {"kpi": "Safety: LTIFR", "target": "Below industry average", "why": "Safety stoppages (Section 54) halt revenue instantly."},
        ],
        "failure": {
            "baseline": "Junior miners fail on funding and permitting timelines; services firms fail when anchored to a single mine client.",
            "drivers": ["Commodity price cycles", "Permitting delays", "Single-client dependency", "Electricity and rail constraints"],
        },
        "success_factors": [
            "Diversified client base across commodities",
            "Tailings retreatment over greenfield (lower capex, faster permits)",
            "Critical-minerals exposure (manganese, vanadium, chrome) over gold/PGM",
        ],
        "gaps": [
            "Mine rehabilitation and closure services (regulatory tailwind)",
            "Tailings reprocessing with modern recovery tech",
            "Critical-minerals beneficiation ahead of export bans on raw ore",
            "Off-grid renewable power supply to mines",
        ],
        "longterm": {
            "score": 45,
            "drivers": ["Critical-minerals demand (EV/battery supply chains)",
                        "Weak rand supports export revenue"],
            "risks": ["Structural decline of gold/PGM deep mining", "Transnet rail capacity",
                      "Policy/regulatory friction", "Global decarbonisation hits coal"],
        },
        "barriers": 90,
        "structural": 45,
    },

    "manufacturing": {
        "name": "Manufacturing",
        "statssa_key": "manufacturing",
        "wb_group": "manufacturing",
        "news_query": "South Africa manufacturing sector factory production",
        "summary": (
            "Two-speed market: legacy heavy manufacturing (steel, autos under "
            "AGOA threat) is under pressure, while niche/light manufacturing "
            "(food processing, packaging, import-substitution) holds up. "
            "Localisation policy and load-shedding recovery are tailwinds; "
            "cheap import competition is the standing headwind."
        ),
        "capital": {
            "micro": "R150k-R1m (CNC/laser job shop, food micro-processing, garment cell)",
            "small": "R2m-R15m (light factory: packaging, plastics, food line with HACCP)",
            "medium": "R30m-R200m (full plant with export certification)",
            "note": "Second-hand equipment and rented industrial space cut entry "
                    "capital ~40%; energy backup (solar+battery) is now a "
                    "non-negotiable line item (add 8-15% of capex).",
        },
        "kpis": [
            {"kpi": "Capacity utilisation", "target": ">75% (Absa PMI benchmark)", "why": "Below ~65% fixed costs eat margin; SA average hovers near 78-80%."},
            {"kpi": "Gross margin after energy", "target": ">30%", "why": "Energy cost shocks are the #1 SA-specific killer."},
            {"kpi": "Order book vs 3-month capacity", "target": ">1.2x", "why": "Import competition makes demand visibility short."},
            {"kpi": "Localisation/designation qualification", "target": "Certified where applicable", "why": "Public procurement designations reserve demand for local makers."},
        ],
        "failure": {
            "baseline": "Consistently among the higher liquidation counts in Stats SA data; energy-intensive and import-exposed subsectors fail most.",
            "drivers": ["Cheap import competition (esp. from China)", "Energy cost and interruption",
                        "Working-capital squeeze on 60-90 day payment terms", "Skills scarcity (artisans)"],
        },
        "success_factors": [
            "Niche products where freight/lead-time beats imports",
            "Energy self-sufficiency (solar) locked in early",
            "Export certification to run both local and export demand",
            "Automation to offset labour productivity gap",
        ],
        "gaps": [
            "Import substitution in packaging, components and fasteners",
            "Food processing for retail private-label (fast-growing shelf space)",
            "Defence/rail component manufacturing (localisation designations)",
            "Solar mounting/electrical BOS component manufacture for the energy boom",
        ],
        "longterm": {
            "score": 58,
            "drivers": ["Localisation policy and public procurement designations",
                        "Energy availability improving from 2024 lows",
                        "AfCFTA regional export potential"],
            "risks": ["AGOA loss would hit autos/agri-processing exports",
                      "Import competition", "Municipal infrastructure decay"],
        },
        "barriers": 65,
        "structural": 58,
    },

    "energy": {
        "name": "Energy & Renewables",
        "statssa_key": "utilities",
        "wb_group": "industry",
        "news_query": "South Africa renewable energy solar wind battery independent power",
        "summary": (
            "The clearest structural growth market in SA. Private generation "
            "liberalised (licence threshold scrapped), wheeling and trading "
            "opening up, REIPPP rounds continuing, plus a massive rooftop "
            "solar and battery retrofit market. Grid connection capacity is "
            "the new bottleneck - and itself an opportunity."
        ),
        "capital": {
            "micro": "R100k-R750k (solar installation business: tools, stock, accreditation)",
            "small": "R2m-R20m (commercial & industrial EPC, O&M contracts, energy trading start-up)",
            "medium": "R50m-R2bn (utility-scale IPP project equity, BESS projects)",
            "note": "Installer businesses are working-capital games (stock + "
                    "30-60 day project cycles); IPP development is a 3-5 year "
                    "development-capital game with 10x payoffs on financial close.",
        },
        "kpis": [
            {"kpi": "Installed cost per kWp (C&I)", "target": "Competitive at R9-R14/Wp installed", "why": "Commoditising fast; cost position decides who wins bids."},
            {"kpi": "O&M contract book (annuity revenue %)", "target": ">30% of revenue recurring", "why": "Install-only businesses die when the retrofit wave slows."},
            {"kpi": "Project pipeline conversion", "target": ">25% quote-to-close", "why": "Long sales cycles kill cash flow if conversion is weak."},
            {"kpi": "CoCT/Eskom wheeling & SSEG registrations", "target": "100% compliant installs", "why": "Regularisation deadlines create both risk and retrofit demand."},
        ],
        "failure": {
            "baseline": "Post-2023 gold rush left an installer glut; failures now among undifferentiated residential installers as load shedding eased. C&I, BESS and O&M remain undersupplied.",
            "drivers": ["Race-to-bottom pricing in residential solar", "Stock financed at high rates",
                        "Post-loadshedding demand normalisation", "Poor workmanship liabilities"],
        },
        "success_factors": [
            "Shift from residential to C&I, agri and body-corporate segments",
            "Recurring O&M and performance-guarantee contracts",
            "Financing partnerships (rent-to-own, PPA) to unlock capex-shy clients",
        ],
        "gaps": [
            "Battery storage retrofits and grid-services aggregation (VPPs)",
            "Energy trading/wheeling services on the new market rules",
            "Municipal grid maintenance outsourcing (distribution crisis)",
            "Solar O&M, cleaning and insurance-repair at scale",
            "EV charging infrastructure ahead of the fleet transition",
        ],
        "longterm": {
            "score": 88,
            "drivers": ["Electricity market liberalisation (ERA amendment)",
                        "8-10GW+ of grid access queue demand",
                        "Carbon border taxes pushing corporate PPAs",
                        "Coal fleet retirement schedule guarantees 15+ years of build-out"],
            "risks": ["Grid connection bottlenecks", "Policy execution speed",
                      "Cheap-import dependency for panels/inverters"],
        },
        "barriers": 45,
        "structural": 88,
    },

    "construction": {
        "name": "Construction & Infrastructure",
        "statssa_key": "construction",
        "wb_group": "industry",
        "news_query": "South Africa construction sector infrastructure projects",
        "summary": (
            "A decade-long decline (major contractors gone: Group Five, Basil "
            "Read...) but bottoming out: Infrastructure SA pipeline, energy "
            "build-out, and private township/affordable housing demand are "
            "reviving niches. High failure rates persist - payment risk and "
            "'construction mafia' site disruption are real operating hazards."
        ),
        "capital": {
            "micro": "R50k-R500k (subcontracting trade: electrical, plumbing, tiling + CIDB Grade 1-2)",
            "small": "R1m-R10m (CIDB Grade 4-6 GB contractor, plant-light model)",
            "medium": "R20m-R150m (Grade 7-8 with owned plant, development JV equity)",
            "note": "CIDB grading gates public work; plant hire over ownership "
                    "keeps balance sheets survivable through payment delays.",
        },
        "kpis": [
            {"kpi": "Days sales outstanding", "target": "<60 days (public clients often run 90-180)", "why": "Late payment is the #1 stated cause of contractor failure in SA."},
            {"kpi": "Tender win rate", "target": ">1 in 8 with disciplined margin floor", "why": "Winning on price below cost is the classic death spiral."},
            {"kpi": "Retention + guarantee exposure vs cash", "target": "<50% of free cash", "why": "Locked-up retentions sink otherwise profitable firms."},
            {"kpi": "Project margin variance", "target": "Actual within 3% of tendered", "why": "Scope creep and disruption erode thin (4-8%) margins fast."},
        ],
        "failure": {
            "baseline": "Persistently high liquidation share in Stats SA data relative to sector size; payment delays and underpricing dominate causes.",
            "drivers": ["Government late payment", "Underpriced tenders", "Site disruption/extortion",
                        "No working-capital buffer for retentions"],
        },
        "success_factors": [
            "Private-sector and energy-sector clients over public tenders early on",
            "Specialised trades (fire, HVAC, solar structural) over general building",
            "Strict credit control and guarantee facility headroom",
        ],
        "gaps": [
            "Renewable-energy civil/structural works (fastest-growing order books)",
            "Affordable/GAP housing developments in metros",
            "Water infrastructure maintenance (municipal crisis outsourcing)",
            "Alternative building tech (LSF, precast) for speed and cost",
        ],
        "longterm": {
            "score": 55,
            "drivers": ["Infrastructure SA / Treasury capex commitments",
                        "Energy transition build-out", "Housing backlog of 2m+ units"],
            "risks": ["State capacity to actually spend budgets", "Payment culture",
                      "Site security costs"],
        },
        "barriers": 50,
        "structural": 55,
    },

    "retail": {
        "name": "Retail, Wholesale & E-commerce",
        "statssa_key": "trade_accommodation",
        "wb_group": "services",
        "news_query": "South Africa retail e-commerce online shopping consumer spending",
        "summary": (
            "Largest employer among these sectors and brutally competitive. "
            "Formal retail is consolidating (Shoprite winning share), while "
            "e-commerce finally hit escape velocity (~10% of retail and "
            "growing 25%+ p.a.; Amazon SA entry, Sixty60/Dash on-demand). "
            "Township/informal retail (spaza ecosystem) is being formalised "
            "and digitised - a major white space."
        ),
        "capital": {
            "micro": "R30k-R300k (online niche store, spaza upgrade, market stall to formal)",
            "small": "R500k-R5m (franchise entry: R800k-R3m typical; independent store fit-out)",
            "medium": "R10m-R100m (multi-store, distribution, private-label brand)",
            "note": "Franchises (food/retail) run R500k-R6m all-in with 60%+ "
                    "5-year survival vs ~20% for independents - the premium "
                    "buys a tested model.",
        },
        "kpis": [
            {"kpi": "Gross margin", "target": "Food 20-25%; apparel 45-55%; electronics 12-18%", "why": "Category-typical margins; below these, volume can't save you."},
            {"kpi": "Stock turns", "target": ">8x/yr food, >4x/yr apparel", "why": "Dead stock is dead cash in a high-interest-rate economy."},
            {"kpi": "CAC vs first-order margin (e-com)", "target": "Payback < 2 orders", "why": "Paid acquisition costs kill most SA online stores before repeat rate matures."},
            {"kpi": "Basket size growth vs inflation", "target": "Real growth positive", "why": "Consumers are trading down; nominal growth flatters."},
        ],
        "failure": {
            "baseline": "Trade/catering/accommodation is consistently the 2nd-highest liquidation industry in Stats SA data - low barriers bring high churn.",
            "drivers": ["Undifferentiated offering vs chains", "Rent escalations in malls",
                        "Thin margins meeting high funding costs", "E-com logistics cost per order"],
        },
        "success_factors": [
            "Niche category authority over general merchandise",
            "Omnichannel from day one (WhatsApp commerce is huge in SA)",
            "Direct import or private label for margin",
            "Township locations: lower rent, underserved demand",
        ],
        "gaps": [
            "Township e-commerce fulfilment and pick-up point networks",
            "Spaza-shop wholesale digitisation (ordering apps, stokvel integration)",
            "Second-hand/recommerce platforms (cost-of-living tailwind)",
            "Halal, plant-based and health niches under-served by chains",
        ],
        "longterm": {
            "score": 66,
            "drivers": ["E-commerce structural shift (off a low base)",
                        "Two-pot retirement withdrawals boosting consumption",
                        "Rate-cut cycle restoring credit-fuelled retail"],
            "risks": ["Consumer under strain (unemployment)", "Chain consolidation squeezing independents",
                      "Shein/Temu direct-import competition"],
        },
        "barriers": 35,
        "structural": 66,
    },

    "tourism": {
        "name": "Tourism & Hospitality",
        "statssa_key": "trade_accommodation",
        "wb_group": "services",
        "news_query": "South Africa tourism hospitality hotels visitors travel sector",
        "summary": (
            "Recovered past pre-COVID arrivals and structurally advantaged by "
            "the weak rand (SA is a value destination) and remote-work "
            "travel. Cape Town is capacity-constrained in peak season. "
            "Visa reform (points-based, digital nomad visa) is unlocking "
            "India/China volume - the big swing factor."
        ),
        "capital": {
            "micro": "R50k-R500k (tour guiding, transfers, experience products, Airbnb arbitrage)",
            "small": "R2m-R15m (guesthouse/boutique lodge purchase or build, restaurant)",
            "medium": "R30m-R300m (hotel development, game lodge)",
            "note": "Experience/service businesses need 10-20x less capital than "
                    "accommodation and scale on marketing skill, not property.",
        },
        "kpis": [
            {"kpi": "Occupancy rate", "target": ">65% annualised (smoothing seasonality)", "why": "Below ~55% most lodging fails to cover fixed costs."},
            {"kpi": "RevPAR growth vs STR benchmark", "target": "At/above market", "why": "The standard measure of whether you're winning share or discounting."},
            {"kpi": "Direct booking share", "target": ">40%", "why": "OTA commissions (15-25%) decide profitability at typical occupancy."},
            {"kpi": "Shoulder/low-season revenue share", "target": ">30% of annual", "why": "Seasonality kills; domestic and MICE demand fill the trough."},
        ],
        "failure": {
            "baseline": "High churn in restaurants and small hospitality (shares the trade/catering/accommodation liquidation line - consistently top-2).",
            "drivers": ["Seasonality without cash reserves", "OTA dependency",
                        "Location misjudgment", "Restaurant margin collapse under food inflation"],
        },
        "success_factors": [
            "Own the guest relationship (direct booking, repeat/referral engine)",
            "Multi-revenue property (rooms + events + experiences)",
            "Target growth source markets (India, China, domestic black middle class)",
        ],
        "gaps": [
            "Mid-market group travel for Indian/Chinese arrivals (visa reform tailwind)",
            "Township and cultural tourism with credible safety wrappers",
            "Remote-work/'workation' products (nomad visa launched)",
            "Adventure and rail tourism outside the Cape-Kruger corridor",
        ],
        "longterm": {
            "score": 76,
            "drivers": ["Weak rand = value destination", "Visa reform unlocking Asia volume",
                        "Air-access expansion", "Global experience-economy growth"],
            "risks": ["Crime perception", "Cape water/energy infrastructure under peak load",
                      "Global recession sensitivity"],
        },
        "barriers": 40,
        "structural": 76,
    },

    "logistics": {
        "name": "Transport & Logistics",
        "statssa_key": "transport_comms",
        "wb_group": "services",
        "news_query": "South Africa logistics freight transport rail ports trucking",
        "summary": (
            "Paradox market: Transnet's rail/port failure is a national "
            "crisis AND the sector's biggest private opportunity - freight "
            "moved to road, and private rail access + port concessions are "
            "opening. Last-mile delivery rides the e-commerce wave. "
            "High operating risk: diesel, tolls, hijacking, driver scarcity."
        ),
        "capital": {
            "micro": "R150k-R800k (bakkie/van last-mile fleet of 1-3, courier franchise)",
            "small": "R2m-R20m (5-15 truck fleet with contracts, cold chain, warehousing 3PL)",
            "medium": "R50m-R500m (fleet + DC network, private rail siding operations)",
            "note": "Vehicle finance is accessible but contract-first is the rule: "
                    "a truck without a lane contract is a depreciating liability.",
        },
        "kpis": [
            {"kpi": "Cost per km vs revenue per km", "target": ">R6/km spread on long-haul", "why": "Diesel is ~40% of cost; the spread is survival."},
            {"kpi": "Fleet utilisation (loaded km %)", "target": ">85% loaded, <15% empty legs", "why": "Empty return legs are the silent killer."},
            {"kpi": "On-time-in-full (OTIF)", "target": ">96%", "why": "Retail DC penalties and contract renewals hinge on it."},
            {"kpi": "Delivery cost per parcel (last-mile)", "target": "<R35 metro", "why": "E-com viability threshold; density is everything."},
        ],
        "failure": {
            "baseline": "Owner-driver and small fleets churn heavily; failures cluster around diesel price spikes, contract loss and hijacking/insurance cost shocks.",
            "drivers": ["Single-contract dependency", "Diesel price exposure without escalation clauses",
                        "Cargo crime", "Under-insured breakdowns"],
        },
        "success_factors": [
            "Contracted lanes with fuel-price escalation clauses",
            "Backhaul networks to kill empty legs",
            "Niche: cold chain, dangerous goods, outsize - where rates hold",
        ],
        "gaps": [
            "Private rail slot operations & rail-adjacent terminals (Transnet reform)",
            "Cold-chain capacity for agri exports and pharma",
            "Township last-mile networks (pick-up points, moto-courier)",
            "Cross-border road freight into SADC (AfCFTA volumes)",
            "Logistics-tech: load-matching to cut the ~30% empty-leg waste",
        ],
        "longterm": {
            "score": 78,
            "drivers": ["Transnet reform opening private participation",
                        "E-commerce last-mile growth 20%+ p.a.",
                        "AfCFTA regional trade corridors"],
            "risks": ["Road infrastructure decay", "Fuel price/rand volatility",
                      "Cargo crime escalation"],
        },
        "barriers": 55,
        "structural": 78,
    },

    "fintech": {
        "name": "Financial Services & Fintech",
        "statssa_key": "finance_realestate_business",
        "wb_group": "services",
        "news_query": "South Africa fintech banking payments financial services startup",
        "summary": (
            "SA produces Africa's most funded fintechs (TymeBank unicorn, "
            "Stitch, Peach Payments). Rapid Payments (PayShap) and open-"
            "banking rules are re-plumbing the market. Traditional advice/ "
            "brokerage remains profitable but consolidating under regulation "
            "(RE exams, COFI incoming). High regulatory moat = high reward."
        ),
        "capital": {
            "micro": "R100k-R1m (FSP brokerage/advisory practice under a licence umbrella)",
            "small": "R2m-R20m (niche lender, payments reseller, insurtech MGA)",
            "medium": "R50m-R500m+ (own banking/insurance licence plays, lending book at scale)",
            "note": "Regulatory capital is the gate: FSP licence is cheap "
                    "(R10k-ish + compliance), NCR lending needs capital "
                    "adequacy, insurance cell captives rent a licence for "
                    "R1m-R5m, full licences need R50m+.",
        },
        "kpis": [
            {"kpi": "Cost of acquisition vs LTV", "target": "LTV/CAC > 3x", "why": "Distribution cost decides fintech survival; SA CACs are high for low-income segments."},
            {"kpi": "Default/loss rate (lenders)", "target": "NPL < 8% unsecured", "why": "SA unsecured credit losses sank African Bank 1.0; underwriting is the business."},
            {"kpi": "Compliance cost as % of revenue", "target": "<12% at scale", "why": "COFI/FICA/POPIA burden crushes sub-scale players."},
            {"kpi": "Assets under advice per adviser", "target": ">R100m", "why": "Advisory practices below this consolidate or die."},
        ],
        "failure": {
            "baseline": "Finance/insurance/real estate/business services is the single highest liquidation line in Stats SA data (it's also the broadest); fintech startups fail on distribution cost, not tech.",
            "drivers": ["CAC exceeding LTV in low-income segments", "Regulatory breach/licence loss",
                        "Credit-loss blowouts", "Funding winter for pre-revenue models"],
        },
        "success_factors": [
            "Embedded distribution (partner with retailers/telcos/employers) over direct",
            "Revenue from day one (SME segment pays; consumers churn)",
            "Compliance as moat: get licensed early, competitors can't follow fast",
        ],
        "gaps": [
            "SME lending against real-time transaction data (R350bn credit gap)",
            "Cross-border remittances SADC corridor (fees still 8-12%)",
            "Insurance for the informal economy (device, funeral+, gig workers)",
            "PayShap/open-banking infrastructure services for corporates",
            "Stokvel formalisation platforms (R50bn+ informal savings pool)",
        ],
        "longterm": {
            "score": 82,
            "drivers": ["Open banking + Rapid Payments re-plumbing",
                        "Huge underbanked SME/informal segments",
                        "SA as fintech gateway to African markets"],
            "risks": ["Regulatory cost escalation", "Big-bank fast-follow crushing niches",
                      "Consumer credit stress"],
        },
        "barriers": 70,
        "structural": 82,
    },

    "realestate": {
        "name": "Real Estate & Property Services",
        "statssa_key": "finance_realestate_business",
        "wb_group": "services",
        "news_query": "South Africa property market real estate residential commercial",
        "summary": (
            "Deeply bifurcated: Western Cape booms (semigration) while "
            "Joburg CBD/office decays; affordable housing demand is "
            "insatiable but development margins are thin. Rate-cut cycle is "
            "the near-term driver. Services (management, sectional title) "
            "are steadier than development."
        ),
        "capital": {
            "micro": "R50k-R500k (rental management agency, sectional-title services, flipping JV)",
            "small": "R2m-R20m (small development JV equity, buy-to-let portfolio seed, student housing conversion)",
            "medium": "R50m-R500m (development projects, REIT-feeder portfolios)",
            "note": "Development leverage is 60-70% senior debt; services "
                    "businesses need almost no capital but scale on trust "
                    "and PPRA compliance.",
        },
        "kpis": [
            {"kpi": "Net rental yield", "target": ">9% affordable segment, >7% mid-market", "why": "Below funding cost = negative carry in a 10%+ prime environment."},
            {"kpi": "Vacancy rate", "target": "<5% residential portfolio", "why": "One vacant month erases a year's margin on a geared unit."},
            {"kpi": "Collections rate", "target": ">97%", "why": "PIE Act makes eviction slow; tenant quality is underwriting."},
            {"kpi": "Development cost per m² vs selling price", "target": "GP margin > 20%", "why": "Construction inflation eats thinner margins mid-project."},
        ],
        "failure": {
            "baseline": "Shares the top liquidation line with finance; small developers fail on pre-sale shortfalls and bridging costs, agencies churned by PPRA compliance and thin deal flow.",
            "drivers": ["Interest-rate exposure", "Pre-sales below bank thresholds",
                        "Municipal services failures killing valuations", "Body-corporate arrears spirals"],
        },
        "success_factors": [
            "Follow semigration and infrastructure (Western Cape, KZN North Coast)",
            "Affordable/GAP segment where demand outruns supply 10:1",
            "Annuity services (management) to smooth transactional income",
        ],
        "gaps": [
            "Affordable rental stock in metros (massive shortfall)",
            "Student accommodation (NSFAS-driven demand, chronic shortage)",
            "Office-to-residential conversions in decayed CBDs",
            "Sectional-title management tech (arrears, compliance automation)",
        ],
        "longterm": {
            "score": 60,
            "drivers": ["Rate-cut cycle", "Household formation and urbanisation",
                        "Semigration re-pricing coastal metros"],
            "risks": ["Municipal decay destroying suburb value", "Rates/levies inflation",
                      "Sluggish income growth capping prices"],
        },
        "barriers": 55,
        "structural": 60,
    },

    "ict": {
        "name": "ICT, Software & Digital Services",
        "statssa_key": "transport_comms",
        "wb_group": "services",
        "news_query": "South Africa technology software startups IT sector digital",
        "summary": (
            "SA's services export champion alongside BPO: software talent at "
            "30-50% of US/EU cost with timezone overlap draws offshore "
            "demand; domestic demand driven by cloud adoption (AWS/Azure "
            "regions in SA), POPIA compliance and AI adoption. Low capital, "
            "high skill barrier. Rand weakness is a feature (export "
            "earnings), not a bug."
        ),
        "capital": {
            "micro": "R20k-R200k (freelance-to-agency, MSP seed, niche SaaS bootstrap)",
            "small": "R500k-R5m (dev agency/MSP with bench, SaaS to first revenue)",
            "medium": "R10m-R100m (funded SaaS scale-up, data-centre adjacent services)",
            "note": "Capital-light but payroll-heavy: 6 months of salary cover "
                    "is the real entry ticket. Offshore clients pay 2-4x local rates.",
        },
        "kpis": [
            {"kpi": "Revenue per developer", "target": ">R1.5m/yr agency; >R2.5m offshore", "why": "Utilisation and rate discipline decide agency survival."},
            {"kpi": "Recurring revenue share", "target": ">40% (retainers/SaaS/MSP)", "why": "Project-only shops die in demand troughs."},
            {"kpi": "Net revenue retention (SaaS)", "target": ">100%", "why": "SA market is small; expansion revenue must offset churn."},
            {"kpi": "Offshore revenue share", "target": ">30%", "why": "Hedge against rand and thin local IT budgets."},
        ],
        "failure": {
            "baseline": "Low formal liquidation counts (asset-light firms just dissolve); failure mode is slow starvation on local-only clients and key-person dependency.",
            "drivers": ["Local-market-only focus", "Key developer departure",
                        "Long enterprise sales cycles without runway", "Competing on price with global freelancers"],
        },
        "success_factors": [
            "Offshore client base earning hard currency",
            "Vertical specialisation (fintech, mining-tech, agri-tech) over generalist",
            "Productise services into retainers/SaaS early",
        ],
        "gaps": [
            "AI implementation services for SA corporates (adoption gap is wide)",
            "POPIA/cyber compliance for mid-market (regulation outpacing skills)",
            "Sector SaaS: body corporates, schools, healthcare practice, logistics",
            "Offshore dev capacity for UK/EU (timezone advantage over Asia)",
        ],
        "longterm": {
            "score": 85,
            "drivers": ["Global services offshoring to SA (cost + timezone + English)",
                        "Cloud/AI adoption cycle domestically",
                        "Hyperscaler data-centre investment (AWS, Azure, Google)"],
            "risks": ["Skills emigration", "Global AI tooling deflating dev-shop rates",
                      "Load shedding/connectivity in outlying areas"],
        },
        "barriers": 30,
        "structural": 85,
    },

    "healthcare": {
        "name": "Healthcare & Wellness",
        "statssa_key": "community_services",
        "wb_group": "services",
        "news_query": "South Africa healthcare private hospitals medical sector NHI",
        "summary": (
            "Defensive growth: ageing insured population, huge unserved "
            "low-income demand, and nursing/GP scarcity. NHI Act creates "
            "policy noise but implementation is years away and funding-"
            "constrained; low-cost private models (Unjani, Intercare-style) "
            "are the growth story either way."
        ),
        "capital": {
            "micro": "R100k-R1m (home care agency, wellness practice, medical logistics)",
            "small": "R2m-R20m (GP/dental multi-room practice, day clinic share, pharmacy franchise ~R3m-R8m)",
            "medium": "R50m-R500m (day hospital, sub-acute/frail care facility)",
            "note": "Licensing (DoH facility licences, HPCSA/SAPC rules on "
                    "ownership) shapes what non-clinicians may own - day "
                    "hospitals and care facilities are investable; GP practices "
                    "mostly aren't.",
        },
        "kpis": [
            {"kpi": "Patient volume per practitioner day", "target": "GP 25-35; dental 8-12", "why": "Fixed clinical salaries need throughput to amortise."},
            {"kpi": "Medical-aid vs cash mix", "target": "Cash/hybrid >30% in low-cost models", "why": "Scheme reimbursement is slow and squeezed; cash models grow faster."},
            {"kpi": "Claim rejection rate", "target": "<5%", "why": "Billing-code errors quietly destroy practice margins."},
            {"kpi": "Bed/chair occupancy (facilities)", "target": ">70%", "why": "Facilities are fixed-cost machines like hotels."},
        ],
        "failure": {
            "baseline": "Low liquidation counts; failures concentrate in under-capitalised facilities awaiting licence/scheme accreditation and in wellness ventures with thin clinical differentiation.",
            "drivers": ["Licensing/accreditation delays burning runway", "Scheme payment squeezes",
                        "Clinical staff scarcity and cost", "NHI-uncertainty freezing investment"],
        },
        "success_factors": [
            "Low-cost cash-based models for the uninsured majority",
            "Nurse-led clinics (regulatory space + cost structure)",
            "Occupational health contracts with mines/factories (B2B annuity)",
        ],
        "gaps": [
            "Low-cost primary care clinics in townships (Unjani model proves it)",
            "Frail care and dementia care (ageing insured cohort, chronic shortage)",
            "Mental health services (massive under-provision, corporate demand)",
            "Telehealth + chronic-medicine delivery to rural areas",
            "Medical tourism (dental/cosmetic at weak-rand prices)",
        ],
        "longterm": {
            "score": 79,
            "drivers": ["Demographics (ageing insured + young uninsured demand)",
                        "Clinician scarcity supports pricing", "Corporate wellness spend growth"],
            "risks": ["NHI policy uncertainty", "Scheme membership stagnation",
                      "Skills emigration of clinicians"],
        },
        "barriers": 65,
        "structural": 79,
    },

    "bpo": {
        "name": "BPO & Global Business Services",
        "statssa_key": "finance_realestate_business",
        "wb_group": "services",
        "news_query": "South Africa BPO call centre global business services outsourcing jobs",
        "summary": (
            "SA's quiet export winner: #1 ranked offshore CX destination "
            "(neutral English accent, timezone, 50-60% cost saving vs UK/US), "
            "government incentives per offshore job, 100k+ international "
            "seats and growing double digits. AI is both the threat (basic "
            "voice work) and the upsell (AI-assisted omnichannel)."
        ),
        "capital": {
            "micro": "R100k-R500k (work-from-home micro-campaign, lead-gen pod of 5-10 seats)",
            "small": "R2m-R15m (50-150 seat facility with BYOC campaigns)",
            "medium": "R30m-R200m (500+ seats multi-client, impact-sourcing at scale)",
            "note": "GBS incentive pays R uptoR1.1k/job/month for offshore work "
                    "(tiered); the real gate is landing the first international "
                    "client - broker/BPO-aggregator routes derisk entry.",
        },
        "kpis": [
            {"kpi": "Seat utilisation", "target": ">85%", "why": "Empty seats with leases and salaries are the classic BPO failure."},
            {"kpi": "Attrition rate", "target": "<35% p.a. (industry runs 40-60%)", "why": "Recruitment/training cost per agent is R15k-R30k."},
            {"kpi": "Revenue per seat vs cost per seat", "target": ">R25k/month offshore revenue", "why": "Domestic campaigns pay half of offshore; mix decides margin."},
            {"kpi": "Client concentration", "target": "No client >40% of seats", "why": "Campaign loss without diversification is instant crisis."},
        ],
        "failure": {
            "baseline": "Failures cluster in domestic-campaign-only centres with thin margins and in operators who built seats before contracts.",
            "drivers": ["Building capacity ahead of contracts", "Domestic-only low-margin campaigns",
                        "Attrition cost spirals", "AI displacing simple voice work"],
        },
        "success_factors": [
            "Offshore (UK/US/AUS) clients from day one",
            "Move up value chain: omnichannel, tech support, back-office, legal/med process",
            "Impact-sourcing angle (township talent) wins global corporate procurement",
        ],
        "gaps": [
            "AI-augmented CX services (human+bot blended offerings)",
            "Specialised verticals: healthcare admin, legal process, fintech compliance ops",
            "Secondary-city delivery centres (Gqeberha, Durban - cost below Cape Town/Joburg)",
            "Training academies feeding the talent pipeline (funded by SETAs)",
        ],
        "longterm": {
            "score": 80,
            "drivers": ["Global offshoring momentum to SA", "Government GBS incentives",
                        "Youth labour pool with neutral English"],
            "risks": ["Generative AI eroding basic voice volumes", "Competitor destinations (Kenya, Egypt)",
                      "Infrastructure reliability perceptions"],
        },
        "barriers": 45,
        "structural": 80,
    },
}
