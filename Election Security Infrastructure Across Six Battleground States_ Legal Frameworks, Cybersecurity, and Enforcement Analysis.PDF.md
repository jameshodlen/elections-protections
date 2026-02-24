

# Election security infrastructure across six battleground states
The six battleground states—Pennsylvania, Michigan, Georgia, Arizona, Nevada, and North Carolina—present a patchwork of election security
capabilities, legal frameworks, and vulnerabilities that any comprehensive lobbying strategy must navigate. **Michigan offers the strongest
citizen enforcement tools** through its constitutionally enshrined private right of action (Proposal 2 of 2022), while **North Carolina faces
the most institutional turbulence** following SB 382's restructuring of its election board appointment authority. Three of the six states
(Michigan, Arizona, Nevada) have joined the 19-state lawsuit against Executive Order 14248; [Democracy Docket +5]
(https://www.democracydocket.com/news-alerts/trump-elections-executive-order-state-lawsuit/) Pennsylvania, Georgia, and North Carolina
have not. All six states operate air-gapped voting systems with paper audit trails, but their cybersecurity maturity varies significantly—North
Carolina's Whole-of-State program is nationally recognized, while Nevada is still building out its statewide Security Operations Center.
This report provides maximum-depth findings for each state across all six research categories, organized for direct use in developing state-
specific election security guides modeled after the existing Minnesota/Wisconsin framework.
## ---
## Pennsylvania: Strong infrastructure, limited secretary authority
### State election authority and legal framework
Pennsylvania's chief election official is the **Secretary of the Commonwealth, Al Schmidt** (Republican, appointed by Governor Josh
Shapiro), operating within the Department of State. The Pennsylvania Election Code (Act of June 3, 1937, P.L. 1333, [pa]
(https://www.pa.gov/content/dam/copapwp-pagov/en/dos/resources/voting-and-elections/grants/PA_24ES_Program_Narrative-FINAL-
5.6.24.pdf) codified at **25 P.S. § 2600 et seq.**) and voter registration statutes (**25 Pa.C.S.**) form the legal backbone. Act 77 of 2019
established no-excuse mail-in voting.
The **Bureau of Election Security and Technology (BEST)** within the Department of State oversees election technology, cybersecurity, and
SURE system administration. [PA Department of State](https://www.dos.pa.gov/VotingElections/BEST/Pages/default.aspx) However, the
Secretary has **limited rulemaking authority** compared to peer states—the General Assembly retains primary legislative control over
election code modifications, a structural constraint that limits executive-branch agility.
Pennsylvania's constitutional provisions center on **Article VII** (14 sections on elections) [Ballotpedia]
(https://ballotpedia.org/Pennsylvania_Constitution) and **Article I, § 5** (Declaration of Rights), which contains the "free and equal elections"
clause expressly disallowing interference with the right to vote. [Paablog](https://paablog.com/voting-rights-constitution-quilt/) The state's
**67 county boards of elections** administer elections locally under **25 P.S. § 2642**, with Philadelphia's three elected city commissioners
serving as the board in first-class cities. [PA General Assembly](https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/25/25.HTM)
Governor Shapiro established the **Pennsylvania Election Threats Task Force** in 2024, led by Secretary Schmidt, comprising 10+ agencies
including U.S. Attorney offices for all three PA districts, the AG's Office, PA State Police, PA National Guard, PEMA, and DHS. [Pennsylvania
Department of Transportation](https://www.pa.gov/governor/newsroom/2024-press-releases/governor-shapiro-launches-pennsylvania-
election-threats-task-for) [NBC News](https://www.nbcnews.com/politics/elections/pennsylvania-election-security-task-force-rcna141024)
### Cybersecurity infrastructure
Pennsylvania's voter registration system, **SURE (Statewide Uniform Registry of Electors)**, was built in the early 2000s [Votebeat]
(https://www.votebeat.org/pennsylvania/2025/03/05/sure-upgrade-voter-registration-system-new-contract-signed/) under **25 Pa.C.S.
Chapter 12** and is critically outdated. In March 2025, PA signed a **$10.6 million contract with Civix** to modernize SURE, targeting the new
voter registration component for 2027 municipal elections. [WITF](https://www.witf.org/2025/03/05/pa-moves-to-update-22-year-old-
elections-voter-registration-systems/) The system uses controlled security credentials, mandatory cybersecurity training for county users,
and encryption. [York County, PA](https://yorkcountypa.gov/1077/Election-Infrastructure-Security)
**Total HAVA Election Security funding to PA** (FY2018–FY2024): **$34,063,403 federal + $4,791,258 state match = $38,854,661**. [pa]
(https://www.pa.gov/content/dam/copapwp-pagov/en/dos/resources/voting-and-elections/grants/PA_24ES_Program_Narrative-FINAL-
5.6.24.pdf) Budget breakdown shows 40% for voting equipment, 26% for voter registration systems, and only 6% for cyber/physical security.
[pa](https://www.pa.gov/content/dam/copapwp-pagov/en/dos/resources/voting-and-elections/grants/PA_24ES_Program_Narrative-FINAL-
5.6.24.pdf) The FY2024 allocation was $1 million federal [Pennsylvania Government](https://www.pa.gov/agencies/dos/resources/voting-
and-elections-resources/federal-grants/2024-federal-grants.html) plus $200,000 state match. [pa]
(https://www.pa.gov/content/dam/copapwp-pagov/en/dos/resources/voting-and-elections/grants/PA_24ES_Program_Narrative-FINAL-
## 5.6.24.pdf)
The **PA National Guard** operates three complementary cyber units: the **112th Cyber Operations Squadron** (71 trained personnel, 18
full-time, based at Horsham AGS), a Defensive Cyber Operations Element, and a Cyber Protection Team–Mission Element. Active since 2016
in election support, [DVIDS](https://www.dvidshub.net/news/382300/pennsylvania-national-guard-cyber-branch-supports-2020-election)
approximately 10–30 Guard members deploy each election cycle, [www.army.mil]
(https://www.army.mil/article/229536/pa_guard_cyber_branch_supports_2019_election) having completed **60+ cybersecurity
assessments** for state agencies and local organizations. [www.army.mil]
(https://www.army.mil/article/289050/pennsylvania_national_guard_strengthens_cyber_defense_at_home_and_abroad)
Pennsylvania was an active **EI-ISAC member** until CISA cut $10 million in funding to CIS in 2025. [Votebeat]
(https://www.votebeat.org/pennsylvania/2025/03/17/secretary-commonwealth-al-schmidt-election-security-cisa-cuts-kristi-noem/)
Secretary Schmidt wrote directly to DHS Secretary Noem warning that the loss would harm PA's election security, citing EI-ISAC's role in
notifying officials of Election Day bomb threats, debunking a fake Bucks County ballot destruction video, and sharing intelligence on
suspicious white-powder envelopes. [Spotlight PA](https://www.spotlightpa.org/news/2025/03/secretary-commonwealth-al-schmidt-
election-security-cisa-cuts-kristi-noem/)

### Physical security and polling place protections
Pennsylvania's buffer zone framework operates on two layers. A **10-foot rule** (**25 P.S. § 3060(d)**) keeps all unauthorized persons at
least 10 feet from the polling place room itself. More significantly, a **100-foot police exclusion zone** (**25 P.S. §§ 3047, 3520**) prohibits
law enforcement within 100 feet of polling places, with exceptions only for active emergencies or when summoned by the judge of elections,
an inspector, or three qualified electors. [Pennsylvania Attorney General](https://www.attorneygeneral.gov/wp-
content/uploads/2024/10/2024-PDAA-Election-Guidance-for-DAs-and-Law-Enforcement.pdf)
Poll watchers require **certification from the county board of elections** and must be qualified registered electors of the county (**25 P.S. §
2687**). [Pennsylvania Attorney General](https://www.attorneygeneral.gov/wp-content/uploads/2024/10/2024-PDAA-Election-Guidance-for-
DAs-and-Law-Enforcement.pdf) Each candidate may appoint 2 watchers per district; parties may appoint 3, with only 1 present at a time.
[Brennan Center for Justice](https://www.brennancenter.org/our-work/research-reports/pennsylvania-election-observers-rules-and-
constraints) Compensation is capped at **$120/day**. [FindLaw](https://codes.findlaw.com/pa/title-25-ps-elections-electoral-districts/pa-st-
sect-25-2687.html) The **Judge of Elections** holds removal authority for watchers engaging in prohibited activities.
Voter intimidation carries serious penalties: up to **2 years' imprisonment** [Saucon Source]
(https://sauconsource.com/2024/10/31/pennsylvania-warns-against-voter-intimidation-ahead-of-election/) under **25 P.S. § 3547**, and
**Felony of the Third Degree** under **25 P.S. § 3527** for preventing elections, threatening officials, or blocking polling place access.
[Brennan Center for Justice](https://www.brennancenter.org/our-work/research-reports/pennsylvania-protections-against-intimidation-
voters-and-election-workers) The AG has prosecutorial jurisdiction over **all** Election Code violations (**25 P.S. § 3555**), concurrent with
county district attorneys. [Pennsylvania Attorney General](https://www.attorneygeneral.gov/wp-
content/uploads/2020/10/PDAAElectionGuidance.pdf) [Brennan Center for Justice](https://www.brennancenter.org/our-work/research-
reports/pennsylvania-election-certification-processes-and-guardrails)
### Legal strategies and constitutional protections
**Pennsylvania is NOT part of the 19-state lawsuit** against Executive Order 14248. The absence is notable given Governor Shapiro's
participation in other multistate coalitions against Trump administration actions. Active litigation includes the **County of Fulton** contempt
case (officials allowing unauthorized third-party inspection of voting equipment) [Protect Democracy](https://protectdemocracy.org/wp-
content/uploads/2024/09/Pennsylvania-Guide.pdf) and **United Sovereign Americans v. Commonwealth** (challenging voter registration
roll accuracy). The PA Supreme Court's **King's Bench authority** (Pa. Const. art. V, § 2) provides an extraordinary jurisdiction pathway for
election disputes. [Protect Democracy](https://protectdemocracy.org/wp-content/uploads/2024/09/Pennsylvania-Guide.pdf)
### Key contacts
- **Secretary of the Commonwealth**: 717-787-6458; www.dos.pa.gov
- **Voter Hotline**: 1-877-VOTESPA (1-877-868-3772) [Pennsylvania Government](https://www.pa.gov/agencies/vote/voter-support/your-
rights-and-the-law/voter-intimidation)
- **PA National Guard Public Affairs**: Lt. Col. Keith Hickox, 717-861-6254 [DVIDS](https://www.dvidshub.net/news/382300/pennsylvania-
national-guard-cyber-branch-supports-2020-election)
- **AG Office**: www.attorneygeneral.gov (AG Michelle Henry)
## ---
## Michigan: Constitutional voter protections and robust enforcement
### State election authority and legal framework
Secretary of State **Jocelyn Benson** serves as Michigan's chief election officer under **MCL § 168.21**, with "supervisory control over
local election officials." [Michigan Legislature](https://www.legislature.mi.gov/documents/mcl/pdf/mcl-chap168.pdf) [Michigan Legislature]
(http://www.legislature.mi.gov/documents/mcl/pdf/mcl-act-116-of-1954.pdf) Her specific duties under **MCL § 168.31** include
promulgating rules under the Administrative Procedures Act, directing local officials, establishing training curricula, and creating an **Election
Day dispute resolution team** with regional representatives. [Onecle](https://law.onecle.com/michigan/chapter-168/168.31.html) The
Bureau of Elections (430 W. Allegan St., Lansing, MI 48933) [Michigan]
(https://www.michigan.gov/-/media/Project/Websites/sos/01vanderroest/contact_us_new_card.pdf?
rev=86ca878eecaf4cc6b315f074bb61ab34) is headed by a Director of Elections appointed under civil service regulations. [Michigan
Legislature](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-168-32)
Michigan's constitutional framework is exceptionally strong following **Proposal 2 of 2022**, which amended **Article II, § 4** to establish
voting as a "fundamental right" and created a comprehensive set of self-executing protections [Ballotpedia]
(https://ballotpedia.org/Michigan_Proposal_2,_Voting_Policies_in_Constitution_Amendment_(2022)) including: no-excuse absentee voting,
same-day registration, 9 days of early in-person voting, state-funded election security measures, mandatory risk-limiting audits, and ballot
tracking. [Michigan Legislature](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-Article-II-4) [Justia]
(https://law.justia.com/codes/michigan/2022/chapter-1/statute-constitution-of-michigan-of-1963/article-ii/section-article-ii-4/) Critically, the
amendment includes an **explicit prohibition** on "harassing, threatening, or intimidating conduct" that burdens voting rights. [Michigan
Legislature](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-Article-II-4)
Michigan's **~1,600 local clerks** (city and township) administer elections in a highly decentralized system, [Ballotpedia]
(https://ballotpedia.org/Michigan_Secretary_of_State_election,_2022) with 83 county clerks playing supervisory roles.
### Cybersecurity infrastructure
The **Department of Technology, Management & Budget (DTMB)** houses state cybersecurity operations under CSO Jayson Cavendish and
CIO Laura Clark. The **2024 Michigan Cyber Roadmap** focuses on five domains: [State of Michigan]

(https://www.michigan.gov/dtmb/services/cybersecurity) threat mitigation, local government protections, AI, partnerships, and workforce.
The **Michigan Cyber Corps** deployed 5 times in 2024–2025 with 7 volunteer members at no cost to recipient entities. [Michigan House]
(https://house.mi.gov/Document/?DocumentId=48015&DocumentType=CommitteeTestimony)
Michigan's **Qualified Voter File (QVF)** (**MCL § 168.509q**) is a state-owned, web-based database accessed by municipal and county
clerks with **multi-factor authentication** and specialized training requirements. The QVF is **not connected to tabulators**—ePollbooks are
downloaded pre-election and operate offline. In September 2025, the **DOJ sued SOS Benson** seeking unredacted QVF data; Michigan
resisted, citing the Privacy Act, Driver Privacy Protection Act, and state law protections.
The **272nd Cyber Operations Squadron** (110th Wing, Michigan Air National Guard, Battle Creek) is one of only **12 such squadrons** in
the Air National Guard. [DVIDS](https://www.dvidshub.net/video/842709/110th-wing-who-we-272d-cyber-operations-squadron) The unit
participates in the **Cyber 9-Line** program linking Guard units with U.S. Cyber Command and NSA for rapid election incident response.
[BankInfoSecurity](https://www.bankinfosecurity.com/national-guard-prepping-for-november-election-security-role-a-14420)
Michigan allocated an additional **$5 million** in HAVA grant funding to local jurisdictions ahead of the 2024 election for physical security,
cybersecurity resilience, and voting equipment. [Michigan Secretary of State]
(https://www.michigan.gov/sos/resources/news/2024/09/26/secretary-benson-launches-new-tools-updates-to-boost-election-security)
Total HAVA grants audited at approximately **$49.88 million**. [U.S. Election Assistance Commission](https://eac.gov/inspector-
general/hava-fund-audits) [Eac](https://oig.eac.gov/reports/audit/audit-administration-help-america-vote-act-grants-awarded-state-michigan)
### Physical security and polling place protections
**MCL § 168.744** establishes a **100-foot buffer zone** from any entrance to a building containing a polling place, prohibiting voter
solicitation, campaign material distribution, and donations. Violation is a **misdemeanor**. [Michigan Legislature]
(https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-168-744)
Michigan enacted legislation (signed by Governor Whitmer in 2024) **banning open carry of firearms** within polling places and within 100
feet of entrances on Election Day and during early voting, [Democracy Docket](https://www.democracydocket.com/news-alerts/michigan-
bans-firearms-at-polling-locations/) [Michigan Advance](https://michiganadvance.com/briefs/whitmer-signs-bills-banning-firearms-at-
michigan-polling-locations/) within 100 feet of absentee ballot drop boxes for 40 days before elections, [Michigan Advance]
(https://michiganadvance.com/briefs/whitmer-signs-bills-banning-firearms-at-michigan-polling-locations/) and within 100 feet of absentee
ballot counting boards. Penalties: up to **$100 fine** and/or **90 days imprisonment**. [Bridge Michigan](https://bridgemi.com/michigan-
government/michigan-dems-aim-ban-guns-voting-locations/) Concealed carry with a valid permit remains permitted. [Michigan Advance]
(https://michiganadvance.com/briefs/whitmer-signs-bills-banning-firearms-at-michigan-polling-locations/)
Michigan uses a distinctive **dual system of challengers and poll watchers**. [Protect The Vote](https://protectthevote.com/michigan-
election-law-information/) Challengers (**MCL § 168.730**) must complete mandatory training and receive certificates of completion.
[Rescuemichigan](https://www.rescuemichigan.com/blog.php?e=fixing-broken-elections-2-poll-challengers) Election inspectors may **order
challengers to leave** for disorderly conduct or repeatedly ignoring instructions (**MCL § 168.678; 168.733(3)**); law enforcement may
remove those who refuse. [Michigan Secretary of State](https://www.michigan.gov/sos/-/media/Project/Websites/sos/Election-
Administrators/Election-Crimes-Manual-Obligations-and-Penalties-Imposed-by-State-Election-Laws.pdf?
rev=94ecc45be2d940baa77310f84b12f239&hash=A0E03AAA4464806B25B1DFFE0749DD43)
Voter intimidation is a **felony with up to 5-year maximum** under **MCL § 168.932(1)(a)**. [Michigan Secretary of State]
(https://www.michigan.gov/sos/-/media/Project/Websites/sos/Elections/Election-Forms/Conduct-Prohibited-at-Voting-Related-
Locations.pdf?rev=7fc76398753b4a7da83b8f5bc7fcde94&hash=E4CFB25A70DC5A3DC0E3FE58FA2845A1) In the landmark *People v.
Burkman and Wohl* case, the Michigan Supreme Court ruled (June 2024) that this statute prohibits **intentionally false speech** related to
voting requirements made to deter votes. [State of Michigan](https://www.michigan.gov/ag/news/press-releases/2024/06/13/mi-supreme-
court-rules-state-correctly-applied-election-law)
### Legal strategies and constitutional protections
**Michigan IS a party to the 19-state lawsuit** against EO 14248, with AG Dana Nessel joining on April 3, 2025. [Civil Rights Litigation
Clearinghouse +3](https://clearinghouse.net/case/46337/) A federal judge granted a **preliminary injunction on June 13, 2025** blocking
documentary proof-of-citizenship requirements. [Civil Rights Litigation Clearinghouse](https://clearinghouse.net/case/46337/) [Democracy
Docket](https://www.democracydocket.com/cases/massachusetts-trump-election-integrity-executive-order-challenge/)
Michigan's **private right of action** provision (Article II, § 4(1)(a), Proposal 2 of 2022) is the strongest among all six states: any citizen has
standing to bring declaratory, injunctive, and/or monetary relief in circuit court, with **mandatory attorney's fee shifting** if the plaintiff
prevails in whole or in part. [Ballotpedia](https://ballotpedia.org/Michigan_Proposal_2,_Voting_Policies_in_Constitution_Amendment_(2022))
This provision is self-executing and must be "liberally construed in favor of voters' rights." [Michigan Legislature]
(https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-Article-II-4)
### Key contacts
- **Bureau of Elections**: 517-335-3234 [Michigan]
(https://www.michigan.gov/-/media/Project/Websites/sos/01vanderroest/contact_us_new_card.pdf?
rev=86ca878eecaf4cc6b315f074bb61ab34)
- **QVF/ePollbook Support**: 800-310-5697 / 517-241-1911; EASupport@Michigan.gov [Michigan]
(https://www.michigan.gov/-/media/Project/Websites/sos/01vanderroest/contact_us_new_card.pdf?
rev=86ca878eecaf4cc6b315f074bb61ab34)
- **AG Voter Intimidation Reports**: 517-335-7659
- **DTMB Cybersecurity Grants**: DTMB-CIP-SLCGP@michigan.gov
## ---

## Georgia: Dominion BMD controversies and evolving board power
### State election authority and legal framework
Secretary of State **Brad Raffensperger** serves as chief elections officer [Justia](https://law.justia.com/codes/georgia/title-21/chapter-
2/article-6/section-21-2-210/) under **GA Const. Art. II, § II, ¶I**, with powers defined in **O.C.G.A. § 21-2-50 et seq.** The Elections Division
(2 MLK Jr. Drive SE, West Tower, Atlanta, GA 30334) oversees all election activity including voter registration across Georgia's 159 counties.
[Georgia Secretary of State](https://sos.ga.gov/elections-division-georgia-secretary-states-office)
**SB 202 (Election Integrity Act of 2021)** remains Georgia's defining election legislation. Key provisions still in effect include: voter ID for
absentee ballots (replacing signature matching), drop box restrictions (**one per 100,000 registered voters**), the food/water prohibition
within buffer zones (with self-service water exception), expanded early voting (minimum 17 days), and shortened runoff periods (9 weeks to
4 weeks). SB 202 also **removed the Secretary of State** as a voting member of the State Election Board and granted the SEB authority to
appoint replacement superintendents for underperforming county boards (**O.C.G.A. § 21-2-33.2**).
The **State Election Board** experienced significant controversy in 2024 when three conservative members (Johnston, Jeffares, King)
adopted 7 rules—including "reasonable inquiry" requirements for certification and hand-count mandates—that were praised by Trump at an
Atlanta rally. AG Chris Carr issued **Official Opinion 2024-1** stating the SEB exceeded its authority; the **Georgia Supreme Court
unanimously struck down the rules on June 10, 2025**.
### Cybersecurity infrastructure
The **Georgia Technology Authority (GTA) Office of Information Security** uses the NIST Risk Management Framework and CIS 18 Critical
Controls. [Georgia](https://gta.georgia.gov/cybersecurity-1/governance-risk-and-compliance) Georgia's crown jewel is the **Georgia Cyber
Center in Augusta**—a **$100 million**, 332,000 sq. ft. facility [Georgia](https://gta.georgia.gov/georgia-cyber-center) [Georgia Department
of Economic Development](https://georgia.org/video/georgias-new-state-art-cyber-center) housing Augusta University's School of Computer
and Cyber Sciences [Georgia](https://gta.georgia.gov/georgia-cyber-center) (one of only **22 institutions nationwide** with NSA NCAE Cyber
Operations designation), [Jagwire](https://jagwire.augusta.edu/au-named-georgias-only-national-center-of-academic-excellence-in-cyber-
ops/) the GBI Cyber Crime Center, [Gacybercenter](https://www.gacybercenter.org/) defense contractors (BAE Systems, Northrop Grumman,
Parsons), and the Georgia Cyber Range. [Georgia](https://gta.georgia.gov/georgia-cyber-center) The center's proximity to **Fort Eisenhower**
(home of U.S. Army Cyber Command, with 17,000+ military/civilian personnel) creates a unique cybersecurity ecosystem. [CyberCityAugusta]
## (https://cybercityaugusta.info/)
Georgia spent approximately **$107 million** on the statewide Dominion Voting Systems contract in 2019. HAVA Election Security grants
total approximately **$46.3 million** (per EAC OIG audit). [Eac](https://oig.eac.gov/reports/audit/audit-administration-help-america-vote-act-
grants-awarded-state-georgia) [U.S. Election Assistance Commission](https://www.eac.gov/sites/default/files/2024-
12/Georgia_G23GA0047_24_14_HAVA_Audit_Report.pdf) The state expects approximately **$9.8 million** from the IIJA-funded State &
Local Cybersecurity Grant Program. [Georgia](https://gta.georgia.gov/policies-and-programs/cybersecurity/state-and-local-cybersecurity-
grant-program) Cloudflare provides DDoS protection for election websites, successfully repelling a foreign cyberattack targeting the absentee
ballot request system in 2024. [Technijian](https://technijian.com/cyber-security/cyberattacks/georgia-election-officials-thwart-cyberattack-
from-foreign-country/)
### Physical security and polling place protections
Georgia operates a two-tier buffer zone under **O.C.G.A. § 21-2-414**: a **150-foot zone** from the outer edge of any building containing a
polling place, and a **25-foot zone** from any voter standing in line. [Justia](https://law.justia.com/codes/georgia/2010/title-21/chapter-
2/article-11/part-1/21-2-414) Violations are **misdemeanors**. [Justia](https://law.justia.com/codes/georgia/2020/title-21/chapter-
2/article-11/part-1/section-21-2-414/) Notably, **all firearms are prohibited within 150 feet** of any polling place during elections (**O.C.G.A.
§§ 21-2-413(i), 16-11-127(b)(7)**), except law enforcement and certified security. [Brennan Center for Justice]
(https://www.brennancenter.org/our-work/research-reports/georgia-protections-against-intimidation-voters-and-election-workers)
Political parties may designate up to **2 poll watchers per precinct** (**O.C.G.A. § 21-2-408(b)**). [Brennan Center for Justice]
(https://www.brennancenter.org/our-work/research-reports/georgia-election-observers-rules-and-constraints) Poll managers have explicit
statutory authority to remove disruptive watchers. [Brennan Center for Justice](https://www.brennancenter.org/our-work/research-
reports/law-georgia-voter-intimidation-poll-watchers-and-challengers) Voter intimidation through force or threats is a **felony** under
**O.C.G.A. § 21-2-567**, as is threatening or using violence against election officials (**O.C.G.A. § 21-2-566**). [Brennan Center for Justice]
(https://www.brennancenter.org/our-work/research-reports/law-georgia-voter-intimidation-poll-watchers-and-challengers)
### Legal strategies and constitutional protections
**Georgia is NOT part of the 19-state EO 14248 lawsuit.** AG Chris Carr (R) has instead defended SB 202 provisions across multiple federal
lawsuits. The DOJ's 2021 challenge to SB 202 was **dismissed March 31, 2025** at AG Bondi's direction. [Georgia Secretary of State]
(https://sos.ga.gov/news/doj-drops-lawsuit-against-georgia-raffenspergers-urging) [Just Security](https://www.justsecurity.org/113745/wjh-
trump-dismissal-voting-rights-lawsuits/) The landmark **Curling v. Raffensperger** case (challenging Dominion BMD constitutionality) was
**dismissed March 31, 2025** by Judge Totenberg for lack of standing [Georgia Recorder](https://georgiarecorder.com/2025/04/01/federal-
judge-dismisses-long-running-lawsuit-that-challenged-georgias-electronic-voting-machine-system/) after a 17-day bench trial, [Law360]
(https://www.law360.com/cases/598ddd501876504259000001/articles) [Georgiara](https://georgiara.com/2025/03/31/after-7-years-at-
trial-judge-dismisses-election-integrity-curling-case/) though the case helped prompt legislation (SB 189, HB 974) mandating QR code
elimination from ballot tabulation by **July 1, 2026**. [Georgiara](https://georgiara.com/2025/03/31/after-7-years-at-trial-judge-dismisses-
election-integrity-curling-case/) Funding for the estimated **$66 million** replacement of 33,000 ballot printers was NOT appropriated in the
2025 session. [AJC](https://www.ajc.com/politics/election-security-proposals-fall-short-in-georgia-before-2026-
midterms/BOFIX44GDVCJTHPBUVO6545NDE/)

Georgia's **Risk-Limiting Audits** [LegalClarity](https://legalclarity.org/what-is-the-curling-v-raffensperger-lawsuit/) use **Arlo** (open-
source software by VotingWorks) under **O.C.G.A. § 21-2-498**, with progressively tightening risk limits: 8% (2024), 6% (2026), 5% (2028+).
[Verified Voting](https://verifiedvoting.org/auditlaw/georgia/)
### Key contacts
- **SOS Elections Division**: 2 MLK Jr. Drive SE, West Tower, Atlanta, GA 30334; sos.ga.gov
- **COO**: Gabriel Sterling
- **GTA Cybersecurity**: gta.georgia.gov/cybersecurity
- **AG Chris Carr**: law.georgia.gov
- **ACCG**: accg.org
## ---
## Arizona: Active litigation landscape and emerging cyber threats
### State election authority and legal framework
Secretary of State **Adrian Fontes** (D, inaugurated January 2023) serves as Arizona's chief election officer, responsible for certifying results
(**A.R.S. § 16-648, § 16-662**), maintaining the statewide voter database AVID (**A.R.S. § 16-168**), and certifying election equipment
[Citizens Clean Elections Commission](https://azcleanelections.gov/en/election-security/how-elections-work) via the Equipment Certification
Advisory Committee (**A.R.S. § 16-442**).
The **Elections Procedures Manual (EPM)** (**A.R.S. § 16-452**) is Arizona's distinctive rulemaking mechanism—the SOS prescribes rules
for "maximum degree of correctness, impartiality, uniformity and efficiency," issued by December 31 of each odd-numbered year with
Governor and AG approval. [Arizona Legislature +2](https://www.azleg.gov/ars/16/00452.htm) The Arizona Supreme Court unanimously
ruled in 2025 that the APA does not apply to the EPM. [Arizona Secretary of State](https://azsos.gov/news/989) [Arizona Secretary of State]
(https://azsos.gov/about/media-center/press-releases) Violation of EPM rules is a **Class 2 misdemeanor**. [LawServer]
## (https://www.lawserver.com/law/state/arizona/az-laws/arizona_laws_16-452)
Arizona's decentralized system across **15 counties** splits election authority between **Boards of Supervisors** (determine polling places,
approve budgets, certify results), **County Recorders** (voter registration, early voting, signature verification), and **Election Directors**
(polling place operations, tabulation). **Maricopa County** (2.6 million registered voters, [Maricopa County]
(https://www.maricopa.gov/6327/Maricopa-County-Tabulation-Election-Cent) 4th-largest county nationally) budgeted approximately **$28
million** for 2024 elections [CNN](https://amp.cnn.com/cnn/2024/09/21/politics/election-security-funds-decline-threats-grow-invs) and
hires approximately **3,000 temporary workers** per election.
Arizona's **Article II, § 21** contains a robust Free and Equal Elections Clause: "no power, civil or military, shall at any time interfere to
prevent the free exercise of the right of suffrage." [States United Democracy Center](https://statesunited.org/wp-
content/uploads/2022/08/2022-06-01-Secretarys-Combined-Resp-to-PI-MTD.pdf)
### Cybersecurity infrastructure
**Arizona Cyber Command**, established July 2021 within AZDOHS, functions as the statewide information security and privacy office with a
**Security Operations Center** providing 24/7 monitoring, detection, analysis, and incident response. The AZDOHS 2025–2029 Strategic Plan
prioritizes establishing **Regional Security Operations Centers (RSOCs)** by June 2029— [Azdohs](https://azdohs.gov/file/5291/download?
token=RPFY_R42) the first launched at Pima Community College in October 2025 in partnership with the University of Arizona. [University of
Arizona](https://infosci.arizona.edu/news/arizona-cybersecurity-academy-pcc-rsoc-opening)
The **AVID (Arizona Voter Information Database)** is hosted on **Microsoft Azure Government Cloud** with always-on DDoS protection,
advanced SQL injection detection, TLS encryption, [Arizona](https://www.arizona.vote/secure_elections) multi-factor authentication, [Citizens
Clean Elections Commission](https://www.azcleanelections.gov/election-security/elections-and-cybersecurity) and **NIST SP 800-53 Rev.
5** security controls. Secretary Fontes's office established Arizona's first dedicated **Election Cybersecurity Unit** and **CISO** role.
[Arizona Secretary of State](https://azsos.gov/news/981)
Arizona experienced real threats in 2025: an **Iranian-linked cyberattack** in June replaced candidate headshots with an image of Ayatollah
Khomeini on the Candidate Portal, [Arizona Secretary of State](https://azsos.gov/news/981) and a July attack targeted the SOS website.
Both were detected and contained. [Arizona Secretary of State](https://azsos.gov/news/959)
Fontes has requested **$9.4 million** in one-time cybersecurity infrastructure funding and **$3.77 million** in ongoing operational support
for FY2027. [Arizona Secretary of State](https://azsos.gov/news/981) Arizona's **unobligated HAVA balance** stands at **$4,109,508** with
total federal HAVA funds authorized at **$19,570,974**. [eac](https://www.eac.gov/sites/default/files/2025-
07/AZ_ES_2024_Annual_FFR.pdf)
### Physical security and polling place protections
**A.R.S. § 16-515** establishes a **75-foot buffer zone** around every voting location. [Arizona Secretary of State]
(https://azsos.gov/elections/about-elections/guidance-voting-location-conduct) [Arizona Courts]
(https://www.azcourts.gov/Portals/0/201/ASC-CV220048%20-%203-9-2022%20-%20FILED%20-
%20AMICUS%20CURIAE%20BRIEF%20OF%20KARI%20LAKE%20SUPPORTING%20APPLICATION%20FOR%20ISSUANCE%20OF%20WRIT%20UNDER%20EXERCISE%20OF%20OR
Arizona is notable for its **explicit firearms prohibition at polling places**: **A.R.S. § 13-3102(A)(11)** makes it **misconduct involving
weapons** to enter an election polling place carrying a deadly weapon on Election Day, [Arizona]
(https://www.arizona.vote/sites/default/files/docs/Voter_Intimidation_Prevention_Guide.pdf) with exceptions only for on-duty military and
peace officers. [Brennan Center for Justice](https://www.brennancenter.org/our-work/research-reports/arizona-protections-against-

intimidation-voters-and-election-workers) [Arizona Secretary of State](https://azsos.gov/sites/default/files/docs/2024-
10_AZSOS_Guidance_Polling_Place_Voter_Intimidation_FINAL_REV20241029.pdf)
Voter intimidation under **A.R.S. § 16-1013** (using force, violence, or threats to compel voting behavior) is a **Class 1 misdemeanor**.
[Arizona Legislature](https://www.azleg.gov/ars/16/01013.htm) [Onecle](https://law.onecle.com/arizona/title-16/16-1013.html) More
serious acts—using corrupt means to change votes (**A.R.S. § 16-1006**)—constitute a **Class 5 felony**. [Civicplus]
(https://content.civicplus.com/api/assets/d645e415-9d28-40bf-a878-ca4ba7822430) Interference with election officers (**A.R.S. § 16-
1004**) is also a **felony**. [Campaign Legal Center](https://campaignlegal.org/sites/default/files/2020-10/IntimidationMemo-AZ-r2.pdf)
The **Citizens Clean Elections Commission** (established by voter-approved initiative, A.R.S. Title 16, Chapter 6, Article 2) provides
comprehensive voter education and election transparency resources, though it does not directly administer elections.
### Legal strategies and constitutional protections
**Arizona IS part of the 19-state lawsuit** against EO 14248, [Connecticut DMV](https://portal.ct.gov/ag/press-releases/2025-press-
releases/lawsuit-over-unlawful-executive-order-seeking-to-impose-sweeping-voting-restrictions) with AG Kris Mayes joining [Votebeat]
(https://www.votebeat.org/2025/04/03/democratic-attorneys-general-sue-trump-executive-order-elections/) on April 3, 2025. [Arizona
Attorney General +3](https://www.azag.gov/press-release/attorney-general-mayes-and-secretary-state-fontes-join-multistate-lawsuit-against)
Arizona has an active litigation landscape including the fake electors indictment (AG Mayes obtained grand jury indictments of 11 "fake
electors" plus 7 others including Mark Meadows and Rudy Giuliani), [AZFamily](https://www.azfamily.com/2024/04/24/arizona-ag-kris-
mayes-announces-indictment-11-fake-electors-heres-what-we-know/) complex proof-of-citizenship litigation (9th Circuit struck down
portions of AZ laws as "unlawful voter suppression" in February 2025), and EPM challenges that reached the Arizona Supreme Court.
The AG's **Election Integrity Unit** handles election complaints, and **A.R.S. § 16-1021** authorizes both the AG and county attorneys to
enforce election laws through civil and criminal actions. [Arizona Legislature](https://www.azleg.gov/arsDetail/?title=16) [Brennan Center for
Justice](https://www.brennancenter.org/our-work/research-reports/arizona-election-certification-processes-and-guardrails) Citizens have
access to **mandamus** under **A.R.S. § 12-2021** to compel public officials to perform legally imposed duties. [Brennan Center for
Justice](https://www.brennancenter.org/our-work/research-reports/arizona-election-certification-processes-and-guardrails)
### Key contacts
- **SOS Elections Division**: (602) 542-8683; azsos.gov
- **Voter Hotline**: 1-877-THE-VOTE (1-877-843-8683)
- **AZDOHS/Cyber Command**: azdohs.gov/cyber
- **AG Election Integrity Unit**: azag.gov/criminal/eiu
- **SOS Grants Manager**: Gatjeak Gew, ggew@azsos.gov, (602) 320-3431 [eac](https://www.eac.gov/sites/default/files/2025-
07/AZ_ES_2024_Annual_FFR.pdf)
## ---
## Nevada: Massive voter database modernization and co-leading EO litigation
### State election authority and legal framework
Secretary of State **Cisco Aguilar** oversees elections [City Cast Las Vegas](https://lasvegas.citycast.fm/3-questions/nevada-secretary-of-
state-cisco-aguilar-election-security) under **NRS § 293.247** (rulemaking authority for all elections), [Public]
(https://nevada.public.law/statutes/nrs_293.247) **NRS § 293.250** (prescribing election computer systems and ballot forms), [Public]
(https://nevada.public.law/statutes/nrs_293.250) and **NRS § 293B.1045** (voting system approval). [Public]
(https://nevada.public.law/statutes/nrs_293b.1045) The Elections Division operates at 101 N. Carson Street, Suite 3, Carson City.
Nevada's **Article 2, Section 1A** (added in 2020 via Question 4) enshrines a **Voters' Bill of Rights** in the constitution, including the right
to vote without intimidation, the right to have complaints resolved fairly, and the right to vote if in line when polls close. [Justia]
(https://law.justia.com/codes/nevada/2020/chapter-293/statute-293-2546/) **AB 321 (2021)** established permanent universal mail voting,
requiring clerks to send every active registered voter a mail ballot [BillTrack50](https://www.billtrack50.com/billdetail/1348534) with
standardized signature verification processes [KTNV-TV](https://www.ktnv.com/news/universal-mail-voting-could-become-permanent-in-
nevada-elections-with-new-bill) and ballot drop boxes at every polling location. [BillTrack50](https://www.billtrack50.com/billdetail/1348534)
**Question 7 (2024)**, approved by 73.7%, would require voter ID but must pass again in **2026** to take effect. [Review Journal]
(https://www.reviewjournal.com/news/politics-and-government/nevada/voters-pass-voter-id-reject-ranked-choice-3207699/)
Nevada's 17 county clerks manage local election administration, [City Cast Las Vegas](https://lasvegas.citycast.fm/3-questions/nevada-
secretary-of-state-cisco-aguilar-election-security) with **Clark County** (registrar Lorena S. Portillo, [U.S. Vote Foundation]
(https://www.usvotefoundation.org/clark-county-nv-election-office) ~70% of NV voters) [Government Technology]
(https://www.govtech.com/elections/nevada-debuts-unified-voter-registration-election-management) and **Washoe County** handling the
vast majority of the electorate.
### Cybersecurity infrastructure
The **Office of Information Security & Cyber Defense (OISCD)**, successor to the Office of Cyber Defense Coordination [Government
Technology](https://www.govtech.com/security/nevada-creates-new-cybersecurity-office-names-its-leader) created by **AB 471 (2017)**,
[Government Technology](https://www.govtech.com/policy/nevada-governor-signs-bill-to-create-office-of-cyber-defense-coordination.html)
operates under the Governor's Technology Office [Nv](https://it.nv.gov/Organization/Nevada_Office_of_Cyber_Defense_Coordination/) with
Deputy Director **Adam Miller** (formerly Senior Policy Adviser to the Principal Cyber Advisor to the Secretary of the Army). [Govtech]
(https://events.govtech.com/Nevada-Public-Sector-Cybersecurity-Summit-2025) The office is building a statewide SOC supporting a **whole-
of-state approach** to cybersecurity [Govtech](https://events.govtech.com/Nevada-Public-Sector-Cybersecurity-Summit-2025) with zero-
trust principles. [Government Technology](https://www.govtech.com/security/nevada-creates-new-cybersecurity-office-names-its-leader)

Nevada's **VREMS (Voter Registration and Election Management Solution)** represents the state's largest election technology investment at
approximately **$57 million total** ($30 million initial [Government Technology](https://www.govtech.com/elections/nevada-debuts-unified-
voter-registration-election-management) + $27 million for Clark County integration and security enhancements). [The Nevada Independent]
(https://thenevadaindependent.com/article/nevadas-election-system-stayed-up-during-massive-statewide-cyberattack-heres-why) The
centralized, top-down system replaced the previous bottom-up county approach, [U.S. Election Assistance Commission]
(https://www.eac.gov/sites/default/files/paymentgrants/Election%20Security/narrative2023/NV_2023_ES_State_Narrative_Budget.pdf) with
all 17 counties integrated before the 2024 general election. [The Nevada Independent](https://thenevadaindependent.com/article/nevadas-
election-system-stayed-up-during-massive-statewide-cyberattack-heres-why) VREMS is isolated from other state systems—during the
**August 2025 statewide cyberattack** that took down DMV and other services for over a week, VREMS was completely unaffected. [Nevada
Current](https://nevadacurrent.com/2025/10/20/nevadas-recent-cyber-attack-shows-the-importance-of-shoring-up-security-for-election-
systems/)
**Albert Sensors** (intrusion detection systems) have been purchased for all counties using HAVA funds. [U.S. Election Assistance
Commission](https://www.eac.gov/blogs/women-elections-barbara-cegavske-nevada-secretary-state) HAVA-funded staff includes **4 full-
time positions** and **3 contractor positions** for cybersecurity. [U.S. Election Assistance Commission]
(https://www.eac.gov/sites/default/files/paymentgrants/narrative2022/NV_2022_ES_State_Narrative_Budget.pdf) [U.S. Election Assistance
## Commission]
(https://www.eac.gov/sites/default/files/paymentgrants/Election%20Security/narrative2023/NV_2023_ES_State_Narrative_Budget.pdf)
The Nevada National Guard maintains the **422nd Expeditionary Signal Battalion** and a **Defensive Cyber Operations Element (DCOE)**
under LTC Johnson (CIO for the Nevada Army National Guard). [Govtech](https://events.govtech.com/Nevada-Public-Sector-Cybersecurity-
## Summit-2025)
### Physical security and polling place protections
**NRS § 293.740** establishes a **100-foot buffer zone** from the entrance of any voting location, with violations classified as a **gross
misdemeanor**. [Public](https://nevada.public.law/statutes/nrs_293.740) County clerks must post visible signs at least 17" × 11" marking
the boundary. [Safeelections](https://safeelections.org/wp-content/uploads/2025/03/CSSE-NV-Pocket-Guide-2026.pdf) [safeelections]
(https://safeelections.org/wp-content/uploads/2025/03/CSSE-NV-Pocket-Guide-2026.pdf)
**Nevada has NO specific statute prohibiting firearms at polling places**, [GIFFORDS](https://giffords.org/lawcenter/state-laws/location-
restrictions-in-nevada/) though school-located polling places are covered by **NRS § 202.265** (firearms on school property). [TheGunZone]
(https://thegunzone.com/can-you-have-a-firearm-at-polling-places-in-nevada/) Even without a specific ban, carrying visible firearms near
polling locations may constitute unlawful intimidation under **NRS § 293.710**. [brennancenter +2](https://www.brennancenter.org/our-
work/research-reports/nevada-protections-against-intimidation-voters-and-election-workers)
Voter intimidation is a **Category E felony** (**NRS § 293.710**), [Public](https://nevada.public.law/statutes/nrs_293.710) punishable by 1–
4 years prison and fines up to $5,000. [Safeelections](https://safeelections.org/wp-content/uploads/2025/03/CSSE-NV-Pocket-Guide-
2026.pdf) Interfering with elections (**NRS § 293.730**), [Public](https://nevada.public.law/statutes/nrs_293.710) including remaining at
polling places to interfere or setting up unauthorized ballot drop boxes, is also a **Category E felony**. Tampering with election equipment
[Public](https://nevada.public.law/statutes/nrs_293.710) with intent to influence outcomes is a **Category B felony** (**NRS § 293.755**).
[safeelections](https://safeelections.org/wp-content/uploads/2025/03/CSSE-NV-Pocket-Guide-2026.pdf) Civil penalties reach **up to
$20,000** per violation (**NRS § 293.840**). [Clarkcountynv]
(https://files.clarkcountynv.gov/government/departments/elections/services/voter_registration/reg-drive.php)
Election official protections are particularly strong: disseminating personal identifying information of election officials without consent, where
it could cause harm, is a **Category E felony** (**NRS § 293.705(3)**). [brennancenter](https://www.brennancenter.org/our-work/research-
reports/nevada-protections-against-intimidation-voters-and-election-workers) [safeelections](https://safeelections.org/wp-
content/uploads/2025/03/CSSE-NV-Pocket-Guide-2026.pdf)
### Legal strategies and constitutional protections
**Nevada is CO-LEADING the 19-state lawsuit** against EO 14248 alongside California, [Connecticut DMV](https://portal.ct.gov/ag/press-
releases/2025-press-releases/lawsuit-over-unlawful-executive-order-seeking-to-impose-sweeping-voting-restrictions) [Votebeat]
(https://www.votebeat.org/2025/04/03/democratic-attorneys-general-sue-trump-executive-order-elections/) with AG Aaron Ford serving as a
principal litigant. [News3LV +2](https://news3lv.com/news/local/nevada-california-lead-lawsuit-against-trump-order-on-election-
administration) SOS Aguilar stated: "The United States Constitution is clear: states have primary responsibility for the administration of
elections." [KOLO](https://www.kolotv.com/2025/04/03/ford-aguilar-announce-lawsuit-against-trump-over-election-order/) Federal judges
have paused parts of the order while the case proceeds. [Hoodline +2](https://hoodline.com/2026/02/nevada-ag-to-trump-our-ballots-our-
rules/)
### Key contacts
- **SOS Elections Division**: (775) 684-5705; [Touro](https://tun.touro.edu/admissions--aid/financial-aid/voter-registration/)
nvelect@sos.nv.gov
- **Clark County Elections**: (702) 455-VOTE (8683); [Clarkcountynv]
(https://files.clarkcountynv.gov/government/departments/elections/services/voter_registration/reg-drive.php) ELinfo@ClarkCountyNV.gov
[Clark County](https://www.clarkcountynv.gov/government/departments/elections/services/voter_registration/reg-ways)
- **OISCD**: Through Governor's Technology Office (it.nv.gov)
- **AG Aaron Ford**: ag.nv.gov
- **All Voting is Local Nevada Director**: Kerry Durmick, Kerry@AllVotingisLocal.org
## ---

## North Carolina: Institutional upheaval and national cybersecurity leadership
### State election authority and legal framework
North Carolina uniquely uses a **Board model** rather than a Secretary of State for elections. The **NC State Board of Elections (NCSBE)**
operates under **N.C.G.S. Chapter 163, Article 3** with 5 bipartisan members. In a major 2024 shift, **SB 382** transferred appointment
authority from the Governor to the **State Auditor**, fundamentally altering the board's political dynamics. [Carolina Journal -]
(https://www.carolinajournal.com/boliek-appointments-to-the-state-election-board-mark-a-shift-in-power/)
The current board, appointed in May 2025 by State Auditor Dave Boliek, includes Chairman **Francis X. De Luca** (former Civitas Institute
president, retired USMC Colonel) [NCSBE](https://www.ncsbe.gov/about) and four other members with a conservative tilt. Executive Director
**Sam Hayes** (attorney, former general counsel to Speaker of the NC House) started May 15, 2025. [NCSBE](https://www.ncsbe.gov/about)
The board's powers under **N.C.G.S. § 163-22** include general supervision over all primaries and elections, [North Carolina General
Assembly](https://ncleg.gov/enactedlegislation/statutes/html/bysection/chapter_163/gs_163-22.html) rulemaking authority, power to
compel county board compliance, [North Carolina General Assembly]
(https://ncleg.gov/enactedlegislation/statutes/html/bysection/chapter_163/gs_163-22.html) and notably, the board is **constituted as an
inferior court** with power to commit persons to jail for up to 30 days for disobedience (**§ 163-24**). [North Carolina General Assembly]
(https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_163/Article_3.pdf) Emergency powers under **§ 163-27.1**
allow the Executive Director to modify election schedules during natural disasters, extreme weather, or armed conflict. [North Carolina
General Assembly](https://www.ncleg.net/enactedlegislation/statutes/html/bychapter/chapter_163.html)
**S.L. 2023-140 (SB 747)** implemented **photo voter ID** requirements (**§ 163-166.16**), overhauled observer rules, and modified
absentee ballot deadlines. [NCSBE](https://www.ncsbe.gov/news/press-releases/2024/02/27/some-election-results-will-be-reported-later-
usual-due-state-law-changes) North Carolina's 100 county boards of elections (**§ 163-30**) each have 3 members appointed by the State
Board. [North Carolina General Assembly](https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter163)
### Cybersecurity infrastructure
North Carolina is **nationally recognized as a leader** in whole-of-state cybersecurity. **NCDIT** operates the State SOC, and the **Joint
Cybersecurity Task Force (JCTF)**, established by Governor Cooper's March 2022 executive order, combines NCDIT, NC Emergency
Management, NC National Guard [NC DPS](https://www.ncdps.gov/news/press-releases/2022/03/16/governor-cooper-signs-executive-
order-establishing-state-north-carolina-joint-cybersecurity-task) Cyber Security Response Force (CSRF), and the NCLGISA Cybersecurity Strike
Team. [NASCIO](https://www.nascio.org/wp-content/uploads/2021/08/NC-JCTF-NASCIO-Nomination-2021-Cyber.pdf) The **Joint
Cybersecurity Mission Center (JCMC)** at the State Emergency Operations Center coordinates all operational response. [NC DPS]
(https://www.ncdps.gov/media/14096/open) NASCIO described the JCTF as "one of only a few in the nation" offering this collaborative
approach. [NASCIO](https://www.nascio.org/wp-content/uploads/2021/08/NC-JCTF-NASCIO-Nomination-2021-Cyber.pdf)
The **NC Cyber Security Response Force (CSRF)** has supported the State Board of Elections through **5+ election cycles** as of 2020,
monitoring security systems, identifying and stopping malicious activity on state and county networks. [NC DPS]
(https://www.ncdps.gov/news/press-releases/2020/11/04/nc-national-guard-cyber-security-response-force-helps-secure) **N.C.G.S. § 143B-
1379** requires all local government entities to report cyber incidents within **24 hours**. [North Carolina Department of Information
Technology](https://it.nc.gov/programs/cybersecurity-risk-management/cyber-incident-reporting)
HAVA Election Security grants to NC total approximately **$32.9 million** (FY2018 + FY2020 + CARES combined). [U.S. Election Assistance
Commission](https://www.eac.gov/sites/default/files/2024-12/NorthCarolina_G22NC0004_24_06_HAVA_Audit.pdf) A notable requirement:
voting system vendors must post a **$17.01 million bond or letter of credit**. [NCSBE](https://www.ncsbe.gov/voting/voting-technology)
In 2025, the DOJ sued North Carolina (**United States v. NC State Board of Elections**, 5:25-cv-00283, E.D.N.C.) alleging 200,000+ voter
records lacked required identification numbers under HAVA § 303(a). [Civil Rights Litigation Clearinghouse]
(https://clearinghouse.net/case/46639/) A **settlement was approved September 8, 2025**, launching the "Registration Repair Project."
### Physical security and polling place protections
**N.C.G.S. § 163-166.4** establishes buffer zones of **25 to 50 feet** from the entrance door, with county boards setting the exact distance.
[North Carolina General Assembly](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_163/GS_163-166.4.html)
County boards [Justia](https://law.justia.com/codes/north-carolina/chapter-163/article-14a/section-163-166-4/) must publish the specific
measurement and area for lawful electioneering at least 30 days before each election. Notably, there is **no specific statutory penalty** for
violating the buffer zone rule per UNC School of Government analysis.
North Carolina uses "**observers**" (not watchers or challengers). Under **§ 163- [NCSBE]
(https://www.ncsbe.gov/blog/2023/12/13/numbered-memo-2023-06-election-observers) 45.1** (enacted by S.L. 2023-140), observers must
be registered voters in the county, present credentials, and comply with conduct restrictions including no voter interaction, no photography of
voters, and no standing close enough to see votes. Chief judges may challenge appointments for good cause; **§ 163-48** authorizes
officials to "prevent and stop improper practices and attempts to obstruct, intimidate, or interfere."
There is **no Chapter 163 prohibition on firearms at polling places**, though **N.C.G.S. § 14-269.2** prohibits firearms on educational
property where many polling places are located.
Voter intimidation is categorized as both a **Class 2 misdemeanor** (§ 163-274, for interference with voters, boisterous conduct) and a
**Class I felony** (§ 163-275(10)–(11), (17), for intimidating voters, election officials, or misrepresenting the law to discourage voting).
### Legal strategies and constitutional protections

**North Carolina is NOT part of the 19-state EO 14248 lawsuit.** Instead, NC was a **target** of DOJ action under the EO. AG Jeff Jackson's
authority has been **significantly restricted** by SB 382, which blocks him from taking legal stances that would invalidate NC law and
requires deference to the General Assembly's lawyers in certain cases. Jackson's office has nonetheless joined 18 lawsuits against the
Trump administration in 2025.
Active litigation includes **Cooper v. Berger/Boliek** (Governor Stein's challenge to SB 382's restructuring of election board appointments)
and the legacy of **Harper v. Hall** (redistricting). ES&S systems are used in **93 of 100 counties**, with Hart InterCivic in the remaining 7.
### Key contacts
- **NCSBE**: (919) 814-0700; elections.sboe@ncsbe.gov; 430 N. Salisbury St., Raleigh
- **NCDIT Cyber Incident Reporting**: it.nc.gov/programs/cybersecurity-risk-management/cyber-incident-reporting
- **NC CSRF**: csrf.nc.gov
- **AG Jeff Jackson**: ncdoj.gov
- **Federal Partners**: CISA (844-729-2472); FBI CyWatch (855-292-3937)
## ---
## Cross-state comparison reveals critical patterns
Several findings emerge from examining all six states together that should inform the development of state-specific election security guides.
**EO 14248 litigation divides along partisan AG lines.** Michigan, Arizona, and Nevada (all with Democratic AGs) joined the 19-state lawsuit.
Pennsylvania (Republican Secretary appointed by Democratic Governor), Georgia (Republican AG), and North Carolina (Democratic AG with
restricted authority) did not. The litigation status shapes each state's relationship with federal election mandates and should be factored into
any advocacy strategy.
**Cybersecurity maturity varies dramatically.** North Carolina's JCTF represents the gold standard for whole-of-state election cybersecurity
coordination. Georgia's $100 million Cyber Center in Augusta provides unmatched physical infrastructure. Michigan's constitutional mandate
for state-funded election security measures provides the strongest legal foundation for cybersecurity investment. Nevada's $57 million
VREMS modernization is the largest single voter registration technology investment. Pennsylvania's aging SURE system represents the most
critical vulnerability among the six states.
**Buffer zones and firearms rules differ significantly across states.** Georgia (150-foot zone with firearms ban) and Arizona (75-foot zone
with weapons misconduct statute) offer the strongest combined protections. Pennsylvania's 100-foot police exclusion zone is unique in
restricting law enforcement rather than voters. Nevada and North Carolina lack specific polling-place firearms prohibitions.
**Citizen enforcement mechanisms range from transformative to minimal.** Michigan's constitutional private right of action with mandatory
fee-shifting is the most powerful tool available to voters in any of these states. Arizona's mandamus provisions and Nevada's $20,000 civil
penalties per violation provide meaningful but narrower pathways. Pennsylvania, Georgia, and North Carolina offer primarily criminal
enforcement channels rather than direct citizen action.
The **termination of EI-ISAC** following CISA's $10 million funding cut impacts all six states and represents a shared vulnerability that any
election security guide should address prominently. States are now operating without the centralized threat intelligence sharing, real-time
monitoring, and rapid incident notification that EI-ISAC provided during the 2024 election cycle.