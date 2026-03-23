/**
 * Protections For Elections — Custom JavaScript
 *
 * Features:
 * 1. Interactive 50-State Table Filter (active on /legal-foundation/50-state-overview/ only)
 * 2. Smooth anchor scroll for legal deep-links
 * 3. Dropdown menus for top navigation tabs
 * 4. Lead-in auto-bold for long paragraphs
 * 5. Animated donut chart for polling data
 * 6. Accordion expand/collapse all controls
 * 7. Interactive US map tooltip and navigation
 * 8. State search in mega-menu dropdown
 */

/* ============================================================
   FEATURE 1: 50-STATE TABLE INTERACTIVE FILTER
   ============================================================ */

/**
 * Initializes the tier filter bar above the 50-state analysis table.
 * Adds GREEN / YELLOW / RED filter buttons that show/hide table rows.
 * Activates only on the 50-state overview page.
 */
function init50StateFilter() {
  // Only activate on the 50-state overview page
  const isTargetPage =
    window.location.pathname.includes("50-state-overview") ||
    window.location.pathname.includes("50_state_overview");

  if (!isTargetPage) return;

  // Find the target table — it's the one with a "Tier" column header
  const tables = document.querySelectorAll(".md-typeset table");
  let stateTable = null;
  let tierColIndex = -1;

  for (const table of tables) {
    const headers = table.querySelectorAll("th");
    headers.forEach((th, i) => {
      if (th.textContent.trim() === "Tier") {
        stateTable = table;
        tierColIndex = i;
      }
    });
    if (stateTable) break;
  }

  if (!stateTable || tierColIndex < 0) return;

  // Tag each data row with its tier value
  const rows = Array.from(stateTable.querySelectorAll("tbody tr"));
  rows.forEach((row) => {
    const tierCell = row.cells[tierColIndex];
    if (!tierCell) return;
    const text = tierCell.textContent.trim().toUpperCase();
    if (text.includes("GREEN")) row.dataset.tier = "GREEN";
    else if (text.includes("YELLOW")) row.dataset.tier = "YELLOW";
    else if (text.includes("RED")) row.dataset.tier = "RED";
    else row.dataset.tier = "other";
  });

  // Count tiers for labels
  const tierCounts = {
    GREEN: rows.filter((r) => r.dataset.tier === "GREEN").length,
    YELLOW: rows.filter((r) => r.dataset.tier === "YELLOW").length,
    RED: rows.filter((r) => r.dataset.tier === "RED").length,
  };
  const total = rows.length;

  // Build filter bar
  const filterBar = document.createElement("div");
  filterBar.id = "tier-filter-bar";
  filterBar.setAttribute("role", "group");
  filterBar.setAttribute("aria-label", "Filter states by viability tier");

  filterBar.innerHTML = `
    <span class="filter-label" id="tier-filter-label">Filter by tier:</span>
    <button class="tier-filter-btn active" data-tier="all" aria-pressed="true"
      aria-describedby="tier-filter-label">
      All States (${total})
    </button>
    <button class="tier-filter-btn" data-tier="GREEN" aria-pressed="false"
      aria-describedby="tier-filter-label">
      GREEN — Strong Viability (${tierCounts.GREEN})
    </button>
    <button class="tier-filter-btn" data-tier="YELLOW" aria-pressed="false"
      aria-describedby="tier-filter-label">
      YELLOW — Proceed with Caution (${tierCounts.YELLOW})
    </button>
    <button class="tier-filter-btn" data-tier="RED" aria-pressed="false"
      aria-describedby="tier-filter-label">
      RED — Significant Barriers (${tierCounts.RED})
    </button>
    <span id="tier-result-count" aria-live="polite" aria-atomic="true"></span>
  `;

  // Insert the filter bar before the table
  stateTable.parentNode.insertBefore(filterBar, stateTable);

  // Wire up filter button click handlers
  const buttons = filterBar.querySelectorAll(".tier-filter-btn");
  const resultCount = filterBar.querySelector("#tier-result-count");

  buttons.forEach((btn) => {
    btn.addEventListener("click", function () {
      const tier = this.dataset.tier;

      // Update button active/pressed states
      buttons.forEach((b) => {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      this.classList.add("active");
      this.setAttribute("aria-pressed", "true");

      // Filter rows
      let visibleCount = 0;
      rows.forEach((row) => {
        const show = tier === "all" || row.dataset.tier === tier;
        row.style.display = show ? "" : "none";
        if (show) visibleCount++;
      });

      // Update result count label
      if (tier === "all") {
        resultCount.textContent = "";
      } else {
        resultCount.textContent = `Showing ${visibleCount} of ${total} states`;
      }
    });
  });
}

/* ============================================================
   FEATURE 2: SMOOTH ANCHOR SCROLL
   Makes in-page legal citation deep-links scroll smoothly
   ============================================================ */

function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href").slice(1);
      const target = document.getElementById(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
        // Update URL without triggering a page reload
        history.pushState(null, null, "#" + targetId);
        // Move focus for accessibility
        target.setAttribute("tabindex", "-1");
        target.focus({ preventScroll: true });
      }
    });
  });
}

/* ============================================================
   FEATURE 3: DROPDOWN MENUS FOR TOP NAVIGATION TABS
   Builds dropdown panels for How to Use, Legal Foundation,
   and State Guides (with nested tier sub-dropdowns).
   ============================================================ */

function initTabDropdowns() {
  // Clear old dropdowns to avoid duplication on SPA navigation
  document.querySelectorAll(".md-tabs__dropdown").forEach(function (el) {
    el.remove();
  });

  var tabs = document.querySelectorAll(".md-tabs__item");
  if (!tabs.length) return;

  var sidebarNav = document.querySelector(".md-nav--primary > .md-nav__list");
  if (!sidebarNav) return;

  // Helper: find a tab by its visible text label
  function findTab(label) {
    var match = null;
    tabs.forEach(function (tab) {
      var link = tab.querySelector(".md-tabs__link");
      if (link && link.textContent.trim() === label) match = tab;
    });
    return match;
  }

  // Helper: find a sidebar nav item by its visible text
  function findSidebarItem(label) {
    var match = null;
    var items = sidebarNav.querySelectorAll(":scope > .md-nav__item");
    items.forEach(function (item) {
      var el =
        item.querySelector(":scope > a.md-nav__link") ||
        item.querySelector(":scope > label.md-nav__link");
      if (el && el.textContent.trim() === label) match = item;
    });
    return match;
  }

  // Helper: create a basic dropdown container
  function makeDropdown() {
    var d = document.createElement("div");
    d.className = "md-tabs__dropdown";
    return d;
  }

  // Helper: create a link element for a dropdown item
  function makeLink(href, text) {
    var a = document.createElement("a");
    a.href = href;
    a.textContent = text;
    return a;
  }

  /* ----------------------------------------------------------
     "How to Use This Guide" — section anchors
     Since this is a single page with no child pages, we
     hard-code the section headings as anchor links.
     ---------------------------------------------------------- */
  (function () {
    var tab = findTab("How to Use This Guide");
    var navItem = findSidebarItem("How to Use This Guide");
    if (!tab) return;

    // Get the base href for the how-to-use page from the sidebar link
    var baseLink = navItem
      ? navItem.querySelector(":scope > a.md-nav__link")
      : null;
    var baseHref = baseLink ? baseLink.getAttribute("href") : "how-to-use/";
    // Strip trailing hash/anchor if present
    baseHref = baseHref.split("#")[0];

    var sections = [
      { anchor: "municipal-officials", text: "Municipal Officials" },
      {
        anchor: "attorneys-and-legal-advocates",
        text: "Attorneys & Legal Advocates",
      },
      { anchor: "coalition-organizers", text: "Coalition Organizers" },
      { anchor: "voters-activists", text: "Voters & Activists" },
      {
        anchor: "understanding-the-tier-system",
        text: "Understanding the Tier System",
      },
      { anchor: "document-conventions", text: "Document Conventions" },
    ];

    var dropdown = makeDropdown();
    sections.forEach(function (s) {
      dropdown.appendChild(makeLink(baseHref + "#" + s.anchor, s.text));
    });
    tab.appendChild(dropdown);
  })();

  /* ----------------------------------------------------------
     "Voter & Activist Guide" — child page links from sidebar
     ---------------------------------------------------------- */
  (function () {
    var tab = findTab("Voter & Activist Guide");
    var navItem = findSidebarItem("Voter & Activist Guide");
    if (!tab || !navItem) return;

    var childNav = navItem.querySelector(":scope > .md-nav");
    if (!childNav) return;

    var dropdown = makeDropdown();
    var links = childNav.querySelectorAll(
      ":scope > .md-nav__list > .md-nav__item > a.md-nav__link"
    );
    links.forEach(function (link) {
      dropdown.appendChild(
        makeLink(link.getAttribute("href"), link.textContent.trim())
      );
    });

    if (dropdown.children.length > 0) tab.appendChild(dropdown);
  })();

  /* ----------------------------------------------------------
     "Legal Foundation" — child page links from sidebar
     ---------------------------------------------------------- */
  (function () {
    var tab = findTab("Legal Foundation");
    var navItem = findSidebarItem("Legal Foundation");
    if (!tab || !navItem) return;

    var childNav = navItem.querySelector(":scope > .md-nav");
    if (!childNav) return;

    var dropdown = makeDropdown();
    var links = childNav.querySelectorAll(
      ":scope > .md-nav__list > .md-nav__item > a.md-nav__link"
    );
    links.forEach(function (link) {
      dropdown.appendChild(
        makeLink(link.getAttribute("href"), link.textContent.trim())
      );
    });

    if (dropdown.children.length > 0) tab.appendChild(dropdown);
  })();

  /* ----------------------------------------------------------
     "State Guides" — Multi-column mega menu showing all 3
     tiers side-by-side for easy state lookup
     ---------------------------------------------------------- */
  (function () {
    var tab = findTab("State Guides");
    var navItem = findSidebarItem("State Guides");
    if (!tab || !navItem) return;

    var childNav = navItem.querySelector(":scope > .md-nav");
    if (!childNav) return;

    var childItems = childNav.querySelectorAll(
      ":scope > .md-nav__list > .md-nav__item"
    );

    var dropdown = makeDropdown();
    dropdown.classList.add("md-tabs__mega-menu");

    var columnsContainer = document.createElement("div");
    columnsContainer.className = "md-tabs__mega-columns";

    childItems.forEach(function (child) {
      var directLink = child.querySelector(":scope > a.md-nav__link");
      var sectionLabel = child.querySelector(":scope > label.md-nav__link");

      if (directLink && !sectionLabel) {
        // "State Guide Overview" — link at top of mega menu
        dropdown.appendChild(
          makeLink(
            directLink.getAttribute("href"),
            directLink.textContent.trim()
          )
        );
      } else if (sectionLabel) {
        // Tier group — create a column
        var tierText = sectionLabel.textContent.trim();
        var col = document.createElement("div");
        col.className = "md-tabs__mega-col";

        // Determine tier color class
        if (tierText.indexOf("Tier 1") !== -1)
          col.classList.add("md-tabs__mega-col--green");
        else if (tierText.indexOf("Tier 2") !== -1)
          col.classList.add("md-tabs__mega-col--yellow");
        else if (tierText.indexOf("Tier 3") !== -1)
          col.classList.add("md-tabs__mega-col--red");

        // Tier header
        var header = document.createElement("div");
        header.className = "md-tabs__mega-col-header";
        header.textContent = tierText;
        col.appendChild(header);

        // State links within this tier
        var subNav = child.querySelector(":scope > .md-nav");
        if (subNav) {
          var stateLinks = subNav.querySelectorAll(
            ":scope > .md-nav__list > .md-nav__item > a.md-nav__link"
          );
          stateLinks.forEach(function (sl) {
            col.appendChild(
              makeLink(sl.getAttribute("href"), sl.textContent.trim())
            );
          });
        }

        columnsContainer.appendChild(col);
      }
    });

    dropdown.appendChild(columnsContainer);
    if (dropdown.children.length > 0) tab.appendChild(dropdown);
  })();
}

/* ============================================================
   FEATURE 4: LEAD-IN AUTO-BOLD
   Wraps the first sentence of long paragraphs in <strong>
   for quick scanning.
   ============================================================ */

function initLeadIns() {
  // Only apply on pages with substantial prose content
  var contentArea = document.querySelector(".md-content__inner");
  if (!contentArea) return;

  var paragraphs = contentArea.querySelectorAll(
    ".md-typeset > p, .md-typeset .lead-in > p"
  );

  paragraphs.forEach(function (p) {
    // Skip short paragraphs, paragraphs inside cards/admonitions, or already-processed ones
    if (p.textContent.length < 200) return;
    if (p.closest(".grid, .admonition, details, .hero-banner, .stat-callout, .flowchart, .risk-chart")) return;
    if (p.querySelector("strong.lead-in")) return;

    // Find the first sentence boundary (period followed by space or end)
    var html = p.innerHTML;
    var match = html.match(/^((?:<[^>]+>)*[^.]*\.)/);
    if (match && match[1].length < html.length * 0.6) {
      p.innerHTML =
        '<strong class="lead-in">' + match[1] + "</strong>" + html.slice(match[1].length);
    }
  });
}

/* ============================================================
   FEATURE 5: ANIMATED DONUT CHART
   Animates the stat donut on scroll into view.
   ============================================================ */

function initDonutChart() {
  var donut = document.querySelector(".stat-donut-fill");
  if (!donut) return;

  // Start with empty ring (total circumference for r=52: 2*PI*52 ≈ 326.7)
  var totalLen = 326.7;
  donut.style.strokeDashoffset = String(totalLen);

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          // Animate to 64%: offset = totalLen * (1 - 0.64) = 117.6
          donut.style.strokeDashoffset = "117.6";
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  observer.observe(donut);
}

/* ============================================================
   FEATURE 6: ACCORDION EXPAND/COLLAPSE ALL
   Adds controls on the Master Ordinance Template page.
   ============================================================ */

function initAccordionControls() {
  if (!window.location.pathname.includes("master-ordinance-template")) return;

  var details = document.querySelectorAll(".md-typeset details.note");
  if (details.length < 3) return;

  var controlDiv = document.createElement("div");
  controlDiv.className = "accordion-controls";
  controlDiv.setAttribute("role", "group");
  controlDiv.setAttribute("aria-label", "Accordion controls");

  var expandBtn = document.createElement("button");
  expandBtn.textContent = "Expand All Sections";
  expandBtn.addEventListener("click", function () {
    details.forEach(function (d) {
      d.open = true;
    });
  });

  var collapseBtn = document.createElement("button");
  collapseBtn.textContent = "Collapse All Sections";
  collapseBtn.addEventListener("click", function () {
    details.forEach(function (d) {
      d.open = false;
    });
  });

  controlDiv.appendChild(expandBtn);
  controlDiv.appendChild(collapseBtn);

  // Insert before the first details.note element
  details[0].parentNode.insertBefore(controlDiv, details[0]);
}

/* ============================================================
   FEATURE 7: INTERACTIVE US MAP (D3 Choropleth)
   Geographic state shapes, tier coloring, click to navigate.
   Requires D3.js v7 and topojson-client loaded via CDN.
   ============================================================ */

var US_STATE_DATA = {
  "01":{name:"Alabama",slug:"alabama",tier:3},
  "02":{name:"Alaska",slug:"alaska",tier:1},
  "04":{name:"Arizona",slug:"arizona",tier:3},
  "05":{name:"Arkansas",slug:"arkansas",tier:3},
  "06":{name:"California",slug:"california",tier:1},
  "08":{name:"Colorado",slug:"colorado",tier:1},
  "09":{name:"Connecticut",slug:"connecticut",tier:2},
  "10":{name:"Delaware",slug:"delaware",tier:2},
  "12":{name:"Florida",slug:"florida",tier:3},
  "13":{name:"Georgia",slug:"georgia",tier:3},
  "15":{name:"Hawaii",slug:"hawaii",tier:2},
  "16":{name:"Idaho",slug:"idaho",tier:3},
  "17":{name:"Illinois",slug:"illinois",tier:1},
  "18":{name:"Indiana",slug:"indiana",tier:3},
  "19":{name:"Iowa",slug:"iowa",tier:3},
  "20":{name:"Kansas",slug:"kansas",tier:2},
  "21":{name:"Kentucky",slug:"kentucky",tier:2},
  "22":{name:"Louisiana",slug:"louisiana",tier:3},
  "23":{name:"Maine",slug:"maine",tier:1},
  "24":{name:"Maryland",slug:"maryland",tier:1},
  "25":{name:"Massachusetts",slug:"massachusetts",tier:1},
  "26":{name:"Michigan",slug:"michigan",tier:1},
  "27":{name:"Minnesota",slug:"minnesota",tier:1},
  "28":{name:"Mississippi",slug:"mississippi",tier:3},
  "29":{name:"Missouri",slug:"missouri",tier:3},
  "30":{name:"Montana",slug:"montana",tier:3},
  "31":{name:"Nebraska",slug:"nebraska",tier:2},
  "32":{name:"Nevada",slug:"nevada",tier:2},
  "33":{name:"New Hampshire",slug:"new-hampshire",tier:2},
  "34":{name:"New Jersey",slug:"new-jersey",tier:1},
  "35":{name:"New Mexico",slug:"new-mexico",tier:1},
  "36":{name:"New York",slug:"new-york",tier:1},
  "37":{name:"North Carolina",slug:"north-carolina",tier:3},
  "38":{name:"North Dakota",slug:"north-dakota",tier:3},
  "39":{name:"Ohio",slug:"ohio",tier:1},
  "40":{name:"Oklahoma",slug:"oklahoma",tier:3},
  "41":{name:"Oregon",slug:"oregon",tier:1},
  "42":{name:"Pennsylvania",slug:"pennsylvania",tier:2},
  "44":{name:"Rhode Island",slug:"rhode-island",tier:1},
  "45":{name:"South Carolina",slug:"south-carolina",tier:3},
  "46":{name:"South Dakota",slug:"south-dakota",tier:3},
  "47":{name:"Tennessee",slug:"tennessee",tier:3},
  "48":{name:"Texas",slug:"texas",tier:3},
  "49":{name:"Utah",slug:"utah",tier:3},
  "50":{name:"Vermont",slug:"vermont",tier:2},
  "51":{name:"Virginia",slug:"virginia",tier:3},
  "53":{name:"Washington",slug:"washington",tier:1},
  "54":{name:"West Virginia",slug:"west-virginia",tier:3},
  "55":{name:"Wisconsin",slug:"wisconsin",tier:2},
  "56":{name:"Wyoming",slug:"wyoming",tier:3}
};

var TIER_LABELS = {
  1: "Tier 1 \u2014 Strong Viability",
  2: "Tier 2 \u2014 Proceed with Caution",
  3: "Tier 3 \u2014 Significant Barriers"
};

function initUSMap() {
  var container = document.getElementById("choropleth-map");
  if (!container) return;
  if (typeof d3 === "undefined" || typeof topojson === "undefined") return;

  // Prevent duplicate renders on SPA navigation
  container.innerHTML = "";

  var tooltip = container.parentElement
    ? container.parentElement.querySelector(".map-tooltip")
    : null;
  if (!tooltip) {
    tooltip = document.querySelector(".map-tooltip");
  }

  var width = 960;
  var height = 600;

  var svg = d3.select(container)
    .append("svg")
    .attr("viewBox", "0 0 " + width + " " + height)
    .attr("preserveAspectRatio", "xMidYMid meet")
    .attr("role", "img")
    .attr("aria-label", "Interactive choropleth map of the United States showing tier classifications for all 50 states. Click a state to view its guide.");

  var style = getComputedStyle(document.documentElement);
  var tierColors = {
    1: style.getPropertyValue("--tier-green").trim() || "#2e7d32",
    2: style.getPropertyValue("--tier-yellow").trim() || "#e65100",
    3: style.getPropertyValue("--tier-red").trim() || "#c62828"
  };

  d3.json("https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json")
    .then(function(topoData) {
      var projection = d3.geoAlbersUsa().fitSize([width, height], topojson.feature(topoData, topoData.objects.states));
      var path = d3.geoPath().projection(projection);
      var features = topojson.feature(topoData, topoData.objects.states).features;

      svg.selectAll(".state-path")
        .data(features)
        .enter()
        .append("path")
        .attr("class", "state-path")
        .attr("d", path)
        .attr("tabindex", "0")
        .attr("fill", function(d) {
          var fips = String(d.id).padStart(2, "0");
          var sd = US_STATE_DATA[fips];
          return sd ? tierColors[sd.tier] : "#ddd";
        })
        .on("mouseover", function(event, d) {
          if (!tooltip) return;
          var fips = String(d.id).padStart(2, "0");
          var sd = US_STATE_DATA[fips];
          if (!sd) return;
          tooltip.textContent = sd.name + " \u2014 " + TIER_LABELS[sd.tier];
          tooltip.classList.add("visible");
        })
        .on("mousemove", function(event) {
          if (!tooltip) return;
          var rect = container.getBoundingClientRect();
          tooltip.style.left = (event.clientX - rect.left + 12) + "px";
          tooltip.style.top = (event.clientY - rect.top - 30) + "px";
        })
        .on("mouseout", function() {
          if (tooltip) tooltip.classList.remove("visible");
        })
        .on("click", function(event, d) {
          var fips = String(d.id).padStart(2, "0");
          var sd = US_STATE_DATA[fips];
          if (sd) window.location.href = "../../state-guides/" + sd.slug + "/";
        })
        .on("keydown", function(event, d) {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            var fips = String(d.id).padStart(2, "0");
            var sd = US_STATE_DATA[fips];
            if (sd) window.location.href = "../../state-guides/" + sd.slug + "/";
          }
        });

      // State borders
      svg.append("path")
        .datum(topojson.mesh(topoData, topoData.objects.states, function(a, b) { return a !== b; }))
        .attr("class", "state-borders")
        .attr("d", path);
    })
    .catch(function(err) {
      console.error("Failed to load map data:", err);
      container.innerHTML = '<p style="color:var(--md-default-fg-color);text-align:center;padding:2rem;">Map unavailable. See the table below for all 50 states.</p>';
    });
}

/* ============================================================
   FEATURE 8: MEGA-MENU STATE SEARCH
   Adds a filter input to the State Guides mega-menu dropdown.
   ============================================================ */

function initMegaMenuSearch() {
  var megaMenu = document.querySelector(".md-tabs__mega-menu");
  if (!megaMenu) return;
  if (megaMenu.querySelector(".mega-menu-search")) return;

  var searchDiv = document.createElement("div");
  searchDiv.className = "mega-menu-search";
  var input = document.createElement("input");
  input.type = "text";
  input.placeholder = "Search states\u2026";
  input.setAttribute("aria-label", "Filter states by name");
  searchDiv.appendChild(input);

  // Insert at the top of the mega menu
  megaMenu.insertBefore(searchDiv, megaMenu.firstChild);

  var stateLinks = megaMenu.querySelectorAll(".md-tabs__mega-col > a");

  input.addEventListener("input", function () {
    var query = this.value.toLowerCase().trim();
    stateLinks.forEach(function (link) {
      var name = link.textContent.toLowerCase();
      link.style.display = !query || name.includes(query) ? "" : "none";
    });
  });

  // Prevent the dropdown from closing when clicking the input
  input.addEventListener("click", function (e) {
    e.stopPropagation();
  });
}

/* ============================================================
   INITIALIZATION
   MkDocs Material uses instant navigation (SPA mode), so we
   listen for the custom event it fires on each page load.
   ============================================================ */

function onPageLoad() {
  init50StateFilter();
  initSmoothScroll();
  initTabDropdowns();
  initLeadIns();
  initDonutChart();
  initAccordionControls();
  initUSMap();
  initMegaMenuSearch();
}

// Standard DOM ready (for initial page load)
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", onPageLoad);
} else {
  onPageLoad();
}

// MkDocs Material instant navigation exposes a document$ RxJS observable
// that emits on every page transition (including the initial load).
if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    onPageLoad();
  });
}
