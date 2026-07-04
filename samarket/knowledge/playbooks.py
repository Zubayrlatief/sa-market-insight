"""Market-entry playbooks for South African sectors.

For each sector: how to get in step by step, a year-by-year roadmap with
realistic ZAR targets, how KPIs evolve by growth stage, how clients are
actually acquired (outbound/inbound) and kept, and the 10-20 year game.

Figures are planning benchmarks for a competent, funded operator - real
results vary widely. Treat every number as a target corridor, not a promise.
"""

PLAYBOOKS = {
    "ict": {
        "positioning": "Enter as a specialist services firm earning rand, "
                       "then convert to offshore clients earning pounds/dollars, "
                       "then productise into recurring revenue.",
        "entry": [
            ("Pick a vertical, not a technology",
             "Choose one industry you'll serve (logistics, healthcare admin, body corporates, "
             "agri) and one painful workflow in it. 'Full-stack dev shop' is a race to the bottom; "
             "'we automate claims admin for medical practices' commands 3x the rate."),
            ("Register and set up lean",
             "CIPC company (R175), SARS tax + VAT once over R1m turnover, business bank account, "
             "professional indemnity insurance (~R6k-R15k/yr). No office - work remote, meet clients on-site."),
            ("Land 2-3 anchor clients before hiring anyone",
             "Use your network, past employers, and direct outreach. Anchor clients on monthly retainers "
             "(R25k-R80k) fund everything else. Never start with one client >50% of revenue."),
            ("Build the delivery bench slowly",
             "First hires: one mid-level dev and one junior per ~R150k/month of contracted revenue. "
             "Salaries are your only real cost - keep 4-6 months of payroll banked before each hire."),
            ("Go offshore within 18 months",
             "List on Clutch/Upwork Enterprise, join UK/EU agency-partner networks, use SA's timezone "
             "pitch (GMT+2 = live overlap with Europe). One UK client at £450-£650/day per dev doubles "
             "your margin overnight."),
            ("Productise by year 3",
             "Take the workflow you've now built 5 times and turn it into a licensed product or hosted "
             "SaaS with monthly billing. Services fund the build; the product is what scales."),
        ],
        "roadmap": [
            ("Year 1", "Prove billable demand solo/tiny",
             ["Revenue R600k-R1.5m (you + 1-2 devs)",
              "2-3 retainer clients, none >50% of revenue",
              "Utilisation of billable people >65%",
              "Effective rate >R650/hour blended",
              "6 months' payroll in the bank by December"]),
            ("Years 2-3", "Team of 5-10, first offshore revenue",
             ["Revenue R3m-R8m, gross margin >45%",
              "Offshore clients = 25-40% of revenue",
              "Recurring (retainer/support) revenue >30%",
              "Revenue per developer >R1.2m/year",
              "Client concentration: top client <35%"]),
            ("Years 4-5", "Specialist firm with a product line",
             ["Revenue R12m-R30m, EBITDA 15-20%",
              "Product/SaaS revenue >15% and growing",
              "Offshore >40% of revenue (rand hedge)",
              "Team 15-30 with 2 delivery leads (you're out of delivery)",
              "Net revenue retention >100% on recurring base"]),
            ("Years 6-10", "Scale-up: agency + product engine",
             ["Revenue R40m-R120m or SaaS ARR R15m-R50m",
              "EBITDA 20%+ services / rule-of-40 on SaaS",
              "3+ verticals or 2+ export markets",
              "Senior team owns sales - founder on strategy/M&A",
              "Consider acquiring 1-2 small shops for capability"]),
            ("Years 10-20", "Regional platform or exit",
             ["Either: sell to an international integrator (services trade at 5-8x EBITDA, "
              "SaaS at 3-6x revenue) - or build an African platform via AfCFTA",
              "AI-native service lines replacing headcount-based pricing with outcome pricing",
              "Talent academy feeding your own pipeline (SETA-funded learnerships)"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Utilisation >65% of billable hours", "Blended rate >R650/hr",
              "Cash runway >4 months always", "Proposal win rate >30%"]),
            ("Growth (years 3-5)",
             ["Revenue per head >R1.2m", "Recurring revenue >30%",
              "Offshore revenue share >35%", "Staff attrition <15%/yr",
              "Gross margin >45%"]),
            ("Scale (years 6-10+)",
             ["EBITDA >20%", "Net revenue retention >105%",
              "Founder-free sales: >70% of new deals closed without you",
              "Product revenue >25%", "Pipeline coverage 3x quarterly target"]),
        ],
        "outbound": [
            "Direct LinkedIn + email to CTOs/CFOs in your vertical: lead with a diagnostic "
            "('we found 4 hours/week of manual work in firms like yours'), not capability lists",
            "Partner channels: Microsoft/AWS partner directories, accounting firms and consultancies "
            "who refer their clients' tech problems",
            "UK/EU agency subcontracting marketplaces (YunoJuno, Distributed, agency-to-agency deals) "
            "to land offshore work before you have a brand",
            "Respond to RFPs/tenders selectively - private sector only until you have cash buffers "
            "for government payment terms",
        ],
        "inbound": [
            "One deep case study per anchor client with real numbers - this is the highest-ROI "
            "marketing asset in B2B services",
            "SEO on vertical problem terms ('practice management integration South Africa'), "
            "not generic 'software development'",
            "Speak at the vertical's industry events (logistics conferences, medical practice "
            "management seminars) - not tech meetups; your buyers aren't there",
            "Open-source a small tool your vertical uses; it ranks, builds trust, and feeds leads",
        ],
        "retention": [
            "Convert every project to a support retainer at handover (aim 60%+ conversion)",
            "Quarterly business reviews showing value delivered in rand saved/earned",
            "Product roadmap co-design with top clients - they fund features and can't leave",
            "Fix the key-person risk: 2 people minimum on every account",
        ],
        "longgame": [
            "AI will deflate hourly-rate coding - move pricing to outcomes and retained products early",
            "SA's durable advantage is talent cost + timezone + English: build the offshore pipe, "
            "and own a niche where domain knowledge (not code volume) is the moat",
            "Data-residency and POPIA-type compliance work grows for 20 years as Africa regulates",
            "Exit optionality: international integrators buy vertical specialists, not generalists",
        ],
    },

    "energy": {
        "positioning": "Enter through C&I solar installation with certified skills, "
                       "build an O&M annuity book, then graduate to storage, wheeling "
                       "and small IPP development.",
        "entry": [
            ("Get the paperwork that wins bids",
             "PV GreenCard training, a registered Master Electrician for CoCs (hire or partner), "
             "SAPVIA membership, CIPC + tax clearance + B-BBEE affidavit. C&I clients and insurers "
             "check all of it."),
            ("Start as a subcontract install crew",
             "Do 6-12 months installing for established EPCs. You learn pricing, standards and "
             "supplier terms on someone else's balance sheet - and you see which niches are underserved."),
            ("Pick the commercial & industrial niche, skip residential",
             "Residential is saturated post-loadshedding. Target factories, farms (irrigation + "
             "cold rooms), body corporates, schools, lodges: 30-200kWp systems, R400k-R3m tickets, "
             "payback logic sells itself at current tariffs."),
            ("Solve the financing objection before it's raised",
             "Partner with solar finance providers (rent-to-own, PPA funds) so capex-shy clients "
             "can sign at R0 upfront. The installer who brings financing closes 2-3x more."),
            ("Attach O&M to every install",
             "Monitoring + cleaning + insurance-repair contract at 1-2% of system value/year. "
             "This annuity is what makes the business sellable later."),
            ("Add storage and energy services from year 3",
             "BESS retrofits, tariff optimisation, and (as market rules open) wheeling/trading "
             "partnerships. Register early interest with NERSA processes via a trading partner."),
        ],
        "roadmap": [
            ("Year 1", "Certified crew, first direct clients",
             ["8-15 C&I installs (or 30-50 subcontracted), revenue R2m-R5m",
              "Gross margin >22% on own projects",
              "Zero CoC/compliance failures",
              "3 finance-partner agreements signed",
              "O&M contracts on >50% of own installs"]),
            ("Years 2-3", "C&I brand with an O&M base",
             ["Revenue R8m-R20m, 25-40 projects/yr",
              "O&M annuity book R500k-R1.5m/yr and growing",
              "Quote-to-close >25% on referred leads",
              "1 anchor segment owned (e.g. agri in your province)",
              "Stock turn >6x - never warehouse panels speculatively"]),
            ("Years 4-5", "Storage + larger projects",
             ["Revenue R30m-R70m, EBITDA 12-18%",
              "BESS attached to >40% of new projects",
              "First 1-5MW ground-mount as EPC or co-developer",
              "O&M book >R4m/yr (this is your valuation anchor)",
              "Wheeling/PPA deal participation via trader partnerships"]),
            ("Years 6-10", "Developer-operator",
             ["Development pipeline 20-100MW (own 10-30% equity positions)",
              "Recurring revenue (O&M + generation) >35% of total",
              "Revenue R100m-R300m or asset-based returns replacing EPC margin",
              "Grid-connection expertise as a paid service (the bottleneck is the business)"]),
            ("Years 10-20", "Yield portfolio",
             ["Own/co-own generating assets earning 15-25 year PPA income",
              "Municipal distribution O&M concessions as they outsource",
              "EV charging network positions on logistics corridors",
              "Exit: sell the O&M book + pipeline to a utility-scale player (annuity books "
              "trade at 4-8x recurring revenue)"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Installed cost R9-R14/Wp competitive", "GM per project >22%",
              "Installs per crew per month >3", "Referral rate >30% of new work"]),
            ("Growth (years 3-5)",
             ["O&M contracts as % of installs >60%", "Quote-to-close >25%",
              "Project margin variance <5% vs quoted", "Days sales outstanding <45",
              "Callback/defect rate <3%"]),
            ("Scale (years 6-10+)",
             ["Recurring revenue >35%", "MW under management growing 30%/yr",
              "Development pipeline conversion >20%", "EBITDA >15%",
              "Fleet performance ratio >80% across managed sites"]),
        ],
        "outbound": [
            "Free energy audits for factories/farms with a one-page payback model - the audit "
            "IS the sales call; aim at operations managers, not procurement",
            "Sector-by-sector campaigns: dairy co-ops, packhouses, private schools, lodges - "
            "one reference client per segment unlocks the rest via word of mouth",
            "Partner with electrical contractors, roofers and agri-equipment dealers who see "
            "the client's roof before you do (pay 3-5% referral fees)",
            "Body corporate AGM presentations with sectional-title-specific finance structures",
        ],
        "inbound": [
            "Publish real production data from your installs (monthly kWh vs promise) - "
            "radical transparency beats every competitor's brochure",
            "Google Ads on 'commercial solar + [city]' with a payback calculator landing page",
            "Case studies with the client's actual saving in rand on the electricity bill",
            "Referral programme: one month's free O&M for every referred install",
        ],
        "retention": [
            "Monitoring portal + WhatsApp alerts - clients who watch their generation daily "
            "never churn and buy batteries next",
            "Annual system health report with upsell path (storage, expansion, tariff review)",
            "Performance guarantees with skin in the game (credit shortfall vs promised yield)",
            "O&M contracts with 3-year terms and CPI escalation",
        ],
        "longgame": [
            "Coal fleet retirement + grid constraints guarantee 15+ years of demand; the profit "
            "pool moves from installation (commoditising) to operations, storage and trading",
            "Position for the energy-trading era now: relationships with licensed traders, "
            "wheeling-ready client base, metering data ownership",
            "Municipal distribution failure = concession opportunity for credible private operators",
            "Own generating assets - the end-state is earning from electrons, not labour",
        ],
    },

    "fintech": {
        "positioning": "Enter with a licensed, revenue-first niche (advisory practice or "
                       "SME-focused product), distribute through partners rather than ads, "
                       "and let the licence moat compound.",
        "entry": [
            ("Choose your regulatory lane first",
             "Advisory/brokerage: FSP licence (Cat I) with RE5 exams - cheapest entry, income from "
             "day one. Payments: partner with a licensed sponsor (bank BIN or TPPP). Lending: NCR "
             "registration. Insurance: cell captive or UMA under an insurer's licence. The lane "
             "decides everything downstream."),
            ("Start under someone else's licence",
             "Join an existing FSP as a representative, or build your product on a sponsor's rails "
             "(Stitch/Peach for payments, a cell captive for insurance). You trade margin for 12-18 "
             "months of speed and compliance cover."),
            ("Pick an underserved segment with money",
             "SMEs (the R350bn credit gap), informal traders (device insurance, stock finance via "
             "spaza platforms), gig workers, stokvels, SADC remitters. Avoid competing with banks "
             "for salaried consumers - CAC will kill you."),
            ("Get to revenue before raising",
             "SA funding is scarce and dilutive pre-revenue. A book of 50 advisory clients or an "
             "SME product with R100k MRR beats any deck. Bootstrap or take angel money only."),
            ("Embed distribution - never buy it retail",
             "Partner with whoever already has your customer's trust: retailers, telcos, employers, "
             "accountants, franchise networks, industry associations. Rev-share beats paid ads on "
             "every metric in SA."),
            ("Build the compliance function early",
             "FICA, POPIA, and (incoming) COFI compliance done properly is a moat - subscale "
             "competitors can't afford it and partners audit it before signing."),
        ],
        "roadmap": [
            ("Year 1", "Licensed and earning",
             ["Advisory: 60-120 clients, R600k-R1.5m revenue | Product: live with 1 "
              "distribution partner, 1,000-5,000 users",
              "Compliance: zero findings; FICA/KYC processes documented",
              "Unit economics mapped: know your CAC and payback per channel",
              "12+ months runway maintained"]),
            ("Years 2-3", "Repeatable distribution",
             ["Advisory: AUA R50m-R150m, recurring fees >60% of income | Product: "
              "MRR R200k-R1m, 2-3 embedded partners",
              "LTV/CAC >3x proven on at least one channel",
              "Default/loss rate <8% if lending; claims ratio <60% if insurance",
              "Team 5-15 incl. dedicated compliance officer"]),
            ("Years 4-5", "Scale the winning channel",
             ["Advisory: AUA R300m-R600m, practice revenue R5m-R12m | Product: "
              "MRR R1.5m-R5m, 50k-250k users",
              "Own licence upgrade complete (own FSP/NCR/insurance cell)",
              "Second product line cross-sold to the same base (>15% attach rate)",
              "EBITDA positive or funded through Series A (R30m-R100m rounds are realistic here)"]),
            ("Years 6-10", "Multi-product platform",
             ["Revenue R30m-R150m; users 250k-1m+ or AUA R1bn+",
              "3+ products per customer relationship (lending + insurance + payments)",
              "Bank/insurer partnership or acquisition interest - banks buy distribution "
              "they can't build",
              "SADC corridor expansion (start with remittance/trade lanes you already touch)"]),
            ("Years 10-20", "Regional financial platform or strategic exit",
             ["African multi-market presence via AfCFTA financial services protocols",
              "Banking-as-a-service or full licence if economics justify (R50m+ capital)",
              "Exit paths: bank acquisition (strategic premium), PE consolidation of "
              "advisory books (2.5-4x recurring revenue), or listed via JSE AltX"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["CAC payback <12 months", "Activation rate >40% of sign-ups",
              "Compliance findings: zero", "MRR growth >15%/month off small base"]),
            ("Growth (years 3-5)",
             ["LTV/CAC >3x", "NPL <8% / claims ratio <60%", "Churn <3%/month",
              "Revenue per employee >R1m", "Partner-sourced share of new business >60%"]),
            ("Scale (years 6-10+)",
             ["Products per customer >2", "Cost-to-income ratio <60%",
              "Cohort LTV still rising at month 24", "Capital adequacy comfortably above minimums",
              "Regulatory relationships: proactive, not reactive"]),
        ],
        "outbound": [
            "Partnership-first outbound: pitch retailers/telcos/employer groups/accounting "
            "networks on rev-share embedded products - one partner = thousands of users",
            "For advisory: structured referral agreements with accountants, attorneys and "
            "estate agents; run retirement/tax workshops at employers",
            "SME lending: work trade associations and franchisors whose members share "
            "transaction data patterns you can underwrite",
            "Conference presence where your partners (not consumers) gather: retail, telco, "
            "HR and franchise industry events",
        ],
        "inbound": [
            "Calculators and tools that answer money questions (retirement gap, business "
            "loan affordability) - SA search volume is huge and trust transfers",
            "Vernacular content and WhatsApp-first onboarding for mass-market products",
            "Media commentary on rates/budget/two-pot - journalists need quotable experts, "
            "and authority compounds",
            "Client testimonials with real outcomes (approved loan, paid claim) - trust is "
            "the entire product in financial services",
        ],
        "retention": [
            "Annual reviews that show value in rand (fees vs returns, premiums vs claims paid)",
            "Product depth: every added product halves churn - engineer the second-product "
            "moment into month 3-6",
            "Proactive service on life events (claims, renewals, rate changes) - the moments "
            "that decide loyalty",
            "For partners: quarterly performance packs proving their rev-share is growing",
        ],
        "longgame": [
            "Open banking + PayShap re-plumb SA finance over the next decade - build on the "
            "new rails, not the old ones",
            "The informal economy formalises slowly but inevitably; whoever holds those "
            "customer relationships at scale becomes an acquisition target",
            "Compliance burden keeps rising - it crushes small players and protects "
            "established ones; get established",
            "SA is the fintech gateway to a 1.4bn-person continent; SADC first, then AfCFTA lanes",
        ],
    },

    "logistics": {
        "positioning": "Enter with contracted vehicles (never speculative), niche into "
                       "cold chain or last-mile density, then build the 3PL layer where "
                       "the real margins live.",
        "entry": [
            ("Secure the contract before the vehicle",
             "A truck without a lane is a liability shedding R30k+/month. Get a signed contract or "
             "sub-contract (courier networks, FMCG distributors, e-com fulfilment) first, then "
             "finance the vehicle against it."),
            ("Set up compliant from day one",
             "CIPC + GIT (goods-in-transit) insurance + operating licences where applicable + "
             "RTMS accreditation as you grow. Big clients audit insurance and roadworthiness "
             "before awarding lanes."),
            ("Start where density or specialisation pays",
             "Metro last-mile (e-com parcels, pharma), cold chain (food/agri exports), or "
             "specialised loads (dangerous goods, outsize). Avoid general long-haul - it's a "
             "rate-war with owner-drivers."),
            ("Engineer out the empty legs",
             "Backhaul agreements and load-matching platforms from vehicle #1. Loaded-km "
             "percentage is the single biggest lever on profit."),
            ("Add the warehouse when clients ask twice",
             "Cross-dock/fulfilment space converts you from commodity transporter to 3PL with "
             "sticky contracts and storage + pick-pack margins."),
            ("Protect the downside ruthlessly",
             "Fuel-price escalation clauses in every contract, telematics + driver vetting for "
             "hijack risk, no client >40% of revenue, maintenance fund of 8-10% of revenue."),
        ],
        "roadmap": [
            ("Year 1", "2-4 vehicles, all contracted",
             ["Revenue R1.8m-R4m, EBITDA >10%",
              "Loaded km >80%; cost per km tracked weekly",
              "Zero uninsured incidents; GIT + liability current",
              "1 anchor contract + 2 secondary revenue streams",
              "Driver retention 100% (pay above market, they're the business)"]),
            ("Years 2-3", "Fleet 8-15, niche established",
             ["Revenue R8m-R20m, EBITDA 12-15%",
              "OTIF >95% measured and reported to clients monthly",
              "Fuel spread (revenue/km minus cost/km) >R6 long-haul or "
              "cost per parcel <R35 metro last-mile",
              "First warehouse/cross-dock (1,000-3,000m²)",
              "Client concentration: top client <40%"]),
            ("Years 4-5", "3PL with contracts",
             ["Revenue R30m-R70m; storage + value-added services >20% of revenue",
              "Fleet 20-40 + owner-driver network for peaks",
              "WMS/TMS systems live - data is what wins corporate tenders",
              "2-3 year contracted revenue >60% of book",
              "EBITDA 15%+"]),
            ("Years 6-10", "Network operator",
             ["Revenue R100m-R300m, multi-node DC network",
              "Cross-border SADC lanes (Zim/Zam/Moz/Bots corridors) >15% of revenue",
              "Private rail siding/slot participation as Transnet opens access",
              "Tech layer: client portals, API integrations to e-com platforms",
              "Consider acquiring niche competitors (cold chain books trade well)"]),
            ("Years 10-20", "Infrastructure-grade logistics",
             ["Rail-linked terminals and port-adjacent facilities as concessions mature",
              "Regional corridor operations under AfCFTA volume growth",
              "EV/alternative-fuel fleet transition (cost advantage arrives ~2030s)",
              "Exit: strategic sale to a global 3PL entering Africa (they buy networks, "
              "not trucks) or private equity roll-up"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Loaded km >80%", "Cost per km vs revenue per km spread >R6",
              "Vehicle utilisation >22 days/month", "Breakdown downtime <3%"]),
            ("Growth (years 3-5)",
             ["OTIF >95%", "EBITDA >12%", "Claims/damage <0.5% of revenue",
              "Contracted revenue >60%", "Driver attrition <20%/yr"]),
            ("Scale (years 6-10+)",
             ["Revenue per vehicle >R2m/yr", "Warehouse utilisation >85%",
              "Revenue from value-added services >25%", "Debt service cover >2x",
              "Cross-border share >15%"]),
        ],
        "outbound": [
            "Target supply-chain managers at FMCG/retail/pharma with a specific lane proposal "
            "and your OTIF data - specificity beats capability brochures",
            "Sub-contract to established 3PLs and courier networks (The Courier Guy, DSV "
            "overflow) to build volume history that wins your own contracts later",
            "Tender for retail DC-to-store and e-com fulfilment contracts once you have "
            "12 months of performance data",
            "Agri exporters and packhouses for cold-chain lanes - approach before harvest "
            "season with reefer capacity commitments",
        ],
        "inbound": [
            "Case studies with hard numbers: OTIF, damage rates, cost per parcel vs "
            "the client's previous provider",
            "Google Business + SEO for '[niche] transport [city]' - surprisingly "
            "uncontested for specialised terms",
            "Industry association membership (SAAFF, RFA) where corporate shippers look "
            "for vetted providers",
            "Referrals from warehouse landlords, clearing agents and packaging suppliers "
            "who hear about capacity needs first",
        ],
        "retention": [
            "Monthly performance packs (OTIF, claims, cost trends) before the client asks - "
            "transparency wins renewals",
            "Integrate into their systems (EDI/API) - switching costs keep contracts",
            "Fuel-price escalation clauses protect margin so you never degrade service to "
            "survive a diesel spike",
            "Dedicated account contact + WhatsApp visibility groups for operational trust",
        ],
        "longgame": [
            "Transnet reform is the decade's opportunity: private rail access, port "
            "concessions and rail-adjacent property will mint the next logistics fortunes",
            "E-commerce last-mile grows 20%+/yr for the foreseeable future - density "
            "compounds into unassailable unit economics",
            "AfCFTA corridor volumes make cross-border capability increasingly valuable",
            "The end-state asset is the network + contracts + data, not the vehicles - "
            "keep the balance sheet light and the relationships heavy",
        ],
    },

    "bpo": {
        "positioning": "Enter with a small offshore-focused pod via aggregators, nail "
                       "attrition and quality metrics, then scale seats into specialised "
                       "verticals where AI augments rather than replaces.",
        "entry": [
            ("Learn the trade inside first",
             "Run a campaign or ops team in an existing BPO for 6-12 months if you haven't. "
             "This business is won or lost on operational discipline you can't learn from outside."),
            ("Start with a 5-15 seat pod, not a call centre",
             "Rent seats in a serviced BPO facility or run work-from-home with monitoring tools. "
             "Capex under R500k. Building a 100-seat floor before contracts is the classic failure."),
            ("Get offshore work via aggregators and brokers",
             "Direct UK/US/AUS clients won't sign an unknown - go through BPO brokers, outsourcing "
             "marketplaces and referral partners who take 5-15% but hand you campaigns. Domestic "
             "campaigns pay half; use them only to keep seats warm."),
            ("Register for the GBS incentive early",
             "The dtic GBS incentive pays up to ~R1.1k/job/month for qualifying offshore jobs - "
             "it materially changes unit economics. Get compliant (job creation reporting) from "
             "the start."),
            ("Specialise within 24 months",
             "Pick a vertical: healthcare admin, legal process, fintech compliance ops, e-commerce "
             "CX. Specialist seats bill 30-60% above generic voice and resist AI displacement."),
            ("Build the talent engine",
             "Recruitment + 4-6 week training academy + team-lead pipeline. Attrition is the "
             "profit killer; the operators who solve it (career paths, transport, culture) win."),
        ],
        "roadmap": [
            ("Year 1", "Prove delivery on 5-15 seats",
             ["Revenue R1.5m-R4m; 1-2 campaigns via brokers",
              "Seat utilisation >85%; QA scores >90% of client target",
              "Attrition <40% annualised",
              "GBS incentive registration complete",
              "One client reference letter you can show"]),
            ("Years 2-3", "50-100 seats, direct offshore clients",
             ["Revenue R10m-R30m; offshore >70% of seats",
              "Revenue per seat >R20k/month offshore",
              "First direct (non-brokered) international client",
              "Attrition <35%; team leads promoted from within >80%",
              "No client >40% of seats"]),
            ("Years 4-5", "Vertical specialist, 150-350 seats",
             ["Revenue R40m-R100m, EBITDA 12-18%",
              "2 specialised verticals with premium billing",
              "AI-assisted workflows live (agent-assist, QA automation) - pitch as "
              "productivity, bill on outcomes",
              "Second-city delivery site (Gqeberha/Durban cost advantage)",
              "Impact-sourcing credentials documented (township talent %, training hours)"]),
            ("Years 6-10", "500-1,500 seats or outcome-based services",
             ["Revenue R150m-R500m",
              "Blended human+AI service lines: billing per resolution/outcome, not per hour",
              "Client mix across UK/US/AUS - currency and cycle diversification",
              "Own training academy with SETA funding feeding 100% of hiring",
              "M&A: bolt-on niche providers or be bolted on (BPOs trade at 4-7x EBITDA)"]),
            ("Years 10-20", "Global business services firm",
             ["Move up-stack permanently: complex ops (claims, underwriting support, "
              "clinical admin), where judgement + empathy resist automation",
              "Multi-country delivery (SA + Kenya/Egypt) for follow-the-sun coverage",
              "The prize: owning client processes end-to-end under multi-year MSAs"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Seat utilisation >85%", "QA/CSAT at or above client target",
              "Attrition <40%", "Cost per hire <R20k"]),
            ("Growth (years 3-5)",
             ["Revenue per seat >R22k/mo offshore", "EBITDA >12%",
              "Client concentration <40%", "Absenteeism <5%",
              "Speed-to-competency <6 weeks"]),
            ("Scale (years 6-10+)",
             ["EBITDA >18%", "Multi-year contract share >60%",
              "Outcome-priced revenue >25%", "Attrition <30%",
              "Net promoter score from clients >50"]),
        ],
        "outbound": [
            "BPO brokers/advisors in UK/US (they place campaigns for a fee) - the fastest "
            "route to offshore revenue without a sales office abroad",
            "Direct outreach to COOs/Heads of CX at mid-size UK/AUS firms (50-500 staff) "
            "too small for Teleperformance but big enough to outsource 10-30 seats",
            "Attend/exhibit at CCW, CX events in London; partner with CapeBPO/GBS SA trade "
            "missions - government actively brokers introductions",
            "Referral agreements with SA firms already serving those markets (software "
            "agencies, accountants) whose clients need back-office capacity",
        ],
        "inbound": [
            "Rank for 'outsourcing to South Africa' comparison content (vs Philippines/India) "
            "- buyers research destination first, provider second",
            "Publish your operational metrics openly (attrition, QA, speed-to-competency) - "
            "operational transparency is rare and converts",
            "Impact-sourcing story (township employment, first-job creation) - global "
            "corporates' procurement teams score it in vendor selection",
            "Client video testimonials with accents your buyers recognise (UK/AUS voices "
            "vouching for SA delivery)",
        ],
        "retention": [
            "Weekly ops reviews + monthly business reviews with improvement roadmaps - "
            "never let performance conversations happen only at renewal",
            "Embed continuous improvement: bring the client cost-reduction ideas before "
            "they ask (even when it cuts your seats - it wins the decade)",
            "Cross-train backup pods so client campaigns never feel key-person risk",
            "Grow share-of-wallet: start with one process, map their org for the next three",
        ],
        "longgame": [
            "Generative AI eats simple voice work - the survivors sell outcomes, complex "
            "judgement work and AI-supervised hybrid teams; start that transition now",
            "SA's accent/empathy/timezone advantages matter more as work gets more complex, "
            "not less",
            "GBS incentives and a young English-speaking labour pool give SA a 10-15 year "
            "policy tailwind",
            "End-state: process ownership under long MSAs (quasi-infrastructure revenue) "
            "or strategic exit to a global GBS platform",
        ],
    },

    "tourism": {
        "positioning": "Enter capital-light through experiences and direct-booking skill, "
                       "then buy/build accommodation once you own a guest pipeline, then "
                       "consolidate into a multi-property brand or inbound operator.",
        "entry": [
            ("Start with experiences, not beds",
             "Tours, transfers, food/wine/township/adventure experiences need R50k-R500k, not "
             "R5m. You learn the guest, the seasonality and the channels before betting on property."),
            ("Get legal and listed",
             "Tour operator: registered guide (CATHSSETA) or hire guides, PDP-licensed vehicles, "
             "passenger liability insurance. List on GetYourGuide/Viator/Airbnb Experiences day one - "
             "their demand is instant, their 20-30% commission is tuition."),
            ("Master reviews as the core asset",
             "4.8+ on TripAdvisor/Google with 200+ reviews outranks any ad budget. Engineer the "
             "review ask into every tour's final 10 minutes."),
            ("Build direct booking muscle",
             "Own website with instant booking, WhatsApp Business, Google Business Profile. Shift "
             "from 100% OTA to 40%+ direct within 2 years - that margin difference funds growth."),
            ("Add accommodation against a known pipeline",
             "Once your experiences feed you guests, lease or buy a guesthouse where your guests "
             "already want to stay. Buy distressed/tired stock and refurbish - never pay for "
             "someone else's goodwill."),
            ("Package into itineraries",
             "Combine your beds + your experiences + partner products into multi-day packages "
             "sold to inbound agents and directly to source markets. Packaging doubles revenue "
             "per guest."),
        ],
        "roadmap": [
            ("Year 1", "One excellent product, review velocity",
             ["500-1,500 guests, revenue R600k-R1.5m",
              "Rating >4.8 with 150+ reviews across platforms",
              "Direct bookings >20% by December",
              "Repeat/referral bookings measurable (ask every guest how they found you)",
              "Gross margin >55% on experiences"]),
            ("Years 2-3", "Product range + first property",
             ["Revenue R3m-R8m; 3-5 experience products",
              "Direct bookings >40% (OTA commission saved = your marketing budget)",
              "First accommodation: 6-12 rooms leased/bought, occupancy >55% year one",
              "Shoulder-season revenue >25% of annual (corporate, domestic, MICE fill)",
              "Database: 5,000+ past guests with email/WhatsApp consent"]),
            ("Years 4-5", "Destination business",
             ["Revenue R12m-R30m, EBITDA 18-25%",
              "Occupancy >65% annualised; RevPAR at/above your STR comp set",
              "Multi-day packages >30% of revenue",
              "Inbound agent relationships in 3+ source markets (UK/DE/NL/US + India/China)",
              "Second property or exclusive-use venue"]),
            ("Years 6-10", "Brand or inbound operator at scale",
             ["Revenue R40m-R120m; 3-6 properties or DMC handling 10k+ pax/yr",
              "Direct + repeat + agent = 80% of bookings (OTA dependence broken)",
              "Yield management running daily (dynamic pricing)",
              "Own source-market representation (agent in UK/India) or niche authority "
              "(SA's best cycling/food/rail operator)"]),
            ("Years 10-20", "Institutional asset",
             ["Property portfolio with hospitality operating company split (opco/propco) - "
              "the structure funds expansion and enables exit",
              "Asia volume: India/China direct packages as visa reform matures",
              "Exit: hotel groups and PE buy occupancy track records and direct-booking "
              "engines; lodges trade on EBITDA multiples of 6-10x"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Review rating >4.8, velocity >10/month", "Direct booking share >20%",
              "Gross margin >55% experiences", "Guest acquisition cost <10% of booking value"]),
            ("Growth (years 3-5)",
             ["Occupancy >65%", "Direct >40%", "Revenue per guest growing 10%+/yr",
              "Shoulder-season share >25%", "Repeat/referral >20% of bookings"]),
            ("Scale (years 6-10+)",
             ["RevPAR vs comp set >100%", "EBITDA >20%", "Database conversion >5%/campaign",
              "Package attach rate >30%", "Staff retention >80% season-to-season"]),
        ],
        "outbound": [
            "Inbound tour operators and DMCs in source markets: pitch with commission "
            "structure, rate sheets and STO agreements before their planning seasons",
            "Corporate/MICE planners for shoulder-season groups (conferences, incentives, "
            "year-end functions)",
            "Partnerships with complementary operators (wine farms, transfer companies, "
            "restaurants) for cross-sell packages",
            "Travel trade shows: WTM Africa, Indaba - one good agent relationship pays "
            "for years of stands",
        ],
        "inbound": [
            "OTA excellence first (photography, first 3 review pages, response times) - "
            "it's the discovery engine whether you like the commission or not",
            "Destination SEO content ('3 days in [town] itinerary') that captures planners "
            "before they hit OTAs",
            "Instagram/TikTok location content - travel is decided visually; user-generated "
            "content from guests outperforms produced content",
            "Google Business Profile + WhatsApp instant response (speed of reply predicts "
            "booking conversion more than price)",
        ],
        "retention": [
            "Post-stay email/WhatsApp journeys: review ask → referral offer → return-visit "
            "offer at 10-11 months",
            "Guest database segmented by source market and interest - your list is the "
            "only channel with zero commission",
            "Loyalty pricing for direct repeat bookers (never discount via OTAs)",
            "Partnerships that keep you in the guest's trip even when beds are full "
            "(cross-referral with trusted competitors)",
        ],
        "longgame": [
            "Weak rand makes SA structurally cheap for hard-currency travellers - a "
            "20-year tailwind independent of domestic economics",
            "Visa reform + air access decide the Asia volume wave; position products for "
            "Indian and Chinese group travel now",
            "Climate/authenticity trends favour nature, township and cultural product - "
            "SA's unfair advantages",
            "The end-state asset is the direct-booking brand + guest database + property "
            "yield; OTA-dependent businesses never compound",
        ],
    },

    "retail": {
        "positioning": "Enter online-first in a niche category (or via a proven franchise), "
                       "build margin through private label, then go omnichannel where the "
                       "chains can't follow.",
        "entry": [
            ("Choose niche depth over general width",
             "Pick a category with passion + repeat purchase + import inefficiency (pet "
             "specialty, outdoor gear, hair care, halaal foods, baby). You must be the most "
             "knowledgeable seller in it, not the cheapest."),
            ("Validate with R30k-R100k, not a store",
             "Land 50-200 units of stock, sell via Takealot Marketplace + Instagram/WhatsApp + "
             "Facebook Marketplace. If you can't sell R50k/month from a spare room, a store "
             "won't save you."),
            ("Set up the boring infrastructure",
             "CIPC, SARS (import code if importing), Payfast/Yoco payments, a Shopify/WooCommerce "
             "store, courier accounts (The Courier Guy, Pudo lockers). Unit economics sheet: "
             "landed cost, CAC, delivery, returns - per SKU."),
            ("Win on availability and service, not price",
             "Same-day dispatch, WhatsApp answers in minutes, easy returns. SA online shoppers "
             "pay for reliability because it's scarce."),
            ("Private label at proven volume",
             "Once a category sells 300+ units/month, import your own brand (Alibaba/local "
             "manufacturers): margin jumps from 25-35% to 50-65% and you become un-undercuttable."),
            ("Add physical presence where your data says",
             "Pop-ups, then a store or franchise in the node where your delivery heatmap is "
             "densest. Alternatively: franchise entry (R800k-R3m) is the lower-risk physical "
             "route - 60%+ 5-year survival vs ~20% independent."),
        ],
        "roadmap": [
            ("Year 1", "Prove the niche online",
             ["GMV R600k-R2m; gross margin >30%",
              "CAC payback <2 orders; repeat purchase rate >20%",
              "Same-day dispatch >95%; rating >4.6 on marketplaces",
              "300+ WhatsApp/email subscribers buying monthly",
              "3 hero SKUs identified for private label"]),
            ("Years 2-3", "Brand + private label",
             ["Revenue R4m-R12m; private label >30% of sales at >50% margin",
              "Repeat rate >30%; email/WhatsApp drive >25% of orders (owned, not paid)",
              "Stock turns >6x; dead stock <5%",
              "Marketplace + own-site + social commerce all >20% of sales each",
              "First pop-up/store trading profitably in month 3"]),
            ("Years 4-5", "Omnichannel category leader",
             ["Revenue R15m-R50m, EBITDA 8-12%",
              "2-4 stores in data-proven nodes; store payback <24 months",
              "Private label >50% of revenue",
              "Township/pick-up point network live (Pudo/Pargo + own points)",
              "Category search: you rank top 3 for your niche terms nationally"]),
            ("Years 6-10", "Chain or house of brands",
             ["Revenue R80m-R250m",
              "8-20 stores or dominant online share of the category",
              "Own distribution (mini-DC) once volume justifies",
              "Second brand launched into adjacent category using same infrastructure",
              "B2B/wholesale line supplying independents and salons/vets/gyms (per niche)"]),
            ("Years 10-20", "Platform economics",
             ["African expansion via marketplace exports (AfCFTA e-commerce protocols) "
              "before physical stores",
              "Recommerce/circular line (trade-in, refurb) as cost-of-living reshapes demand",
              "Exit: strategic sale to a retail group buying your category authority + "
              "private-label margins, or PE (retail brands trade 4-8x EBITDA)"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["CAC payback <2 orders", "Repeat rate >20%", "Gross margin >30%",
              "Dispatch same-day >95%"]),
            ("Growth (years 3-5)",
             ["Repeat rate >30%", "Private label share >40%", "Stock turns >6x",
              "Owned-channel revenue >25%", "Return rate <8%"]),
            ("Scale (years 6-10+)",
             ["EBITDA >10%", "Revenue per store vs rent ratio >10x", "NPS >50",
              "Basket growth beating inflation", "New-brand revenue >15%"]),
        ],
        "outbound": [
            "B2B outreach to the trade around your niche (vets for pet, salons for hair, "
            "schools for stationery) - wholesale anchors cash flow",
            "WhatsApp broadcast lists (opt-in) with weekly drops - SA's highest-converting "
            "retail channel, treat it like gold",
            "Influencer seeding: 20 micro-influencers (5k-50k followers) in your niche "
            "beats one celebrity; pay in product + commission codes",
            "Corporate gifting and stokvel/group-buying offers around pay cycles and "
            "Dec/Jan and Easter peaks",
        ],
        "inbound": [
            "Rank for niche buying-intent terms ('best [product] South Africa') with "
            "genuine comparison content - low competition, high conversion",
            "Marketplace optimisation: reviews, Q&A, listing quality on Takealot/Amazon SA - "
            "the search bar inside marketplaces is your biggest free channel",
            "TikTok/Instagram Reels product demos - social commerce discovery drives SA "
            "niche retail now",
            "Google Shopping ads on exact SKUs (high intent, measurable ROAS - keep "
            "ROAS >4 or kill the ad)",
        ],
        "retention": [
            "Replenishment reminders timed to product life (consumables are retention "
            "gold - engineer subscriptions with a discount)",
            "Loyalty in rand, not points ('R50 off your 5th order' beats schemes nobody "
            "understands)",
            "Post-purchase WhatsApp care (usage tips, warranty registration) that makes "
            "the second purchase feel obvious",
            "Community: WhatsApp/Facebook groups around the passion (pet owners, runners) "
            "- communities don't price-compare",
        ],
        "longgame": [
            "E-commerce penetration doubles again this decade off SA's low base - "
            "infrastructure (lockers, payments) is finally in place",
            "Chains consolidate the middle; survivors are niche authorities and township-"
            "embedded operators - be one of those two",
            "Private label + owned audience = the only durable retail margins",
            "Watch Temu/Shein economics: never compete on generic imported goods; "
            "curation, service, trust and local relevance are the moat",
        ],
    },

    "agriculture": {
        "positioning": "Enter through intensive high-value production or agri-services "
                       "with secured offtake, then move up the chain into packing and "
                       "processing where the margins and the defensibility live.",
        "entry": [
            ("Choose intensive over extensive",
             "You can't out-scale established commercial farmers on maize. Enter where "
             "management intensity beats hectares: tunnel vegetables, herbs, berries, "
             "mushrooms, poultry, or agri-services (spraying, scouting, pack labour)."),
            ("Secure offtake before planting anything",
             "Signed programmes with packhouses, fresh produce agents, retailers' local "
             "supplier programmes (Shoprite/PnP local sourcing), or export agents. No "
             "offtake, no planting - this rule alone beats most failure modes."),
            ("Control water before land",
             "Verify water rights/borehole yield/municipal reliability first. Lease land "
             "(R2k-R8k/ha/yr dryland, more irrigated) rather than buying - capital "
             "belongs in production infrastructure, not soil."),
            ("Start at half the scale your budget allows",
             "First two seasons are tuition: pests, timing, market grading. Surviving "
             "season one matters more than maximising it. Keep 18 months of costs banked."),
            ("Get certified for the buyers who pay",
             "GlobalG.A.P. for export, HACCP for processing, SA-GAP for retail programmes. "
             "Certification is the gate between R8/kg local and R25/kg export."),
            ("Move up the chain deliberately",
             "Year 3-5: packhouse share or processing line (drying, freezing, juicing, "
             "value-added). Primary production margins are 8-15%; processing adds 20-35% "
             "and smooths seasonality."),
        ],
        "roadmap": [
            ("Year 1", "First production cycles survived",
             ["0.5-2ha intensive (or services book), revenue R400k-R1.2m",
              "Offtake agreements covering >70% of planned volume",
              "Class 1/A-grade pass rate >70% (learning curve)",
              "Water security verified and backup plan tested",
              "Cost per kg tracked per crop cycle - know your break-even cold"]),
            ("Years 2-3", "Consistent quality, growing programmes",
             ["3-8ha or equivalent, revenue R2m-R6m",
              "Class 1 rate >80%; rejection rate <8%",
              "2+ buyers so no single offtake >60%",
              "GlobalG.A.P./SA-GAP certification achieved",
              "Gross margin >35% on core crops; debt service cover >1.5x"]),
            ("Years 4-5", "Packhouse economics",
             ["Revenue R8m-R25m; export or retail programme volume >30%",
              "Packhouse share/own line: earning packing margin on your + neighbours' fruit",
              "Yield within 10% of top-quartile benchmarks for your crops",
              "Crop insurance + forward cover on inputs (fuel, fertiliser) standard",
              "Second production site or crop for seasonal spread"]),
            ("Years 6-10", "Agri-business, not farm",
             ["Revenue R30m-R100m across production + packing + services",
              "Processing line converting B-grade into value-added products (30%+ margin)",
              "Own brand into retail or export programmes under your label",
              "Outgrower network: your packhouse + inputs + agronomy supporting 5-20 "
              "smaller farmers (volume without capex)",
              "AfCFTA/Middle East export lanes opened (halaal certification where relevant)"]),
            ("Years 10-20", "Vertically integrated food company",
             ["Brand + processing + farming + outgrower supply = food company economics "
              "(these trade at 6-10x EBITDA vs farmland yields)",
              "Water and climate resilience infrastructure (storage, drip, shade net) as "
              "the compounding moat",
              "Land acquisition now makes sense - buy the soil your business proved",
              "Exit/partnership: agri-corporates and PE funds buy integrated operations "
              "with export books"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Class 1 pass rate >70%", "Offtake coverage >70% of volume",
              "Cost per kg vs market price margin >25%", "Cash runway >12 months"]),
            ("Growth (years 3-5)",
             ["Yield per ha within 10% of benchmark", "Class 1 >80%",
              "Water cost per ton falling", "Gross margin >35%",
              "Debt service cover >1.5x through worst season"]),
            ("Scale (years 6-10+)",
             ["Processing/packing margin >20% of revenue", "Export share >30%",
              "Outgrower volume >25% of throughput", "EBITDA >15%",
              "Climate loss events <5% of revenue (insurance + infrastructure)"]),
        ],
        "outbound": [
            "Packhouses, export agents and fresh produce market agents before each "
            "season - bring samples, certifications and volume commitments",
            "Retail local-sourcing programmes (Shoprite, PnP, SPAR DCs actively recruit "
            "local growers - smaller volumes accepted than people assume)",
            "Restaurants/hotel groups for premium direct programmes (herbs, specialty "
            "veg at 2x wholesale)",
            "Neighbouring commercial farmers for services revenue (your equipment/labour "
            "in their off-peak = cash flow smoothing)",
        ],
        "inbound": [
            "Be findable when buyers search: Google Business, Farmer's Weekly/agri "
            "publications, provincial agri associations (buyers scout there)",
            "Show the operation: farm open days and social media of your practices - "
            "buyers audit informally before they call",
            "List on fresh-produce trading platforms (Nile.ag, agri marketplaces) for "
            "spot-volume discovery",
            "Word of mouth via agronomists, input suppliers and packhouse managers - "
            "keep them close, they broker everything informally",
        ],
        "retention": [
            "Never short a programme: if you promised 10 tons, deliver 10 - buyers "
            "forgive price negotiation, never unreliability",
            "Consistent grading and cold-chain discipline (one bad pallet costs a "
            "season's trust)",
            "Season-ahead planning meetings with each buyer (their promotions calendar "
            "= your planting calendar)",
            "Transparent problem communication: call the buyer before they discover "
            "the hail damage",
        ],
        "longgame": [
            "Food demand + weak rand + AfCFTA = 20-year export tailwind; SA's counter-"
            "seasonal window to the northern hemisphere is permanent",
            "Water is the binding constraint - every rand into water efficiency and "
            "storage compounds for decades",
            "Climate volatility rewards protected cropping (tunnels, nets) and "
            "diversified geography - build both",
            "The wealth is in the chain, not the field: packing, processing, brand, "
            "logistics - integrate relentlessly",
        ],
    },

    "realestate": {
        "positioning": "Enter through property services (income now, market knowledge "
                       "free), build a rental portfolio through the cycle, then develop "
                       "where the data says demand outruns supply.",
        "entry": [
            ("Qualify and pick a patch",
             "PPRA Fidelity Fund Certificate (candidate then full status), join an agency "
             "or open under a principal. Choose ONE suburb cluster or niche (student "
             "housing, sectional title rentals) and know it street by street."),
            ("Start with rentals, not sales",
             "Rental management pays monthly (8-12% of rent + placement fees) and builds "
             "the two assets that matter: landlord relationships and occupancy data. Sales "
             "commissions are lumpy; rentals compound."),
            ("Systematise management early",
             "PayProp/WeconnectU-type systems, credit vetting (TPN), inspection routines, "
             "arrears playbooks. 100 well-run units = R1.5m-R3m annuity revenue with tiny "
             "capital."),
            ("Buy your first units where you manage",
             "You see every deal first and know real yields. Target 9%+ net yield "
             "(affordable units, student rooms) with 60-70% bonds. Two units/year, "
             "never negative carry."),
            ("Add sectional-title/HOA management",
             "Body corporate management (R30-R60/unit/month at scale) is sticky annuity "
             "income and feeds sales/rental mandates from inside the schemes."),
            ("Develop only with pre-sales or pre-lets",
             "First development: small (6-20 units), in your proven patch, with 60%+ "
             "pre-sales or a rental underwrite before breaking ground. Development is "
             "where fortunes are made and lost - enter it from knowledge, not hope."),
        ],
        "roadmap": [
            ("Year 1", "Licensed, first mandates",
             ["30-60 rental mandates under management, fee revenue R300k-R800k",
              "Vacancy on managed book <6%; arrears <5%",
              "Own deals analysed weekly (build the buy-list even before buying)",
              "TPN/credit vetting on 100% of placements"]),
            ("Years 2-3", "Management book + first own units",
             ["120-250 units managed, revenue R1.5m-R3.5m",
              "2-5 own rental units at >9% net yield, collections >97%",
              "1-2 body corporates under management",
              "Landlord churn <10%/yr (the book is the business)"]),
            ("Years 4-5", "Portfolio + first development",
             ["400+ managed units, revenue R5m-R10m; own portfolio 8-15 units",
              "First micro-development: 6-20 units, GP margin >20%, 60%+ pre-sold",
              "Own portfolio LTV <65%; interest cover >1.5x at stressed rates",
              "Student/affordable niche position established (demand outruns supply 10:1)"]),
            ("Years 6-10", "Developer-operator",
             ["Development pipeline 50-200 units/yr in proven nodes",
              "Own rental portfolio 30-80 units (R50m-R150m assets) self-managing "
              "through your own company",
              "Revenue R20m-R60m across fees + development profits + net rentals",
              "Institutional partnerships: equity partners/debt funds for bigger projects"]),
            ("Years 10-20", "Property company",
             ["Yield portfolio R200m-R1bn (opco/propco structure)",
              "Affordable rental at scale - SA's structural shortage is your annuity",
              "Possible REIT-feeder sale of stabilised assets, recycling capital into "
              "development",
              "The management book (now thousands of units) remains the deal-flow and "
              "data engine underneath everything"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Managed-book vacancy <6%", "Arrears <5%", "Mandate growth >5/month",
              "Landlord churn <10%"]),
            ("Growth (years 3-5)",
             ["Own portfolio net yield >9%", "Collections >97%",
              "Development GP margin >20%", "Pre-sales before ground-break >60%",
              "Fee revenue covering all overheads (own portfolio is pure compounding)"]),
            ("Scale (years 6-10+)",
             ["Portfolio LTV <60%", "Interest cover >2x", "Units developed/yr growing",
              "Cost per unit vs market <90%", "Tenant retention >70%/yr"]),
        ],
        "outbound": [
            "Direct outreach to landlords of visibly under-managed buildings (vacancy, "
            "arrears pain) with a rent-roll rescue pitch",
            "Body corporate trustees before AGM season with a management proposal + "
            "arrears-recovery track record",
            "Developers and investors for bulk rental mandates on new schemes (manage "
            "the whole building from day one)",
            "Estate late-payment/distressed lists, auctions and deceased estates for "
            "acquisition deal flow (attorney relationships are the source)",
        ],
        "inbound": [
            "Own the suburb online: Google Business, suburb market reports ('what sold/"
            "rented in [suburb] this quarter'), local Facebook groups",
            "TPN/PayProp data-driven content for landlords (achieved rents, vacancy "
            "trends) - data authority converts landlords, not lifestyle content",
            "Property portals (Property24/Private Property) optimised listings - "
            "photography and response speed win the mandate war",
            "Student housing: relationships with university accommodation offices + "
            "NSFAS accreditation gets you listed on official channels",
        ],
        "retention": [
            "Landlords: monthly statements that read like fund reports (yield, arrears, "
            "maintenance ROI) - treat every landlord like an investor client",
            "Tenants: fast maintenance response (the #1 churn driver), renewal offers "
            "60 days out, upgrade paths within your portfolio",
            "Bodies corporate: transparent finances + visible compliance (CSOS, audits) "
            "- trustees renew what they don't have to defend",
            "Own tenants: keep rent increases at/below CPI for good payers - vacancy "
            "costs more than generosity",
        ],
        "longgame": [
            "SA's housing shortfall (2m+ units) and rental demand are structural - "
            "affordable rental is a 20-year compounding trade",
            "Semigration and infrastructure decide geography: follow the Western Cape/"
            "KZN coast data, avoid decaying municipal nodes ruthlessly",
            "Rate cycles are your friend with patience: buy in high-rate distress, "
            "refinance in cuts",
            "End-state: the propco compounds wealth, the opco (management + development) "
            "compounds capability - build both, never confuse them",
        ],
    },

    "healthcare": {
        "positioning": "Enter through cash-based primary care or B2B health services "
                       "(where regulation permits non-clinician ownership), scale into "
                       "multi-site delivery, then facilities where licensing is the moat.",
        "entry": [
            ("Map the ownership rules to your situation",
             "Clinicians can own practices; non-clinicians build in the permitted lanes: "
             "day hospitals, sub-acute/frail care facilities, home care agencies, occupational "
             "health companies, health-tech and admin services. Choose your lane accordingly."),
            ("Start cash-based, low-cost, high-volume",
             "The Unjani/low-cost clinic model proves it: nurse-led primary care at R250-R450 "
             "consultations serves the uninsured majority profitably. Cash removes the "
             "medical-scheme payment nightmare that sinks new practices."),
            ("Location = footfall + trust",
             "Taxi ranks, township main roads, retail centres near commuter flows. Partner "
             "with community leaders and existing pharmacies. Visibility and word-of-mouth "
             "beat any healthcare marketing."),
            ("Get licensing and billing right from day one",
             "Practice numbers (BHF), DoH facility licence where required, HPCSA/SANC "
             "compliance, and if billing schemes: coding discipline (rejection rate is a "
             "practice killer). A part-time practice manager pays for themselves."),
            ("Add B2B revenue early",
             "Occupational health contracts (mines, factories, farms need medicals by law), "
             "corporate wellness days, school screening programmes. B2B contracts smooth the "
             "cash-based consumer volume."),
            ("Scale sites on a repeatable model",
             "Document everything (clinical protocols, stock, staffing ratios) at site one. "
             "Sites 2-5 succeed on systems, not heroics. Day-clinic/facility licences come "
             "when your patient volumes prove the demand to funders."),
        ],
        "roadmap": [
            ("Year 1", "One site, proven unit economics",
             ["15-30 patients/day by month 12, revenue R1m-R2.5m",
              "Cash/hybrid mix >50% (scheme dependence <50%)",
              "Claim rejection rate <5% on scheme billing",
              "Break-even by month 8-10",
              "1-2 occupational health/B2B contracts signed"]),
            ("Years 2-3", "2-4 sites + B2B book",
             ["Revenue R4m-R10m; each new site break-even <10 months",
              "Patient volume per practitioner-day >22",
              "B2B/contract revenue >25% (occupational health, wellness)",
              "Clinical protocols + stock systems documented (the scaling asset)",
              "Staff: nurse-led model with sessional doctors - clinician cost <45% of revenue"]),
            ("Years 4-5", "Multi-site group + first facility",
             ["Revenue R15m-R35m, EBITDA 15-20%",
              "6-12 sites or 2-3 sites + day clinic licence application/build",
              "Chronic programme patients >1,000 (repeat revenue backbone)",
              "Telehealth + medicine delivery extending rural reach",
              "Scheme network contracts (low-cost benefit options actively recruit "
              "cash-model networks)"]),
            ("Years 6-10", "Healthcare platform",
             ["Revenue R50m-R150m; 15-40 sites or facility group (day hospitals, "
              "sub-acute, frail care)",
              "Frail/dementia care beds - the ageing insured cohort is the decade's "
              "certain demand",
              "Funder contracts (capitation/DRG deals) - you're now infrastructure "
              "schemes need",
              "Training pipeline: enrolled nursing partnerships feeding your own staffing"]),
            ("Years 10-20", "Institutional health asset",
             ["NHI-era positioning: accredited primary-care networks will be contracted "
              "whoever funds them - scale + accreditation + cost discipline wins either way",
              "Facility portfolio (day hospitals, care facilities) = licensed, scarce, "
              "yield-bearing assets",
              "Exit: hospital groups, funders and PE actively acquire primary-care "
              "networks and care facilities (8-12x EBITDA for scaled platforms)"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Patients/practitioner-day >20", "Claim rejection <5%",
              "Cash mix >50%", "Cost per consultation <60% of fee"]),
            ("Growth (years 3-5)",
             ["Site break-even <10 months", "Chronic/repeat patient share >30%",
              "B2B revenue >25%", "Clinician cost <45% of revenue",
              "Patient satisfaction >90% (measure it - funders ask)"]),
            ("Scale (years 6-10+)",
             ["EBITDA >15%", "Bed/chair occupancy >70% (facilities)",
              "Funder-contracted revenue >30%", "Clinical incident rate at benchmark",
              "Staff retention >80% (scarcity makes this existential)"]),
        ],
        "outbound": [
            "Occupational health: direct proposals to mines, factories, farms, logistics "
            "depots (legally mandated medicals = guaranteed demand; bundle with wellness)",
            "Employer groups and unions for worksite clinic contracts and staff "
            "healthcare packages",
            "Medical scheme network teams: pitch inclusion in low-cost options and "
            "primary-care networks (they need footprint in underserved areas)",
            "Schools and creches for screening programmes (vision, hearing, immunisation "
            "catch-up) - low margin, high trust-building",
        ],
        "inbound": [
            "Google Business + WhatsApp booking: 'clinic near me open now' is the "
            "highest-intent search in healthcare - own it with hours, prices, reviews",
            "Transparent pricing published (R350 consultation) - price certainty is "
            "the uninsured patient's #1 anxiety",
            "Community presence: taxi rank visibility, community radio health slots, "
            "church and stokvel health talks",
            "Patient reviews and word-of-mouth engineering (SMS review ask post-visit; "
            "township healthcare travels by word of mouth faster than any channel)",
        ],
        "retention": [
            "Chronic care programmes (HIV, hypertension, diabetes) with medicine "
            "collection/delivery - monthly touchpoints = permanent patients",
            "Family files and continuity (same nurse relationship) - healthcare loyalty "
            "is personal, engineer the continuity",
            "SMS/WhatsApp follow-ups, results delivery and recall reminders",
            "B2B clients: quarterly utilisation and absenteeism-impact reports proving "
            "ROI to the HR director who signed you",
        ],
        "longgame": [
            "Demographics are destiny: an ageing insured cohort (frail care demand) + "
            "a young uninsured majority (low-cost primary care demand) - both certain",
            "Clinician scarcity worsens for 20 years - models that leverage nurses, "
            "protocols and telehealth hold the cost advantage permanently",
            "NHI in any form needs contracted primary-care networks - scaled, "
            "accredited, cost-disciplined operators win under every scenario",
            "Facilities licensing scarcity = the moat deepens over time; licensed beds "
            "compound in value",
        ],
    },

    "manufacturing": {
        "positioning": "Enter as a niche job-shop or contract manufacturer where freight "
                       "and lead times beat imports, secure energy independence early, "
                       "then own products and export certification.",
        "entry": [
            ("Pick a niche imports serve badly",
             "Heavy/bulky relative to value (packaging, tanks, trailers), custom/short-run "
             "(CNC parts, shopfitting, technical textiles), fast-turnaround (signage, food "
             "co-packing), or regulated-local (defence/rail designations). Never compete "
             "with containers of generic goods."),
            ("Start in rented space with used equipment",
             "Industrial parks rent at R35-R70/m²; second-hand machinery is 40-60% off new. "
             "Capital belongs in working capital (materials, payroll through 60-day payment "
             "terms), not shiny machines."),
            ("Lock in an anchor customer's overflow",
             "Contract manufacturing/co-packing for a brand or OEM that's capacity-"
             "constrained. Their overflow is your base load; their standards force your "
             "quality systems to grow up fast."),
            ("Solve energy before it solves you",
             "Solar + storage sized to your shifts (budget 8-15% of setup capex). An "
             "interrupted production run destroys margins and delivery promises - energy "
             "independence is a competitive weapon in SA."),
            ("Get the certifications that gate demand",
             "ISO 9001 baseline, HACCP/FSSC for food, SABS/NRCS marks where regulated, "
             "B-BBEE level for corporate/public procurement, local-content designation "
             "registration. Each certificate unlocks a demand pool competitors can't enter."),
            ("Own a product by year 3",
             "Take the thing you make best under contract and launch your own SKU/brand "
             "into wholesale + online. Contract work funds the factory; own products own "
             "the margin."),
        ],
        "roadmap": [
            ("Year 1", "Job-shop earning its keep",
             ["Revenue R1.5m-R4m, gross margin >30%",
              "Capacity utilisation >50% by month 12",
              "1 anchor contract + 10-20 repeat SME customers",
              "Quote turnaround <48 hours (speed is the small-shop weapon)",
              "Zero energy-related missed deliveries"]),
            ("Years 2-3", "Contract manufacturer with systems",
             ["Revenue R6m-R18m; utilisation >70%",
              "ISO/HACCP certification complete; reject rate <2%",
              "On-time-in-full >95%",
              "Top customer <35% of revenue",
              "Own-product line launched (>10% of revenue by year 3)"]),
            ("Years 4-5", "Certified, energy-independent, exporting",
             ["Revenue R25m-R60m, EBITDA 12-16%",
              "Own products >25% of revenue at >45% margin",
              "First export orders (SADC first - logistics you can drive to)",
              "Energy self-sufficiency >60% of consumption",
              "Automation of the bottleneck process (not everything - the bottleneck)"]),
            ("Years 6-10", "Scale plant + regional exports",
             ["Revenue R80m-R250m",
              "Export >20% of revenue (AfCFTA lanes, rand hedge)",
              "Public procurement designations won where applicable (rail, defence, "
              "renewables components)",
              "Second facility or 24/7 shifts; revenue per employee >R1.5m",
              "Acquire a struggling competitor for capacity + book (plenty available)"]),
            ("Years 10-20", "Industrial group",
             ["Multi-plant, multi-product industrial company R300m-R1bn",
              "Renewables/battery/EV component manufacturing as the energy transition "
              "localises supply chains",
              "Own brands distributed continentally; contract base load underneath",
              "Exit: industrial consolidators and PE buy certified, energy-independent "
              "plants with export books (5-7x EBITDA)"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Utilisation >50%", "GM >30%", "Quote turnaround <48h",
              "DSO <45 days (payment terms discipline from day one)"]),
            ("Growth (years 3-5)",
             ["Utilisation >75%", "OTIF >95%", "Reject rate <2%",
              "Energy cost <8% of revenue", "Own-product share >25%"]),
            ("Scale (years 6-10+)",
             ["EBITDA >14%", "Revenue per employee >R1.5m", "Export >20%",
              "Inventory turns >8x", "Safety LTIFR at benchmark"]),
        ],
        "outbound": [
            "Direct to procurement at brands/OEMs with a capacity + certification + "
            "lead-time pitch (their import lead times are your opening)",
            "Retail buyers' local-supplier programmes and private-label tenders "
            "(retailers actively de-risk from import supply chains)",
            "Tender portals for designated local-content categories - but private "
            "sector first until you can carry government payment terms",
            "Industry cluster bodies and export councils (they broker buyer "
            "introductions and grant funding: dtic EMIA export incentives)",
        ],
        "inbound": [
            "Rank for '[product] manufacturer South Africa' - genuine buyers search "
            "exactly this and competition is weak",
            "Factory content: capability videos, machine lists, certifications on a "
            "real website (most SA factories are invisible online - being visible wins)",
            "B2B marketplaces and directories (Made-in-SA type platforms, industry "
            "association member lists)",
            "Trade show presence in your niche (Propak, Electra Mining, NAMPO depending "
            "on sector) - one show, worked properly, fills a year's pipeline",
        ],
        "retention": [
            "OTIF religion: track it, report it to customers before they measure it - "
            "supply reliability is why they left imports",
            "Vendor-managed inventory / call-off stock agreements that embed you in "
            "their planning",
            "Annual cost-down reviews sharing efficiency gains (procurement teams "
            "renew suppliers who help their KPIs)",
            "Co-development: prototype fast for their new products - the supplier "
            "in at design stage never gets tendered out",
        ],
        "longgame": [
            "Global supply-chain regionalisation + AfCFTA + a weak rand = a 20-year "
            "window for African-based manufacturing",
            "Energy transition localises demand: solar mounting, electrical BOS, "
            "battery packs, e-mobility parts - position in the component chain",
            "Automation + energy independence neutralise SA's productivity gaps; "
            "adopt both faster than incumbents",
            "The compounding assets: certifications, export relationships and "
            "designated-supplier status - all take years and gate competitors out",
        ],
    },

    "construction": {
        "positioning": "Enter as a specialised subcontractor with brutal cash discipline, "
                       "climb CIDB grades on private + energy work, and only then touch "
                       "development and public infrastructure at scale.",
        "entry": [
            ("Start specialised, not general",
             "Electrical, plumbing, HVAC, fire systems, waterproofing, solar structural, "
             "or shopfitting. Specialised trades price on skill; general building prices "
             "on desperation. Get trade-qualified staff and CIDB Grade 1-2 registration."),
            ("Serve private clients first",
             "Commercial fit-outs, franchise rollouts, body corporates, renewable EPCs, "
             "private developers. Government work at low grades = payment-delay roulette "
             "your balance sheet can't survive yet."),
            ("Run cash flow like a religion",
             "Deposit before mobilisation (30-50% on private work), weekly invoicing on "
             "measured progress, stop-work triggers at 30 days unpaid, DSO reported "
             "weekly. Most SA contractor deaths are cash deaths with profitable order books."),
            ("Price with a margin floor and walk away",
             "Cost every tender fully (prelims, retention finance, escalation), add "
             "minimum 12% margin at small scale, and decline work below it. Winning "
             "underpriced tenders is how you buy your own liquidation."),
            ("Climb CIDB grades deliberately",
             "Each grade unlocks bigger tenders; grades need track record + financial "
             "capability. Joint ventures with higher-grade contractors accelerate the "
             "climb while sharing risk."),
            ("Niche into the funded pipelines",
             "Renewable energy civils/structural, water infrastructure maintenance, "
             "affordable housing, logistics warehousing - the pockets where budgets are "
             "real and clients pay. Follow funded demand, not tender volume."),
        ],
        "roadmap": [
            ("Year 1", "Specialised crew, private work",
             ["Revenue R1.5m-R4m, net margin >10%",
              "DSO <45 days; zero jobs started without deposit",
              "CIDB Grade 2; SAFCEC/MBA membership for credibility",
              "10+ completed references with photos and sign-offs",
              "Tender/quote win rate >1 in 6 at full margin"]),
            ("Years 2-3", "Grade 4-5 contractor",
             ["Revenue R8m-R20m; margin variance <3% vs tender",
              "Retention + guarantee exposure <50% of free cash",
              "1-2 anchor client relationships (franchise rollouts, EPC frame "
              "agreements) giving repeat work",
              "Site management systems (daily diaries, QA sign-offs, H&S files) "
              "audit-ready",
              "First energy-sector contracts (solar civils/structures)"]),
            ("Years 4-5", "Niche mid-tier",
             ["Revenue R30m-R70m, EBITDA 8-12%",
              "CIDB Grade 6-7; JV track record on larger projects",
              "Specialised niche = >50% of book (energy, water, warehousing)",
              "Owned plant only where utilisation >70%, else hire",
              "Public work <30% of book and only with escalation + payment protections"]),
            ("Years 6-10", "Grade 7-8 + development",
             ["Revenue R100m-R300m",
              "First own developments (JV equity in affordable housing/industrial "
              "units where you build at cost)",
              "Framework agreements with IPPs, water boards, retail property funds",
              "Professional team: QSes, engineers, contracts managers - claims "
              "capability protects margin at this scale",
              "Bonding/guarantee facilities R50m+ (the real constraint on growth)"]),
            ("Years 10-20", "Infrastructure group",
             ["Construction + development + O&M concessions (roads, water, energy "
              "assets need 20-year operators)",
              "Public-private partnership positions as state capacity outsources",
              "Annuity income (facilities management, O&M) >25% smoothing the cycle",
              "Exit/succession: mid-tier contractors with niche books and clean "
              "balance sheets are scarce and acquirable"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["DSO <45 days", "Net margin >10%", "Win rate >1 in 6 at margin floor",
              "Rework <3% of contract value"]),
            ("Growth (years 3-5)",
             ["Margin variance <3% vs tender", "Retention exposure <50% of free cash",
              "Repeat-client revenue >50%", "Claims recovered vs submitted >70%",
              "H&S: zero fatal incidents, LTIFR at benchmark"]),
            ("Scale (years 6-10+)",
             ["EBITDA >10%", "Order book >12 months forward cover",
              "Guarantee facility headroom >30%", "Public-sector exposure <30%",
              "Development ROE >25% on JV equity"]),
        ],
        "outbound": [
            "Framework-agreement pitches to repeat builders: franchise brands, retail "
            "property funds, solar EPCs, warehouse developers - rollout clients beat "
            "tender lotteries",
            "Professional team relationships (architects, QSes, engineers) who "
            "recommend contractors to their clients - breakfast circuit, site "
            "performance, prompt paperwork",
            "Selective tendering with a bid/no-bid scorecard (client payment "
            "reputation, site risk, margin) - capacity spent on bad tenders is "
            "capacity stolen from good ones",
            "Body corporates and property managers for maintenance/refurb annuity "
            "work between projects",
        ],
        "inbound": [
            "Reference marketing: photographed, signed-off case studies per niche - "
            "construction buyers verify, they don't browse",
            "Google Business + '[trade] contractor [city]' SEO for private work flow",
            "CIDB registers and industry body directories where corporate procurement "
            "pre-screens",
            "Site boards, branded fleet and finished-project signage - still the "
            "highest-converting local advertising in this trade",
        ],
        "retention": [
            "Finish snag-free and on date - the contractor who hands over clean gets "
            "the next phase without tender",
            "Post-completion service (12-month defect response within 48h) that "
            "makes you the default for the client's next project",
            "Transparent variation/claims communication early - surprises at final "
            "account end relationships",
            "Maintenance contracts on what you built (you know the building; annuity "
            "revenue smooths the pipeline)",
        ],
        "longgame": [
            "SA's infrastructure backlog is generational (energy, water, housing, "
            "logistics) - the funded parts of it will build for 20 years",
            "State delivery capacity keeps outsourcing: PPPs, concessions and O&M "
            "contracts are where construction margins become infrastructure returns",
            "Alternative building tech (LSF, precast, modular) wins as skills "
            "scarcity and speed pressure grow - adopt early",
            "Survive the cycle, compound the reputation: in construction, longevity "
            "itself is the moat - most competitors won't still be there",
        ],
    },

    "mining": {
        "positioning": "Enter through mining services (no mining right needed), build "
                       "multi-commodity client spread, then take positions in tailings "
                       "retreatment and critical-minerals niches where juniors can win.",
        "entry": [
            ("Services first - always",
             "Drilling support, safety training and file management, rehabilitation, "
             "surveying/drone services, PPE and consumables supply, plant maintenance. "
             "Services revenue starts in months; mining rights take years."),
            ("Get compliant for site access",
             "CIPC + tax clearance + B-BBEE (procurement scoring is decisive in mining), "
             "COIDA letter of good standing, medicals and inductions for staff, and the "
             "MHSA safety file that gets you through the gate."),
            ("Land vendor numbers at 2-3 operations",
             "Mine procurement portals and supplier days; start with small POs delivered "
             "perfectly. A vendor number at a major is an asset worth more than "
             "equipment - protect it with flawless compliance."),
            ("Diversify commodity exposure deliberately",
             "Spread clients across coal, PGMs, chrome, manganese, iron ore - commodity "
             "cycles hit one at a time, and single-commodity service books die in "
             "downturns."),
            ("Move toward the resource with tailings",
             "Tailings retreatment (chrome from platinum dumps, gold from old slimes) "
             "needs processing skill + offtake, not deep-level mining capital. Permits "
             "are faster (the material is already mined) and ESG tailwinds help."),
            ("Only then consider a mining permit",
             "Small-scale mining permits (under 5ha) for chrome/aggregates/industrial "
             "minerals with a signed offtake. Full mining rights are a 3-5 year, "
             "R10m+ regulatory journey - enter it with cash flow, not hope."),
        ],
        "roadmap": [
            ("Year 1", "Services foothold",
             ["Revenue R2m-R5m from 2-3 mine clients",
              "Vendor numbers at 3+ operations",
              "Zero safety incidents / Section 54 triggers from your work",
              "B-BBEE level 1-2 structured (it decides tender scoring)",
              "One niche where you're demonstrably better (turnaround, tech, price)"]),
            ("Years 2-3", "Multi-commodity service book",
             ["Revenue R8m-R20m; 6-10 clients across 3+ commodities",
              "Contract book >12 months forward revenue",
              "No client >35% of revenue",
              "Term contracts (1-3yr) >50% of book vs spot POs",
              "Adjacent service lines added (one crew, multiple billable skills)"]),
            ("Years 4-5", "Tailings/processing position",
             ["Revenue R30m-R80m",
              "First tailings retreatment JV or toll-processing arrangement "
              "(your plant, their dump, shared revenue)",
              "Offtake agreement signed before plant commissioning",
              "Processing margin >25%; recovery rates hitting design specs",
              "Rehabilitation services line (guaranteed growth - closures accelerate)"]),
            ("Years 6-10", "Junior operator",
             ["Revenue R100m-R400m across services + processing + small-scale mining",
              "Mining permit operations cash-flowing with contracted offtake "
              "(chrome/manganese/aggregates)",
              "Critical-minerals exposure (manganese, vanadium, REE prospects) - "
              "the demand decade belongs to battery/energy metals",
              "Own beneficiation step (crushing, washing, concentrating) capturing "
              "margin before export"]),
            ("Years 10-20", "Mid-tier resources company",
             ["Full mining right on a proven deposit, funded by the services/processing "
              "cash engine",
              "Beneficiation ahead of raw-ore export restrictions (policy is moving "
              "this way across Africa)",
              "Renewable-powered operations (cost + ESG + offtake advantage)",
              "Exit paths: JSE/ASX listing, trade sale to mid-tiers hungry for "
              "developed assets, or hold as a cash-generative private producer"]),
        ],
        "kpi_stages": [
            ("Startup (years 1-2)",
             ["Safety incidents: zero", "Contract book >6 months",
              "Client concentration <40%", "PO-to-payment cycle <45 days"]),
            ("Growth (years 3-5)",
             ["Forward contract cover >12 months", "Commodity spread: 3+",
              "Processing recovery vs design >95%", "EBITDA >15%",
              "B-BBEE procurement scoring maintained at level 1-2"]),
            ("Scale (years 6-10+)",
             ["AISC below 80% of spot on owned production", "Offtake cover >80% "
              "of planned volumes", "Rehab liability fully funded/guaranteed",
              "Renewable energy share of power >40%", "Reserve life >10 years"]),
        ],
        "outbound": [
            "Mine procurement offices and supplier development programmes (majors "
            "have ESD budgets that fund and mentor local suppliers - use them)",
            "Mining indabas and commodity conferences (Junior Indaba, Mining Indaba) "
            "- deals and JVs are relationship-brokered in this industry",
            "Direct proposals to mine managers for pain-point services (rehab "
            "backlogs, safety file audits, water treatment) with fixed-price pilots",
            "Offtake traders (chrome/manganese buyers, commodity trading houses) - "
            "they'll co-fund production against supply agreements",
        ],
        "inbound": [
            "Referrals via engineering consultancies and mine contractors already "
            "on site - be the subcontractor they trust",
            "Supplier databases and mining procurement platforms (vendor "
            "registration is inbound infrastructure)",
            "Technical case studies (recovery rates achieved, rehab hectares "
            "certified) in industry press - engineers buy on data",
            "ESG/local-content credentials visible: mines must procure local and "
            "empowered - make yourself the easy compliant choice",
        ],
        "retention": [
            "Safety record as the relationship foundation: one incident can end a "
            "vendor number; over-invest in it",
            "Contract performance reporting aligned to the mine's own KPIs "
            "(availability, turnaround, compliance) every month",
            "Embed on site: dedicated crews who know the operation beat cheaper "
            "rotating outsiders",
            "Term-contract renewals negotiated 6 months early with productivity "
            "improvements offered proactively",
        ],
        "longgame": [
            "The demand decade belongs to critical minerals (manganese, vanadium, "
            "chrome, REE) - position exposure there, not in deep-level gold/PGM decline",
            "Beneficiation policy pressure grows across Africa - owning a processing "
            "step future-proofs against raw-export restrictions",
            "Mine closures accelerate for 20 years: rehabilitation, closure "
            "management and tailings reprocessing are counter-cyclical growth markets",
            "The junior path is real but slow - let services and processing cash "
            "flow fund the resource positions, never the reverse",
        ],
    },
}
