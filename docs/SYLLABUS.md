# Roadmap and Syllabus

The complete content plan for Free Exercise Book: **115 topics** across General Studies for UPSC CSE Prelims (GS-I), WBCS, other State PSCs, SSC CGL/CHSL, Banking and Railways. Every topic has a fixed **ID, folder and queue number** before it is written.

**Progress: 11 / 115 topics written.** Status: ✅ written · 🔲 queued.

## How content is produced (one topic per day)

A scheduled daily routine takes the **lowest-numbered 🔲 topic** in the queue below and:

1. **Writes** the topic: `topic.yaml`, `notes.en.md`, `notes.bn.md` (6–9 sections, same anchors), `questions.yaml` (30 MCQs: ~12 single, 6 statements, 4 match, 4 assertion-reason, 4 chronology), following docs/CONTENT_STRUCTURE.md and docs/CONTENT_GUIDELINES.md.
2. **Fact-checks** it in a separate pass that did not write it: every answer key recomputed, exactly one defensible option, disputed facts removed or hedged, Bengali matching English.
3. **Validates** with `python3 -I tools/content-check/validate.py content`, adds the topic to its `unit.yaml`, marks it ✅ here.
4. **Opens a pull request** for human review. Nothing reaches `main` without review. Content stays `status: ai-generated` until a human reviewer signs it off.

Current affairs are separate: a monthly pack (`ca.<yyyy>.<mm>`) for the previous month, built from official sources only (see CONTENT_GUIDELINES §6).

## Roadmap

| Phase | Area | Topics | Approx. days |
|---|---|---|---|
| 1 | Modern History (finish) | 23 | 23 |
| 2 | Indian Polity | 19 | 19 |
| 3 | Geography | 13 | 13 |
| 4 | Economy | 14 | 14 |
| 5 | Environment and Science | 18 | 18 |
| 6 | Ancient & Medieval History, Art & Culture | 18 | 18 |
| 7 | West Bengal and Static GK | 10 | 10 |
| 8 | Aptitude: Reasoning, Quantitative, English | planned | needs a numeric/worked-solution question format first |

At one topic per day the General Studies syllabus takes about **104 more days**. Phase order follows exam weight: Polity, Geography and Economy are high-yield for every target exam, so they come right after Modern History.

## Daily queue


### Phase 1: Modern History (finish)


#### History › Modern India (`hist.modern`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 1 | `hist.modern.european-arrival` | `content/subjects/history/modern/european-arrival/` | Advent of the Europeans | Portuguese, Dutch, English, Danish, French companies; factories; Anglo-French rivalry and the Carnatic Wars | ✅ batch 1 |
| 2 | `hist.modern.british-expansion` | `content/subjects/history/modern/british-expansion/` | Expansion of British Power | Plassey, Buxar, Dual Government; Anglo-Mysore, Anglo-Maratha, Anglo-Sikh wars; Subsidiary Alliance; Doctrine of Lapse | ✅ batch 1 |
| 3 | `hist.modern.company-acts` | `content/subjects/history/modern/company-acts/` | Company Rule: Acts 1773–1853 | Regulating Act 1773, Pitt's India Act 1784, Charter Acts 1793/1813/1833/1853 | ✅ batch 1 |
| 4 | `hist.modern.economic-impact` | `content/subjects/history/modern/economic-impact/` | Economic Impact of British Rule | Permanent Settlement, Ryotwari, Mahalwari; drain of wealth; deindustrialisation; commercialisation of agriculture; famines | ✅ batch 1 |
| 5 | `hist.modern.social-reform` | `content/subjects/history/modern/social-reform/` | Socio-Religious Reform Movements | Bengal Renaissance, Brahmo Samaj, Young Bengal, Prarthana Samaj, Arya Samaj, Ramakrishna Mission, Aligarh, Satyashodhak, Sree Narayana; laws on sati, widow remarriage, age of consent | ✅ batch 1 |
| 6 | `hist.modern.peasant-tribal` | `content/subjects/history/modern/peasant-tribal/` | Peasant and Tribal Movements (pre-1857 to 1900) | Sanyasi-Fakir, Kol, Santhal (Hul), Munda (Ulgulan), Indigo Revolt, Pabna, Deccan riots, Wahabi and Faraizi movements | ✅ batch 2 |
| 7 | `hist.modern.revolt-1857` | `content/subjects/history/modern/revolt-of-1857/` | The Revolt of 1857 | Causes, spread, leaders, suppression, nature, consequences | ✅ |
| 8 | `hist.modern.education-press` | `content/subjects/history/modern/education-press/` | Education, Press and the Indian Middle Class | Charter Act 1813 grant, Macaulay's Minute 1835, Wood's Despatch 1854, Hunter Commission, universities 1857; Vernacular Press Act 1878 | ✅ batch 2 |
| 9 | `hist.modern.early-nationalism` | `content/subjects/history/modern/early-nationalism/` | Rise of Nationalism and the Moderates | Pre-Congress associations, INC 1885, Moderates' methods and demands, Indian Councils Act 1892 | ✅ batch 2 |
| 10 | `hist.modern.swadeshi` | `content/subjects/history/modern/swadeshi/` | Partition of Bengal and the Swadeshi Movement | Curzon, partition 1905, Swadeshi and Boycott, Extremists (Lal-Bal-Pal), Surat split 1907, Morley-Minto Reforms 1909, Muslim League 1906, annulment 1911 | ✅ batch 2 |
| 11 | `hist.modern.revolutionaries` | `content/subjects/history/modern/revolutionaries/` | Revolutionary Nationalism | Anushilan Samiti, Jugantar, Alipore case, Ghadar Party, Kakori, HSRA (Bhagat Singh), Chittagong Armoury Raid, revolutionaries abroad | ✅ batch 2 |
| 12 | `hist.modern.home-rule` | `content/subjects/history/modern/home-rule/` | First World War, Home Rule and Lucknow Pact | Home Rule Leagues (Tilak, Besant), Lucknow Pact 1916, Montagu Declaration 1917, Government of India Act 1919 | 🔲 |
| 13 | `hist.modern.gandhi-early` | `content/subjects/history/modern/gandhi-early/` | Arrival of Gandhi | South Africa, Champaran, Kheda, Ahmedabad mill strike, Rowlatt Satyagraha, Jallianwala Bagh, Hunter Committee | 🔲 |
| 14 | `hist.modern.non-cooperation` | `content/subjects/history/modern/non-cooperation/` | Khilafat and Non-Cooperation Movement | Khilafat issue, NCM programme, Nagpur session 1920, Chauri Chaura, Moplah rebellion | 🔲 |
| 15 | `hist.modern.twenties` | `content/subjects/history/modern/twenties/` | The 1920s: Swarajists to Purna Swaraj | Swaraj Party, Simon Commission, Nehru Report, Jinnah's 14 points, Lahore Session 1929 | 🔲 |
| 16 | `hist.modern.civil-disobedience` | `content/subjects/history/modern/civil-disobedience/` | Civil Disobedience and the Round Table Conferences | Dandi March, CDM, Gandhi-Irwin Pact, Round Table Conferences, Communal Award, Poona Pact | 🔲 |
| 17 | `hist.modern.act-1935` | `content/subjects/history/modern/act-1935/` | Government of India Act 1935 and Provincial Ministries | Act of 1935, 1937 elections, Congress ministries, resignation 1939 | 🔲 |
| 18 | `hist.modern.quit-india` | `content/subjects/history/modern/quit-india/` | Second World War, Quit India and the INA | August Offer, Individual Satyagraha, Cripps Mission, Quit India, Subhas Chandra Bose and the INA, INA trials | 🔲 |
| 19 | `hist.modern.independence` | `content/subjects/history/modern/independence/` | Towards Independence and Partition | Wavell Plan and Simla Conference, RIN mutiny, Cabinet Mission, Direct Action Day, Mountbatten Plan, Indian Independence Act 1947 | 🔲 |
| 20 | `hist.modern.social-movements` | `content/subjects/history/modern/social-movements/` | Depressed Classes, Labour and Peasant Organisations (20th c.) | Ambedkar, Vaikom and Guruvayur satyagrahas, AITUC, Kisan Sabhas, Tebhaga, Telangana | 🔲 |
| 21 | `hist.modern.governors-general` | `content/subjects/history/modern/governors-general/` | Governors-General and Viceroys | Who did what: Hastings to Mountbatten, with key events and reforms | 🔲 |
| 22 | `hist.modern.bengal-history` | `content/subjects/history/modern/bengal-history/` | Bengal in the Freedom Struggle (WBCS focus) | Bengal personalities, organisations, events; Tebhaga; Bengal famine 1943 | 🔲 |
| 23 | `hist.modern.post-independence` | `content/subjects/history/modern/post-independence/` | India after Independence (1947–1950s) | Integration of states, linguistic reorganisation, early planning | 🔲 |

### Phase 2: Indian Polity


#### Polity › Constitutional Framework (`polity.constitution`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 24 | `polity.constitution.making` | `content/subjects/polity/constitution/making/` | Making of the Constitution | Constituent Assembly, committees, sources, adoption | 🔲 |
| 25 | `polity.constitution.features` | `content/subjects/polity/constitution/features/` | Salient Features and Preamble | Features, Preamble, its interpretation | 🔲 |
| 26 | `polity.constitution.union-territory` | `content/subjects/polity/constitution/union-territory/` | Union and its Territory; Citizenship | Articles 1–11, reorganisation, Citizenship Act | 🔲 |
| 27 | `polity.constitution.fundamental-rights` | `content/subjects/polity/constitution/fundamental-rights/` | Fundamental Rights | Articles 12–35, writs | 🔲 |
| 28 | `polity.constitution.dpsp-duties` | `content/subjects/polity/constitution/dpsp-duties/` | Directive Principles and Fundamental Duties | Articles 36–51A, conflicts with FRs | 🔲 |
| 29 | `polity.constitution.amendment-basic-structure` | `content/subjects/polity/constitution/amendment-basic-structure/` | Amendment and Basic Structure | Article 368, Kesavananda Bharati, key amendments | 🔲 |

#### Polity › System of Government (`polity.system`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 30 | `polity.system.parliamentary-federal` | `content/subjects/polity/system/parliamentary-federal/` | Parliamentary and Federal System | Features, centre-state relations | 🔲 |
| 31 | `polity.system.emergency` | `content/subjects/polity/system/emergency/` | Emergency Provisions | Articles 352, 356, 360 | 🔲 |
| 32 | `polity.system.president-vp` | `content/subjects/polity/system/president-vp/` | President and Vice-President | Election, powers, ordinances, pardon | 🔲 |
| 33 | `polity.system.pm-council` | `content/subjects/polity/system/pm-council/` | Prime Minister and Council of Ministers | Appointment, collective responsibility, cabinet | 🔲 |
| 34 | `polity.system.parliament` | `content/subjects/polity/system/parliament/` | Parliament | Houses, sessions, bills, budget, committees, privileges | 🔲 |
| 35 | `polity.system.judiciary` | `content/subjects/polity/system/judiciary/` | Supreme Court and High Courts | Appointment, jurisdiction, judicial review, PIL | 🔲 |
| 36 | `polity.system.state-government` | `content/subjects/polity/system/state-government/` | State Government | Governor, CM, state legislature | 🔲 |
| 37 | `polity.system.local-government` | `content/subjects/polity/system/local-government/` | Panchayati Raj and Municipalities | 73rd and 74th Amendments, committees | 🔲 |
| 38 | `polity.system.uts-special` | `content/subjects/polity/system/uts-special/` | Union Territories and Special Areas | UTs, Fifth and Sixth Schedules | 🔲 |

#### Polity › Bodies, Elections and Issues (`polity.bodies`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 39 | `polity.bodies.constitutional-bodies` | `content/subjects/polity/bodies/constitutional-bodies/` | Constitutional Bodies | ECI, UPSC, SPSC, Finance Commission, CAG, AG, NCSC/NCST/NCBC | 🔲 |
| 40 | `polity.bodies.non-constitutional-bodies` | `content/subjects/polity/bodies/non-constitutional-bodies/` | Non-Constitutional Bodies | NITI Aayog, NHRC, CVC, CBI, Lokpal, information commissions | 🔲 |
| 41 | `polity.bodies.elections` | `content/subjects/polity/bodies/elections/` | Elections and Political Parties | Electoral system, anti-defection, RPA, electoral reforms | 🔲 |
| 42 | `polity.bodies.languages-misc` | `content/subjects/polity/bodies/languages-misc/` | Official Language, Tribunals and Miscellany | Official language, tribunals, cooperative societies, special provisions | 🔲 |

### Phase 3: Geography


#### Geography › Indian Geography (`geo.india`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 43 | `geo.india.physiography` | `content/subjects/geography/india/physiography/` | Physiography of India | Himalaya, plains, peninsula, coasts, islands | 🔲 |
| 44 | `geo.india.drainage` | `content/subjects/geography/india/drainage/` | Drainage System | Himalayan and peninsular rivers, lakes, interlinking | 🔲 |
| 45 | `geo.india.climate` | `content/subjects/geography/india/climate/` | Climate and Monsoon | Monsoon mechanism, seasons, rainfall distribution | 🔲 |
| 46 | `geo.india.soils-vegetation` | `content/subjects/geography/india/soils-vegetation/` | Soils and Natural Vegetation | Soil types, forests, wildlife regions | 🔲 |
| 47 | `geo.india.agriculture` | `content/subjects/geography/india/agriculture/` | Agriculture | Crops, seasons, irrigation, revolutions | 🔲 |
| 48 | `geo.india.minerals-energy` | `content/subjects/geography/india/minerals-energy/` | Minerals and Energy | Mineral belts, coal, oil, renewables | 🔲 |
| 49 | `geo.india.industries-transport` | `content/subjects/geography/india/industries-transport/` | Industries and Transport | Industrial regions, roads, rail, ports, airports | 🔲 |
| 50 | `geo.india.population` | `content/subjects/geography/india/population/` | Population and Settlement | Census facts, urbanisation, tribes | 🔲 |

#### Geography › Physical Geography (`geo.physical`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 51 | `geo.physical.universe-earth` | `content/subjects/geography/physical/universe-earth/` | The Universe and the Earth | Solar system, earth's motions, latitudes, time zones | 🔲 |
| 52 | `geo.physical.geomorphology` | `content/subjects/geography/physical/geomorphology/` | Geomorphology | Interior, rocks, plate tectonics, earthquakes, volcanoes, landforms | 🔲 |
| 53 | `geo.physical.climatology` | `content/subjects/geography/physical/climatology/` | Climatology | Atmosphere, pressure, winds, cyclones, climate types | 🔲 |
| 54 | `geo.physical.oceanography` | `content/subjects/geography/physical/oceanography/` | Oceanography | Relief, currents, tides, salinity, coral reefs | 🔲 |
| 55 | `geo.physical.world-regions` | `content/subjects/geography/physical/world-regions/` | World Geography Essentials | Continents, major features, straits, grasslands | 🔲 |

### Phase 4: Economy


#### Economy › Economic Concepts (`econ.basics`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 56 | `econ.basics.national-income` | `content/subjects/economy/basics/national-income/` | National Income and Growth | GDP, GVA, GNP, measurement, growth vs development | 🔲 |
| 57 | `econ.basics.inflation` | `content/subjects/economy/basics/inflation/` | Inflation | Types, CPI/WPI, causes, control | 🔲 |
| 58 | `econ.basics.money-banking` | `content/subjects/economy/basics/money-banking/` | Money and Banking | Money supply, banks, NPAs, financial inclusion | 🔲 |
| 59 | `econ.basics.rbi-monetary` | `content/subjects/economy/basics/rbi-monetary/` | RBI and Monetary Policy | Tools, MPC, repo, CRR/SLR, inflation targeting | 🔲 |
| 60 | `econ.basics.fiscal-budget` | `content/subjects/economy/basics/fiscal-budget/` | Fiscal Policy and Budget | Budget, deficits, FRBM | 🔲 |
| 61 | `econ.basics.taxation-gst` | `content/subjects/economy/basics/taxation-gst/` | Taxation and GST | Direct and indirect taxes, GST structure and council | 🔲 |
| 62 | `econ.basics.external-sector` | `content/subjects/economy/basics/external-sector/` | External Sector | BoP, exchange rate, forex reserves, FDI/FPI | 🔲 |
| 63 | `econ.basics.international-orgs` | `content/subjects/economy/basics/international-orgs/` | International Economic Organisations | WTO, IMF, World Bank, ADB, AIIB, NDB | 🔲 |
| 64 | `econ.basics.financial-markets` | `content/subjects/economy/basics/financial-markets/` | Financial Markets and Regulators | SEBI, stock markets, insurance, pensions | 🔲 |

#### Economy › Indian Economy (`econ.indian`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 65 | `econ.indian.planning-niti` | `content/subjects/economy/indian/planning-niti/` | Planning and NITI Aayog | Five-year plans, NITI Aayog | 🔲 |
| 66 | `econ.indian.poverty-employment` | `content/subjects/economy/indian/poverty-employment/` | Poverty, Unemployment and HDI | Estimates, schemes, human development | 🔲 |
| 67 | `econ.indian.agri-economy` | `content/subjects/economy/indian/agri-economy/` | Agricultural Economy | MSP, food security, PDS, agri reforms | 🔲 |
| 68 | `econ.indian.industry-infra` | `content/subjects/economy/indian/industry-infra/` | Industry and Infrastructure | Industrial policy, MSMEs, infrastructure | 🔲 |
| 69 | `econ.indian.schemes` | `content/subjects/economy/indian/schemes/` | Major Government Schemes | Flagship schemes by sector | 🔲 |

### Phase 5: Environment and Science


#### Environment › Environment and Ecology (`env.ecology`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 70 | `env.ecology.ecology-basics` | `content/subjects/environment/ecology/ecology-basics/` | Ecology Basics | Ecosystems, food chains, biogeochemical cycles | 🔲 |
| 71 | `env.ecology.biodiversity` | `content/subjects/environment/ecology/biodiversity/` | Biodiversity | Hotspots, IUCN categories, conservation | 🔲 |
| 72 | `env.ecology.protected-areas` | `content/subjects/environment/ecology/protected-areas/` | Protected Areas of India | National parks, sanctuaries, biosphere reserves, Ramsar sites | 🔲 |
| 73 | `env.ecology.climate-change` | `content/subjects/environment/ecology/climate-change/` | Climate Change | Greenhouse effect, UNFCCC, Kyoto, Paris, NDCs | 🔲 |
| 74 | `env.ecology.pollution` | `content/subjects/environment/ecology/pollution/` | Pollution and Waste | Air, water, soil, noise, plastic, e-waste | 🔲 |
| 75 | `env.ecology.conventions-laws` | `content/subjects/environment/ecology/conventions-laws/` | Environmental Conventions and Laws | CBD, CITES, Montreal, Indian environment laws, NGT | 🔲 |

#### Science › General Science (`sci.general`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 76 | `sci.general.physics-mechanics` | `content/subjects/science/general/physics-mechanics/` | Physics: Motion, Force and Energy | Units, laws of motion, work, gravitation | 🔲 |
| 77 | `sci.general.physics-heat-sound-light` | `content/subjects/science/general/physics-heat-sound-light/` | Physics: Heat, Sound and Light | Thermodynamics basics, waves, optics | 🔲 |
| 78 | `sci.general.physics-electricity` | `content/subjects/science/general/physics-electricity/` | Physics: Electricity and Magnetism | Current, circuits, magnetism, devices | 🔲 |
| 79 | `sci.general.chemistry-basics` | `content/subjects/science/general/chemistry-basics/` | Chemistry: Matter and Reactions | Atoms, periodic table, reactions, acids/bases | 🔲 |
| 80 | `sci.general.chemistry-everyday` | `content/subjects/science/general/chemistry-everyday/` | Chemistry in Everyday Life | Metals, polymers, fuels, fertilisers, medicines | 🔲 |
| 81 | `sci.general.biology-cell-genetics` | `content/subjects/science/general/biology-cell-genetics/` | Biology: Cell and Genetics | Cell, DNA, heredity | 🔲 |
| 82 | `sci.general.human-body` | `content/subjects/science/general/human-body/` | Human Body | Organ systems, nutrition, vitamins, blood | 🔲 |
| 83 | `sci.general.health-diseases` | `content/subjects/science/general/health-diseases/` | Health and Diseases | Diseases, vaccines, immunity | 🔲 |
| 84 | `sci.general.plants-animals` | `content/subjects/science/general/plants-animals/` | Plants and Animals | Classification, plant physiology | 🔲 |
| 85 | `sci.general.space-tech` | `content/subjects/science/general/space-tech/` | Space Technology | ISRO missions, satellites, launch vehicles | 🔲 |
| 86 | `sci.general.defence-nuclear-it` | `content/subjects/science/general/defence-nuclear-it/` | Defence, Nuclear and IT | Missiles, nuclear programme, computers, AI | 🔲 |
| 87 | `sci.general.biotech` | `content/subjects/science/general/biotech/` | Biotechnology | GM crops, cloning, stem cells | 🔲 |

### Phase 6: Ancient & Medieval History, Art & Culture


#### History › Ancient India (`hist.ancient`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 88 | `hist.ancient.prehistoric-ivc` | `content/subjects/history/ancient/prehistoric-ivc/` | Prehistory and the Indus Valley Civilisation | Stone ages, Harappan sites and features | 🔲 |
| 89 | `hist.ancient.vedic` | `content/subjects/history/ancient/vedic/` | Vedic Age | Early and later Vedic society, literature | 🔲 |
| 90 | `hist.ancient.buddhism-jainism` | `content/subjects/history/ancient/buddhism-jainism/` | Buddhism and Jainism | Teachings, councils, sects | 🔲 |
| 91 | `hist.ancient.mahajanapadas-mauryas` | `content/subjects/history/ancient/mahajanapadas-mauryas/` | Mahajanapadas and the Mauryas | Magadha, Ashoka, administration | 🔲 |
| 92 | `hist.ancient.post-mauryan` | `content/subjects/history/ancient/post-mauryan/` | Post-Mauryan Period | Shungas, Kushanas, Satavahanas, Sangam age | 🔲 |
| 93 | `hist.ancient.guptas` | `content/subjects/history/ancient/guptas/` | The Gupta Age | Rulers, culture, science | 🔲 |
| 94 | `hist.ancient.post-gupta-south` | `content/subjects/history/ancient/post-gupta-south/` | Post-Gupta and Early Medieval South | Harsha, Pallavas, Chalukyas, Cholas | 🔲 |

#### History › Medieval India (`hist.medieval`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 95 | `hist.medieval.delhi-sultanate` | `content/subjects/history/medieval/delhi-sultanate/` | Delhi Sultanate | Dynasties, administration, economy | 🔲 |
| 96 | `hist.medieval.vijayanagara-bahmani` | `content/subjects/history/medieval/vijayanagara-bahmani/` | Vijayanagara and Bahmani | Rulers, administration, culture | 🔲 |
| 97 | `hist.medieval.bhakti-sufi` | `content/subjects/history/medieval/bhakti-sufi/` | Bhakti and Sufi Movements | Saints, ideas, regions | 🔲 |
| 98 | `hist.medieval.mughals` | `content/subjects/history/medieval/mughals/` | The Mughals | Rulers, administration, mansabdari, culture | 🔲 |
| 99 | `hist.medieval.marathas-later` | `content/subjects/history/medieval/marathas-later/` | Marathas and Later Mughals | Shivaji, Peshwas, decline of the Mughals | 🔲 |

#### Art & Culture › Art and Culture (`art.culture`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 100 | `art.culture.architecture` | `content/subjects/art-culture/culture/architecture/` | Indian Architecture | Temple styles, Indo-Islamic, colonial | 🔲 |
| 101 | `art.culture.painting-sculpture` | `content/subjects/art-culture/culture/painting-sculpture/` | Painting and Sculpture | Schools, cave paintings, miniature | 🔲 |
| 102 | `art.culture.music-dance` | `content/subjects/art-culture/culture/music-dance/` | Music, Dance and Theatre | Classical and folk forms | 🔲 |
| 103 | `art.culture.religion-philosophy` | `content/subjects/art-culture/culture/religion-philosophy/` | Religion and Philosophy | Schools of philosophy, religions | 🔲 |
| 104 | `art.culture.literature-languages` | `content/subjects/art-culture/culture/literature-languages/` | Literature and Languages | Classical, regional, Eighth Schedule | 🔲 |
| 105 | `art.culture.festivals-heritage` | `content/subjects/art-culture/culture/festivals-heritage/` | Festivals, Fairs and Heritage | UNESCO sites, intangible heritage, GI tags | 🔲 |

### Phase 7: West Bengal and Static GK


#### West Bengal › West Bengal (WBCS) (`wb.state`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 106 | `wb.state.wb-geography` | `content/subjects/west-bengal/state/wb-geography/` | Geography of West Bengal | Physiography, rivers, climate, districts | 🔲 |
| 107 | `wb.state.wb-economy` | `content/subjects/west-bengal/state/wb-economy/` | Economy of West Bengal | Agriculture, industry, state schemes | 🔲 |
| 108 | `wb.state.wb-culture` | `content/subjects/west-bengal/state/wb-culture/` | Culture of West Bengal | Literature, art, festivals, personalities | 🔲 |
| 109 | `wb.state.wb-polity` | `content/subjects/west-bengal/state/wb-polity/` | Polity and Administration of West Bengal | Legislature, local bodies, state bodies | 🔲 |

#### Static GK › Static General Knowledge (`gk.static`)

| Q | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 110 | `gk.static.national-symbols` | `content/subjects/static-gk/static/national-symbols/` | National Symbols and Firsts | Symbols, firsts in India and the world | 🔲 |
| 111 | `gk.static.books-authors` | `content/subjects/static-gk/static/books-authors/` | Books and Authors | Classic and modern works | 🔲 |
| 112 | `gk.static.awards` | `content/subjects/static-gk/static/awards/` | Awards and Honours | Bharat Ratna, Padma, Nobel, Jnanpith, sports awards | 🔲 |
| 113 | `gk.static.sports` | `content/subjects/static-gk/static/sports/` | Sports | Trophies, venues, terms, Olympics | 🔲 |
| 114 | `gk.static.organisations` | `content/subjects/static-gk/static/organisations/` | International Organisations | UN bodies, regional groups, headquarters | 🔲 |
| 115 | `gk.static.days-events` | `content/subjects/static-gk/static/days-events/` | Important Days and Events | National and international days | 🔲 |

## Adding or changing topics
- New topics get the next free queue number in their phase; never renumber written topics (IDs are permanent).
- A subject or unit that does not exist yet needs `subject.yaml` / `unit.yaml` (see docs/CONTENT_STRUCTURE.md §3); the daily routine creates them when it reaches the first topic of a new unit.

