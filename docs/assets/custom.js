/**
 * Protections For Elections — Custom JavaScript
 *
 * Features:
 * 1. Interactive 50-State Table Filter (active on /legal-foundation/50-state-overview/ only)
 * 2. Smooth anchor scroll for legal deep-links
 * 3. Dropdown menus for top navigation tabs
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
     "State Guides" — Overview link + 3 tier items, each with
     a nested sub-dropdown of individual states
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

    childItems.forEach(function (child) {
      var directLink = child.querySelector(":scope > a.md-nav__link");
      var sectionLabel = child.querySelector(":scope > label.md-nav__link");

      if (directLink && !sectionLabel) {
        // "State Guide Overview" — direct link at top
        dropdown.appendChild(
          makeLink(
            directLink.getAttribute("href"),
            directLink.textContent.trim()
          )
        );
      } else if (sectionLabel) {
        // Tier group — create a hoverable item with sub-dropdown
        var tierText = sectionLabel.textContent.trim();
        var tierItem = document.createElement("div");
        tierItem.className = "md-tabs__dropdown-tier";

        // Determine tier color class
        if (tierText.indexOf("Tier 1") !== -1)
          tierItem.classList.add("md-tabs__dropdown-tier--green");
        else if (tierText.indexOf("Tier 2") !== -1)
          tierItem.classList.add("md-tabs__dropdown-tier--yellow");
        else if (tierText.indexOf("Tier 3") !== -1)
          tierItem.classList.add("md-tabs__dropdown-tier--red");

        // Tier label with arrow indicator
        var tierLabel = document.createElement("span");
        tierLabel.className = "md-tabs__dropdown-tier-label";
        tierLabel.innerHTML =
          '<span class="md-tabs__dropdown-tier-text">' +
          tierText +
          "</span>" +
          '<span class="md-tabs__dropdown-tier-arrow">\u25B6</span>';
        tierItem.appendChild(tierLabel);

        // Build nested sub-dropdown with individual states
        var subNav = child.querySelector(":scope > .md-nav");
        if (subNav) {
          var subDropdown = document.createElement("div");
          subDropdown.className = "md-tabs__subdropdown";

          var stateLinks = subNav.querySelectorAll(
            ":scope > .md-nav__list > .md-nav__item > a.md-nav__link"
          );
          stateLinks.forEach(function (sl) {
            subDropdown.appendChild(
              makeLink(sl.getAttribute("href"), sl.textContent.trim())
            );
          });

          if (subDropdown.children.length > 0)
            tierItem.appendChild(subDropdown);
        }

        dropdown.appendChild(tierItem);
      }
    });

    if (dropdown.children.length > 0) tab.appendChild(dropdown);
  })();
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
