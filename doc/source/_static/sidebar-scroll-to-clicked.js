(function () {
  const STORAGE_KEY = "furo-sidebar-from-click";
  const NAV_TOGGLE_ID = "__navigation";

  console.log("[sidebar-keep-clicked] script loaded");

  function focusSidebarSearch() {
    const navToggle = document.getElementById(NAV_TOGGLE_ID);
    if (navToggle && !navToggle.checked) {
      navToggle.checked = true;
    }

    const input = document.querySelector(".sidebar-search-container .sidebar-search");
    if (!input) return;

    // Wait a frame so focusing works reliably right after opening the drawer on mobile.
    window.requestAnimationFrame(() => {
      input.focus();
      input.select();
    });
  }

  function closeSidebarSearch() {
    const input = document.querySelector(".sidebar-search-container .sidebar-search");
    if (input) {
      input.blur();
    }

    const navToggle = document.getElementById(NAV_TOGGLE_ID);
    if (navToggle && navToggle.checked) {
      navToggle.checked = false;
    }
  }

  document.addEventListener("keydown", (e) => {
    const target = e.target;
    const isTypingContext =
      target &&
      (target.tagName === "INPUT" ||
        target.tagName === "TEXTAREA" ||
        target.isContentEditable);

    if (isTypingContext) return;

    const isCtrlOrCmdK = (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k";
    if (!isCtrlOrCmdK) return;

    e.preventDefault();
    focusSidebarSearch();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;

    const activeElement = document.activeElement;
    const isSidebarSearchFocused =
      activeElement &&
      activeElement.matches &&
      activeElement.matches(".sidebar-search-container .sidebar-search");

    if (!isSidebarSearchFocused) return;

    e.preventDefault();
    closeSidebarSearch();
  });

  // 1) 사이드바에서 클릭되었다는 "사실"만 저장 (href 저장 X)
  document.addEventListener("click", (e) => {
    const link = e.target.closest(".sidebar-scroll a[href]");
    if (!link) return;

    // 그냥 플래그만 저장
    sessionStorage.setItem(STORAGE_KEY, "1");
    console.log("[sidebar-keep-clicked] sidebar click detected");
  });

  // 2) 새 페이지 로딩 후: 현재 활성 항목(current) 기준으로 사이드바만 스크롤
  window.addEventListener("load", () => {
    const sidebar = document.querySelector(".sidebar-scroll");
    if (!sidebar) {
      console.log("[sidebar-keep-clicked] no .sidebar-scroll");
      return;
    }

    const fromClick = sessionStorage.getItem(STORAGE_KEY);
    console.log("[sidebar-keep-clicked] load, fromClick:", fromClick);

    // 사이드바 클릭으로 온 게 아니면 (예: F5) 아무것도 안 함
    if (!fromClick) {
      return;
    }

    // 🔹 현재 페이지에서 "활성된" TOC 항목 찾기
    let targetLink =
      sidebar.querySelector('a[aria-current="page"]') ||
      sidebar.querySelector("a.current");

    console.log("[sidebar-keep-clicked] targetLink (current):", targetLink);

    if (!targetLink) {
      console.log("[sidebar-keep-clicked] no current targetLink, abort");
      sessionStorage.removeItem(STORAGE_KEY);
      return;
    }

    // 사이드바와 타겟 링크의 화면 좌표
    const sidebarRect = sidebar.getBoundingClientRect();
    const linkRect = targetLink.getBoundingClientRect();

    const sidebarHeight = sidebar.clientHeight;
    const linkHeight = targetLink.offsetHeight;

    // 현재 스크롤에서 링크가 sidebar 안에서 차지하는 상대 위치
    const offsetInside = linkRect.top - sidebarRect.top;

    // 링크를 sidebar 가운데쯤 두고 싶으면:
    let desiredScrollTop =
      sidebar.scrollTop + offsetInside - (sidebarHeight / 2 - linkHeight / 2);

    // clamp
    if (desiredScrollTop < 0) desiredScrollTop = 0;
    const maxScroll = sidebar.scrollHeight - sidebarHeight;
    if (desiredScrollTop > maxScroll) desiredScrollTop = maxScroll;

    console.log(
      "[sidebar-keep-clicked] before scrollTop:",
      sidebar.scrollTop,
      "desired:",
      desiredScrollTop,
      "max:",
      maxScroll,
    );

    sidebar.style.scrollBehavior = "auto"; // 애니메이션 없이
    const diff = Math.abs(desiredScrollTop - sidebar.scrollTop);
    if (diff > 20) {  // 20px 이상 차이날 때만 조정 (작은 움직임은 무시)
      sidebar.scrollTop = desiredScrollTop;
    }

    console.log(
      "[sidebar-keep-clicked] after  scrollTop:",
      sidebar.scrollTop,
    );

    // 한 번 쓰고 끝 — F5 에서는 동작 안 하게
    sessionStorage.removeItem(STORAGE_KEY);
  });
})();
