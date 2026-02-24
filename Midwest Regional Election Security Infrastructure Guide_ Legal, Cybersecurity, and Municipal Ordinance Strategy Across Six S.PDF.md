\# Midwest Regional Election Security Infrastructure Guide

\*\*Five of six states in this Midwest batch lack any explicit
prohibition on ﬁrearms at polling places, and all ﬁve are constitutional
carry states — making this region the highest-priority target nationally
for municipal ordinance campaigns enforcing 18 U.S.C. § 592.\*\* Only
Illinois joined the 19-state lawsuit against Executive Order 14248, and
only Nebraska maintains a partial concealed-carry prohibition at polls.
The region's cybersecurity posture ranges from nationally leading (Ohio,
Illinois) to resource-constrained (Nebraska, Kansas), and the impending
loss of CISA and EI-ISAC support threatens to widen that gap. This guide
provides the detailed legal, technical, and strategic foundation needed
for Protections for Elections to pursue municipal ordinance strategies
across Kansas, Nebraska, Iowa, Illinois, Ohio, and Indiana.

---

\## Kansas: Constitutional carry and zero polling place protections

\### State election authority and legal framework

Kansas election administration is centralized under \*\*Secretary of
State Scott Schwab (R)\*\*, who serves as chief elections oﬃcer with
authority derived from Article 1 of the Kansas Constitution and K.S.A.
Chapter 25. The SOS was granted independent prosecutorial power over
voter fraud in 2015. Kansas has 105 counties, each with a county
election oﬃcer; in the four largest counties (Johnson, Sedgwick,
Shawnee, Wyandotte), the SOS appoints election commissioners directly.

Key statutes governing elections include K.S.A. 25-2301 et seq. (voter
registration), K.S.A. 25-2430 (electioneering buffer zone), K.S.A.
25-2415 (voter intimidation), K.S.A. 25-3005a (poll agents), K.S.A.
25-4401–25-4416 (Electronic and Electromechanical Voting Systems Act),
and K.S.A. 25-3009 (post-election audits). Major reform came through
\*\*HB 2138 (2022)\*\*, which mandated voter-veriﬁed paper ballots with
distinctive watermarks effective January 1, 2024, prohibited
internet-connected voting equipment, and expanded post-election audits.
\[Kansas Secretary of
State\](https://sos.ks.gov/media-center/media-releases/2022/04-26-22-kansas-legislature-passes-bill-to-strengthen-election-integrity-in-kansas.html)
\[Kansas Secretary of
State\](https://sos.ks.gov/elections/did-you-know.html) Kansas now uses
hand-marked paper ballots with ES&S DS200 optical scanners in most
counties, with ExpressVote ballot marking devices for ADA accessibility.

Kansas's home rule framework provides \*\*constitutional home rule for
cities\*\* under Article 12, Section 5, with ordinances entitled to a
presumption of validity. Counties have statutory home rule under K.S.A.
19-101a, but this provision \*\*explicitly subjects counties to all
state election legislation\*\* (§19-101a(a)(6)). State ﬁrearms
preemption under K.S.A. 75-7c20 poses the greatest barrier to municipal
polling place ordinances: local governments cannot broadly prohibit
ﬁrearms in public buildings without providing metal detectors and armed
guards at all public entrances.

\### Cybersecurity infrastructure

The Kansas Information Security Oﬃce (KISO), created by the Kansas
Cybersecurity Act (House Sub. for SB 56, 2018), operates within the Oﬃce
of Information Technology Services.
\[KLRD\](https://klrd.gov/publications/brieﬁng-book-2021/cybersecurity/)
A critical structural gap exists: the Act's deﬁnition of "executive
branch agency" \*\*excludes elected oﬃces including the Secretary of
State\*\*, meaning election infrastructure falls outside mandatory KISO
oversight. The Kansas Cybersecurity Task Force, created by Governor
Kelly in 2021, provides cross-sector collaboration including the Kansas
Intelligence Fusion Center Director.

Kansas joined MS-ISAC in June 2012 and EI-ISAC in April 2018.
\[Kslegresearch\](https://www.kslegresearch.org/KLRD-web/Publications/StateLocalGovt/2018-08-08-ElectionSecurityKansas.pdf)
HAVA funding totals approximately \*\*\$10.3 million in election
security grants (2018–2025)\*\*,
\[Kslegresearch\](https://www.kslegresearch.org/KLRD-web/Publications/ElectionsEthics/memo_genl_pratt_hava.pdf)
with the 2018 allocation at \$4,383,595. \[Kslegresearch\]
(https://www.kslegresearch.org/KLRD-web/Publications/StateLocalGovt/2018-08-08-ElectionSecurityKansas.pdf)
Kansas law explicitly directs KISO to coordinate with CISA for annual
audits (K.S.A. 75-7239(c)(5)), creating a \*\*statutory gap\*\* if CISA
services are defunded. Current spending allocates approximately 90% to
cybersecurity initiatives, including monitoring cyber threats against
local election oﬃces. \[Issue
One\](https://issueone.org/articles/federal-funding-for-american-elections-hava-grants/)

\### Physical security and polling place protections

Kansas maintains one of the nation's largest electioneering buffer zones
at \*\*250 feet\*\* (K.S.A. 25-2430), upheld as constitutional in
\*Clark et al. v. Schwab and Metsker\* (D. Kan., 2020).
\[KMUW\](https://www.kmuw.org/politics/2020-10-09/judge-rules-kansas-polling-site-buffer-zone-constitutional)
However, \*\*Kansas has no statutory prohibition on ﬁrearms at polling
places.\*\* \[Movement Advancement Project\]
(https://www.lgbtmap.org/img/maps/citations-guns-in-polling-places.pdf)
As a constitutional carry state since 2015, open carry is legal for
anyone 18+ and concealed carry legal without a permit for anyone 21+.
\[USCCA\]
(https://www.usconcealedcarry.com/resources/ccw_reciprocity_map/ks-gun-laws/)
Even at school polling places, K.S.A. 21-6301(j)(4) permits voters to
keep ﬁrearms in vehicles.
\[FindLaw\](https://codes.ﬁndlaw.com/ks/chapter-21-crimes-and-punishments/ks-st-sect-21-6301/)
\[ATF\](https://www.atf.gov/ﬁrearms/docs/guide/kansas-ﬁrearms-statutes-and-codes/download)
A 2013 AG advisory opinion conﬁrmed that concealed and open carry remain
permitted at publicly owned polling places unless building-speciﬁc
security measures are implemented.
\[KCUR\](https://www.kcur.org/politics-elections-and-government/2016-11-01/are-you-ready-to-vote-in-kansas-or-missouri-

heres-your-checklist) "No weapons" signs carry no criminal penalty;
violators can only be asked to leave. \[Criminal Defense Lawyer\]
(https://www.criminaldefenselawyer.com/resources/weapons-charges-kansas.htm)

Poll watchers ("authorized poll agents") under K.S.A. 25-3005a must be
appointed in writing, wear OBSERVER badges in 32-point type, and are
limited to one per entity per voting place. \[Kansas
Revisor\](https://ksrevisor.gov/statutes/chapters/ch25/025_030_0005a.html)
Voter intimidation is a \*\*severity level 7, nonperson felony\*\* under
K.S.A. 25-2415.
\[Justia\](https://law.justia.com/codes/kansas/2015/chapter-25/article-24/section-25-2415/)
No speciﬁc anti-paramilitary statute exists.

\### Legal strategies

Kansas \*\*did not join\*\* the 19-state EO 14248 lawsuit. \*\*AG Kris
Kobach (R)\*\*, who took oﬃce in January 2023, \[Ballotpedia\]
(https://ballotpedia.org/Kris_Kobach) has focused on voter fraud
prosecution rather than voter protection. \[NBC News\]
(https://www.nbcnews.com/politics/2022-election/kris-kobach-voter-fraud-crusader-wins-kansas-attorney-general-race-rcna56623)
Federal private rights of action under 42 U.S.C. § 1983 and § 1985(3)
are available, alongside the HAVA administrative complaint procedure
(K.S.A. 25-4701–25-4716).

\### Key contacts

\- \*\*Secretary of State\*\*: 800-262-VOTE (8683); sos.ks.gov -
\*\*Attorney General\*\*: (785) 296-2215; ag.ks.gov

\- \*\*KISO\*\*: (785) 296-4999 or 1-833-765-2001
\[Ks\](https://www.ebit.ks.gov/security/information-security-oﬃce) -
\*\*Division of Emergency Management\*\*: (785) 274-1401

---

\## Nebraska: Partial polling place ﬁrearms ban amid constitutional
carry

\### State election authority and legal framework

\*\*Secretary of State Bob Evnen (R)\*\* oversees elections as chief
election oﬃcer, \[Ballotpedia\]
(https://ballotpedia.org/Nebraska_Secretary_of_State) administering
elections through 93 counties with election commissioners in counties
over 100,000 population and county clerks elsewhere. \[Nebraska
Legislature\](https://nebraskalegislature.gov/laws/laws-index/chap32-full.html)
Nebraska's election code spans Neb. Rev. Stat. §§ 32-101 to 32-1552.
\[Nebraska Legislature\]
(https://www.nebraskalegislature.gov/laws/statutes.php?statute=32-101)
The unicameral legislature — the only one in the nation — simpliﬁes
election law passage by eliminating bicameral negotiations, though a
ﬁlibuster system requires 33 votes for cloture. \[Nebraska
Examiner\](https://nebraskaexaminer.com/2023/03/28/permitless-concealed-carry-of-handguns-in-nebraska-advances-to-ﬁnal-round-debate/)

Nebraska uses \*\*hand-marked paper ballots with optical scan tabulation
statewide\*\* from ES&S. DRE machines are explicitly prohibited: §
32-1041(2) states "No electronic voting system shall be used under the
Election Act." \[Nebraska Secretary of State\]
(https://sos.nebraska.gov/nebraska-election-security) \[Nebraska
Legislature\](https://nebraskalegislature.gov/laws/statutes.php?statute=32-1041)
Post-election audits, while discretionary, are regularly conducted
\[Veriﬁed Voting\](https://veriﬁedvoting.org/auditlaw/nebraska/) at 2–
2.5% of precincts for primaries and 10% for generals. \[Nebraska
Secretary of
State\](https://sos.nebraska.gov/nebraska-election-security)

Home rule charter authority for cities over 5,000 (Neb. Const. Art. XI,
§§ 2, 5) is limited by statewide concern preemption, \[Nebraska
Legislature\](https://nebraskalegislature.gov/laws/articles.php?article=XI-2)
reinforced by \*\*LB 77 (2023)\*\*, which both enacted constitutional
carry and explicitly \*\*preempted local ﬁrearms regulation\*\*. \[NP
Telegraph\](https://nptelegraph.com/news/state-regional/government-politics/nebraskas-concealed-carry-law-takes-effect-saturday/article_6f7a4600-83c7-57db-a472-ce5916892915.html)
Elections are administered under state law with limited local deviation
authority.

Recent legislative changes include LB 77 (2023 constitutional carry),
\[We Are
Armed\](https://wearearmed.com/individual-state/nebraska-ﬁrearm-laws-complete-guide/)
voter ID implementation following a 2022 constitutional amendment,
\[Nebraska Examiner\]
(https://nebraskaexaminer.com/2025/06/06/nebraska-secretary-of-state-bob-evnen-announces-reelection-bid/)
LB 287 (2024 drop-box buffer zone protections), and LB 521 (2025 poll
watcher regulation updates).

\### Cybersecurity infrastructure

Nebraska's cybersecurity apparatus centers on the Oﬃce of the CIO
(OCIO), \[Nebraska\](https://cio.nebraska.gov/about/) with a newly
launched \*\*Joint Security Operations Center (JSOC)\*\* in 2024.
\[Government
Technology\](https://www.govtech.com/workforce/nebraska-ﬁnds-an-interim-state-cybersecurity-leader-within)
The interim CISO \*\*Bryce Bailey\*\*, a former CISA employee, was
appointed in January 2026. \[Government
Technology\](https://www.govtech.com/workforce/nebraska-ﬁnds-an-interim-state-cybersecurity-leader-within)
A critical vulnerability: CIO Matthew McCarville has acknowledged that
\*\*cybersecurity has not been a dedicated budget line item\*\* within
OCIO, making the state heavily reliant on federal support. \[Route
Fifty\](https://www.route-ﬁfty.com/digital-government/2024/10/new-cio-plans-modernize-it-mindset/400539/)
The Nebraska National Guard maintains Defense Cyberspace Operations
capability under Adjutant General BG Craig Strong. \[Nebraska\]

(https://nema.nebraska.gov/admin/assets/ﬁles/public/publications/Nebraska_National_Guard_Domestic_Operations_Capabilities\_\_2024.pdf)
\[Nebraska\](https://nema.nebraska.gov/about-nema.php)

HAVA funding includes approximately \*\*\$21.5 million initially\*\*
\[KOLN\](https://www.1011now.com/content/news/Nebraska-getting-federal-funds-for-elections-as-part-of-omnibus-spending-bill-477791013.html)
and an estimated \$2.3 million from the 2018 election security
appropriation. The SOS oﬃce conducts external risk assessments
\[Nebraska Secretary of
State\](https://sos.nebraska.gov/nebraska-election-security) and works
with ES&S on vendor security scanning. \[Nebraska Secretary of
State\](https://sos.nebraska.gov/nebraska-election-security)

\### Physical security and polling place protections

The electioneering buffer zone is \*\*200 feet\*\* from polling place
entrances (Neb. Rev. Stat. § 32-1524), \[Justia\]
(https://law.justia.com/codes/nebraska/chapter-32/statute-32-1524/)
\[Justia\](https://law.justia.com/codes/nebraska/chapter-32/statute-32-1524/)
updated by LB 287 (2024) to include secure ballot drop-boxes. \[Nebraska
Legislature\]
(https://nebraskalegislature.gov/laws/statutes.php?statute=32-1524) Exit
polling is restricted within 20 feet of polling entrances or 100 feet of
voting booths (§ 32-1525(1)).
\[FindLaw\](https://codes.ﬁndlaw.com/ne/chapter-32-elections/ne-rev-st-sect-32-1525/)

Nebraska is \*\*unique in this batch\*\*: despite enacting
constitutional carry in 2023, \*\*concealed carry of handguns at polling
places remains speciﬁcally prohibited\*\* under Neb. Rev. Stat. §
28-1202.01( \[Movement Advancement Project\]
(https://www.lgbtmap.org/img/maps/citations-guns-in-polling-places.pdf)
3), \[Movement Advancement Project\]
(https://www.lgbtmap.org/img/maps/citations-guns-in-polling-places.pdf)
\[Nebraska Legislature\]
(https://nebraskalegislature.gov/laws/statutes.php?statute=28-1202.01)
with a ﬁrst offense constituting a Class 3 misdemeanor. \[Liberty Law
Group\](https://libertylawnebraska.com/blog/constitutional-carry-in-nebraska/)
However, open carry at polling places is not speciﬁcally addressed in
statute, creating a partial gap. Poll watchers under §§ 32-961–962 must
maintain an \*\*8-foot distance\*\* from sign-in tables, voting booths,
and ballot boxes, \[Nebraska
Legislature\](https://nebraskalegislature.gov/laws/statutes.php?statute=32-1525)
expanded by LB 521 (2025).

Nebraska lacks a single clearly labeled voter intimidation statute;
protections are distributed across Chapter 32 penalty provisions and
general criminal law. Federal protections under the Voting Rights Act
and 18 U.S.C. §§ 241, 594 apply. \[Civic Nebraska\]
(https://civicnebraska.org/20221031-faq-voter-intimidation/)

\### Legal strategies

Nebraska \*\*did not join\*\* the EO 14248 lawsuit; SOS Evnen actively
supported the executive order. \[Nebraska Examiner\]
(https://nebraskaexaminer.com/2025/03/27/nebraska-secretary-of-state-bob-evnen-echoes-trump-concerns-over-elections/)
\*\*AG Mike Hilgers (R)\*\* has pursued election integrity enforcement,
\[KLIN\](https://klin.com/2025/12/15/nebraska-attorney-general-mike-hilgers-running-for-re-election/)
including a lawsuit against foreign election funding
\[WOWT\](https://www.wowt.com/2025/11/05/live-10-am-ne-

attorney-general-make-election-related-announcement/) and challenges to
felony re-enfranchisement. No state-speciﬁc private right of action for
election intimidation was identiﬁed; federal causes of action (§ 1983,
VRA) are available.

\### Key contacts

\- \*\*Secretary of State\*\*: (402) 471-2554; \[Nebraska Secretary of
State\](https://sos.nebraska.gov/elections/information-candidates)
sos.nebraska.gov

\- \*\*Attorney General\*\*: (402) 471-2683; ago.nebraska.gov

\- \*\*OCIO/SISO\*\*: Patrick Wright, (402) 473-3677, siso@nebraska.gov
\[Southeast\](https://www.southeast.edu/ncsc/) - \*\*NEMA\*\*:
nema.nebraska.gov

---

\## Iowa: Largest buffer zone but no ﬁrearms restriction at polls

\### State election authority and legal framework

\*\*Secretary of State Paul Pate (R)\*\* serves as State Commissioner of
Elections, \[Ballotpedia\]
(https://ballotpedia.org/Iowa_Secretary_of_State) supervising 99 county
auditors \[Iowa Secretary of
State\](https://sos.iowa.gov/elections-voting) \[Iowa Secretary of
State\](https://sos.iowa.gov/elections/voterinformation/voterIDfaq.html)
through Iowa Code Chapters 39–53. Iowa operates under a Republican
trifecta. The Election Misconduct and Penalties Act (Chapter 39A)
establishes a four-tier penalty structure: \[Iowa
Legislature\](https://www.legis.iowa.gov/docs/code/39A.1.pdf)
ﬁrst-degree misconduct including voter intimidation is a \*\*Class D
felony\*\* \[Iowa
Legislature\](https://www.legis.iowa.gov/docs/ico/chapter/39A.pdf) (§
39A.2(1)(d)); \[LawServer\]
(https://www.lawserver.com/law/state/iowa/ia-code/iowa_code_39a-4)
fourth-degree violations are simple misdemeanors (§ 39A.5).

Iowa uses \*\*hand-marked paper ballots with optical scan tabulators
statewide\*\* \[Veriﬁed
Voting\](https://veriﬁedvoting.org/auditlaw/iowa/) — no DRE machines.
Primary vendors include ES&S (DS200 scanners, ExpressVote BMDs)
\[Johnson County\]
(https://www.johnsoncountyiowa.gov/auditor/elections-voting-faqs) and
Unisyn Voting Solutions. \[Veriﬁed Voting\]
(https://veriﬁedvoting.org/election-system/unisyn-voting-solutions-openelect-ovo/)
Post-election audits are mandatory under § 50.51 but results "shall not
change the results, or invalidate the certiﬁcation, of an election."
\[Veriﬁed Voting\](https://veriﬁedvoting.org/auditlaw/iowa/)

Municipal and county home rule exists under Iowa Constitution Art. III,
§§ 38A and 39A, \[Iowa Publications Online\]
(https://publications.iowa.gov/9883/1/CONSTITUTION_OF_THE_STATE_OF_IOWA.pdf)
but \*\*state preemption of ﬁrearms laws\*\* (Iowa Code § 724.28)
prevents localities from restricting ﬁrearms beyond state law. Election
administration is substantially preempted by state law. Signiﬁcant
recent changes include SF 413 (2021),
\[Lawyersdemocracyfund\](https://lawyersdemocracyfund.org/iowas-new-voting-laws-fact-sheet/)
which reduced early voting from 29 to 20 days and shortened poll hours;
a 2022 constitutional amendment requiring strict scrutiny for ﬁrearms
restrictions;
\[FindLaw\](https://www.ﬁndlaw.com/state/iowa-law/iowa-gun-control-laws.html)
and HF 954 (2025) prohibiting ranked-choice voting. \[Iowa Capital
Dispatch\](https://iowacapitaldispatch.com/2025/03/25/iowa-house-passes-bills-on-voter-roll-veriﬁcation-election-recounts/)

\### Cybersecurity infrastructure

Iowa's cybersecurity posture is strengthened by an unusual asset:
\*\*Chief Cybersecurity Oﬃcer Jeff Franklin\*\*, hired in February 2020
speciﬁcally for the SOS oﬃce, and a dedicated \*\*Elections Cyber
Working Group\*\* (established 2018) comprising CISA, Iowa HSEM, OCIO,
the National Guard, and county oﬃcials. The Iowa National Guard stood up
a dedicated cyber unit in 2018 to support election infrastructure,
conducting website security assessments for all 99 county oﬃces.

Iowa Administrative Code r. 721-29.4 (effective February 2025) imposes
\*\*mandatory cybersecurity requirements\*\* on all county
commissioners, including weekly CISA vulnerability scanning, remediation
of critical vulnerabilities, \[Iowa Legislature\]
(https://www.legis.iowa.gov/docs/iac/rule/02-05-2025.721.29.4.pdf)
two-factor authentication for voter registration system access, and use

of county-issued email for election business. HAVA funding totals
approximately \*\*\$18.28 million cumulative\*\*, \[U.S. Election
Assistance
Commission\](https://eac.gov/inspector-general/hava-fund-audits) with
\$4.6 million from the 2018 appropriation, \[The Gazette\]
(https://www.thegazette.com/government-politics/iowa-lands-4-6-million-for-improvements-to-voting-election-security/)
focused heavily on cybersecurity improvements.

The CISA defunding presents a speciﬁc challenge: Iowa's administrative
rules \*require\* CISA services, though the rule anticipates disruptions
by providing that "failure of CISA to provide properly requested
services does not constitute a technical violation." \[Iowa
Legislature\]
(https://www.legis.iowa.gov/docs/iac/rule/02-05-2025.721.29.4.pdf)

\### Physical security and polling place protections

Iowa maintains the \*\*largest electioneering buffer zone in this batch
at 300 feet\*\* (Iowa Code § 39A.4(1)(a)(1)), measured from any outside
door of a building affording access to the polling place. \[North
Carolina Recording
Law\](https://www.dmlp.org/iowa-documenting-2012-vote) However, \*\*Iowa
has no statute prohibiting ﬁrearms at polling places\*\*.
\[GIFFORDS\](https://giffords.org/lawcenter/state-laws/location-restrictions-in-iowa/)
\[Movement Advancement
Project\](https://www.lgbtmap.org/img/maps/citations-guns-in-polling-places.pdf)
Permitless carry has been law since July 1, 2021
\[FindLaw\](https://www.ﬁndlaw.com/state/iowa-law/iowa-gun-control-laws.html)
(HF 756), and the 2022 constitutional amendment requiring strict
scrutiny for any ﬁrearms restriction makes future prohibition extremely
diﬃcult. State preemption under § 724.28 blocks local government action.
\[Wikipedia\](https://en.wikipedia.org/wiki/Gun_laws_in_Iowa) Polling
places in schools are covered by the \*\*1,000-foot school weapons-free
zone\*\*
\[FindLaw\](https://www.ﬁndlaw.com/state/iowa-law/iowa-gun-control-laws.html)
(§ 724.4B), but non-school polling locations have no protection.

Poll watcher regulations under § 49.104 allow up to three observers per
political party, with written credentials required. \[NASS\]
(https://www.nass.org/sites/default/ﬁles/reports/summary-poll-watcher-challenger-laws-jan2024.pdf)
Challengers must be registered voters in the county. \[Iowa Secretary of
State\](https://sos.iowa.gov/elections/pdf/pollwatcherguidebook.pdf) The
voter intimidation statute (§ 39A.2(1)(d)) treats intimidation as
election misconduct in the ﬁrst degree — a \*\*Class D felony\*\*
\[LawServer\]
(https://www.lawserver.com/law/state/iowa/ia-code/iowa_code_39a-2)
carrying up to ﬁve years imprisonment.

Iowa Code § 39.28 provides that the AG or \*\*any eligible elector\*\*
may bring an action in court to enforce Chapters 39–53, establishing a
meaningful citizen enforcement mechanism.

\### Legal strategies

Iowa \*\*did not join\*\* the EO 14248 lawsuit. \*\*AG Brenna Bird
(R)\*\* instead ﬁled a separate lawsuit against DHS/USCIS to obtain
citizenship veriﬁcation data, \[Iowa Attorney
General\](https://www.iowaattorneygeneral.gov/newsroom/attorney-general-bird-and-secretary-pate-sue-the-biden-harris-administration-to-hand-over-election-i)
reaching a settlement in December 2025 granting 20-year access to the
federal SAVE database. The AG has been active in election integrity
enforcement but not voter protection in the traditional sense.

\### Key contacts

\- \*\*Secretary of State\*\*: 1-888-SOS-VOTE (767-8683); \[Iowa
Secretary of State\](https://sos.iowa.gov/voter-hotline) sos.iowa.gov
\[Iowa Secretary of
State\](https://sos.iowa.gov/elections/voterinformation/voterIDfaq.html)

\- \*\*Attorney General\*\*: iowaattorneygeneral.gov

\- \*\*OCIO/Cybersecurity\*\*: (515) 281-5503;
SecurityAwareness@iowa.gov
\[Iowa\](https://ocio.iowa.gov/cybersecurity) - \*\*HSEM\*\*: (515)
725-3231; \[Iowa\](https://homelandsecurity.iowa.gov/about/newsroom)
homelandsecurity.iowa.gov

---

\## Illinois: Strongest protections and sole EO 14248 plaintiff in this
batch

\### State election authority and legal framework

Illinois is the \*\*only state in this batch using a Board of Elections
model\*\* rather than a Secretary of State. The Illinois State Board of
Elections (SBE), established under the 1970 Illinois Constitution,
\[Documenters\](https://www.documenters.org/agencies/illinois-state-board-of-elections-215/)
comprises eight members appointed by the Governor — four from Cook
County, four from outside — with bipartisan

balance requirements.
\[Illinois\](https://govappointments.illinois.gov/boardsandcommissions/details/?id=1915cb5e-2007-ee11-8f6d-001dd8068008)
The SBE oversees \*\*108 local election authorities\*\* (county clerks
and boards of election commissioners). \[Illinois State Board of
Elections\](https://www.elections.il.gov/abouttheboard/DivVotingAndRegistrationSystems.aspx)
\[Revize\]

(https://cms4ﬁles.revize.com/madisoncountyilus/document_center/CountyClerk/PublicationsILStBoard/Illinois_State_Board_of_Elections_FAQs.pd

The Illinois Election Code (10 ILCS 5/) governs all election procedures.
Virtually all counties use hand-marked paper ballots with optical scan
tabulators; \*\*DRE systems are no longer in use.\*\* \[Veriﬁed
Voting\](https://veriﬁedvoting.org/recountlaw/illinois/) Cook County's
upgraded touchscreen ballot marking devices still produce paper records.
A \*\*5% random post-election retabulation\*\* is required under 10 ILCS
5/24B-15. \[Veriﬁed
Voting\](https://veriﬁedvoting.org/auditlaw/illinois/)

Illinois's \*\*exceptionally strong home rule framework\*\* under
Article VII, Section 6 of the 1970 Constitution is the most favorable in
this batch for municipal ordinance strategies.
\[Civicfed\](https://www.civicfed.org/iifs/blog/inventory-local-governments-illinois-municipalities)
\*\*224 home rule municipalities\*\* automatically qualify (population
over 25,000) \[Iml\](https://www.iml.org/homerule) and may "exercise any
power and perform any function pertaining to its government and
affairs," with powers construed liberally. \[FindLaw\]
(https://codes.ﬁndlaw.com/il/constitution-of-the-state-of-illinois/il-const-art-7-sect-6/)
\[Iml\](https://www.iml.org/ﬁle.cfm?key=13451) However, the state
preempts local handgun regulation while allowing local long gun
restrictions. \[Handgunlaw\] (https://handgunlaw.us/states/illinois.pdf)
Regulation of electioneering at polling places is an "exclusive power
and function of the State" (10 ILCS 5/17-29).
\[FindLaw\](https://codes.ﬁndlaw.com/il/chapter-10-elections/il-st-sect-10-5-17-29/)
\[McLean County, IL\]
(https://www.mcleancountyil.gov/DocumentCenter/View/25032/2024-Precinct-Election_Manual)

Recent legislative milestones include the \*\*Protect Illinois
Communities Act (HB 5471, 2023)\*\* banning assault weapons sales,
\[Illinois State Police
+2\](https://isp.illinois.gov/Home/AssaultWeapons) though compliance
rates remain extremely low (highest county: 1.8%). \[WGLT\]
(https://www.wglt.org/politics-and-government/2024-02-19/after-illinois-banned-assault-weapons-rural-gun-owners-registered-very-few-of-them)
HB 5178 (2024) proposed an explicit ﬁrearms ban at polling places \[WTTW
Chicago\](https://news.wttw.com/2024/03/07/new-bill-would-ban-guns-illinois-polling-places)
but does not appear to have been enacted.

\### Cybersecurity infrastructure

Illinois's cybersecurity posture was forged by crisis. The \*\*2016
Russian breach\*\* of the Illinois Voter Registration System — in which
attackers hit SBE servers ﬁve times per second
\[Senate\](https://www.intelligence.senate.gov/wp-content/uploads/2024/08/sites-default-ﬁles-documents-os-ssandvoss-062117-0.pdf)
for a month, viewing \*\*76,000 voter records\*\*
\[Herald-Review\](https://herald-review.com/news/local/govt-and-politics/hackers-got-info-for-76-000-illinois-voters-in-16-heres-whats-being-done-in/article_dbce736f-3160-5f07-acbd-5ca738d4d917.html)
and fully compromising 3,500 \[Government
Technology\](https://www.govtech.com/security/half-of-federal-election-security-funds-will-go-to-cyber-program-in-illinois.html)
— became the catalyst for national election cybersecurity reform. In
response, Illinois created the \*\*Cyber Navigator Program (CNP)\*\* in
2018, \[Illinois Department of Innovation & Technology\]
(https://doit.illinois.gov/initiatives/cybersecurity/slcgp/cyber-navigator-program.html)
\[WTTW Chicago\]
(https://news.wttw.com/2024/09/17/sensitive-illinois-voter-data-exposed-contractor-s-unsecured-databases)
a nationally recognized three-agency partnership between SBE, the
Department of Innovation & Technology (DoIT), and the Illinois State
Police's STIC fusion center. \[NIST\]
(https://www.nist.gov/itl/applied-cybersecurity/nice/nice-enewsletter-spring-2021-government-spotlight)
Nine dedicated cybersecurity specialists serve all 108 election
authorities. \[WTTW
Chicago\](https://news.wttw.com/2019/04/18/illinois-voter-data-hack-part-mueller-report)
The program won the \*\*2020 EAC Clearinghouse Award for Outstanding
Innovation in Election Cybersecurity\*\*, \[Elections Group\]
(https://electionsgroup.com/resource/illinois-cyber-navigator-program/)
and no state-level data breach has occurred since its launch. \[WTTW
Chicago\](https://news.wttw.com/2024/09/17/sensitive-illinois-voter-data-exposed-contractor-s-unsecured-databases)

HAVA funding includes \*\*\$13.2 million from the 2018 allocation\*\*,
\[WTTW
Chicago\](https://news.wttw.com/2019/04/18/illinois-voter-data-hack-part-mueller-report)
with at least half dedicated to the CNP. Base \$10,000 grants go to
every participating county. \[Elections Group\]
(https://electionsgroup.com/resource/illinois-cyber-navigator-program/)
Original HAVA funding for voting equipment replacement was \$140
million, \[WTTW
Chicago\](https://news.wttw.com/2019/04/18/illinois-voter-data-hack-part-mueller-report)
with an estimated \$175 million needed for statewide replacement.
\[Brennan Center for
Justice\](https://www.brennancenter.org/our-work/research-reports/defending-elections-federal-funding-needs-state-election-security)

The loss of EI-ISAC — whose funding was terminated by CISA/DHS \[The
Record\](https://therecord.cisa-cuts-10-million-isac-funding) in
March 2025
\[Votebeat\](https://www.votebeat.org/2025/03/11/cisa-ends-support-election-security-nass-nased/)
— eliminates Albert sensor monitoring and penetration testing services.
Illinois's CNP provides a signiﬁcant state-level buffer, but smaller
rural election authorities

lacking in-house IT are most vulnerable. A \*\*2024 contractor
breach\*\* exposed sensitive voter data in approximately 15 counties
through unsecured databases. \[WTTW
Chicago\](https://news.wttw.com/2024/09/17/sensitive-illinois-voter-data-exposed-contractor-s-unsecured-databases)

\### Physical security and polling place protections

The electioneering buffer zone is \*\*100 feet\*\* from each polling
room entrance (10 ILCS 5/17-29). \[Kslegresearch\]
(https://www.kslegresearch.org/KLRD-web/Publications/ElectionsEthics/electioneering-distances_2022-update.pdf)
Despite Illinois's strong overall ﬁrearms regulation framework — FOID
card requirements, assault weapons ban, concealed carry restrictions —
\*\*no explicit statutory ban on ﬁrearms at polling places exists.\*\*
The concealed carry law (430 ILCS 66/65) prohibits ﬁrearms in schools,
libraries, and government buildings that commonly serve as polling
places, but this coverage is incidental to their regular function rather
than polling-place-speciﬁc. \[WTTW
Chicago\](https://news.wttw.com/2024/03/07/new-bill-would-ban-guns-illinois-polling-places)
The Movement Advancement Project classiﬁes Illinois as having "no clear
prohibition." \[Movement Advancement
Project\](https://www.lgbtmap.org/democracy-maps/guns_in_polling_places)

Voter intimidation constitutes a \*\*Class 4 felony\*\* under 10 ILCS
5/29-4.
\[Justia\](https://law.justia.com/codes/illinois/chapter-10/act-10-ilcs-5/article-29/)
\[Illinois Attorney
General\](https://illinoisattorneygeneral.gov/news/story/attorney-general-raoul-assigns-teams-to-monitor-general-election)
Critically, 10 ILCS 5/29-17 establishes an \*\*explicit private right of
action\*\*: any citizen whose election rights are deprived "shall be
liable to the party injured or any person affected, in any action or
proceeding for redress." \[Justia\]
(https://law.justia.com/codes/illinois/chapter-10/act-10-ilcs-5/article-29/)
This is the strongest citizen enforcement tool in this batch.

The AG assigns monitoring teams to polling places statewide on Election
Day. \[Illinois Attorney General\]
(https://illinoisattorneygeneral.gov/news/story/attorney-general-raoul-assigns-teams-to-monitor-general-election)
Election judges have authority to keep the peace and cause arrests under
10 ILCS 5/18-7.
\[Safeelections\](https://safeelections.org/wp-content/uploads/2024/02/CSSE-IL-Pocket-Guide-2024.pdf)

\### Legal strategies

\*\*Illinois joined the 19-state lawsuit\*\* against EO 14248 \[New
Jersey Oﬃce of Attorney
General\](https://www.njoag.gov/attorney-general-matthew-j-platkin-joins-multistate-lawsuit-against-trump-administration-over-unlawful-executive-order-seeking-to-impose-sweeping-voting-restrictions/)
\[NPR\](https://www.npr.org/2025/04/03/nx-s1-5351751/voting-executive-order-lawsuit)
(\*State of California v. Trump\*, \[CA\]
(https://oag.ca.gov/news/press-releases/attorney-general-bonta-co-leads-multistate-lawsuit-against-trump-administration)
Case No. 1:25-cv-10810, D. Mass.), ﬁled April 3, 2025. \[Civil Rights
Litigation Clearinghouse\](https://clearinghouse.net/case/46337/) \*\*AG
Kwame Raoul (D)\*\* secured a preliminary injunction on June 13, 2025,
blocking
\[CA\](https://oag.ca.gov/news/press-releases/attorney-general-bonta-defeats-trump-administration%E2%80%99s-effort-dismiss-states%E2%80%99)
challenged provisions including documentary proof of citizenship
requirements \[Democracy
Docket\](https://www.democracydocket.com/cases/massachusetts-trump-election-integrity-executive-order-challenge/)
and federal funding conditionality.
\[Congress.gov\](https://www.congress.gov/crs-product/LSB11368) \[New
York State Attorney
General\](https://ag.ny.gov/press-release/2025/attorney-general-james-takes-action-block-president-trumps-unconstitutional)
The case is ongoing following the court's denial of the motion to
dismiss \[Civil Rights Litigation
Clearinghouse\](https://clearinghouse.net/case/46337/) on September 17,
2025. \[Democracy
Docket\](https://www.democracydocket.com/cases/massachusetts-trump-election-integrity-executive-order-challenge/)

Illinois is involved in 35+ multistate lawsuits against the federal
government as of mid-2025.
\[Herald-Review\](https://herald-review.com/news/state-regional/government-politics/article_cdfd7465-c88e-53b0-8443-71ce3e057484.html)
The AG's oﬃce operates dedicated election protection hotlines: Northern
Illinois at \*\*1-866-536-3496\*\* and Central/Southern Illinois at
\*\*1-866-559-6812\*\*. \[Illinois Attorney
General\](https://illinoisattorneygeneral.gov/news/story/attorney-general-raoul-assigns-teams-to-monitor-general-election)

\### Key contacts

\- \*\*State Board of Elections\*\*: (217) 782-4141; elections.il.gov -
\*\*AG Election Protection (North)\*\*: 1-866-536-3496

\- \*\*AG Election Protection (Central/South)\*\*: 1-866-559-6812

\- \*\*DoIT\*\*: (217) 524-3648; Cyber Navigator:
James.L.Patterson@illinois.gov - \*\*IEMA\*\*: (217) 782-2700

---

\## Ohio: Nationally leading cybersecurity with partial ﬁrearms gaps

\### State election authority and legal framework

\*\*Secretary of State Frank LaRose (R)\*\* oversees Ohio's election
infrastructure through 88 \[Ohio Secretary of State\]
(https://www.ohiosos.gov/media-center/press-releases/2020/2020-12-17/)
bipartisan county boards of elections, a structure established under
O.R.C. Title 35. LaRose won the SANS 2020 Difference Makers Award for
cybersecurity \[Ohio Secretary of State\]
(https://www.ohiosos.gov/media-center/press-releases/2020/2020-12-17/)
and has issued \*\*six comprehensive security directives\*\* to county
boards \[Ohio Secretary of
State\](https://www.ohiosos.gov/media-center/week-in-review-archive/2025-06-06/)
through 2025.

Ohio uses a mixed voting system: \*\*47 counties\*\* use hand-marked
paper ballots with optical scanners, \*\*28 counties\*\* use ballot
marking devices for all voters, and \*\*13 counties\*\* retain DRE
machines — all with legally mandated voter-veriﬁed paper audit trails
(O.R.C. § 3506.01(H)). Internet connectivity is prohibited by law.
\[Ohio Secretary of
State\](https://www.ohiosos.gov/elections/voters/security-and-voter-education/)
Mandatory post-election audits in all 88 counties returned a \*\*99.98%
accuracy rate\*\* in the 2020 general election,
\[Clermontcountyohio\](https://boe.clermontcountyohio.gov/board_of_elections/white_paper.php)
with escalation to full hand counts required if accuracy falls below
99.5%. \[Veriﬁed Voting\](https://veriﬁedvoting.org/auditlaw/ohio/)

Ohio's constitutional home rule under Article XVIII, Section 3 grants
municipalities authority to exercise "all powers of local
self-government,"
\[Csuohio\](https://engagedscholarship.csuohio.edu/cgi/viewcontent.cgi?article=4027&context=clevstlrev)
but \*\*O.R.C. § 9.68 expressly preempts local ﬁrearms regulation\*\*,
upheld by the Ohio Supreme Court.
\[GIFFORDS\](https://giffords.org/lawcenter/state-laws/preemption-of-local-laws-in-ohio/)
Election administration is generally considered a matter of statewide
concern, limiting municipal home rule in this area. Key recent
legislative changes include SB 215 (constitutional carry, effective June
2022) \[Walter Haverﬁeld\]
(https://www.walterhav.com/ohios-new-constitutional-carry-provisions-sb-215-what-it-means-for-schools/)
and the defeat of Issue 1 (August 2023), preserving the simple majority
threshold for constitutional amendments. \[Ballotpedia\]
(https://ballotpedia.org/Ohio_2023_ballot_measures)

\### Cybersecurity infrastructure

Ohio is \*\*nationally recognized as a Tier 1 leader\*\* in election
cybersecurity. The \*\*Ohio Cyber Reserve (OhCR)\*\*, created by SB 52
under LaRose's leadership, is a ﬁrst-of-its-kind volunteer civilian
cyber defense force \[Ohio House of Representatives\]
(https://ohiohouse.gov/news/republican/representative-mark-romanchuk-announces-passage-of-ohio-cyber-reserve-legislation-101278)
under the Adjutant General, \[Ohio\](https://ohcr.ohio.gov/join/)
modeled on volunteer ﬁreﬁghter departments. Target strength is 200+
vetted members
\[Ccao\](https://ccao.org/aws/CCAO/asset_manager/get_ﬁle/912184?ver=1)
conducting cybersecurity assessments and incident response.
\[Ohio\](https://ohcr.ohio.gov/)

The state has deployed \*\*Albert intrusion detection sensors\*\* to all
88 county boards and all major election system vendors, alongside
\*\*SIEM (Security Information and Event Management)\*\* monitoring at
every county board. \[eac\]
(https://www.eac.gov/sites/default/ﬁles/paymentgrants/narrative2022/OH_2022_ES_State_Narrative_Budget.pdf)
LaRose's 34-point Security Directive (2019) was "widely considered to be
the most comprehensive in the United States" and has been used as a
model nationally. \[Ohio Secretary of
State\](https://www.ohiosos.gov/media-center/press-releases/2020/2010-01-08/)
Additional infrastructure includes MARCS radios for emergency election
communications and mandatory DHS cybersecurity training for all board
staff. \[Ohio Secretary of State\]
(https://www.ohiosos.gov/media-center/press-releases/2024/2024-06-21/)

HAVA funding through 2022 totals \*\*\$27.9 million federal plus \$3.75
million state match (\$31.66 million combined)\*\*, with 88% allocated
to cyber and physical security. \[eac\]
(https://www.eac.gov/sites/default/ﬁles/paymentgrants/narrative2022/OH_2022_ES_State_Narrative_Budget.pdf)
The Ohio Cyber Integration Center, formally opened in 2025, handles
statewide breach reporting. \[Ccao\]
(https://ccao.org/aws/CCAO/asset_manager/get_ﬁle/912184?ver=1) LaRose
has been vocal about the need for sustained federal funding, writing in
a May 2025 op-ed that the \$15 million FY2025 HAVA allocation "is an
important step, but election security requires more than temporary
funding." \[Record
Herald\](https://www.recordherald.com/2025/05/15/investing-in-election-security-keeps-ohio-ahead-of-emerging-threats/)

\### Physical security and polling place protections

The electioneering buffer zone is \*\*100 feet\*\* (O.R.C. § 3501.35),
marked by small U.S. ﬂags. \[Ohio Revised Code\]
(https://codes.ohio.gov/ohio-revised-code/section-3501.30)
\[Cuyahogacounty\](https://boe.cuyahogacounty.gov/docs/default-source/boe/training-materials-page/bp---no-campaigning---100-foot-line_080717.pdf?sfvrsn=8cc62484_2)
If voter lines extend beyond ﬂags, campaigning is prohibited within
\*\*10 feet of any elector in line\*\* \[Ohio Revised
Code\](http://codes.ohio.gov/orc/3501.35) (§ 3501.35(A)(1)). Ohio law
does not speciﬁcally prohibit carrying ﬁrearms at polling places for
voters, though several layered restrictions apply: school safety zones
\[Everytown
Law\](https://everytownlaw.org/documents/2020/10/election-protection-oh.pdf/)
(§ 2923.122) cover many polling locations; government facility
restrictions (§ 2923.126) apply to buildings with regular government
employees; \[Everytown Law\]
(https://everytownlaw.org/documents/2020/10/election-protection-oh.pdf/)
and \*\*poll observers are speciﬁcally prohibited from carrying
ﬁrearms\*\* (O.R.C. § 3505.21(B)) — the only election-speciﬁc ﬁrearms
restriction. \[Movement Advancement Project\]
(https://www.lgbtmap.org/img/maps/citations-guns-in-polling-places.pdf)

Voter intimidation is a \*\*felony of the fourth degree\*\* (6–18 months
imprisonment, up to \$5,000 ﬁne) under O.R.C. § 3599.01(2). \[Brennan
Center for
Justice\](https://www.brennancenter.org/our-work/research-reports/ohio-protections-against-intimidation-voters-and-election-workers-0)
The county board or SOS may request police oﬃcer assignment to precincts
under § 3501.34. \[Brennan Center for Justice\]
(https://www.brennancenter.org/our-work/research-reports/ohio-protections-against-intimidation-voters-and-election-workers-0)
No Ohio-speciﬁc anti-paramilitary statute was identiﬁed.

\### Legal strategies

Ohio \*\*did not join\*\* the EO 14248 lawsuit. \*\*AG Dave Yost (R)\*\*
has no independent prosecution authority for election crimes — the AG
cannot bring criminal charges unless invited by a county prosecutor.
\[Ohio Capital
Journal\](https://ohiocapitaljournal.com/2023/03/13/ohio-ag-dave-yost-moves-to-get-state-lawsuit-over-bribery-scandal-going-again-now-that-trial-is-over/)
Private rights of action rely on federal statutes (42 U.S.C. § 1983,
VRA). Active litigation includes frequent Supreme Court challenges to
ballot initiative language.

\### Key contacts

\- \*\*Secretary of State\*\*: (877) 767-6446; Elections@OhioSoS.gov;
ohiosos.gov - \*\*Attorney General\*\*: ohioattorneygeneral.gov

\- \*\*Ohio Cyber Reserve\*\*: ohcr.ohio.gov
\[Ohio\](https://ohcr.ohio.gov/join/) - \*\*Ohio EMA\*\*: (614)
889-7150; ema.ohio.gov

---

\## Indiana: DRE legacy and weakest home rule for municipal action

\### State election authority and legal framework

Indiana employs a unique \*\*co-director model\*\* for its Election
Division, with bipartisan co-directors \*\*J. Bradley King (R)\*\* and
\*\*Angela M. Nussmeyer (D)\*\* who must agree for any oﬃcial action.
\[Government of Indiana\](https://www.in.gov/sos/elections/ied-staff/)
\*\*Secretary of State Diego Morales (R)\*\* serves as chief election
oﬃcial under IC 3-6-3.7-1 \[MIT Election Lab\]
(https://electionlab.mit.edu/landscapes/indiana) and chairs the IECC
Elections Committee. The four-member Indiana Election Commission (2R,
2D) administers state election laws. \[MIT Election
Lab\](https://electionlab.mit.edu/landscapes/indiana)

Indiana's voting system history represents the \*\*most signiﬁcant
election security vulnerability\*\* in this batch. As recently as 2020,
approximately \*\*60% of Indiana's voting equipment produced no paper
trail\*\* — 52 of 92 counties used paperless MicroVote Inﬁnity
push-button DRE machines. Senate Enrolled Act 750 (2019) required
phase-out of paperless DREs by 2029; House Bill 1116 (2022) accelerated
the timeline, requiring VVPAT printers on at least 10% of machines by
July 2024. The state used \*\*\$1.9 million in HAVA funds\*\* to
purchase VVPAT equipment for initial counties. \[Bipartisan Policy
Center\](https://bipartisanpolicy.org/explainer/federal-election-funding-path/)
HEA 1680 (2025) introduced mandatory procedure audits, \[Government of
Indiana\](https://www.in.gov/sos/elections/ﬁles/2025-Indiana-Election-Legislation-Summary.FINAL.pdf)
though audit provisions remain weaker than peer states: audits are
discretionary, require party requests for optical scan systems, and can
be waived by the Secretary of State. \[Veriﬁed
Voting\](https://veriﬁedvoting.org/auditlaw/indiana/)

Indiana presents the \*\*most hostile home rule environment\*\* for
municipal ordinance campaigns. While the 1980 Home Rule Act (IC 36-1-3)
nominally abrogated Dillon's Rule, IC 36-1-3-8(a)(12) \*\*expressly
reserves the power to order or conduct elections to the state.\*\* Local
ﬁrearms ordinances have been invalidated under statewide preemption
(Gary and East Chicago assault weapons bans struck down).
\[Wikipedia\](https://en.wikipedia.org/wiki/Gun_laws_in_Indiana)

Recent legislative changes include HEA 1265 (2024), which redeﬁned the
electioneering "chute" to 50 feet in radius \[Government of Indiana\]
(https://www.in.gov/sos/elections/ﬁles/2024-Indiana-Election-Legislation-Summary.FINAL.pdf)
and created Level 6 felony penalties for obstructing election workers;
\[Government of
Indiana\](https://www.in.gov/sos/elections/ﬁles/2024-Indiana-Election-Legislation-Summary.FINAL.pdf)
constitutional carry (effective July 1, 2022); \[USCCA\]
(https://www.usconcealedcarry.com/resources/ccw_reciprocity_map/in-gun-laws/)
and SEA 472 (2025), requiring all public entities to adopt cybersecurity
policies by December 2027. \[Frost Brown
Todd\](https://frostbrowntodd.com/indianas-new-cybersecurity-requirements-effective-july-1-2025/)

\### Cybersecurity infrastructure

Indiana's cybersecurity governance is anchored by the \*\*Indiana
Executive Council on Cybersecurity (IECC)\*\*, established in 2016 and
reauthorized through Executive Order 25-10 (January 2025). Led by four
agencies — IDHS, the Indiana Oﬃce of Technology (IOT), State Police, and
National Guard — the IECC includes 35 voting council members and 250+
advisors across 15 committees. \*\*CISO Hemant Jain\*\* was named Top
Global CISO 2023 and StateScoop State Cybersecurity Leader of the Year
2019.

Indiana's military cyber assets are exceptional: the \*\*127th Cyber
Protection Battalion\*\*, activated in October 2020 at Stout Field in
Indianapolis, commands the 137th Cyber Security Company and 147th Cyber
Warfare Company, along with two Cyber Protection Teams. The
\*\*Muscatatuck Urban Training Complex (MUTC)\*\* is the DoD's only
live, full-scale cyber range. \[National Guard Association of the United
States\](https://www.ngaus.org/about-ngaus/newsroom/indiana-chosen-new-guard-cyber-battalion)
Academic partnerships include Ball State University's Voting System
Technical Oversight Program \[Government of
Indiana\](https://www.in.gov/cybersecurity/government/best-practices-standards-and-resources/)
and Purdue's cyberTAP assessment program.
\[Votesafein\](https://staging.votesafein.gov/secure-portal/)

HAVA funding totals \*\*\$26.3 million audited through 2022\*\*,
\[Oversight.gov\](https://www.oversight.gov/report/EAC/Audit-Help-America-Vote-Act-Grants-Awarded-State-Indiana)
covering MFA implementation, VVPAT purchases, e-poll book security, and
cybersecurity training. The CISA Region 5 Election Security Advisor for
Indiana is \*\*Spencer Wood\*\* (spencer.wood@cisa.dhs.gov).
\[Votesafein\] (https://staging.votesafein.gov/secure-portal/)

\### Physical security and polling place protections

Indiana's electioneering buffer zone — the "chute" — extends only \*\*50
feet in radius\*\* from the polling entrance (IC 3-14-3-16), the
smallest in this batch, as redeﬁned by HEA 1265 (2024). \*\*Indiana has
no speciﬁc statutory prohibition on ﬁrearms at polling places.\*\*
\[Movement Advancement
Project\](https://www.lgbtmap.org/img/maps/citations-guns-in-polling-places.pdf)
Constitutional carry since July 2022 means anyone 18+ who is not a
prohibited person may carry handguns openly or concealed. \[USCCA\]
(https://www.usconcealedcarry.com/resources/ccw_reciprocity_map/in-gun-laws/)
Location-based restrictions apply only to schools, courthouses, the
Statehouse, casinos, and aircraft.
\[Wikipedia\](https://en.wikipedia.org/wiki/Gun_laws_in_Indiana) If a
polling place is in a ﬁre station, community center, or similar public
building, \*\*ﬁrearms are fully permitted\*\*. Failed legislative
attempts include SB 28 (2022), "Prohibition of ﬁrearms at polling
places," which did not advance.

Voter intimidation under IC 3-14-3-21.5 criminalizes knowingly or
intentionally intimidating, threatening, or coercing an individual for
exercising election rights.
\[Justia\](https://law.justia.com/codes/indiana/2021/title-3/article-14/chapter-3/section-3-14-3-21-5/)
The 2024 reform (HEA 1265) added a \*\*Level 6 felony\*\* for
obstructing or injuring election workers or voters in the chute. \[Indy
Justice\] (https://www.indyjustice.com/blog/new-indiana-election-law/)
Private rights of action are limited; the Election Commission handles
administrative complaints, with federal claims under § 1983 and the VRA
providing the primary civil remedies.

\### Legal strategies

Indiana \*\*did not join\*\* the EO 14248 lawsuit. \*\*AG Todd Rokita
(R)\*\* has actively supported the EO's objectives, ﬁling a citizenship
veriﬁcation lawsuit against DHS (settled 2025) and identifying 165
registered non-citizens with 21 having cast ballots. Rokita previously
defended Indiana's voter photo ID law before the Supreme Court in
\*Crawford v. Marion County Election Board\*, 553 U.S. 181 (2008).

\### Key contacts

\- \*\*Election Division\*\*: (317)
\[Votesafein\](https://staging.votesafein.gov/secure-portal/) 232-3939;
elections@iec.in.gov - \*\*Election Security Center\*\*: Jenifer Nelson,
jnelson@sos.in.gov, (317) 234-8555

\- \*\*Attorney General\*\*: in.gov/attorneygeneral

\- \*\*IOT/CISO\*\*: Hemant Jain; Local Gov: Brett Edstene, (463)
261-6177 - \*\*IDHS\*\*: in.gov/dhs

---

\## Cross-state comparison tables

\### EO 14248 litigation status

\| State \| Joined Lawsuit \| AG \| AG Party \| Notes \|
\|-------\|:-:\|---\|:-:\|---\|

\| \*\*Kansas\*\* \| No \| Kris Kobach \| R \| Philosophically aligned
with EO; focused on voter fraud prosecution \|

\| \*\*Nebraska\*\* \| No \| Mike Hilgers \| R \| SOS Evnen actively
supported EO; AG signed multistate support letter \|

\| \*\*Iowa\*\* \| No \| Brenna Bird \| R \| Filed own lawsuit for
citizenship data; settled Dec. 2025 with 20-year SAVE access \| \|
\*\*Illinois\*\* \| \*\*Yes\*\* \| Kwame Raoul \| D \| Secured
preliminary injunction June 13, 2025; active plaintiff \|

\| \*\*Ohio\*\* \| No \| Dave Yost \| R \| AG lacks independent
prosecution authority \|

\| \*\*Indiana\*\* \| No \| Todd Rokita \| R \| Actively supported EO;
ﬁled parallel citizenship veriﬁcation lawsuit \|

\### Firearms at polling places

\| State \| Explicit Polling Place Prohibition \| Constitutional Carry
\| Scope of Protection \| Key Gap \| \|---\|:-:\|:-:\|---\|---\|

\| \*\*Kansas\*\* \| \*\*None\*\* \| Yes (2015) \| Zero protection; even
school polling places allow vehicle storage \| No statutory mechanism to
restrict any ﬁrearms at any polling place \|

\| \*\*Nebraska\*\* \| \*\*Partial\*\* \| Yes (2023) \| § 28-1202.01(3)
bans concealed handguns at polls \| Open carry not addressed; long guns
unregulated at polls \|

\| \*\*Iowa\*\* \| \*\*None\*\* \| Yes (2021) \| School polling places
protected under § 724.4B only \| 2022 constitutional amendment requires
strict scrutiny for any restriction \|

\| \*\*Illinois\*\* \| \*\*None (de facto partial)\*\* \| No (FOID
required) \| Concealed carry banned in schools, libraries, govt
buildings that serve as polls \| No polling-place-speciﬁc ban;
non-traditional venues unprotected \|

\| \*\*Ohio\*\* \| \*\*Observer-speciﬁc only\*\* \| Yes (2022) \| §
3505.21(B) bans observer ﬁrearms; school zones apply \| Voters may carry
at non-school, non-government polling places \|

\| \*\*Indiana\*\* \| \*\*None\*\* \| Yes (2022) \| School/courthouse
venues only \| SB 28 (2022) to ban guns at polls failed; no pending
legislation \|

\### Electioneering buffer zones

\| State \| Distance \| Statute \| Notable Features \|
\|---\|:-:\|---\|---\|

\| \*\*Iowa\*\* \| \*\*300 ft\*\* \| § 39A.4(1)(a)(1) \| Largest in
batch; measured from any outside door; signs on private property
generally exempt \| \| \*\*Kansas\*\* \| \*\*250 ft\*\* \| K.S.A.
25-2430 \| Second-largest; upheld in \*Clark v. Schwab\* (2020); no
private property exemption \|

\| \*\*Nebraska\*\* \| \*\*200 ft\*\* \| § 32-1524 \| Includes
drop-boxes (LB 287, 2024); private property yard signs exempt \| \|
\*\*Illinois\*\* \| \*\*100 ft\*\* \| 10 ILCS 5/17-29 \| Churches may
designate entire property; exclusive state function \|

\| \*\*Ohio\*\* \| \*\*100 ft\*\* \| § 3501.35 \| Marked with U.S. ﬂags;
10-ft extension protects voters in overﬂow lines \|

\| \*\*Indiana\*\* \| \*\*50 ft\*\* \| IC 3-14-3-16 \| Smallest in
batch; redeﬁned as radius (not linear) by HEA 1265 (2024) \|

\### Cybersecurity maturity assessment

\| State \| Tier \| Key Differentiators \| Biggest Vulnerability \|
\|---\|:-:\|---\|---\|

\| \*\*Ohio\*\* \| \*\*1\*\* \| Cyber Reserve (ﬁrst in nation),
Albert/SIEM to all 88 counties, 6 security directives, 99.98% audit
accuracy, \$31.6M HAVA investment \| Federal funding dependency; 13
counties still on DRE (with VVPAT) \|

\| \*\*Illinois\*\* \| \*\*1\*\* \| Cyber Navigator Program (EAC
award-winning), 9 dedicated specialists for 108 EAs, post-2016-breach
resilience \| 108 decentralized EAs with varying maturity; 2024
contractor breach exposed 15 counties \|

\| \*\*Iowa\*\* \| \*\*2\*\* \| Dedicated SOS cybersecurity oﬃcer,
National Guard cyber partnership since 2018, mandatory admin rules
(721-29.4) \| Admin rules require CISA services now disrupted; no
dedicated state cyber budget identiﬁed \|

\| \*\*Indiana\*\* \| \*\*2\*\* \| IECC since 2016, 127th Cyber
Protection Battalion (exceptional military asset), CISO of the Year,
academic partnerships \| DRE legacy (full compliance not until 2029),
weak audit requirements \|

\| \*\*Kansas\*\* \| \*\*2–3\*\* \| KISO and Cybersecurity Task Force,
Fusion Center coordination \| KISO authority excludes SOS oﬃce;
statutory CISA dependency (K.S.A. 75-7239) \|

\| \*\*Nebraska\*\* \| \*\*3\*\* \| New JSOC (2024), National Guard DCO
capability \| No dedicated cybersecurity budget; interim CISO; smallest
state capacity in batch \|

\### Citizen enforcement tools

\| State \| Private Right of Action \| Key Mechanism \| Strength \|
\|---\|:-:\|---\|:-:\|

\| \*\*Illinois\*\* \| \*\*Yes (explicit)\*\* \| 10 ILCS 5/29-17: any
citizen deprived of election rights can bring action for redress \|
\*\*Strong\*\* \|

\| \*\*Iowa\*\* \| \*\*Yes (statutory)\*\* \| § 39.28: AG or any
eligible elector may bring action to enforce election law \|
\*\*Moderate–Strong\*\* \| \| \*\*Kansas\*\* \| \*\*Federal only\*\* \|
42 U.S.C. § 1983; HAVA admin complaint (K.S.A. 25-4701) \|
\*\*Moderate\*\* \|

\| \*\*Ohio\*\* \| \*\*Federal only\*\* \| 42 U.S.C. § 1983; state law
primarily criminal penalties \| \*\*Moderate\*\* \| \| \*\*Nebraska\*\*
\| \*\*Federal only\*\* \| 42 U.S.C. § 1983; VRA \|
\*\*Weak–Moderate\*\* \|

\| \*\*Indiana\*\* \| \*\*Federal only\*\* \| 42 U.S.C. § 1983; Election
Commission admin complaints \| \*\*Weak\*\* \|

\### CISA withdrawal impact assessment

\| State \| Impact Level \| Key Risk Factor \| Mitigation Capacity \|
\|---\|:-:\|---\|---\|

\| \*\*Nebraska\*\* \| \*\*Most Affected\*\* \| No dedicated
cybersecurity budget; interim CISO; smallest election infrastructure \|
JSOC launched 2024 but immature; former CISA employee as interim CISO \|

\| \*\*Kansas\*\* \| \*\*Highly Affected\*\* \| State law mandates CISA
coordination (K.S.A. 75-7239); SOS excluded from KISO \| State-level
grants program exists but cannot replace federal services \|

\| \*\*Iowa\*\* \| \*\*Signiﬁcantly Affected\*\* \| Admin rules
(721-29.4) require CISA services for all 99 counties \| National Guard
partnership and Elections Cyber Working Group provide partial offset \|

\| \*\*Indiana\*\* \| \*\*Moderately Affected\*\* \| 92 small counties
reliant on free federal services \| Strong IECC governance, 127th Cyber
Battalion, IOT programs buffer impact \|

\| \*\*Illinois\*\* \| \*\*Moderately Affected\*\* \| 108 EAs vary
widely; smaller rural jurisdictions most exposed \| Cyber Navigator
Program provides dedicated state-funded capacity \|

\| \*\*Ohio\*\* \| \*\*Best Positioned\*\* \| Already invested \$31.6M+
in independent state infrastructure \| Cyber Reserve, full Albert/SIEM
deployment, six security directives \|

---

\## Strategic implications for municipal ordinance campaigns under 18
U.S.C. § 592

\### Highest-priority targets where protections are weakest

\*\*Kansas and Indiana\*\* represent the most urgent targets for
municipal ordinance campaigns. Both have zero polling place ﬁrearms
prohibitions, constitutional carry, no pending legislation to address
the gap, and hostile state-level political environments. Kansas's
vulnerability is compounded by having no speciﬁc anti-paramilitary
statute and an AG (Kobach) whose agenda centers on voter fraud

prosecution rather than voter protection. Indiana's weak home rule
framework — with election authority expressly reserved to the state
under IC 36-1-3-8(a)(12) — makes municipal action legally precarious but
not necessarily impossible if the ordinance is framed as enforcing
federal criminal law rather than regulating elections.

\*\*Iowa\*\* is a close third priority. Despite the nation's
second-largest buffer zone (300 feet), Iowa has no ﬁrearms restriction
at polling places, constitutional carry, and the 2022 strict-scrutiny
constitutional amendment creates an extremely hostile legal environment
for any new ﬁrearms restriction. The ﬁrearms preemption statute (§
724.28) blocks local action. However, Iowa's citizen enforcement
provision (§ 39.28) enabling any elector to bring enforcement actions
offers a unique litigation pathway.

\### States where existing frameworks provide some protection

\*\*Illinois\*\* offers the most supportive environment. Its 224 home
rule municipalities have broad authority construed liberally. While
state preemption covers handguns and electioneering regulation is an
exclusive state function, a municipal ordinance enforcing 18 U.S.C. §
592 — which addresses armed federal troops, not general ﬁrearms carry —
could be framed as a public safety measure distinct from both ﬁrearms
regulation and election administration. Illinois's explicit private
right of action (10 ILCS 5/29-17) provides a powerful citizen
enforcement tool. The AG's active participation in EO 14248 litigation
signals a state environment receptive to election protection measures.

\*\*Nebraska\*\* occupies a unique middle ground as the only state in
this batch with an explicit concealed-carry prohibition at polling
places (§ 28-1202.01(3)). This establishes state-level precedent that
polling places warrant special ﬁrearms treatment, which a municipal
ordinance could build upon. However, LB 77's statewide preemption of
local ﬁrearms regulation and the legislative hostility to additional
restrictions limit the pathway.

\*\*Ohio's\*\* strong cybersecurity infrastructure and observer-speciﬁc
ﬁrearms prohibition (§ 3505.21(B)) demonstrate some legislative openness
to election-speciﬁc weapons restrictions, but O.R.C. § 9.68 preemption
forecloses municipal ﬁrearms ordinances. The most viable Ohio strategy
may be advocacy for expanding § 3505.21(B) to cover all individuals at
polling places, building on existing legislative precedent.

\### Coalition-building opportunities based on political environment

The regional political landscape demands a \*\*bipartisan framing
strategy\*\*. Only Illinois has Democratic statewide leadership; the
other ﬁve states have uniﬁed Republican government. The most promising
coalition-building approach leverages the fact that 18 U.S.C. § 592 is a
longstanding federal criminal statute — not a new gun control measure —
and that election security is a stated priority of leaders across the
political spectrum. Ohio Secretary of State LaRose's vocal advocacy for
sustained election security funding and his nationally recognized
cybersecurity directives demonstrate that Republican election oﬃcials
can be strong partners on infrastructure security, even if they oppose
the EO 14248 litigation.

\- \*\*Illinois\*\*: Direct coalition with AG Raoul's oﬃce, SBE, and
home rule municipalities (especially those in the Chicago metro area
already active on ﬁrearms regulation)

\- \*\*Ohio\*\*: Engage LaRose's oﬃce on the security dimension;
leverage Cyber Reserve volunteers as advocates; target the legislature's
willingness to restrict observer ﬁrearms as an opening

\- \*\*Nebraska\*\*: Build on the existing polling place concealed-carry
ban to argue for comprehensive coverage including open carry

\- \*\*Iowa/Kansas/Indiana\*\*: Focus on local election oﬃcials (county
auditors and election commissioners) who experience polling place safety
as a practical concern

\### Speciﬁc gaps that municipal ordinances could ﬁll

The most legally defensible municipal ordinance strategy frames
compliance with 18 U.S.C. § 592 as a matter of enforcing existing
federal law rather than creating new ﬁrearms restrictions or regulating
election administration. Key gaps addressable through municipal action
include:

\- \*\*Absence of any mechanism to prevent armed groups near polling
places\*\* in Kansas, Iowa, and Indiana — where neither state law nor
local authority currently addresses paramilitary or organized armed
presence

\- \*\*No state-level election day security coordination requirement\*\*
in Kansas or Nebraska, where municipalities could establish their own
polling place safety protocols as a public safety function

\- \*\*Lack of private enforcement mechanisms\*\* in Kansas, Ohio,
Nebraska, and Indiana — municipal ordinances could create local civil
causes of action for voters subjected to armed intimidation at polling
places

\- \*\*The open carry gap in Nebraska\*\* — where concealed carry is
banned at polls but open carry of ﬁrearms is unaddressed, a municipal
ordinance could close this speciﬁc statutory gap if structured to
withstand preemption challenge

The strongest legal theory across all six states is that a municipal
ordinance implementing 18 U.S.C. § 592 does not "regulate ﬁrearms"
(triggering preemption) but rather enforces a federal criminal statute
concerning the deployment of armed forces at election sites — a
distinction that has not been tested in any of these states' courts and
presents a viable ﬁrst-impression argument for litigation.
