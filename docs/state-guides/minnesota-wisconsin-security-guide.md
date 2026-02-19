---
title: Minnesota & Wisconsin — Election Security Without Federal Support
description: >-
  Technical guide to securing Minnesota and Wisconsin elections following CISA staff reductions and the EI-ISAC fee transition, covering independent state cyber capabilities, physical security protocols, chain of custody, and official contacts for both states.
tags:
  - minnesota
  - wisconsin
  - election-security
  - cybersecurity
  - cisa
  - ei-isac
  - voter-protection
---

# Securing elections in Minnesota and Wisconsin without federal support

**The federal government's withdrawal from election security assistance creates urgent gaps that state and local officials must fill before 2026.** With CISA's election staff reduced by 130+ positions, the EI-ISAC losing federal funding, and interagency task forces dismantled, Minnesota and Wisconsin cannot rely on the protective infrastructure that safeguarded recent elections. However, both states possess substantial independent authority, existing resources, and partnership opportunities to maintain election integrity—if officials act decisively in the months ahead.

Secretary of State Steve Simon captured the uncertainty facing election administrators: "We do not have a sense of whether we can rely on CISA for these services as we approach a big election year in 2026." This report provides a comprehensive roadmap for state and local action across cyber/technical security, physical protection, legal defenses, and available resources.

---

## Minnesota and Wisconsin control their own election security destiny

The Constitution's Elections Clause grants states primary authority over election administration, and the 10th Amendment prevents federal commandeering of state officials. Both states have robust statutory frameworks, dedicated cybersecurity resources, and legal tools to resist interference.

**Minnesota's advantages** include Secretary of State Steve Simon's broad rulemaking authority under Minn. Stat. § 201.221, a dedicated IT security team blocking **100,000+ potentially malicious IP addresses monthly**, the **$6 million VOTER Fund** for FY2026-27, and one of only four state National Guard Cyber Protection Teams. The state's emergency rulemaking process under Minn. Stat. § 14.388 allows rapid response to "serious and immediate threats to public safety," with rules effective within days and lasting two years.

**Wisconsin's strengths** include the Wisconsin Elections Commission's certification and guidance authority, **$5.6 million in available HAVA funds** lasting through approximately May 2028, and the Wisconsin Cyber Response Team with **over 400 members** available for deployment. While Wisconsin's decentralized structure of 1,850+ municipal clerks presents coordination challenges, it also provides resilience against centralized attacks.

---

## Cyber and technical security measures for independent implementation

### Protecting voter registration databases without federal penetration testing

With CISA vulnerability assessments paused, states must implement self-assessment alternatives and enhanced defensive measures. Both Minnesota's Statewide Voter Registration System (SVRS) and Wisconsin's WisVote require immediate attention.

**Essential technical controls** include multi-factor authentication for all database access, Database Activity Monitoring (DAM) software for real-time threat detection, network segmentation isolating voter registration systems, and role-based access limiting permissions to operational necessity. Minnesota's Secretary of State office has implemented all these measures and uses a vendor-hosted Vulnerability Disclosure Program for ongoing vulnerability discovery.

**Self-assessment alternatives** to replace federal testing include the CIS Election Infrastructure Assessment Tool (EIAT), available free at cisecurity.org/elections, and commercial vulnerability scanning tools for public-facing systems. The EAC continues providing its Election Security Risk Profile Tool at no cost.

**Backup protocols** should follow the 3-2-1 rule: three copies, two different media types, one offsite. Minnesota SOS's goal is restoration capability within hours, not days. Air-gapped offline backups protect against ransomware, while incremental backups with versioning enable point-in-time recovery.

### Voting system and election management security

Under Minn. Stat. § 206.57, Secretary Simon holds authority to examine, certify, and decertify electronic voting systems—including requiring source code submission for independent review. Wisconsin's WEC similarly approves voting equipment under Wis. Stat. § 5.37-5.40.

Pre-election Logic and Accuracy (L&A) testing remains mandatory in both states, with public observation permitted. Election Management Systems should be air-gapped from internet-connected networks, with data transferred only via dedicated USB drives under strict chain of custody. The EAC's July 2025 certification of the first VVSG 2.0-compliant system (Hart InterCivic Verity Vanguard) establishes new cybersecurity benchmarks states can require.

### Election night reporting protection

**Free DDoS mitigation** is available through Cloudflare Project Galileo (used in 31 states) and Google Project Shield, which achieves **99.99%+ uptime efficacy** for election-related websites. Minnesota's Secretary of State has partnered with Microsoft's Defending Democracy Program for additional protection.

Technical preparations should include:
- Dual DNS services from different providers running simultaneously
- Content Delivery Networks with maximized caching
- Baseline traffic monitoring to detect anomalies
- Static backup websites on separate infrastructure
- PDF results files uploaded to state network as failover
- Established relationships with local media for alternative results dissemination

---

## The EI-ISAC transition and alternative cybersecurity resources

The Elections Infrastructure Information Sharing and Analysis Center lost federal funding in 2025 and transitioned to a **fee-based membership model**. Approximately 500 election offices have enrolled in paid membership, according to CIS President John Gilligan. Both states should immediately assess their membership status and budget accordingly.

**EI-ISAC services now available to paying members** include 24/7/365 Security Operations Center monitoring, Albert network intrusion detection sensors, Endpoint Detection and Response (EDR), Malicious Domain Blocking and Reporting (MDBR), and election-specific threat intelligence. Registration: learn.cisecurity.org/ei-isac-terms.

### State-level cybersecurity capabilities

**MN.IT Services** operates the Minnesota Security Operations Center with Next-Generation Security Information and Event Management (NGS) providing centralized threat detection. The **Cybersecurity Task Force** includes 15 members representing state, county, city, and tribal governments. The state's **Whole-of-State Cybersecurity Plan** deploys $18 million federal and $5.5 million state funds, with 80% going directly to programming and 25% designated for rural areas.

Key MN.IT contacts:
- Enterprise Service Desk: 651-297-1111 or 1-888-717-6638
- Cybersecurity Task Force: CTF.MNIT@state.mn.us
- Incident Reporting: CN.MNIT@state.mn.us

**Wisconsin's Division of Enterprise Technology (DET)** hosts WisVote infrastructure and handles approximately **9 million scanning attempts annually**. Staff hold Secret Security Clearances and provide mandatory cybersecurity training for all state system users.

The **Wisconsin Cyber Response Team** under Emergency Management offers particularly valuable capabilities: over 400 volunteer members, approximately 140 incident responders deployable across five regional teams (including a National Guard team), and quarterly training exercises. This resource is available to election officials for risk assessments, penetration testing, and incident response.

**Wisconsin CRT Emergency Hotline: (800) 943-0003, option 2**
Email: CRT@widma.gov

---

## Physical security and polling place protection

### Minnesota's comprehensive polling place framework

Minn. Stat. § 204C.06 establishes robust protections that apply directly to federal interference concerns:

- **100-foot buffer zone** around polling places, permitting only voters, election officials, and exit pollsters
- **6-foot ballot security zone** around voting booths and equipment
- **50-foot restriction on peace officers** from polling place entrances, except when summoned by election judges or voting
- Election judges may appoint a **sergeant-at-arms** to keep the peace
- Voters have the right to travel to and from polling places "without unlawful interference"

### Wisconsin observer rules and removal authority

Under Wis. Stat. § 7.41 and EL Chapter 4, observers must remain **3-8 feet from voter check-in tables**, sign logs, present photo ID, and wear identifying badges. They cannot initiate contact with voters, handle election documents, or use cameras during voting hours.

Chief inspectors hold **authority to remove** observers who disrupt operations, engage in electioneering, or fail to comply with instructions. Removal requires a written order stating the reason—election officials should prepare template orders in advance.

### Election worker protection programs

Minnesota's 2023 law (Minn. Stat. § 211B.076) provides substantial protections:
- Prohibits direct or indirect force, coercion, or economic reprisal to influence election officials
- Civil actions require only showing the conduct "would cause a reasonable person to feel intimidated"—**no intent to intimidate required**
- **Anti-doxxing provisions** prohibit publishing personal information (home addresses, photographs) when it poses an imminent threat
- Physical obstruction of polling places, canvassing boards, or ballot storage is prohibited
- Violations are gross misdemeanors; equipment tampering may be a felony

Address confidentiality programs modeled on Safe at Home (originally for domestic violence survivors) can protect election workers, with mail redirected to substitute addresses and public records responses excluding worker locations.

### Ballot chain of custody requirements

**Minnesota drop boxes** (Minn. Stat. § 203B.082) require continuous video recording, tamper-resistant design, secure installation (bolted to concrete or attached to buildings), weather protection, clear identification signage, and daily collection minimum. Collected ballots must be date-stamped and stored in locked containers.

**Wisconsin drop boxes** were upheld by the Wisconsin Supreme Court in *Priorities USA v. WEC* (July 2024), overruling *Teigen v. WEC*. Use is discretionary for municipal clerks. Milwaukee's model implementation includes heavy-duty steel construction, permanent ground bolting, 24-hour video surveillance, city property locations with staffed security, and specially trained officials for chain of custody tracking.

Both states require **multi-partisan custody** throughout ballot handling, with two-person accountability, tamper-evident seals with recorded serial numbers, and detailed documentation at each transfer point.

---

## Protection from federal law enforcement interference at polling places

### The primary federal prohibition election officials must know

**18 U.S.C. § 592** makes it a federal crime—punishable by up to five years imprisonment, fine, and disqualification from office—for any "officer of the Army or Navy, or **other person in the civil, military, or naval service of the United States**" to order, bring, keep, or control "any troops or armed men at any place where a general or special election is held."

The DOJ Election Crimes Manual confirms this statute bars **any armed federal agent** from election sites. ICE agents, as armed federal law enforcement, fall squarely within this prohibition. The only exception is repelling "armed enemies of the United States."

Additional federal protections include:
- **18 U.S.C. § 593**: Prohibits military interference with election officers' duties
- **18 U.S.C. § 594**: Prohibits intimidating, threatening, or coercing voters
- **18 U.S.C. § 595**: Criminalizes federal employees using official authority to interfere with elections
- **52 U.S.C. § 10307(a)**: Bars persons under color of law from preventing entitled voters from voting

### State protocols if federal agents appear near polling places

Minnesota Attorney General Keith Ellison's May 2025 guidance clarifies that ICE may enter public areas without permission but **cannot enter non-public/private areas without a judicial warrant**—administrative warrants signed by immigration officers do not authorize such entry.

**Recommended response protocols**:
1. Election judges have authority to call local law enforcement to restore peace
2. Clearly distinguish between judicial warrants (issued by courts) and administrative warrants (invalid for entry)
3. Document all interactions thoroughly—video, written notes, witness statements
4. Report immediately to state Secretary of State and Attorney General
5. Invoke 18 U.S.C. § 592 explicitly in any communication
6. Contact state AG for emergency injunctive relief if interference continues

**Voter communication** should prominently post rights information, provide hotline numbers (Minnesota: 877-600-VOTE), and inform voters that ICE operations at polling places violate federal law.

---

## State-level administrative and legislative actions

### Minnesota emergency rulemaking pathway

Under Minn. Stat. § 14.388, Secretary Simon can adopt emergency rules when addressing "a serious and immediate threat to public health, safety, or welfare." This process requires only **5 working days for comments** to the Office of Administrative Hearings, with rules effective upon State Register publication and lasting **two years**.

**Administrative actions available without legislation**:
- Issue security directives and uniform procedures for county auditors
- Require enhanced cybersecurity training for election officials
- Prescribe electronic roster requirements with security standards
- Conduct voting system certification reviews and decertify non-compliant equipment
- Deploy Cyber Navigator assistance to counties
- Mandate Database Activity Monitoring and network segmentation

### Wisconsin administrative options

The Wisconsin Elections Commission can issue formal advisory opinions under Wis. Stat. § 5.05(6a) with binding legal effect if supported by statute or case law. Administrator Meagan Wolfe, whose position was unanimously affirmed by the Wisconsin Supreme Court in February 2025, serves as chief election officer.

**WEC emergency rulemaking** under Wis. Stat. § 227.24 is available when preservation of public peace, health, safety, or welfare necessitates—but **requires Governor approval** before filing. Rules can be implemented relatively quickly with proper emergency justification and last 150 days (extendable by the Joint Committee for Review of Administrative Rules).

**Existing WEC training mandates**: Completion of the "Securing WisVote" cybersecurity training series is **required** before receiving system credentials. This award-winning online curriculum can be expanded administratively.

### Available state funding

| Funding Source | Minnesota | Wisconsin |
|----------------|-----------|-----------|
| Dedicated State Funds | VOTER Fund: $3M/year FY26-27 | ~$5.1M GPR annual base |
| HAVA Funds Available | Ongoing with 20% state match | ~$5.6M through May 2028 |
| Recent Appropriations | $200K HAVA match (FY26) | Motion #71 IT costs |
| Local Distribution | 80% to counties, 25% to municipalities | Subgrant programs |

---

## County and municipal clerk authorities and actions

### What local officials can implement independently

**County auditors (Minnesota)** and **municipal clerks (Wisconsin)** hold primary operational responsibility for elections. Local measures within existing authority include:

- **Enhanced poll worker training** on de-escalation techniques, security awareness, and federal law restrictions
- **Physical security upgrades**: tamper-evident seals on all equipment, security cameras in storage areas, access logs for secure facilities
- **Communication protocols**: two-way communication with local law enforcement, designated responders at each location, incident reporting chains
- **Pre-election testing**: expanded Logic and Accuracy testing with public observation
- **Election night redundancy**: backup websites, PDF results files, local media relationships for alternative dissemination

### Local law enforcement coordination

Minnesota law requires peace officers to remain **50 feet from polling places** unless summoned by election judges. Wisconsin's chief inspectors may call law enforcement under Wis. Stat. § 7.37(2) to aid in enforcing law, preserving order, and stopping voter intimidation.

**Best practice protocols** developed in jurisdictions like Willmar, Minnesota include:
- Pre-election meetings between law enforcement and election judges
- Contingency planning for emergencies
- Added patrol staff during voting hours
- Intelligence monitoring on threats
- Clear communication about buffer zone requirements

### Public communication strategies

The NASS **#TrustedInfo campaign** provides resources for promoting election officials as trusted sources of information. Local officials should:
- Establish themselves as authoritative sources before misinformation spreads
- Prepare responses to common voter concerns about federal interference
- Prominently display voter rights information at polling places
- Coordinate messaging with state election offices
- Use official .gov email domains (Wisconsin offers .gov domain subgrant reimbursement)

---

## Legal strategies and constitutional protections

### State constitutional foundations

The **Minnesota Constitution Article VII** establishes eligibility for voting, civil process suspension on election day, secret ballot requirements, and creates the Board of Canvassers for certifying statewide elections. Minnesota courts have interpreted state constitutional protections more expansively than federal rights.

**Wisconsin Constitution Article III** was strengthened in April 2024 when voters approved amendments stating "No individual other than an election official designated by law may perform any task in the conduct of any primary, election, or referendum" and prohibiting non-governmental funding of election administration.

### Active multistate litigation

Both Minnesota and Wisconsin are among **19 states** that sued the Trump Administration in April 2025 over Executive Order 14248, which attempted to:
- Force proof of citizenship on federal voter registration forms
- Ban counting mail ballots received after Election Day
- Threaten withholding federal election funding

In May 2025, U.S. District Court (D. Mass.) granted a **preliminary injunction blocking key provisions**. Attorney General Keith Ellison and Attorney General Josh Kaul continue coordinating legal responses through this coalition.

### Voter intimidation enforcement

**Minnesota**: The Attorney General has authority under Minn. Stat. § 8.31 to bring civil actions, with the Office of Administrative Hearings empowered to impose penalties up to $5,000 and refer for criminal prosecution. County attorneys have primary jurisdiction for election law violations.

**Wisconsin**: The Attorney General can seek injunctive relief, mandamus, or other legal remedy under Wis. Stat. § 5.07. Critically, **any elector may sue** for injunctive relief under this statute—enabling citizen enforcement. District attorneys hold exclusive prosecution authority for election crimes, which under Wis. Stat. § 12.09 constitute **Class I felonies** (up to 3.5 years imprisonment, $10,000 fine).

### Pre-emptive legal preparation

State attorneys general should:
- Prepare emergency injunction templates citing 18 U.S.C. § 592
- Establish communication chains between local officials, county attorneys, and AG offices
- Coordinate with legal organizations (ACLU, Brennan Center, Law Forward) for rapid response
- Consider declaratory judgment actions establishing state authority before conflicts arise
- Document all federal communications for potential litigation evidence

---

## Available resources and partnership opportunities

### Remaining federal resources

The **Election Assistance Commission** remains fully operational, continuing voting system certification (now to VVSG 2.0 standards), quarterly threat intelligence briefings with Mandiant, election security preparedness resources, and grant administration. Contact: grants@eac.gov.

**CISA services technically remain available** but with significantly reduced capacity. States should contact electionsecurity@cisa.dhs.gov to confirm availability of specific services. Downloadable tabletop exercise packages and training materials remain accessible at cisa.gov/topics/election-security.

### Critical nonprofit partnerships

| Organization | Key Services | Contact |
|--------------|--------------|---------|
| **Verified Voting** | Voting system database, audit law resources, eGeeks troubleshooting | verifiedvoting.org |
| **Brennan Center** | Committee for Safe and Secure Elections, cyber navigator guidance, state security recommendations | brennancenter.org/election-security |
| **CEIR** | Election Official Legal Defense Network (pro bono attorneys), communications support | info@electioninnovation.org |
| **CIS/EI-ISAC** | SOC monitoring, Albert sensors, EDR, MDBR (now fee-based) | cisecurity.org/ei-isac |
| **Election Center** | CERA certification, peer networking, electionline news clearinghouse | electioncenter.org |

### Academic partnerships

The **University of Minnesota Humphrey School** offers the nation's first Certificate in Election Administration, including dedicated election security courses (PA 3983-3985) covering introduction to election security, protecting America's elections, and physical election security. All students pay resident tuition rates for the online program. Contact: [email protected].

The **UW-Madison Elections Research Center** conducts cutting-edge research and hosts the State Democracy Research Initiative with attorneys covering Minnesota and Wisconsin election law issues. Contact: Barry Burden, Director.

**MIT Election Data + Science Lab** provides the Elections Performance Index for state comparisons, public election data repositories, and research partnerships. Contact: electionlab@mit.edu.

### Free technology resources

**Microsoft ElectionGuard** is a free, open-source SDK for end-to-end verifiable elections using homomorphic encryption. It has been successfully piloted in Wisconsin (Fulton), California, Idaho, and elsewhere. Integration partners include VotingWorks and Hart InterCivic. Website: electionguard.vote.

**VotingWorks** provides Arlo, open-source risk-limiting audit software, at no cost. This nonprofit also offers ElectionGuard integration support.

---

## Key contacts for Minnesota and Wisconsin officials

### Minnesota
- **Secretary of State Elections Division**: 651-215-1440, elections.dept@state.mn.us
- **Voter Hotline**: 877-600-VOTE (8683)
- **MN.IT Enterprise Service Desk**: 651-297-1111
- **Attorney General**: ag.state.mn.us

### Wisconsin
- **WEC Help Desk**: (608) 261-2028, elections@wi.gov
- **Wisconsin Cyber Response Team**: (800) 943-0003 option 2, CRT@widma.gov
- **County Clerks Association**: wisconsincountyclerks.org
- **Attorney General**: doj.state.wi.us

### Federal and National
- **EAC Grants**: grants@eac.gov
- **EI-ISAC Registration**: learn.cisecurity.org/ei-isac-terms
- **CEIR Legal Defense Network**: legaldefense@electioninnovation.org
- **FBI IC3** (cyber incidents): ic3.gov

The withdrawal of federal election security support presents genuine challenges, but Minnesota and Wisconsin possess the legal authority, technical capabilities, and partnership opportunities to protect election integrity. Success requires immediate action to deploy available resources, train election workers on new protocols, establish legal defenses against interference, and coordinate across state and local jurisdictions. The 2026 elections can be secured—if officials act now.