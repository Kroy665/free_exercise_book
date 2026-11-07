# Syllabus Outline

The content plan: every topic has a fixed **ID, folder and order** before it is written, so batches can be produced and reviewed independently. Status: ✅ written · 🔲 planned.

Exam coverage: UPSC CSE Prelims (GS-I), WBCS, other State PSCs, SSC CGL/CHSL, Banking, Railways. Folder = `content/subjects/<subject>/<unit>/<folder>/`.

## History › Modern India (`hist.modern`)

| # | ID | Folder | Topic | Covers | Status |
|---|---|---|---|---|---|
| 1 | `hist.modern.european-arrival` | `european-arrival` | Advent of the Europeans | Portuguese, Dutch, English, Danish, French companies; factories; Anglo-French rivalry and the Carnatic Wars | ✅ batch 1 |
| 2 | `hist.modern.british-expansion` | `british-expansion` | Expansion of British Power | Plassey, Buxar, Dual Government; Anglo-Mysore, Anglo-Maratha, Anglo-Sikh wars; Subsidiary Alliance; Doctrine of Lapse | ✅ batch 1 |
| 3 | `hist.modern.company-acts` | `company-acts` | Company Rule: Acts 1773–1853 | Regulating Act 1773, Pitt's India Act 1784, Charter Acts 1793/1813/1833/1853 | ✅ batch 1 |
| 4 | `hist.modern.economic-impact` | `economic-impact` | Economic Impact of British Rule | Permanent Settlement, Ryotwari, Mahalwari; drain of wealth; deindustrialisation; commercialisation of agriculture; famines | ✅ batch 1 |
| 5 | `hist.modern.social-reform` | `social-reform` | Socio-Religious Reform Movements | Bengal Renaissance, Brahmo Samaj, Young Bengal, Prarthana Samaj, Arya Samaj, Ramakrishna Mission, Aligarh, Satyashodhak, Sree Narayana; laws on sati, widow remarriage, age of consent | ✅ batch 1 |
| 6 | `hist.modern.peasant-tribal` | `peasant-tribal` | Peasant and Tribal Movements (pre-1857 to 1900) | Sanyasi-Fakir, Kol, Santhal (Hul), Munda (Ulgulan), Indigo Revolt, Pabna, Deccan riots, Wahabi and Faraizi movements | ✅ batch 2 |
| 7 | `hist.modern.revolt-1857` | `revolt-of-1857` | The Revolt of 1857 | Causes, spread, leaders, suppression, nature, consequences | ✅ |
| 8 | `hist.modern.education-press` | `education-press` | Education, Press and the Indian Middle Class | Charter Act 1813 grant, Macaulay's Minute 1835, Wood's Despatch 1854, Hunter Commission, universities 1857; Vernacular Press Act 1878 | ✅ batch 2 |
| 9 | `hist.modern.early-nationalism` | `early-nationalism` | Rise of Nationalism and the Moderates | Pre-Congress associations, INC 1885, Moderates' methods and demands, Indian Councils Act 1892 | ✅ batch 2 |
| 10 | `hist.modern.swadeshi` | `swadeshi` | Partition of Bengal and the Swadeshi Movement | Curzon, partition 1905, Swadeshi and Boycott, Extremists (Lal-Bal-Pal), Surat split 1907, Morley-Minto Reforms 1909, Muslim League 1906, annulment 1911 | ✅ batch 2 |
| 11 | `hist.modern.revolutionaries` | `revolutionaries` | Revolutionary Nationalism | Anushilan Samiti, Jugantar, Alipore case, Ghadar Party, Kakori, HSRA (Bhagat Singh), Chittagong Armoury Raid, revolutionaries abroad | ✅ batch 2 |
| 12 | `hist.modern.home-rule` | `home-rule` | First World War, Home Rule and Lucknow Pact | Home Rule Leagues (Tilak, Besant), Lucknow Pact 1916, Montagu Declaration 1917, Government of India Act 1919 | 🔲 |
| 13 | `hist.modern.gandhi-early` | `gandhi-early` | Arrival of Gandhi | South Africa, Champaran, Kheda, Ahmedabad mill strike, Rowlatt Satyagraha, Jallianwala Bagh, Hunter Committee | 🔲 |
| 14 | `hist.modern.non-cooperation` | `non-cooperation` | Khilafat and Non-Cooperation Movement | Khilafat issue, NCM programme, Nagpur session 1920, Chauri Chaura, Moplah rebellion | 🔲 |
| 15 | `hist.modern.1920s` | `twenties` | The 1920s: Swarajists to Purna Swaraj | Swaraj Party, Simon Commission, Nehru Report, Jinnah's 14 points, Lahore Session 1929 | 🔲 |
| 16 | `hist.modern.civil-disobedience` | `civil-disobedience` | Civil Disobedience and the Round Table Conferences | Dandi March, CDM, Gandhi-Irwin Pact, Round Table Conferences, Communal Award, Poona Pact | 🔲 |
| 17 | `hist.modern.act-1935` | `act-1935` | Government of India Act 1935 and Provincial Ministries | Act of 1935, 1937 elections, Congress ministries, resignation 1939 | 🔲 |
| 18 | `hist.modern.quit-india` | `quit-india` | Second World War, Quit India and the INA | August Offer, Individual Satyagraha, Cripps Mission, Quit India, Subhas Chandra Bose and the INA, INA trials | 🔲 |
| 19 | `hist.modern.independence` | `independence` | Towards Independence and Partition | Wavell Plan and Simla Conference, RIN mutiny, Cabinet Mission, Direct Action Day, Mountbatten Plan, Indian Independence Act 1947 | 🔲 |
| 20 | `hist.modern.social-movements` | `social-movements` | Depressed Classes, Labour and Peasant Organisations (20th c.) | Ambedkar, Vaikom and Guruvayur satyagrahas, AITUC, Kisan Sabhas, Tebhaga, Telangana | 🔲 |
| 21 | `hist.modern.governors-general` | `governors-general` | Governors-General and Viceroys | Who did what: Hastings to Mountbatten, with key events and reforms | 🔲 |
| 22 | `hist.modern.bengal-history` | `bengal-history` | Bengal in the Freedom Struggle (WBCS focus) | Bengal personalities, organisations, events; Tebhaga; Bengal famine 1943 | 🔲 |

Next units (planned): Ancient India (`hist.ancient`), Medieval India (`hist.medieval`), Art & Culture, Polity, Geography, Economy, Science, Environment. Current affairs: one month per pack (`ca.<yyyy>.<mm>`).

## How a batch is produced
1. Writers produce each topic from this outline (notes `en` + `bn`, 30+ MCQs, all five question types), following CONTENT_STRUCTURE and CONTENT_GUIDELINES.
2. A separate reviewer, who did not write the topic, fact-checks every answer and explanation, fixes errors and records uncertain facts.
3. `tools/content-check/validate.py` and the core tests must pass. Status stays `ai-generated` until a human reviewer signs off.
