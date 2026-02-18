/**
 * Municipal Election Integrity Ordinance — Custom JavaScript
 *
 * Features:
 * 1. Interactive 50-State Table Filter (active on /legal-foundation/50-state-overview/ only)
 * 2. Smooth anchor scroll for legal deep-links
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
   INITIALIZATION
   MkDocs Material uses instant navigation (SPA mode), so we
   listen for the custom event it fires on each page load.
   ============================================================ */

function onPageLoad() {
  init50StateFilter();
  initSmoothScroll();
}

// Standard DOM ready (for initial page load)
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", onPageLoad);
} else {
  onPageLoad();
}

// MkDocs Material instant navigation fires this event on subsequent page loads
document.addEventListener("DOMContentSwitch", function () {
  onPageLoad();
});
